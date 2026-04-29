from http import HTTPStatus

from src.models.responses import ServerInfoResponse, CurrentUserResponse
from src.requests.requester import BaseRequester


class ServerRequester(BaseRequester):
    def get_server_info(self) -> ServerInfoResponse:
        response = self._get('server')
        if response.status_code == HTTPStatus.OK:
            return ServerInfoResponse(**response.json())

    def get_current_user(self) -> CurrentUserResponse:
        response = self._get('users/current')
        if response.status_code == HTTPStatus.OK:
            return CurrentUserResponse(**response.json())

