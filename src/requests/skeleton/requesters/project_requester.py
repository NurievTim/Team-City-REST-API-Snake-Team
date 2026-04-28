from typing import Optional

from src.models.requests import CreateProjectRequest
from src.models.responses import ProjectsListResponse, ProjectResponse
from src.requests.skeleton.endpoint import Endpoint
from src.requests.skeleton.requesters.crud_requester import CrudRequester
from src.specs.response_spec import ResponseSpecs


class ProjectRequester(CrudRequester):

    def get_projects(self) -> Optional[ProjectsListResponse]:
        response = self.get(endpoint=Endpoint.GET_PROJECTS)
        if not response.ok:
            return None
        return ProjectsListResponse(**response.json())

    def create_project(self, create_project_request: CreateProjectRequest) -> Optional[ProjectResponse]:
        response = self.post(model=create_project_request, endpoint=Endpoint.CREATE_PROJECT)
        if not response.ok:
            return None
        return ProjectResponse(**response.json())

    def delete_project(self, project_id: str) -> None:
        previous_spec = self.response_spec
        try:
            self.response_spec = ResponseSpecs.entity_was_deleted()
            self.delete(locator=f'id:{project_id}', endpoint=Endpoint.DELETE_PROJECT)
        finally:
            self.response_spec = previous_spec
