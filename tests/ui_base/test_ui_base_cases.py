import allure
from playwright.sync_api import Page, expect

from src.generators.random_data import RandomData
from tests.ui_base.test_ui_base import BaseUITest


class TestLoginAdmin(BaseUITest):
    @allure.id("51")
    @allure.title("UI — логин админа с корректными данными")
    def test_admin_login_with_correct_data(self, page: Page, admin_username: str, admin_password: str):
        page.set_viewport_size({"width": 1920, "height": 1080})
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
            f"expected : '{admin_username}', received: '{actual_username}'"

    @allure.id("52")
    @allure.title("UI — логин с неверным паролем")
    def test_admin_login_with_wrong_password(self, page: Page, admin_username: str):
        page.set_viewport_size({"width": 1920, "height": 1080})
        page.goto(f"{self.UI_BASE_URL}/login.html", wait_until="domcontentloaded")
        expect(page.locator("#header")).to_be_visible()
        expect(page.locator("#header")).to_have_text("Log in to TeamCity")

        page.locator("#username").fill(admin_username)
        page.locator("#password").fill(admin_username)
        page.get_by_role("button", name="Log in").click()

        expect(page.locator("#errorMessage")).to_be_visible()
        expect(page.locator("#errorMessage")).to_have_text("Incorrect username or password.")

    @allure.id("53")
    @allure.title("UI — логин с пустым логином и паролем")
    def test_login_with_empty_credentials(self, page: Page):
        page.set_viewport_size({"width": 1920, "height": 1080})
        page.goto(f"{self.UI_BASE_URL}/login.html", wait_until="domcontentloaded")
        expect(page.locator("#header")).to_be_visible()
        expect(page.locator("#header")).to_have_text("Log in to TeamCity")

        page.get_by_role("button", name="Log in").click()

        # Остаёмся на странице логина
        expect(page.locator("#errorMessage")).to_be_visible()
        expect(page.locator("#errorMessage")).to_have_text("Incorrect username or password.")
        expect(page).to_have_url(f"{self.UI_BASE_URL}/login.html")
        expect(page.locator("#header")).to_be_visible()

    @allure.id("55")
    @allure.title("UI — логаут админа")
    def test_admin_logout(self, page: Page, admin_username: str, admin_password: str):
        page.set_viewport_size({"width": 1920, "height": 1080})
        page.goto(f"{self.UI_BASE_URL}/login.html", wait_until="domcontentloaded")
        expect(page.locator("#header")).to_be_visible()
        expect(page.locator("#header")).to_have_text("Log in to TeamCity")

        page.locator("#username").fill(admin_username)
        page.locator("#password").fill(admin_password)
        page.get_by_role("button", name="Log in").click()

        page.get_by_role("button", name=admin_username).click()
        page.get_by_text("Log out").click()

        expect(page).to_have_url(f"{self.UI_BASE_URL}/login.html")
        expect(page.locator("#header")).to_be_visible()
        expect(page.locator("#header")).to_be_visible()
        expect(page.locator("#header")).to_have_text("Log in to TeamCity")

    @allure.id("56")
    @allure.title("UI — 5 раз неверный логинг")
    def test_five_time_loging_get_error(self, page: Page):
        page.set_viewport_size({"width": 1920, "height": 1080})
        page.goto(f"{self.UI_BASE_URL}/login.html", wait_until="domcontentloaded")
        expect(page.locator("#header")).to_be_visible()
        expect(page.locator("#header")).to_have_text("Log in to TeamCity")

        page.locator("#username").fill(RandomData.get_name())
        page.get_by_role("button", name="Log in").click()
        page.get_by_role("button", name="Log in").click()
        page.get_by_role("button", name="Log in").click()
        page.get_by_role("button", name="Log in").click()
        page.get_by_role("button", name="Log in").click()
        page.get_by_role("button", name="Log in").click()

        expect(page.locator("#errorMessage")).to_be_visible()
        expect(page.locator("#errorMessage")).to_contain_text("You made 5 failed login attempts in 1m.")
        expect(page).to_have_url(f"{self.UI_BASE_URL}/login.html")
        expect(page.locator("#header")).to_be_visible()
