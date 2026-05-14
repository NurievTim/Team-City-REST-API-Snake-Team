import allure
import pytest
from playwright.sync_api import Page, expect

from src.enums import UiAlert
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
        login_page = LoginPage(page).open()
        login_page.admin_login_with_wrong_password(admin_username)

        login_page.check_incorrect_data_error()

    @allure.id("53")
    @allure.title("UI — логин с пустым логином и паролем")
    def test_login_with_empty_credentials(self, page: Page):
        login_page = LoginPage(page).open()
        login_page.click_login_button()

        login_page.check_incorrect_data_error()

    @allure.id("55")
    @allure.title("UI — логаут админа")
    def test_admin_logout(self, page: Page, admin_username, admin_password):
        login_page = self.auth_as_admin(page, admin_username, admin_password)
        login_page.get_page(ProjectPanel).click_go_to_log_out()

        login_page.check_text_login_to_tc()

    @allure.id("56")
    @allure.title("UI — 5 раз неверный логинг, получаем ошибку лимита авторизации")
    def test_five_time_loging_get_error(self, page: Page):
        login_page = LoginPage(page).open()
        login_page.admin_name_input.fill(RandomData.get_name())

        for x in range(6):
            login_page.admin_password_input.fill(RandomData.get_password())
            login_page.click_login_button()

        login_page.check_limit_auth_error()

