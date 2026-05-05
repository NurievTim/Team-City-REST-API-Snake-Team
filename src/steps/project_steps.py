from src.models.comparison.model_assertions import ModelAssertions
from src.models.requests import CreateProjectRequest
from src.models.responses import ProjectsListResponse, ProjectResponse
from src.requests.skeleton.endpoint import Endpoint
from src.requests.skeleton.requesters.crud_requester import CrudRequester
from src.requests.skeleton.requesters.validated_crud_requester import ValidatedCrudRequester
from src.specs.request_spec import RequestSpecs
from src.specs.response_spec import ResponseSpecs
from src.steps.base_steps import BaseSteps


class ProjectSteps(BaseSteps):
    def get_projects(self) -> ProjectsListResponse:
        projects: ProjectsListResponse = ValidatedCrudRequester(
            RequestSpecs.admin_base_headers(),
            Endpoint.GET_PROJECTS,
            ResponseSpecs.request_return_ok(),
        ).get()

        assert projects.count >= 1
        return projects

    def get_projects_unauthorized(self):
        CrudRequester(
            request_spec=RequestSpecs.unauth_spec(),
            endpoint=Endpoint.GET_PROJECTS,
            response_spec=ResponseSpecs.request_return_unauth(),
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
            ResponseSpecs.request_return_ok(),
        ).post(create_project_request)
        self.created_objects.append(project)

        ModelAssertions(create_project_request, project).match()
        return project

    def delete_project(self, locator: str):
        ValidatedCrudRequester(
            RequestSpecs.admin_base_headers(),
            Endpoint.DELETE_PROJECT,
            ResponseSpecs.entity_was_deleted(),
        ).delete(locator)
