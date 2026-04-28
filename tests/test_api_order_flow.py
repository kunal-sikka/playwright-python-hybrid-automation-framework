import allure
import pytest


@allure.epic("Ecommerce Automation")
@allure.feature("API Validation")
@allure.story("User Authentication")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Login API returns a valid authentication token")
@pytest.mark.api
def test_login_api_returns_token(auth_client, user_credentials):
    login_response = auth_client.login(user_credentials)
    with allure.step("Verify token is returned in API response"):
        assert login_response["token"], "Login API returned an empty token"


@allure.epic("Ecommerce Automation")
@allure.feature("API Validation")
@allure.story("Order Management")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create order API returns a valid order id")
@pytest.mark.api
def test_create_order_api_returns_order_id(auth_client, orders_client, user_credentials):
    token = auth_client.get_token(user_credentials)
    order_id = None
    try:
        create_order_response = orders_client.create_order(token)
        order_id = create_order_response["orders"][0]
        with allure.step("Verify order id is returned in API response"):
            assert order_id, "Create order API returned an empty order id"
    finally:
        if order_id:
            orders_client.delete_order(token, order_id)
