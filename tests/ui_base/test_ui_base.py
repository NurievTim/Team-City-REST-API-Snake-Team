from playwright.sync_api import Page, expect

from src.configs.config import Config
from src.enums import UiAlert
from src.ui_pages.login_page import LoginPage


class BaseUITest:
    UI_BASE_URL = Config.get("UI_BASE_URL", "http://localhost:8111")

    def auth_as_admin(self, page: Page, admin_username: str, admin_password: str):
        page.set_viewport_size({"width": 1920, "height": 1080})
        login_page = LoginPage(page).open()

        expect(page.locator("#header")).to_be_visible()
        expect(page.locator("#header")).to_have_text(UiAlert.LOGIN_PAGE_VISIBLE)

        login_page.admin_login(admin_username, admin_password)
        return login_page
