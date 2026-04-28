import allure
import pytest
from pytest_bdd import given, scenario, then, when

from config.test_data import DEFAULT_COUNTRY, DEFAULT_PRODUCT_NAME
from pages.login_page import LoginPage


@allure.epic("Ecommerce Automation")
@allure.feature("BDD Checkout")
@allure.title("BDD: User places an order from checkout")
@pytest.mark.bdd
@pytest.mark.hybrid
@scenario("../../features/checkout.feature", "User places an order from checkout")
def test_bdd_user_places_order_from_checkout():
    pass


@given("checkout user is logged in")
def checkout_user_is_logged_in(page, settings, user_credentials, bdd_context):
    login_page = LoginPage(page, settings)
    login_page.navigate_to_site()
    bdd_context["dashboard_page"] = login_page.login(
        user_credentials["userEmail"],
        user_credentials["userPassword"],
    )


@given("checkout user has product in cart")
def checkout_user_has_product_in_cart(bdd_context):
    bdd_context["dashboard_page"].add_product_to_cart(DEFAULT_PRODUCT_NAME)
    cart_page = bdd_context["dashboard_page"].open_cart()
    cart_page.expect_product_visible(DEFAULT_PRODUCT_NAME)
    bdd_context["checkout_page"] = cart_page.checkout()


@when("checkout user places the order")
def checkout_user_places_order(bdd_context):
    bdd_context["confirmation_page"] = bdd_context["checkout_page"].place_order(DEFAULT_COUNTRY)


@then("checkout user should see order confirmation")
def checkout_user_should_see_confirmation(bdd_context, auth_client, orders_client, user_credentials):
    bdd_context["confirmation_page"].expect_order_confirmation_visible()
    order_id = bdd_context["confirmation_page"].get_order_id()
    token = auth_client.get_token(user_credentials)
    orders_client.delete_order(token, order_id)
