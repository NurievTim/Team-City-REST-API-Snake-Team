from http import HTTPStatus

from src.models.responses import AgentsListResponse
from src.requests.requester import BaseRequester


class AgentRequester(BaseRequester):

    def get_authorized_agents(self) -> AgentsListResponse:
        response = self._get_with_params('agents', params={'locator': 'authorized:true'})
        if response.status_code == HTTPStatus.OK:
            return AgentsListResponse(**response.json())

