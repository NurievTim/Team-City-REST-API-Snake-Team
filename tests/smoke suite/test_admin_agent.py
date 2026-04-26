import allure
import pytest
import requests

from dotenv import load_dotenv
from src.models.responses import AgentsListResponse
from src.specs.request_spec import RequestSpecs

load_dotenv()


@pytest.mark.smoke
class TestAgents:

    @allure.id("7")   # В окружении есть хотя бы один авторизованный агент
    @allure.title("GET /agents?locator=authorized:true — HTTP 200, >= 1 авторизованный агент")
    def test_get_authorized_agents(self):
        response = requests.get(
            url=f'{RequestSpecs.BASE_URL}agents',
            headers=RequestSpecs.admin_base_headers()['headers'],
            params={'locator': 'authorized:true'},
        )

        assert response.status_code == 200
        body = AgentsListResponse(**response.json())
        assert body.count >= 1
