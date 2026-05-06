import pytest

from src.classes.api_manager import ApiManager
from src.fixtures.api_fixtures import api_manager
from src.models.responses import AgentsListResponse


@pytest.fixture()
def get_disable_agent(api_manager) -> AgentsListResponse:
    return api_manager.agent_steps.get_disabled_agents()


@pytest.fixture()
def enable_agent(get_disable_agent: AgentsListResponse, api_manager: ApiManager) -> None:
    api_manager.agent_steps.enable_agent(get_disable_agent.agent[0].id)
