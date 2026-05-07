from src.models.requests import CreateVcsRootRequest
from src.models.responses import VcsRootResponse
from src.requests.skeleton.endpoint import Endpoint
from src.requests.skeleton.requesters.validated_crud_requester import ValidatedCrudRequester
from src.specs.request_spec import RequestSpecs
from src.specs.response_spec import ResponseSpecs
from src.steps.base_steps import BaseSteps


class VcsRootSteps(BaseSteps):

    def create_vcs_root(self, create_vcs_root_request: CreateVcsRootRequest) -> VcsRootResponse:
        vcs_root: VcsRootResponse = ValidatedCrudRequester(
            RequestSpecs.admin_base_headers(),
            Endpoint.CREATE_VCS_ROOT,
            ResponseSpecs.request_return_ok(),
        ).post(create_vcs_root_request)
        self.created_objects.append(vcs_root)
        return vcs_root

    def get_vcs_root_by_id(self, vcs_root_id: str) -> VcsRootResponse:
        vcs_root: VcsRootResponse = ValidatedCrudRequester(
            RequestSpecs.admin_base_headers(),
            Endpoint.GET_VCS_ROOT,
            ResponseSpecs.request_return_ok(),
        ).get(locator=f'id:{vcs_root_id}')

        assert vcs_root.id == vcs_root_id
        return vcs_root

    def delete_vcs_root(self, vcs_root_id: str) -> None:
        ValidatedCrudRequester(
            RequestSpecs.admin_base_headers(),
            Endpoint.DELETE_VCS_ROOT,
            ResponseSpecs.entity_was_deleted(),
        ).delete(locator=f'id:{vcs_root_id}')
