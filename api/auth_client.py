import allure
from playwright.sync_api import Playwright

from api.assertions import assert_json_has_keys, assert_status
from config.settings import Settings


class AuthClient:
    def __init__(self, playwright: Playwright, settings: Settings):
        self.request_context = playwright.request.new_context(base_url=settings.client_base_url)

    def login(self, user_credentials: dict) -> dict:
        with allure.step("Authenticate user through Login API"):
            response = self.request_context.post(
                "/api/ecom/auth/login",
                data={
                    "userEmail": user_credentials["userEmail"],
                    "userPassword": user_credentials["userPassword"],
                },
            )

            assert_status(response, 200, "Login API")
            response_body = response.json()
            assert_json_has_keys(response_body, ["token"], "Login API")
        return response_body

    def get_token(self, user_credentials: dict) -> str:
        return self.login(user_credentials)["token"]

    def login_with_payload(self, payload: dict):
        with allure.step("Send Login API request with custom payload"):
            return self.request_context.post(
                "/api/ecom/auth/login",
                data=payload,
            )

    def dispose(self) -> None:
        self.request_context.dispose()
