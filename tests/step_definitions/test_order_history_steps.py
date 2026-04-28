import allure
import pytest
from pytest_bdd import given, scenario, then, when

from pages.login_page import LoginPage


@allure.epic("Ecommerce Automation")
@allure.feature("BDD Order History")
@allure.title("BDD: User sees API-created order in order history")
@pytest.mark.bdd
@pytest.mark.hybrid
@scenario("../../features/order_history.feature", "User sees API-created order in order history")
def test_bdd_user_sees_api_created_order_in_history():
    pass


@given("order history has an order created by API")
def order_history_has_api_created_order(api_workflow, user_credentials, bdd_context):
    bdd_context["order_id"] = api_workflow.create_order_for_user(user_credentials)


@when("order history user opens order history page")
def order_history_user_opens_history(page, settings, user_credentials, bdd_context):
    login_page = LoginPage(page, settings)
    login_page.navigate_to_site()
    dashboard_page = login_page.login(user_credentials["userEmail"], user_credentials["userPassword"])
    bdd_context["order_history_page"] = dashboard_page.open_order_history()


@then("order history should display the created order")
def order_history_should_display_created_order(bdd_context, auth_client, orders_client, user_credentials):
    bdd_context["order_history_page"].expect_order_visible(bdd_context["order_id"])
    token = auth_client.get_token(user_credentials)
    orders_client.delete_order(token, bdd_context["order_id"])
