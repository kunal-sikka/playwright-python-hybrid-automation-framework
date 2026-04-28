import allure
from playwright.sync_api import expect

from .order_history_page import OrderHistoryPage


class DashboardPage:
    def __init__(self, page):
        self.page = page

    def open_order_history(self):
        with allure.step("Open order history page"):
            self.page.get_by_role("button", name="ORDERS").click()
            return OrderHistoryPage(self.page)

    def expect_loaded(self):
        with allure.step("Verify dashboard is loaded"):
            expect(self.page.get_by_role("button", name="ORDERS")).to_be_visible()

    def add_product_to_cart(self, product_name: str):
        with allure.step(f"Add product to cart: {product_name}"):
            self.page.locator(".card-body").filter(has_text=product_name).get_by_role(
                "button",
                name="Add To Cart",
            ).click()

    def open_cart(self):
        with allure.step("Open cart page"):
            self.page.locator("button[routerlink='/dashboard/cart']").click()
            from .cart_page import CartPage

            return CartPage(self.page)
