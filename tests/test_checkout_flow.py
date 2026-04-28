import allure
import pytest

from config.test_data import DEFAULT_COUNTRY, DEFAULT_PRODUCT_NAME
from pages.login_page import LoginPage


@allure.epic("Ecommerce Automation")
@allure.feature("Hybrid E2E")
@allure.story("Checkout")
@allure.severity(allure.severity_level.BLOCKER)
@allure.title("User can complete checkout for selected product")
@pytest.mark.e2e
def test_user_can_complete_checkout(page, settings, user_credentials, auth_client, orders_client):
    login_page = LoginPage(page, settings)
    login_page.navigate_to_site()
    dashboard_page = login_page.login(user_credentials["userEmail"], user_credentials["userPassword"])

    dashboard_page.add_product_to_cart(DEFAULT_PRODUCT_NAME)
    cart_page = dashboard_page.open_cart()
    cart_page.expect_product_visible(DEFAULT_PRODUCT_NAME)
    checkout_page = cart_page.checkout()
    checkout_page.expect_loaded()
    confirmation_page = checkout_page.place_order(DEFAULT_COUNTRY)
    order_id = confirmation_page.get_order_id()
    token = auth_client.get_token(user_credentials)
    try:
        confirmation_page.expect_order_confirmation_visible()
    finally:
        orders_client.delete_order(token, order_id)


@allure.epic("Ecommerce Automation")
@allure.feature("Hybrid E2E")
@allure.story("Order Persistence")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("UI-created order is available through API order history")
@pytest.mark.e2e
def test_ui_created_order_is_available_in_api(page, settings, user_credentials, auth_client, orders_client):
    login_page = LoginPage(page, settings)
    login_page.navigate_to_site()
    dashboard_page = login_page.login(user_credentials["userEmail"], user_credentials["userPassword"])

    dashboard_page.add_product_to_cart(DEFAULT_PRODUCT_NAME)
    confirmation_page = dashboard_page.open_cart().checkout().place_order(DEFAULT_COUNTRY)
    order_id = confirmation_page.get_order_id()
    token = None

    try:
        login_response = auth_client.login(user_credentials)
        token = login_response["token"]
        orders_response = orders_client.get_orders_for_customer(
            token,
            login_response["userId"],
        )
        with allure.step("Verify UI-created order exists in API order history"):
            assert order_id in str(orders_response), f"Order id {order_id} was not found in API response"
    finally:
        if token and order_id:
            orders_client.delete_order(token, order_id)
