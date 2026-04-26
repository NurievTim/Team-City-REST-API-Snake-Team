import os
import allure
import pytest
import requests

from dotenv import load_dotenv

load_dotenv()


@pytest.mark.smoke
class TestAgents:

    @allure.id("7")   # В окружении есть хотя бы один авторизованный агент
    @allure.title("GET /agents?locator=authorized:true — HTTP 200, >= 1 авторизованный агент")
    def test_get_authorized_agents(self):
        response = requests.get(
            url=f'http://localhost:8111/app/rest/agents',
            headers={
                'Authorization': f'Bearer {os.getenv("TC_ADMIN_TOKEN")}',
                'Content-Type': 'application/json',
                'Accept': 'application/json',
            },
            params={'locator': 'authorized:true'},
        )

        assert response.status_code == 200
        assert response.json().get('count') >= 1
