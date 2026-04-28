import base64

import allure
from playwright.sync_api import Playwright

from api.assertions import assert_json_has_keys, assert_status
from config.settings import Settings


PRODUCT_IMAGE = base64.b64decode(
    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMB/az8"
    "fN8AAAAASUVORK5CYII="
)


class ProductsClient:
    def __init__(self, playwright: Playwright, settings: Settings):
        self.request_context = playwright.request.new_context(base_url=settings.base_url)

    def add_product(self, token: str, user_id: str, product: dict) -> dict:
        with allure.step("Add product through Product API"):
            response = self.request_context.post(
                "/api/ecom/product/add-product",
                headers={"authorization": token},
                multipart={
                    "productName": product["name"],
                    "productAddedBy": user_id,
                    "productCategory": product["category"],
                    "productSubCategory": product["sub_category"],
                    "productPrice": product["price"],
                    "productDescription": product["description"],
                    "productFor": product["product_for"],
                    "productImage": {
                        "name": "product.png",
                        "mimeType": "image/png",
                        "buffer": PRODUCT_IMAGE,
                    },
                },
            )

            assert_status(response, 201, "Add product API")
            response_body = response.json()
            assert_json_has_keys(response_body, ["productId"], "Add product API")
            assert response_body["productId"], f"Add product API returned empty product id: {response_body}"
            return response_body

    def add_product_with_payload(self, token: str, payload: dict):
        with allure.step("Send Add Product API request with custom payload"):
            return self.request_context.post(
                "/api/ecom/product/add-product",
                headers={"authorization": token},
                multipart=payload,
            )

    def delete_product(self, token: str, product_id: str) -> dict:
        with allure.step("Delete product through Product API"):
            response = self.request_context.delete(
                f"/api/ecom/product/delete-product/{product_id}",
                headers={"authorization": token},
            )
            assert_status(response, 200, "Delete product API")
            return response.json()

    def dispose(self) -> None:
        self.request_context.dispose()
