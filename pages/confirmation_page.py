import re

import allure
from playwright.sync_api import expect


class ConfirmationPage:
    def __init__(self, page):
        self.page = page

    def expect_order_confirmation_visible(self):
        with allure.step("Verify order confirmation is visible"):
            expect(self.page.get_by_text("Thankyou for the order.")).to_be_visible()

    def get_order_id(self) -> str:
        with allure.step("Capture order id from confirmation page"):
            text = self.page.locator(".em-spacer-1 .ng-star-inserted").inner_text()
            return re.sub(r"[^a-zA-Z0-9]", "", text)
