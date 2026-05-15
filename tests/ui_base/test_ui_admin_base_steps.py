import allure
import pytest

from src.ui_pages.login_page import LoginPage


@pytest.mark.ui
class TestLoginAdmin:
    @allure.id("57")
    @allure.title("UI — админ жмёт кнопку создать проект через wellcome button")
    def test_admin_click_welcome_create_project_button(self, page, admin_username, admin_password):
        LoginPage(page).open() \
            .admin_login_with_correct_data(admin_username, admin_password) \
            .click_create_project_wellcome_button() \
            .check_new_project_create_page()

    @allure.id("58")
    @allure.title("UI — админ жмёт кнопку создать проект через main button")
    def test_admin_click_main_create_project_button(self, page, admin_username, admin_password):
        LoginPage(page).open() \
            .admin_login_with_correct_data(admin_username, admin_password) \
            .click_create_project_main_button() \
            .check_new_project_create_page()

    # @allure.id("59")  # появится вместо приветсвенной кнопки создать проект
    # @allure.title("UI — админ жмёт кнопку создать проект через dropdown button")
    # def test_admin_click_dropdown__create_project_button(self, page, admin_username, admin_password):
    #     LoginPage(page).open() \
    #         .admin_login_with_correct_data(admin_username, admin_password) \
    #         .click_create_project_dropdown_button() \
    #         .check_new_project_create_page()

    @allure.id("60")
    @allure.title("UI — админ жмёт кнопку Changes")
    def test_admin_click_changes_button(self, page, admin_username, admin_password):
        LoginPage(page).open() \
            .admin_login_with_correct_data(admin_username, admin_password) \
            .click_switch_to_changes() \
            .check_changes_page()
