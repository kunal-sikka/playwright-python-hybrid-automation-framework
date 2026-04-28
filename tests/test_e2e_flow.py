import allure
import pytest

from pages.login_page import LoginPage


@allure.epic("Ecommerce Automation")
@allure.feature("Hybrid E2E")
@allure.story("API order setup with UI verification")
@allure.severity(allure.severity_level.BLOCKER)
@allure.title("User can view API-created order details in UI")
@pytest.mark.e2e
def test_login_to_site(page, settings, user_credentials, api_workflow, auth_client, orders_client):
    user_email = user_credentials["userEmail"]
    user_password = user_credentials["userPassword"]

    order_id = api_workflow.create_order_for_user(user_credentials)
    token = auth_client.get_token(user_credentials)
    try:
        login_page = LoginPage(page, settings)
        login_page.navigate_to_site()
        dashboard = login_page.login(user_email, user_password)

        order_history_page = dashboard.open_order_history()
        order_details_page = order_history_page.open_order_details(order_id)
        order_details_page.expect_success_message_visible()
    finally:
        orders_client.delete_order(token, order_id)


@allure.epic("Ecommerce Automation")
@allure.feature("UI Validation")
@allure.story("Order history empty state")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Order history shows no orders message when API returns empty list")
@pytest.mark.ui
def test_no_orders_message(page, settings, user_credentials):
    with allure.step("Login through UI"):
        login_page = LoginPage(page, settings)
        login_page.navigate_to_site()
        login_page.login(user_credentials["userEmail"], user_credentials["userPassword"])

    # Intercept the orders API and return an empty orders list
    def mock_empty_orders(route):
        route.fulfill(
            status=200,
            content_type="application/json",
            body='{"data": [], "count": 0, "message": "No Orders"}'
        )

    with allure.step("Mock order history API to return an empty order list"):
        page.route("**/api/ecom/order/get-orders-for-customer/**", mock_empty_orders)

    with allure.step("Open order history page"):
        page.goto(settings.orders_url)
        page.wait_for_load_state("networkidle")

    with allure.step("Verify no orders message is visible"):
        from pages.order_history_page import OrderHistoryPage

        OrderHistoryPage(page).expect_no_orders_message_visible()
