import pytest

from src.models.requests import (CreateBuildTypeRequest, ProjectRef)
from src.requests.skeleton.endpoint import Endpoint
from src.requests.skeleton.requesters.build_requester import BuildRequester
from src.specs.request_spec import RequestSpecs
from src.specs.response_spec import ResponseSpecs


@pytest.fixture
def build_requester():
    return BuildRequester(
        request_spec=RequestSpecs.admin_base_headers(),
        endpoint=Endpoint.CREATE_BUILD_TYPE,
        response_spec=ResponseSpecs.request_return_ok(),
    )


@pytest.fixture
def build_type_request(created_project):
    return CreateBuildTypeRequest(
        id=f'{created_project.id}_Build',
        name='Smoke Build',
        project=ProjectRef(id=created_project.id),
    )
