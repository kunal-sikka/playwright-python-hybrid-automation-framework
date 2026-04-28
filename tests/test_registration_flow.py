import allure
import pytest

from pages.register_page import RegisterPage
from utils.user_factory import build_registered_user


@allure.epic("Ecommerce Automation")
@allure.feature("User Registration")
@allure.story("Register user and validate login")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Newly registered user can login successfully")
@pytest.mark.ui
@pytest.mark.smoke
def test_registered_user_can_login(page, settings):
    registered_user = build_registered_user()

    register_page = RegisterPage(page, settings)
    register_page.navigate_to_registration_page()
    register_page.register_user(registered_user)
    register_page.expect_registration_success_message()

    login_page = register_page.open_login_page()
    dashboard_page = login_page.login(
        registered_user["email"],
        registered_user["password"],
    )
    dashboard_page.expect_loaded()
