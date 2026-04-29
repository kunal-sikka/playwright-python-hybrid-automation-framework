import allure
from playwright.sync_api import Error as PlaywrightError
from playwright.sync_api import Playwright

from api.assertions import assert_json_has_keys, assert_status
from config.settings import Settings


class OrdersClient:
    def __init__(self, playwright: Playwright, settings: Settings):
        self.settings = settings
        self.request_context = playwright.request.new_context(base_url=settings.base_url)

    def create_order(self, token: str, order_payload: dict | None = None) -> dict:
        with allure.step("Create order through Orders API"):
            response = self.request_context.post(
                "/api/ecom/order/create-order",
                data=order_payload or self.settings.default_order_payload,
                headers={"authorization": token, "content-type": "application/json"},
            )

            assert_status(response, 201, "Create order API")
            response_body = response.json()
            assert_json_has_keys(response_body, ["orders"], "Create order API")
            assert response_body["orders"], f"Create order API returned empty orders list: {response_body}"
        return response_body

    def create_order_and_get_id(self, token: str, order_payload: dict | None = None) -> str:
        response_body = self.create_order(token, order_payload)
        return response_body["orders"][0]

    def get_orders_for_customer(self, token: str, user_id: str) -> dict:
        with allure.step("Get customer orders through Orders API"):
            response = self.request_context.get(
                f"/api/ecom/order/get-orders-for-customer/{user_id}",
                headers={"authorization": token},
            )
            assert_status(response, 200, "Get customer orders API")
            return response.json()

    def get_order_details(self, token: str, order_id: str) -> dict:
        with allure.step("Get order details through Orders API"):
            response = self.request_context.get(
                f"/api/ecom/order/get-orders-details?id={order_id}",
                headers={"authorization": token},
            )
            assert_status(response, 200, "Get order details API")
            return response.json()

    def delete_order(self, token: str, order_id: str) -> dict:
        last_error = None

        for attempt in range(3):
            try:
                with allure.step("Delete order through Orders API"):
                    response = self.request_context.delete(
                        f"/api/ecom/order/delete-order/{order_id}",
                        headers={"authorization": token},
                    )

                    assert_status(response, 200, "Delete order API")
                    return response.json()

            except PlaywrightError as error:
                last_error = error
                if attempt == 2:
                    raise
                time.sleep(2)

        raise last_error

    def delete_order_without_token(self, order_id: str):
        with allure.step("Attempt to delete order without authorization token"):
            return self.request_context.delete(f"/api/ecom/order/delete-order/{order_id}")

    def delete_order_with_invalid_id(self, token: str):
        with allure.step("Attempt to delete order with invalid order id"):
            return self.request_context.delete(
                "/api/ecom/order/delete-order/invalid-order-id",
                headers={"authorization": token},
            )

    def create_order_without_token(self, order_payload: dict | None = None):
        with allure.step("Attempt to create order without authorization token"):
            return self.request_context.post(
                "/api/ecom/order/create-order",
                data=order_payload or self.settings.default_order_payload,
                headers={"content-type": "application/json"},
            )

    def dispose(self) -> None:
        self.request_context.dispose()
