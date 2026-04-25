import os
import allure
import pytest

from hamcrest import assert_that, not_none, equal_to
from framework.steps.admin_steps import AdminSteps


@pytest.mark.smoke
class TestServer:

    @allure.id("1")    # сервер отвечает и возвращает версию
    @allure.title("GET /server — HTTP 200, поле version присутствует")
    def test_get_server_info(self, admin_steps: AdminSteps) -> None:
        body = admin_steps.get_server_info_with_version()

        assert_that(body.get("version"), not_none(), "Поле version отсутствует в ответе")

    @allure.id("2")     # токен соответствует ожидаемому пользователю
    @allure.title("GET /users/current — HTTP 200, username совпадает с TC_ADMIN_USERNAME")
    def test_get_current_user(self, admin_steps: AdminSteps, ) -> None:
        expected = os.getenv("TC_ADMIN_USERNAME")
        if not expected:
            pytest.skip("Переменная окружения TC_ADMIN_USERNAME не задана")
        user = admin_steps.get_current_user_and_check_username()

        assert_that(user, equal_to(expected), f'username ожидался «{expected}», получен «{user}»')

