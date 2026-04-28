import allure
from playwright.sync_api import expect


class CheckoutPage:
    def __init__(self, page):
        self.page = page

    def place_order(self, country: str):
        with allure.step("Place order from checkout page"):
            self.page.get_by_placeholder("Select Country").press_sequentially(country[:3])
            self.page.locator(".ta-results button").filter(has_text=country).first.click()
            self.page.get_by_text("Place Order").click()
            from .confirmation_page import ConfirmationPage

            return ConfirmationPage(self.page)

    def expect_loaded(self):
        with allure.step("Verify checkout page is loaded"):
            expect(self.page.get_by_text("Payment Method")).to_be_visible()
