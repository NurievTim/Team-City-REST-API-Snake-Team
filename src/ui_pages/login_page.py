from src.ui_pages.base_page import BasePage


class LoginPage(BasePage):

    def url(self):
        return "/login.html"

    @property
    def login_button(self):
        return self.page.get_by_role("button", name="Log in")

    @property
    def error_message(self):
        return self.page.locator("#errorMessage")

    @property
    def login_to_teamcity_text(self):
        return self.page.locator("#header")

    def admin_login(self, admin_username: str, admin_password: str):
        self.page.locator("#username").fill(admin_username)
        self.page.locator("#password").fill(admin_password)
        self.login_button.click()
        return self

    def admin_login_with_wrong_password(self, admin_username: str):
        self.page.locator("#username").fill(admin_username)
        self.page.locator("#password").fill(admin_username)
        self.login_button.click()
        return self

    def click_login_button(self):
        self.login_button.click()
