import allure
import pytest
from pytest_bdd import given, scenario, then, when

from pages.login_page import LoginPage


@allure.epic("Ecommerce Automation")
@allure.feature("BDD Hybrid Order")
@allure.title("BDD: API-created order is visible in UI")
@pytest.mark.bdd
@pytest.mark.hybrid
@scenario("../../features/hybrid_order.feature", "API-created order is visible in UI")
def test_bdd_api_created_order_is_visible_in_ui():
    pass


@given("hybrid order is created through API")
def hybrid_order_is_created_through_api(api_workflow, user_credentials, bdd_context):
    bdd_context["order_id"] = api_workflow.create_order_for_user(user_credentials)


@when("hybrid user opens the order from order history")
def hybrid_user_opens_order(page, settings, user_credentials, bdd_context):
    login_page = LoginPage(page, settings)
    login_page.navigate_to_site()
    dashboard_page = login_page.login(user_credentials["userEmail"], user_credentials["userPassword"])
    order_history_page = dashboard_page.open_order_history()
    bdd_context["order_details_page"] = order_history_page.open_order_details(bdd_context["order_id"])


@then("hybrid order details should show success message")
def hybrid_order_details_should_show_success(bdd_context, auth_client, orders_client, user_credentials):
    bdd_context["order_details_page"].expect_success_message_visible()
    token = auth_client.get_token(user_credentials)
    orders_client.delete_order(token, bdd_context["order_id"])
