import allure
from playwright.sync_api import expect

from config.settings import Settings


class RegisterPage:
    def __init__(self, page, settings: Settings):
        self.page = page
        self.settings = settings

    def navigate_to_registration_page(self):
        with allure.step("Navigate to ecommerce registration page"):
            self.page.goto(self.settings.registration_url)

    def register_user(self, user: dict):
        with allure.step("Register a new ecommerce user"):
            self.page.locator("#firstName").fill(user["first_name"])
            self.page.locator("#lastName").fill(user["last_name"])
            self.page.locator("#userEmail").fill(user["email"])
            self.page.locator("#userMobile").fill(user["mobile"])
            self.page.locator("select[formcontrolname='occupation']").select_option(label=user["occupation"])
            self.page.locator("input[formcontrolname='gender']").first.check()
            self.page.locator("#userPassword").fill(user["password"])
            self.page.locator("#confirmPassword").fill(user["password"])
            self.page.locator("input[formcontrolname='required']").check()
            self.page.locator("#login").click()

    def expect_registration_success_message(self):
        with allure.step("Verify registration success message is displayed"):
            expect(self.page.get_by_text("Registered Successfully")).to_be_visible()

    def open_login_page(self):
        with allure.step("Open login page after successful registration"):
            self.page.get_by_text("Login").click()
            from .login_page import LoginPage

            return LoginPage(self.page, self.settings)
