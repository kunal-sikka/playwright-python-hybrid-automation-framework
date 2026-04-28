import allure
from playwright.sync_api import expect

from config.settings import Settings


class LoginPage:
    def __init__(self, page, settings: Settings):
        self.page = page
        self.settings = settings

    def navigate_to_site(self):
        with allure.step("Navigate to ecommerce login page"):
            self.page.goto(self.settings.login_url)

    def login(self, user_email, user_password):
        with allure.step("Login through ecommerce UI"):
            self.page.get_by_role("textbox", name="email@example.com").fill(user_email)
            self.page.get_by_role("textbox", name="enter your passsword").fill(user_password)
            self.page.locator("#login").click()
            expect(self.page.get_by_role("button", name="ORDERS")).to_be_visible()
            from .dashboard_page import DashboardPage

            return DashboardPage(self.page)

    def expect_login_error_visible(self):
        with allure.step("Verify invalid login error message is visible"):
            expect(self.page.get_by_text("Incorrect email or password.")).to_be_visible()
