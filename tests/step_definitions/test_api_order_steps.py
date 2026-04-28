import allure
import pytest
from pytest_bdd import given, scenario, then, when


@allure.epic("Ecommerce Automation")
@allure.feature("BDD API Order")
@allure.title("BDD: Create order using API")
@pytest.mark.bdd
@pytest.mark.api
@scenario("../../features/api_order.feature", "Create order using API")
def test_bdd_create_order_using_api():
    pass


@given("api order user is authenticated")
def api_order_user_is_authenticated(auth_client, orders_client, user_credentials, bdd_context):
    bdd_context["orders_client"] = orders_client
    bdd_context["token"] = auth_client.get_token(user_credentials)


@when("api order user creates an order")
def api_order_user_creates_order(bdd_context):
    bdd_context["order_id"] = bdd_context["orders_client"].create_order_and_get_id(bdd_context["token"])


@then("api order response should contain order id")
def api_order_response_should_contain_order_id(bdd_context):
    assert bdd_context["order_id"], "Order ID was not returned"
    bdd_context["orders_client"].delete_order(bdd_context["token"], bdd_context["order_id"])
