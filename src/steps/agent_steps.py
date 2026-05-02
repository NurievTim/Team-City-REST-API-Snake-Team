from src.models.responses import AgentsListResponse
from src.requests.skeleton.endpoint import Endpoint
from src.requests.skeleton.requesters.validated_crud_requester import ValidatedCrudRequester
from src.specs.request_spec import RequestSpecs
from src.specs.response_spec import ResponseSpecs


class AgentSteps:
    def get_authorized_agents(self) -> AgentsListResponse:
        agents: AgentsListResponse = ValidatedCrudRequester(
            RequestSpecs.admin_base_headers(),
            Endpoint.GET_AGENT,
            ResponseSpecs.request_return_ok(),
        ).get(params={'locator': 'authorized:true'})

        assert agents.count >= 1, f"Ожидался count >= 1, получен count={agents.count}"
        return agents
