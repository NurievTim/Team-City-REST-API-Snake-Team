from src.models.responses import AgentsListResponse, AgentResponse
from src.requests.skeleton.endpoint import Endpoint
from src.requests.skeleton.requesters.validated_crud_requester import ValidatedCrudRequester
from src.specs.request_spec import RequestSpecs
from src.specs.response_spec import ResponseSpecs
from src.steps.base_steps import BaseSteps


class AgentSteps(BaseSteps):
    def get_enabled_agents(self) -> AgentsListResponse:
        agents: AgentsListResponse = ValidatedCrudRequester(
            RequestSpecs.admin_base_headers(),
            Endpoint.GET_LIST_AGENTS,
            ResponseSpecs.request_return_ok(),
        ).get(params={'locator': 'enabled:true'})

        return agents

    def get_disabled_agents(self) -> AgentsListResponse:
        agents: AgentsListResponse = ValidatedCrudRequester(
            RequestSpecs.admin_base_headers(),
            Endpoint.GET_LIST_AGENTS,
            ResponseSpecs.request_return_ok(),
        ).get(params={'locator': 'enabled:false'})

        return agents

    def get_agent_by_id(self, locator: int):
        agent: AgentResponse = ValidatedCrudRequester(
            RequestSpecs.admin_base_headers(),
            Endpoint.GET_AGENT,
            ResponseSpecs.request_return_ok(),
        ).get(locator=f'id:{locator}')

        return agent

    def enable_agent(self, agent_response: AgentResponse) -> None:
        ValidatedCrudRequester(
            RequestSpecs.admin_base_headers(),
            Endpoint.GET_AGENT,
            ResponseSpecs.request_return_ok(),
        ).put(locator=f'id:{agent_response.id}/enabled', body='true')
        self.created_objects.append(agent_response)

    def disable_agent(self, agent_response: AgentResponse) -> None:
        ValidatedCrudRequester(
            RequestSpecs.admin_base_headers(),
            Endpoint.GET_AGENT,
            ResponseSpecs.request_return_ok(),
        ).put(locator=f'id:{agent_response.id}/enabled', body='false')
