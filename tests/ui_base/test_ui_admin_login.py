import allure
import pytest
from playwright.sync_api import Page, expect

from src.ui_pages.login_page import LoginPage
from src.ui_pages.project_page import ProjectPanel


@pytest.mark.ui
class TestLoginAdmin:
    @allure.id("51")
    @allure.title("UI — логин админа с корректными данными")
    def test_admin_login_with_correct_data(self, page, admin_username, admin_password):
        project_panel = (
            LoginPage(page).open()
            .admin_login_with_correct_data(admin_username, admin_password)
            .get_page(ProjectPanel)
        )

        expect(project_panel.project_wellcome_text.or_(project_panel.favorite_projects_text)).to_be_visible()

    @allure.id("52")
    @allure.title("UI — логин с неверным паролем")
    def test_admin_login_with_wrong_password(self, page: Page, admin_username):
        LoginPage(page).open().admin_login_with_wrong_password(admin_username).check_incorrect_data_error()

    @allure.id("53")
    @allure.title("UI — логин с пустым логином и паролем")
    def test_login_with_empty_credentials(self, page: Page):
        LoginPage(page).open().click_login_button().check_incorrect_data_error()

    @allure.id("55")
    @allure.title("UI — логаут админа")
    def test_admin_logout(self, page: Page, admin_username, admin_password):
        project_panel = (
            LoginPage(page).open()
            .admin_login_with_correct_data(admin_username, admin_password)
            .get_page(ProjectPanel)
        )

        project_panel.click_go_to_log_out().check_text_login_to_tc()

    @allure.id("56")
    @allure.title("UI — 5 раз неверный логинг, получаем ошибку лимита авторизации")
    def test_five_time_loging_get_error(self, page: Page):
        LoginPage(page).open() \
            .admin_login_multiple_times(times=6) \
            .check_limit_auth_error()
