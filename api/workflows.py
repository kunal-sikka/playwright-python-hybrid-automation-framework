import allure
from playwright.sync_api import Playwright

from api.auth_client import AuthClient
from api.orders_client import OrdersClient
from config.settings import Settings


class EcommerceApiWorkflow:
    def __init__(self, playwright: Playwright, settings: Settings):
        self.auth_client = AuthClient(playwright, settings)
        self.orders_client = OrdersClient(playwright, settings)

    def create_order_for_user(self, user_credentials: dict) -> str:
        with allure.step("Create test order through API workflow"):
            token = self.auth_client.get_token(user_credentials)
            return self.orders_client.create_order_and_get_id(token)

    def dispose(self) -> None:
        self.auth_client.dispose()
        self.orders_client.dispose()
