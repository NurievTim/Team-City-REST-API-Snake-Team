import os
import allure
import pytest
import requests
from dotenv import load_dotenv

load_dotenv()


@pytest.mark.smoke
class TestServer:

    @allure.id("1")  # сервер отвечает и возвращает версию
    @allure.title("GET /server — HTTP 200, поле version присутствует")
    def test_get_server_info(self):
        response = requests.get(
            url=f'http://localhost:8111/app/rest/server',
            headers={
                'Authorization': f'Bearer {os.getenv("TC_ADMIN_TOKEN")}',
                'Content-Type': 'application/json',
                'Accept': 'application/json',
            }
        )

        assert response.status_code == 200
        assert response.json().get('version') is not None

    @allure.id("2")  # токен соответствует ожидаемому пользователю
    @allure.title("GET /users/current — HTTP 200, username совпадает с TC_ADMIN_USERNAME")
    def test_get_current_user(self):
        response = requests.get(
            url='http://localhost:8111/app/rest/users/current',
            headers={
                'Authorization': f'Bearer {os.getenv("TC_ADMIN_TOKEN")}',
                'Content-Type': 'application/json',
                'Accept': 'application/json',
            }
        )

        assert response.status_code == 200
        assert response.json().get('username') == os.getenv('TC_ADMIN_USERNAME')

