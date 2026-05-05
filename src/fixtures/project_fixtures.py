import pytest

from src.generators.random_model_generator import RandomModelGenerator
from src.models.project_models.create_project_request import CreateProjectRequest


@pytest.fixture()
def get_project_request():
    project_data: CreateProjectRequest = RandomModelGenerator.generate(CreateProjectRequest)
    return project_data
import requests

from src.configs.config import Config
from src.generators.random_data import RandomData
from src.requests.skeleton.endpoint import Endpoint
from src.requests.skeleton.requesters.crud_requester import CrudRequester
from src.models.requests import CreateProjectRequest, ParentProject
from src.specs.request_spec import RequestSpecs
from src.specs.response_spec import ResponseSpecs
from src.steps.project_steps import ProjectSteps


@pytest.fixture()
def project_steps() -> ProjectSteps:
    return ProjectSteps()


def _make_uid() -> str:
    return RandomData.get_name()


@pytest.fixture()
def get_project_request() -> CreateProjectRequest:
    uid = _make_uid()
    return CreateProjectRequest(
        id=f'SmokeProject{uid}',
        name=f'Smoke Test Project {uid}',
        parentProject=ParentProject(locator='_Root'),
    )


@pytest.fixture()
def created_project(get_project_request, api_manager):
    project = api_manager.project_steps.create_project(get_project_request)
    return project
def created_project(project_steps, get_project_request):
    project = project_steps.create_project(get_project_request)
    yield project
    project_steps.delete_project(project.id)


@pytest.fixture()
def project_not_found():
    return CrudRequester(
        request_spec=RequestSpecs.admin_base_headers(),
        endpoint=Endpoint.GET_PROJECTS,
        response_spec=ResponseSpecs.entity_was_not_found()
    )


@pytest.fixture()
def archive_project():
    def _set_archived(project_id: str, archived: bool):
        headers = dict(RequestSpecs.admin_base_headers())
        headers["Content-Type"] = "text/plain"
        headers["Accept"] = "text/plain"
        response = requests.put(
            url=f"{Config.get('baseurl')}projects/id:{project_id}/archived",
            data=str(archived).lower(),
            headers=headers,
        )
        ResponseSpecs.request_return_ok()(response)

    return _set_archived
