from src.models.comparison.model_assertions import ModelAssertions
from src.models.requests import QueueBuildRequest, BuildCancelRequest
from src.models.responses import QueueBuildResponse
from src.requests.skeleton.endpoint import Endpoint
from src.requests.skeleton.requesters.validated_crud_requester import ValidatedCrudRequester
from src.specs.response_spec import ResponseSpecs
from src.steps.base_steps import BaseSteps
from src.specs.request_spec import RequestSpecs


class BuildQueueSteps(BaseSteps):
    def add_build_to_queue(self, queue_build_request: QueueBuildRequest):
        add_build_to_queue_response: QueueBuildResponse = ValidatedCrudRequester(
            RequestSpecs.admin_base_headers(),
            Endpoint.QUEUE_BUILD,
            ResponseSpecs.request_return_ok()
        ).post(queue_build_request)
        ModelAssertions(queue_build_request, add_build_to_queue_response).match()

        assert add_build_to_queue_response.state == 'Queued'
        return add_build_to_queue_response

    def cancel_queued_build(self, cancel_queued_build_request: BuildCancelRequest, locator: str):
        cancel_queued_build_response: QueueBuildResponse = ValidatedCrudRequester(
            RequestSpecs.admin_base_headers(),
            Endpoint.CANCEL_QUEUED_BUILD,
            ResponseSpecs.request_return_ok()
        ).post(cancel_queued_build_request, locator)

        ModelAssertions(cancel_queued_build_request, cancel_queued_build_response).match()

        return cancel_queued_build_response