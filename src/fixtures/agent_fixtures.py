import pytest

from src.classes.api_manager import ApiManager
from src.fixtures.api_fixtures import api_manager
from src.models.responses import AgentResponse


@pytest.fixture()
def get_disable_agent(api_manager) -> AgentResponse:
    agents = api_manager.agent_steps.get_disabled_agents()
    return agents.agent[0]



@pytest.fixture()
def enable_agent(get_disable_agent: AgentResponse, api_manager: ApiManager) -> None:
    api_manager.agent_steps.enable_agent(get_disable_agent)
