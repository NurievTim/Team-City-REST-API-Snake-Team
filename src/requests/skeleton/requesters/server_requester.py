from typing import Optional

from src.models.responses import ServerInfoResponse, CurrentUserResponse
from src.requests.skeleton.endpoint import Endpoint
from src.requests.skeleton.requesters.crud_requester import CrudRequester


class ServerRequester(CrudRequester):

    def get_server_info(self) -> Optional[ServerInfoResponse]:
        response = self.get(endpoint=Endpoint.GET_SERVER_INFO)
        if not response.ok:
            return None
        return ServerInfoResponse(**response.json())

    def get_current_user(self) -> Optional[CurrentUserResponse]:
        response = self.get(endpoint=Endpoint.GET_CURRENT_USER)
        if not response.ok:
            return None
        return CurrentUserResponse(**response.json())
