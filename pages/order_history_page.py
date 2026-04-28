import allure

from .order_details_page import OrderDetailsPage


class OrderHistoryPage:
    def __init__(self, page):
        self.page = page

    def open_order_details(self, order_id):
        with allure.step(f"Open order details for order id: {order_id}"):
            self.page.locator("tr").filter(has_text=order_id).locator("button").filter(has_text="View").click()
            return OrderDetailsPage(self.page)

    def expect_order_visible(self, order_id: str):
        with allure.step(f"Verify order id is visible in order history: {order_id}"):
            from playwright.sync_api import expect

            expect(self.page.locator("tr").filter(has_text=order_id)).to_be_visible()

    def expect_no_orders_message_visible(self):
        with allure.step("Verify no orders message is visible"):
            from playwright.sync_api import expect

            expect(self.page.get_by_text("No Orders")).to_be_visible()

    def delete_order(self, order_id: str):
        with allure.step(f"Delete order from order history: {order_id}"):
            self.page.locator("tr").filter(has_text=order_id).locator("button").filter(has_text="Delete").click()
