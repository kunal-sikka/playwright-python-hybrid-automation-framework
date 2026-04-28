import allure
import pytest

from config.test_data import DEFAULT_PRODUCT_NAME
from pages.login_page import LoginPage


@allure.epic("Ecommerce Automation")
@allure.feature("Hybrid E2E")
@allure.story("Cart Management")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("User can add product to cart and view it in cart")
@pytest.mark.e2e
def test_user_can_add_product_to_cart(page, settings, user_credentials):
    login_page = LoginPage(page, settings)
    login_page.navigate_to_site()
    dashboard_page = login_page.login(user_credentials["userEmail"], user_credentials["userPassword"])

    dashboard_page.add_product_to_cart(DEFAULT_PRODUCT_NAME)
    cart_page = dashboard_page.open_cart()
    cart_page.expect_product_visible(DEFAULT_PRODUCT_NAME)
