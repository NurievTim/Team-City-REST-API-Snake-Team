from src.models.requests import CreateProjectRequest
from src.models.responses import ProjectsListResponse, ProjectResponse
from src.requests.skeleton.endpoint import Endpoint
from src.requests.skeleton.requesters.crud_requester import CrudRequester


class ProjectRequester(CrudRequester):

    def get_projects(self) -> ProjectsListResponse:
        return self.get(endpoint=Endpoint.GET_PROJECTS)

    def create_project(self, create_project_request: CreateProjectRequest) -> ProjectResponse:
        return self.post(model=create_project_request, endpoint=Endpoint.CREATE_PROJECT)

    def delete_project(self, project_id: str) -> None:
        self.delete(locator=f'id:{project_id}', endpoint=Endpoint.DELETE_PROJECT)
