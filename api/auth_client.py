import allure
from playwright.sync_api import Playwright

from api.assertions import assert_json_has_keys, assert_status
from config.settings import Settings


class AuthClient:
    def __init__(self, request_context):
        self.request_context = request_context

    def login(self, user_credentials):
        last_error = None

        for attempt in range(3):
            try:
                response = self.request_context.post(
                    "/api/ecom/auth/login",
                    data=user_credentials,
                )
                assert_status(response, 200, "Login API")
                return response.json()

            except PlaywrightError as error:
                last_error = error
                if attempt == 2:
                    raise
                time.sleep(2)

        raise last_error

    def get_token(self, user_credentials):
        return self.login(user_credentials)["token"]

    def login_with_payload(self, payload: dict):
        with allure.step("Send Login API request with custom payload"):
            return self.request_context.post(
                "/api/ecom/auth/login",
                data=payload,
            )

    def dispose(self) -> None:
        self.request_context.dispose()
