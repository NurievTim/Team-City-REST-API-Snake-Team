import os
import allure
import pytest
import requests

from dotenv import load_dotenv
from src.specs.request_spec import RequestSpecs
from src.models.responses import ServerInfoResponse, CurrentUserResponse

load_dotenv()


@pytest.mark.smoke
class TestServer:

    @allure.id("1")  # сервер отвечает и возвращает версию
    @allure.title("GET /server — HTTP 200, поле version присутствует")
    def test_get_server_info(self):
        response = requests.get(
            url=f'{RequestSpecs.BASE_URL}server',
            headers=RequestSpecs.admin_base_headers()['headers']
        )

        assert response.status_code == 200
        body = ServerInfoResponse(**response.json())
        assert body.version is not None

    @allure.id("2")  # токен соответствует ожидаемому пользователю
    @allure.title("GET /users/current — HTTP 200, username совпадает с TC_ADMIN_USERNAME")
    def test_get_current_user(self):
        response = requests.get(
            url=f'{RequestSpecs.BASE_URL}users/current',
            headers=RequestSpecs.admin_base_headers()['headers']
        )

        assert response.status_code == 200
        body = CurrentUserResponse(**response.json())
        assert body.username == os.getenv('TC_ADMIN_USERNAME')

    @allure.id("2.1")  # отсутствует токен авторизации
    @allure.title("GET /users/current — HTTP 401, отсутсвтует или не верный токен")
    def test_get_current_user_unauthorized(self):
        response = requests.get(
            url=f'{RequestSpecs.BASE_URL}users/current',
            headers=RequestSpecs.unauth_spec()['headers'],
        )

        assert response.status_code == 401
