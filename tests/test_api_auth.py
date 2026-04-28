import allure
import pytest


@allure.epic("Ecommerce Automation")
@allure.feature("API Validation")
@allure.story("Invalid authentication payloads")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Login API rejects invalid payloads")
@pytest.mark.api
@pytest.mark.parametrize(
    "payload",
    [
        {"userPassword": "Password@123"},
        {"userEmail": "missing.password@example.com"},
    ],
    ids=["missing_email", "missing_password"],
)
def test_login_api_rejects_invalid_payload(auth_client, payload):
    response = auth_client.login_with_payload(payload)

    with allure.step("Verify Login API does not authenticate invalid payload"):
        assert response.status in [400, 401], (
            f"Expected validation or authentication failure, got {response.status}. "
            f"Response: {response.text()}"
        )
        assert "token" not in response.text(), "Invalid login payload should not return token"
