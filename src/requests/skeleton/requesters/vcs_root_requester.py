from src.models.requests import CreateVcsRootRequest
from src.models.responses import VcsRootResponse
from src.requests.skeleton.endpoint import Endpoint
from src.requests.skeleton.requesters.crud_requester import CrudRequester
from src.specs.response_spec import ResponseSpecs


class VcsRootRequester(CrudRequester):
    def create_vcs_root(self, create_vcs_root_request: CreateVcsRootRequest) -> VcsRootResponse:
        response = self.post(model=create_vcs_root_request, endpoint=Endpoint.CREATE_VCS_ROOT)
        return VcsRootResponse(**response.json())

    def delete_vcs_root(self, vcs_root_id: str) -> None:
        previous_spec = self.response_spec
        try:
            self.response_spec = ResponseSpecs.entity_was_deleted()
            self.delete(locator=f"id:{vcs_root_id}", endpoint=Endpoint.CREATE_VCS_ROOT)
        finally:
            self.response_spec = previous_spec
