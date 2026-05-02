from src.models.comparison.model_assertions import ModelAssertions
from src.models.requests import QueueBuildRequest, BuildCancelRequest, CreateBuildTypeRequest
from src.models.responses import QueueBuildResponse, BuildTypeResponse
from src.requests.skeleton.endpoint import Endpoint
from src.requests.skeleton.requesters.validated_crud_requester import ValidatedCrudRequester
from src.specs.request_spec import RequestSpecs
from src.specs.response_spec import ResponseSpecs
from src.steps.base_steps import BaseSteps


class BuildQueueSteps(BaseSteps):

    def create_build_type(self, create_build_type_request: CreateBuildTypeRequest) -> BuildTypeResponse:
        build_type: BuildTypeResponse = ValidatedCrudRequester(
            RequestSpecs.admin_base_headers(),
            Endpoint.CREATE_BUILD_TYPE,
            ResponseSpecs.entity_was_created(),
        ).post(create_build_type_request)

        ModelAssertions(create_build_type_request, build_type).match()
        return build_type

    def get_build_type_by_id(self, build_type_id: str) -> BuildTypeResponse:
        build_type: BuildTypeResponse = ValidatedCrudRequester(
            RequestSpecs.admin_base_headers(),
            Endpoint.GET_BUILD_TYPE,
            ResponseSpecs.request_return_ok(),
        ).get(locator=build_type_id)

        assert build_type.id == build_type_id
        return build_type

    def add_build_to_queue(self, queue_build_request: QueueBuildRequest) -> QueueBuildResponse:
        add_build_to_queue_response: QueueBuildResponse = ValidatedCrudRequester(
            RequestSpecs.admin_base_headers(),
            Endpoint.QUEUE_BUILD,
            ResponseSpecs.request_return_ok()
        ).post(queue_build_request)
        ModelAssertions(queue_build_request, add_build_to_queue_response).match()

        assert add_build_to_queue_response.state == 'Queued'
        return add_build_to_queue_response

    def get_queued_build_by_id(self, build_id: int) -> QueueBuildResponse:
        queued_build: QueueBuildResponse = ValidatedCrudRequester(
            RequestSpecs.admin_base_headers(),
            Endpoint.GET_QUEUED_BUILD,
            ResponseSpecs.request_return_ok(),
        ).get(locator=str(build_id))

        assert queued_build.id == build_id
        return queued_build

    def cancel_queued_build(self, cancel_queued_build_request: BuildCancelRequest, locator: str):
        cancel_queued_build_response: QueueBuildResponse = ValidatedCrudRequester(
            RequestSpecs.admin_base_headers(),
            Endpoint.CANCEL_QUEUED_BUILD,
            ResponseSpecs.request_return_ok()
        ).post(cancel_queued_build_request, locator)

        ModelAssertions(cancel_queued_build_request, cancel_queued_build_response).match()

        return cancel_queued_build_response
