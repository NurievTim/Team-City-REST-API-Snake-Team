from http import HTTPStatus

from src.models.requests import CreateBuildTypeRequest, QueueBuildRequest
from src.models.responses import BuildTypeResponse, QueueBuildResponse
from src.requests.requester import BaseRequester


class BuildRequester(BaseRequester):

    def create_build_type(self, create_build_type_request: CreateBuildTypeRequest) -> BuildTypeResponse:
        response = self._post('buildTypes', create_build_type_request)
        if response.status_code == HTTPStatus.OK:
            return BuildTypeResponse(**response.json())

    def queue_build(self, queue_build_request: QueueBuildRequest) -> QueueBuildResponse:
        response = self._post('buildQueue', queue_build_request)
        if response.status_code == HTTPStatus.OK:
            return QueueBuildResponse(**response.json())

