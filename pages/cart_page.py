import allure
from playwright.sync_api import expect


class CartPage:
    def __init__(self, page):
        self.page = page

    def expect_product_visible(self, product_name: str):
        with allure.step(f"Verify cart contains product: {product_name}"):
            expect(self.page.get_by_text(product_name)).to_be_visible()

    def checkout(self):
        with allure.step("Proceed to checkout"):
            self.page.get_by_text("Checkout").click()
            from .checkout_page import CheckoutPage

            return CheckoutPage(self.page)
