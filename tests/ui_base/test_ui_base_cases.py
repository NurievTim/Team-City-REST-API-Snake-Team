import allure
import pytest
from playwright.sync_api import Page, expect

from src.generators.random_data import RandomData
from src.ui_pages.login_page import LoginPage
from src.ui_pages.project_page import ProjectPanel
from tests.ui_base.test_ui_base import BaseUITest


@pytest.mark.ui
class TestLoginAdmin(BaseUITest):
    @allure.id("51")
    @allure.title("UI — логин админа с корректными данными")
    def test_admin_login_with_correct_data(self, page, admin_username, admin_password):
        login_page = self.auth_as_admin(page, admin_username, admin_password)
        project_panel = login_page.get_page(ProjectPanel)
        expect(project_panel.project_wellcome_text.or_(project_panel.favorite_projects_text)).to_be_visible()

    @allure.id("52")
    @allure.title("UI — логин с неверным паролем")
    def test_admin_login_with_wrong_password(self, page: Page, admin_username):
        page.set_viewport_size({"width": 1920, "height": 1080})
        login_page = LoginPage(page).open()
        login_page.admin_login_with_wrong_password(admin_username)

        expect(login_page.error_message).to_be_visible()
        expect(login_page.error_message).to_have_text("Incorrect username or password.")

    @allure.id("53")
    @allure.title("UI — логин с пустым логином и паролем")
    def test_login_with_empty_credentials(self, page: Page):
        page.set_viewport_size({"width": 1920, "height": 1080})
        login_page = LoginPage(page).open()
        login_page.click_login_button()

        expect(login_page.error_message).to_be_visible()
        expect(login_page.error_message).to_have_text("Incorrect username or password.")

    @allure.id("55")
    @allure.title("UI — логаут админа")
    def test_admin_logout(self, page: Page, admin_username, admin_password):
        login_page = self.auth_as_admin(page, admin_username, admin_password)

        login_page.get_page(ProjectPanel).click_go_to_log_out()

        expect(login_page.login_to_teamcity_text).to_be_visible()
        expect(login_page.login_to_teamcity_text).to_have_text("Log in to TeamCity")

    @allure.id("56")
    @allure.title("UI — 5 раз неверный логинг")
    def test_five_time_loging_get_error(self, page: Page):
        page.set_viewport_size({"width": 1920, "height": 1080})
        login_page = LoginPage(page).open()
        login_page.admin_name_input.fill(RandomData.get_name())

        for _ in range(6):
            login_page.admin_password_input.fill(RandomData.get_password())
            login_page.click_login_button()

        expect(login_page.error_message).to_be_visible()
        expect(login_page.error_message).to_contain_text("You made 5 failed login attempts in 1m.")

