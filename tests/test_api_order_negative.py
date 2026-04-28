import allure
import pytest


@allure.epic("Ecommerce Automation")
@allure.feature("API Security")
@allure.story("Delete Order Negative")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Delete order API rejects invalid and unauthorized requests")
@pytest.mark.api
def test_delete_order_api_rejects_invalid_requests(auth_client, orders_client, user_credentials):
    token = auth_client.get_token(user_credentials)
    invalid_id_response = orders_client.delete_order_with_invalid_id(token)
    missing_token_response = orders_client.delete_order_without_token("invalid-order-id")

    with allure.step("Verify delete order API rejects invalid order id"):
        assert invalid_id_response.status in [400, 404, 500], (
            f"Unexpected status for invalid id: {invalid_id_response.status}"
        )

    with allure.step("Verify delete order API rejects missing token"):
        assert missing_token_response.status in [401, 403], (
            f"Unexpected status for missing token: {missing_token_response.status}"
        )
