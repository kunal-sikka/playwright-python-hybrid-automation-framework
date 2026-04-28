import allure
from playwright.sync_api import expect


class OrderDetailsPage:
    def __init__(self, page):
        self.page = page

    def expect_success_message_visible(self):
        with allure.step("Verify order success message is visible"):
            expect(self.page.get_by_text("Thank you for Shopping With Us")).to_be_visible()
