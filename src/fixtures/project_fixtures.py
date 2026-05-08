import pytest

from src.generators.data_factory import make_sub_project_request
from src.generators.random_model_generator import RandomModelGenerator
from src.models.project_models.create_project_request import CreateProjectRequest
from src.models.responses import ProjectResponse
from src.requests.skeleton.endpoint import Endpoint
from src.requests.skeleton.requesters.crud_requester import CrudRequester
from src.specs.request_spec import RequestSpecs
from src.specs.response_spec import ResponseSpecs
from src.steps.project_steps import ProjectSteps


@pytest.fixture()
def project_steps(api_manager) -> ProjectSteps:
    return api_manager.project_steps


@pytest.fixture()
def get_project_request():
    project_data: CreateProjectRequest = RandomModelGenerator.generate(CreateProjectRequest)
    return project_data


@pytest.fixture()
def created_project(get_project_request, api_manager):
    project = api_manager.project_steps.create_project(get_project_request)
    return project


@pytest.fixture()
def project_not_found():
    return CrudRequester(
        request_spec=RequestSpecs.admin_base_headers(),
        endpoint=Endpoint.GET_PROJECTS,
        response_spec=ResponseSpecs.entity_was_not_found()
    )


@pytest.fixture()
def archive_project(api_manager):
    return api_manager.project_steps.archive_project


@pytest.fixture()
def sub_project(api_manager, created_project):
    return api_manager.project_steps.create_project(make_sub_project_request(created_project))


@pytest.fixture()
def sub_project_request(created_project) -> CreateProjectRequest:
    return make_sub_project_request(created_project)


@pytest.fixture()
def target_project(api_manager) -> ProjectResponse:
    project_data = RandomModelGenerator.generate(CreateProjectRequest)
    return api_manager.project_steps.create_project(project_data)
