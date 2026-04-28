import allure
import pytest


@allure.epic("Ecommerce Automation")
@allure.feature("API Security")
@allure.story("Unauthorized access")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Create order API rejects request without authorization token")
@pytest.mark.api
@pytest.mark.smoke
def test_create_order_api_rejects_missing_token(orders_client):
    response = orders_client.create_order_without_token()

    with allure.step("Verify protected API rejects missing token"):
        assert response.status in [401, 403], (
            f"Expected unauthorized or forbidden response, got {response.status}. "
            f"Response: {response.text()}"
        )
