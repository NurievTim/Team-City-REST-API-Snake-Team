import allure
from playwright.sync_api import Page, expect

from tests.ui_base.test_ui_base import BaseUITest


class TestLoginAdmin(BaseUITest):
    @allure.id("51")
    @allure.title("UI — логин админа с корректными данными")
    def test_admin_login_with_correct_data(self, page: Page, admin_username: str, admin_password: str):
        # 1. Переходим на страницу логина
        page.goto(f"{self.UI_BASE_URL}/login.html", wait_until="domcontentloaded")

        # 2. Проверяем лейбл TeamCity
        expect(page.locator("#header")).to_be_visible()
        expect(page.locator("#header")).to_have_text("Log in to TeamCity")

        # 3. Вводим логин 4. пароль  5. нажимаем кнопку
        page.locator("#username").fill(admin_username)
        page.locator("#password").fill(admin_password)
        page.get_by_role("button", name="Log in").click()

        # 6. Нажимаем на иконку профиля
        page.get_by_role("button", name=admin_username).click()

        # 7. Во всплывающем меню нажимаем Profile
        page.get_by_text("Profile").click()

        # 8. Проверяем страницу профиля
        expect(page).to_have_url(f"{self.UI_BASE_URL}/profile.html")

        # 9. Проверяем что username на странице совпадает с тем под которым логинились
        actual_username = page.locator("#text_teamcityUsername").inner_text()
        assert actual_username == admin_username, \
            f"Ожидали username: '{admin_username}', получили: '{actual_username}'"