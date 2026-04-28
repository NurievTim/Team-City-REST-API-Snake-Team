from src.models.requests import CreateBuildTypeRequest, QueueBuildRequest
from src.models.responses import BuildTypeResponse, QueueBuildResponse
from src.requests.skeleton.endpoint import Endpoint
from src.requests.skeleton.requesters.crud_requester import CrudRequester


class BuildRequester(CrudRequester):

    def create_build_type(self, create_build_type_request: CreateBuildTypeRequest) -> BuildTypeResponse:
        return self.post(model=create_build_type_request, endpoint=Endpoint.CREATE_BUILD_TYPE)

    def queue_build(self, queue_build_request: QueueBuildRequest) -> QueueBuildResponse:
        return self.post(model=queue_build_request, endpoint=Endpoint.QUEUE_BUILD)

