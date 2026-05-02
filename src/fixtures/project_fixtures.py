import uuid
import pytest

from src.models.requests import CreateProjectRequest, ParentProject
from src.requests.skeleton.endpoint import Endpoint
from src.requests.skeleton.requesters.project_requester import ProjectRequester
from src.specs.request_spec import RequestSpecs
from src.specs.response_spec import ResponseSpecs


@pytest.fixture()
def get_project_requester():
    return ProjectRequester(
        request_spec=RequestSpecs.admin_base_headers(),
        endpoint=Endpoint.GET_PROJECTS,
        response_spec=ResponseSpecs.request_return_ok()
    )


@pytest.fixture()
def get_project_request():
    uid = uuid.uuid4().hex[:8].upper()
    return CreateProjectRequest(
        id=f'SmokeProject{uid}',
        name=f'Smoke Test Project {uid}',
        parentProject=ParentProject(locator='_Root'),
    )


@pytest.fixture()
def created_project(get_project_requester, get_project_request):
    response = get_project_requester.create_project(get_project_request)
    yield response
    get_project_requester.delete_project(get_project_request.id)


@pytest.fixture()
def factory_created_project(get_project_requester, get_project_request):
    created_ids = []

    def create():
        response = get_project_requester.create_project(get_project_request)
        created_ids.append(get_project_request.id)
        return response
    yield create
    for project_id in created_ids:
        get_project_requester.delete_project(project_id)
