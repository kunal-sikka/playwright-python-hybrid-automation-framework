import allure
import pytest

from pages.login_page import LoginPage


@allure.epic("Ecommerce Automation")
@allure.feature("UI Validation")
@allure.story("Negative Login")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Login fails with invalid password")
@pytest.mark.ui
@pytest.mark.smoke
def test_login_fails_with_invalid_password(page, settings, user_credentials):
    login_page = LoginPage(page, settings)

    login_page.navigate_to_site()
    login_page.login_with_invalid_credentials(
        user_credentials["userEmail"],
        "InvalidPassword@123",
    )
    login_page.expect_login_error_visible()
