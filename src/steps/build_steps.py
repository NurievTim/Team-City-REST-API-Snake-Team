from src.models.comparison.model_assertions import ModelAssertions
from src.models.requests import QueueBuildRequest, BuildCancelRequest, CreateBuildTypeRequest, CopyBuildTypeRequest
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

    def delete_build_type(self, build_type_id: str) -> None:
        ValidatedCrudRequester(
            RequestSpecs.admin_base_headers(),
            Endpoint.CREATE_BUILD_TYPE,
            ResponseSpecs.entity_was_deleted(),
        ).delete(locator=f'id:{build_type_id}')

    def get_build_type_paused(self, build_type_id: str) -> bool:
        response = ValidatedCrudRequester(
            RequestSpecs.admin_base_headers(),
            Endpoint.GET_BUILD_TYPE,
            ResponseSpecs.request_return_ok(),
        ).crud_requester.get(locator=f'{build_type_id}/paused', accept='text/plain')
        return response.text.strip().lower() == 'true'

    def set_build_type_paused(self, build_type_id: str, paused: bool) -> None:
        ValidatedCrudRequester(
            RequestSpecs.admin_base_headers(),
            Endpoint.GET_BUILD_TYPE,
            ResponseSpecs.request_return_ok(),
        ).put(locator=f'{build_type_id}/paused', body=str(paused).lower())

    def get_build_type_parameter(self, build_type_id: str, param_name: str) -> dict:
        response = ValidatedCrudRequester(
            RequestSpecs.admin_base_headers(),
            Endpoint.GET_BUILD_TYPE,
            ResponseSpecs.request_return_ok(),
        ).crud_requester.get(locator=f'{build_type_id}/parameters/{param_name}')
        return response.json()

    def set_build_type_parameter(self, build_type_id: str, param_name: str, value: str) -> None:
        ValidatedCrudRequester(
            RequestSpecs.admin_base_headers(),
            Endpoint.GET_BUILD_TYPE,
            ResponseSpecs.request_return_ok(),
        ).put(locator=f'{build_type_id}/parameters/{param_name}', body=value)

    def delete_build_type_parameter(self, build_type_id: str, param_name: str) -> None:
        ValidatedCrudRequester(
            RequestSpecs.admin_base_headers(),
            Endpoint.GET_BUILD_TYPE,
            ResponseSpecs.entity_was_deleted(),
        ).delete(locator=f'{build_type_id}/parameters/{param_name}')

    def copy_build_type_to_project(self, project_id: str, copy_request: CopyBuildTypeRequest) -> BuildTypeResponse:
        build_type: BuildTypeResponse = ValidatedCrudRequester(
            RequestSpecs.admin_base_headers(),
            Endpoint.GET_PROJECT,
            ResponseSpecs.request_return_ok(),
        ).post(copy_request, locator=f'{project_id}/buildTypes')

        return build_type

    def add_build_to_queue(self, queue_build_request: QueueBuildRequest) -> QueueBuildResponse:
        queued_build: QueueBuildResponse = ValidatedCrudRequester(
            RequestSpecs.admin_base_headers(),
            Endpoint.QUEUE_BUILD,
            ResponseSpecs.request_return_ok(),
        ).post(queue_build_request)

        assert queued_build.state == 'queued'
        return queued_build

    def get_queued_build_by_id(self, build_id: int) -> QueueBuildResponse:
        queued_build: QueueBuildResponse = ValidatedCrudRequester(
            RequestSpecs.admin_base_headers(),
            Endpoint.GET_QUEUED_BUILD,
            ResponseSpecs.request_return_ok(),
        ).get(locator=str(build_id))

        assert queued_build.id == build_id
        return queued_build

    def cancel_queued_build(self, build_id: int) -> QueueBuildResponse:
        cancel_request = BuildCancelRequest(comment='Cancelled by test cleanup', readdIntoQueue=False)
        cancelled_build: QueueBuildResponse = ValidatedCrudRequester(
            RequestSpecs.admin_base_headers(),
            Endpoint.CANCEL_QUEUED_BUILD,
            ResponseSpecs.request_return_ok(),
        ).post(cancel_request, locator=str(build_id))

        return cancelled_build
