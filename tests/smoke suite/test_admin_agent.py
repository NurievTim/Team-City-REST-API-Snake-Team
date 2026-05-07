import allure
import pytest

from src.classes.api_manager import ApiManager


@pytest.mark.smoke
class TestAgents:

    @allure.id("7")  # В окружении есть хотя бы один авторизованный агент
    @allure.title("GET /agents?locator=authorized:true — HTTP 200, >= 1 авторизованный агент")
    def test_get_authorized_agents(self, api_manager: ApiManager):
        agents = api_manager.agent_steps.get_authorized_agents()
        assert agents.count >= 1
