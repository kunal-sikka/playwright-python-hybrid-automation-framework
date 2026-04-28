import allure
import pytest
from pytest_bdd import given, scenario, then, when

from config.test_data import DEFAULT_PRODUCT_NAME
from pages.login_page import LoginPage


@allure.epic("Ecommerce Automation")
@allure.feature("BDD Cart")
@allure.title("BDD: User adds product to cart")
@pytest.mark.bdd
@pytest.mark.hybrid
@scenario("../../features/cart.feature", "User adds product to cart")
def test_bdd_user_adds_product_to_cart():
    pass


@given("cart user is logged in")
def cart_user_is_logged_in(page, settings, user_credentials, bdd_context):
    login_page = LoginPage(page, settings)
    login_page.navigate_to_site()
    bdd_context["dashboard_page"] = login_page.login(
        user_credentials["userEmail"],
        user_credentials["userPassword"],
    )


@when("cart user adds product to the cart")
def cart_user_adds_product(bdd_context):
    bdd_context["dashboard_page"].add_product_to_cart(DEFAULT_PRODUCT_NAME)
    bdd_context["cart_page"] = bdd_context["dashboard_page"].open_cart()


@then("cart should display the selected product")
def cart_should_display_product(bdd_context):
    bdd_context["cart_page"].expect_product_visible(DEFAULT_PRODUCT_NAME)
