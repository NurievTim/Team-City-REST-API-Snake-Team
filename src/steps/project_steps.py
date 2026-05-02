from src.models.comparison.model_assertions import ModelAssertions
from src.models.requests import CreateProjectRequest
from src.models.responses import ProjectsListResponse, ProjectResponse
from src.requests.skeleton.endpoint import Endpoint
from src.requests.skeleton.requesters.validated_crud_requester import ValidatedCrudRequester
from src.specs.request_spec import RequestSpecs
from src.specs.response_spec import ResponseSpecs


class ProjectSteps:
    def get_projects(self) -> ProjectsListResponse:
        projects: ProjectsListResponse = ValidatedCrudRequester(
            RequestSpecs.admin_base_headers(),
            Endpoint.GET_PROJECT,
            ResponseSpecs.request_return_ok(),
        ).get()

        assert projects.count >= 1
        return projects

    def get_projects_unauthorized(self):
        ValidatedCrudRequester(
            RequestSpecs.unauth_spec(),
            Endpoint.GET_PROJECT,
            ResponseSpecs.request_return_unauth(),
        ).get()

    def get_project_by_id(self, project_id: str) -> ProjectResponse:
        project: ProjectResponse = ValidatedCrudRequester(
            RequestSpecs.admin_base_headers(),
            Endpoint.GET_PROJECT,
            ResponseSpecs.request_return_ok(),
        ).get(locator=project_id)

        assert project.id == project_id
        return project

    def create_project(self, create_project_request: CreateProjectRequest) -> ProjectResponse:
        project: ProjectResponse = ValidatedCrudRequester(
            RequestSpecs.admin_base_headers(),
            Endpoint.CREATE_PROJECT,
            ResponseSpecs.entity_was_created(),
        ).post(create_project_request)

        ModelAssertions(create_project_request, project).match()
        return project

    def delete_project(self, locator: str):
        ValidatedCrudRequester(
            RequestSpecs.admin_base_headers(),
            Endpoint.DELETE_PROJECT,
            ResponseSpecs.entity_was_deleted(),
        ).delete(locator)
