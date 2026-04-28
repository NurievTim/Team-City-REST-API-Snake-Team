from src.models.responses import AgentsListResponse
from src.requests.skeleton.endpoint import Endpoint
from src.requests.skeleton.requesters.crud_requester import CrudRequester


class AgentRequester(CrudRequester):

    def get_authorized_agents(self) -> AgentsListResponse:
        return self.get(endpoint=Endpoint.GET_AGENTS, params={'locator': 'authorized:true'})


