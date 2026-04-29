import allure
from playwright.sync_api import Error as PlaywrightError

from api.assertions import assert_json_has_keys, assert_status
from config.settings import Settings


class AuthClient:
    def __init__(self, playwright, settings: Settings):
        self.request_context = playwright.request.new_context(
            base_url=settings.base_url
        )

    def login(self, user_credentials):
        last_error = None

        for attempt in range(3):
            try:
                with allure.step("Login through API"):
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
        with allure.step(f"Login API with payload: {payload}"):
            response = self.request_context.post(
                "/api/ecom/auth/login",
                data=payload,
            )
            return response

    def dispose(self):
        self.request_context.dispose()
