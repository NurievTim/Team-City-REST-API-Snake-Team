import allure
import pytest


from src.specs.request_spec import RequestSpecs
from src.specs.response_spec import ResponseSpecs


@pytest.mark.smoke
class TestAgents:

    @allure.id("7")   # В окружении есть хотя бы один авторизованный агент
    @allure.title("GET /agents?locator=authorized:true — HTTP 200, >= 1 авторизованный агент")
    def test_get_authorized_agents(self):
        agents = AgentRequester(
            RequestSpecs.admin_base_headers(),
            ResponseSpecs.request_return_ok(),
        ).get_authorized_agents()

        assert agents.count >= 1
