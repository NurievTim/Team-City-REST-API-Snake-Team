from http import HTTPStatus

from src.models.requests import CreateProjectRequest
from src.models.responses import ProjectsListResponse, ProjectResponse
from src.requests.requester import BaseRequester


class ProjectRequester(BaseRequester):

    def get_projects(self) -> ProjectsListResponse:
        response = self._get('projects')
        if response.status_code == HTTPStatus.OK:
            return ProjectsListResponse(**response.json())

    def create_project(self, create_project_request: CreateProjectRequest) -> ProjectResponse:
        response = self._post('projects', create_project_request)
        if response.status_code == HTTPStatus.OK:
            return ProjectResponse(**response.json())

    def delete_project(self, project_id: str) -> None:
        self._delete(f'projects/id:{project_id}')

