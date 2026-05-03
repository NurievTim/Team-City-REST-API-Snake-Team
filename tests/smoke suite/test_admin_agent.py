import allure
import pytest

from src.steps.agent_steps import AgentSteps


@pytest.mark.smoke
class TestAgents:

    @allure.id("7")  # В окружении есть хотя бы один авторизованный агент
    @allure.title("GET /agents?locator=authorized:true — HTTP 200, >= 1 авторизованный агент")
    def test_get_authorized_agents(self):
        get_agent = AgentSteps().get_authorized_agents()

        assert get_agent.count >= 1

