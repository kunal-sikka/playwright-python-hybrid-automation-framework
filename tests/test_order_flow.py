import allure
import pytest

from pages.login_page import LoginPage


@allure.epic("Ecommerce Automation")
@allure.feature("Hybrid E2E")
@allure.story("Order Details")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("API and UI show accessible order details")
@pytest.mark.e2e
def test_api_created_order_details_are_accessible_in_api_and_ui(
    page, settings, user_credentials, api_workflow, auth_client, orders_client
):
    order_id = api_workflow.create_order_for_user(user_credentials)
    token = auth_client.get_token(user_credentials)
    try:
        order_details = orders_client.get_order_details(token, order_id)
        with allure.step("Verify API returns order details"):
            assert order_id in str(order_details), f"Order id {order_id} was not found in order details API"

        login_page = LoginPage(page, settings)
        login_page.navigate_to_site()
        dashboard_page = login_page.login(user_credentials["userEmail"], user_credentials["userPassword"])
        order_history_page = dashboard_page.open_order_history()
        order_details_page = order_history_page.open_order_details(order_id)
        order_details_page.expect_success_message_visible()
    finally:
        orders_client.delete_order(token, order_id)


@allure.epic("Ecommerce Automation")
@allure.feature("Hybrid E2E")
@allure.story("Order History")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Order history displays API-created order")
@pytest.mark.e2e
def test_order_history_displays_api_created_order(
    page, settings, user_credentials, api_workflow, auth_client, orders_client
):
    order_id = api_workflow.create_order_for_user(user_credentials)
    token = auth_client.get_token(user_credentials)
    try:
        login_page = LoginPage(page, settings)
        login_page.navigate_to_site()
        dashboard_page = login_page.login(user_credentials["userEmail"], user_credentials["userPassword"])
        order_history_page = dashboard_page.open_order_history()
        order_history_page.expect_order_visible(order_id)
    finally:
        orders_client.delete_order(token, order_id)


@allure.epic("Ecommerce Automation")
@allure.feature("Hybrid E2E")
@allure.story("Delete Order")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Deleted order is removed from API order history")
@pytest.mark.e2e
def test_delete_order_removes_order_from_api_history(page, settings, user_credentials, auth_client, orders_client):
    login_response = auth_client.login(user_credentials)
    order_id = orders_client.create_order_and_get_id(login_response["token"])

    orders_client.delete_order(login_response["token"], order_id)
    orders_response = orders_client.get_orders_for_customer(
        login_response["token"],
        login_response["userId"],
    )
    with allure.step("Verify deleted order is not present in API order history"):
        assert order_id not in str(orders_response), f"Deleted order id {order_id} still exists"
