import allure
import pytest

from utils.product_factory import build_product


@allure.epic("Ecommerce Automation")
@allure.feature("API Validation")
@allure.story("Product Management")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Add product API creates product successfully")
@pytest.mark.api
def test_add_product_api_returns_product_id(auth_client, products_client, user_credentials):
    product_id = None
    token = None
    try:
        login_response = auth_client.login(user_credentials)
        token = login_response["token"]
        product = build_product()
        add_product_response = products_client.add_product(
            token,
            login_response["userId"],
            product,
        )
        product_id = add_product_response["productId"]

        with allure.step("Verify product id is returned in API response"):
            assert product_id, "Add product API returned an empty product id"
    finally:
        if token and product_id:
            products_client.delete_product(token, product_id)


@allure.epic("Ecommerce Automation")
@allure.feature("API Validation")
@allure.story("Product Management")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Add product API rejects invalid payload")
@pytest.mark.api
def test_add_product_api_rejects_invalid_payload(auth_client, products_client, user_credentials):
    login_response = auth_client.login(user_credentials)
    response = products_client.add_product_with_payload(
        login_response["token"],
        {"productPrice": "1200"},
    )

    with allure.step("Verify Add Product API rejects invalid payload"):
        assert response.status in [400, 422, 500], f"Unexpected status: {response.status}"


@allure.epic("Ecommerce Automation")
@allure.feature("API Validation")
@allure.story("Product Management")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Delete product API removes created product")
@pytest.mark.api
def test_delete_product_api_removes_created_product(auth_client, products_client, user_credentials):
    login_response = auth_client.login(user_credentials)
    product = build_product()
    add_response = products_client.add_product(
        login_response["token"],
        login_response["userId"],
        product,
    )

    delete_response = products_client.delete_product(
        login_response["token"],
        add_response["productId"],
    )

    with allure.step("Verify product delete API returns success message"):
        assert delete_response, "Delete product API returned empty response"
