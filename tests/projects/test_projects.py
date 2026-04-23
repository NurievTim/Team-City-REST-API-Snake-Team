import os
import allure
import pytest
import requests

from hamcrest import assert_that, greater_than_or_equal_to, not_none, equal_to
from framework.checkers import check


@pytest.mark.smoke
class TestProjectsSmoke:
    _queued_build_id: int | None = None

    @allure.id('1')
    @allure.title('GET /server — HTTP 200, version присутствует')
    def test_get_server_info(self, team_city_api_client, admin_headers):
        response = team_city_api_client.get_server_info(headers=admin_headers, check_status=None)
        check.check_status_code(response=response, expected_status_code=requests.codes.ok)
        body = response.json()
        assert_that(body.get('version'), not_none(), 'Поле version отсутствует в ответе')

    @allure.id('2')
    @allure.title('GET /users/current — HTTP 200, username совпадает с ожидаемым')
    def test_get_current_user(self, team_city_api_client, admin_headers):
        expected_username = os.getenv('TC_ADMIN_USERNAME')
        if not expected_username:
            pytest.skip("Переменная окружения TC_ADMIN_USERNAME не задана")

        response = team_city_api_client.get_current_user(headers=admin_headers, check_status=None)
        check.check_status_code(response=response, expected_status_code=requests.codes.ok)
        actual_username = response.json().get('username')
        assert_that(actual_username, equal_to(expected_username), f'username ожидался «{expected_username}», получен «{actual_username}»')

    @allure.id('3')
    @allure.title('GET /projects без токена, 401')
    def test_get_projects_without_token(self, team_city_api_client, invalid_auth_headers):
        response = team_city_api_client.get_projects(headers=invalid_auth_headers, check_status=None)
        check.check_status_code(response=response, expected_status_code=requests.codes.unauthorized)

    @allure.id('4')
    @allure.title('POST /buildQueue — HTTP 200, state=queued')
    def test_add_build_to_queue(self, team_city_api_client, admin_headers):
        build_type_id = os.getenv('TC_BUILD_TYPE_ID')
        if not build_type_id:
            pytest.skip("Переменная окружения TC_BUILD_TYPE_ID не задана")

        payload = {'buildType': {'id': build_type_id}}
        response = team_city_api_client.add_build_to_queue(headers=admin_headers, data=payload, check_status=None)
        check.check_status_code(response=response, expected_status_code=requests.codes.ok)
        body = response.json()
        assert_that(body.get('state'), equal_to('queued'), 'state == «queued»')
        TestProjectsSmoke._queued_build_id = body.get('id')   # Сохраняем id для теста №5

    @allure.id('5')
    @allure.title('GET /builds/{id} — HTTP 200, state=running')
    def test_get_running_build(self, team_city_api_client, admin_headers):
        # Используем id из теста №4; если не получили — берём явный env-параметр
        build_id = TestProjectsSmoke._queued_build_id or os.getenv('TC_RUNNING_BUILD_ID')
        if not build_id:
            pytest.skip("build_id недоступен: тест №4 не выполнялся либо переменная TC_RUNNING_BUILD_ID не задана")

        response = team_city_api_client.get_build(build_locator=str(build_id), headers=admin_headers, check_status=None)
        check.check_status_code(response=response, expected_status_code=requests.codes.ok)
        actual_state = response.json().get('state')
        assert_that(actual_state, equal_to('running'), f'state должен быть «running», получен «{actual_state}»')

    @allure.id('6')
    @allure.title('GET /projects — HTTP 200, count >= 1')
    def test_get_projects(self, team_city_api_client, admin_headers):
        response = team_city_api_client.get_projects(headers=admin_headers, check_status=None)
        check.check_status_code(response=response, expected_status_code=requests.codes.ok)

        count = response.json().get('count', 0)
        assert_that(count, greater_than_or_equal_to(1), 'count >= 1')

    @allure.id('7')
    @allure.title('GET /agents?locator=authorized:true — HTTP 200, ≥1 авторизованный агент')
    def test_get_authorized_agents(self, team_city_api_client, admin_headers):
        response = team_city_api_client.get_agents(headers=admin_headers, params={'locator': 'authorized:true'}, check_status=None)
        check.check_status_code(response=response, expected_status_code=requests.codes.ok)

        count = response.json().get('count', 0)
        assert_that(count, greater_than_or_equal_to(1))  # Должен быть хотя бы 1 авторизованный агент



