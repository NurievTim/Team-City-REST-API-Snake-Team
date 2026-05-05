from src.enums import BuildState
from src.models.requests import QueueBuildRequest, BuildCancelRequest, CreateBuildTypeRequest
from src.models.responses import QueueBuildResponse, BuildTypeResponse
from src.requests.skeleton.endpoint import Endpoint
from src.requests.skeleton.requesters.validated_crud_requester import ValidatedCrudRequester
from src.specs.response_spec import ResponseSpecs
from src.steps.base_steps import BaseSteps
from src.specs.request_spec import RequestSpecs


class BuildSteps(BaseSteps):

    def create_build_type(self, create_build_type_request: CreateBuildTypeRequest) -> BuildTypeResponse:
        build_type: BuildTypeResponse = ValidatedCrudRequester(
            RequestSpecs.admin_base_headers(),
            Endpoint.CREATE_BUILD_TYPE,
            ResponseSpecs.request_return_ok(),
        ).post(create_build_type_request)
        self.created_objects.append(build_type)
        # ModelAssertions(create_build_type_request, build_type).match()
        return build_type

    def delete_build_type(self, build_type_id: str) -> None:
        ValidatedCrudRequester(
            RequestSpecs.admin_base_headers(),
            Endpoint.DELETE_BUILD_TYPE,
            ResponseSpecs.entity_was_deleted(),
        ).delete(locator=f'name:{build_type_id}')
        # не понятно где делать get

    def get_build_type_by_id(self, build_type_id: str) -> BuildTypeResponse:
        build_type: BuildTypeResponse = ValidatedCrudRequester(
            RequestSpecs.admin_base_headers(),
            Endpoint.GET_BUILD_TYPE,
            ResponseSpecs.request_return_ok(),
        ).get(locator=build_type_id)

        assert build_type.id == build_type_id
        return build_type

    def add_build_to_queue(self, queue_build_request: QueueBuildRequest) -> QueueBuildResponse:
        queued_build: QueueBuildResponse = ValidatedCrudRequester(
            RequestSpecs.admin_base_headers(),
            Endpoint.QUEUE_BUILD,
            ResponseSpecs.request_return_ok(),
        ).post(queue_build_request)

        assert queued_build.state == BuildState.QUEUED
        return queued_build

    def get_queued_build_by_id(self, build_id: int) -> QueueBuildResponse:
        queued_build: QueueBuildResponse = ValidatedCrudRequester(
            RequestSpecs.admin_base_headers(),
            Endpoint.GET_QUEUED_BUILD,
            ResponseSpecs.request_return_ok(),
        ).get(locator=str(build_id))

        assert queued_build.id == build_id
        return queued_build

    def cancel_queued_build(self, build_cancel_request: BuildCancelRequest, locator: str) -> QueueBuildResponse:
        build_cancel_request: QueueBuildResponse = ValidatedCrudRequester(
            RequestSpecs.admin_base_headers(),
            Endpoint.CANCEL_QUEUED_BUILD,
            ResponseSpecs.request_return_ok()
        ).post(build_cancel_request, locator)

        # ModelAssertions(cancel_queued_build_request, cancel_queued_build_response).match()
        return build_cancel_request
