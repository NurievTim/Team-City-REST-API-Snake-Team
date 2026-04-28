from src.models.responses import ServerInfoResponse, CurrentUserResponse
from src.requests.skeleton.endpoint import Endpoint
from src.requests.skeleton.requesters.crud_requester import CrudRequester


class ServerRequester(CrudRequester):

    def get_server_info(self) -> ServerInfoResponse:
        return self.get(endpoint=Endpoint.GET_SERVER_INFO)

    def get_current_user(self) -> CurrentUserResponse:
        return self.get(endpoint=Endpoint.GET_CURRENT_USER)

