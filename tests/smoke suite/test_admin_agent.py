import allure
import pytest

from framework.checkers import check
from framework.steps.admin_steps import AdminSteps


@pytest.mark.smoke
class TestAgents:

    @allure.id("7")   # В окружении есть хотя бы один авторизованный агент
    @allure.title("GET /agents?locator=authorized:true — HTTP 200, >= 1 авторизованный агент")
    def test_get_authorized_agents(self, admin_steps: AdminSteps) -> None:
        response = admin_steps.get_authorized_agents()

        check.check_agent_is_authorize(response=response)
