from src.models.requests import CreateBuildTypeRequest, QueueBuildRequest
from src.models.responses import BuildTypeResponse, QueueBuildResponse
from src.requests.skeleton.endpoint import Endpoint
from src.requests.skeleton.requesters.crud_requester import CrudRequester
from src.specs.response_spec import ResponseSpecs


class BuildRequester(CrudRequester):

    def create_build_type(self, create_build_type_request: CreateBuildTypeRequest) -> BuildTypeResponse:
        response = self.post(model=create_build_type_request, endpoint=Endpoint.CREATE_BUILD_TYPE)
        return BuildTypeResponse(**response.json())

    def queue_build(self, queue_build_request: QueueBuildRequest) -> QueueBuildResponse:
        response = self.post(model=queue_build_request, endpoint=Endpoint.QUEUE_BUILD)
        return QueueBuildResponse(**response.json())

    def delete_build_type(self, build_type_id: str) -> None:
        previous_spec = self.response_spec
        try:
            self.response_spec = ResponseSpecs.entity_was_deleted()
            self.delete(locator=f'id:{build_type_id}', endpoint=Endpoint.CREATE_BUILD_TYPE)
        finally:
            self.response_spec = previous_spec
