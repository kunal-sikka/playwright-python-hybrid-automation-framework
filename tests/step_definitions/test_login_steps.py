import allure
import pytest
from pytest_bdd import given, scenario, then, when

from pages.login_page import LoginPage


@allure.epic("Ecommerce Automation")
@allure.feature("BDD Login")
@allure.title("BDD: User logs in with valid credentials")
@pytest.mark.bdd
@pytest.mark.ui
@scenario("../../features/login.feature", "User logs in with valid credentials")
def test_bdd_user_logs_in_with_valid_credentials():
    pass


@given("login user is on the login page")
def login_user_is_on_login_page(page, settings, bdd_context):
    login_page = LoginPage(page, settings)
    login_page.navigate_to_site()
    bdd_context["login_page"] = login_page


@when("login user logs in with valid credentials")
def login_user_logs_in(user_credentials, bdd_context):
    bdd_context["dashboard_page"] = bdd_context["login_page"].login(
        user_credentials["userEmail"],
        user_credentials["userPassword"],
    )


@then("login user should see the products page")
def login_user_should_see_products_page(bdd_context):
    bdd_context["dashboard_page"].expect_loaded()
