import pytest

from src.generators.random_data import RandomData
from src.models.requests import (CreateBuildTypeRequest, ProjectRef, CopyBuildTypeRequest)
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


@pytest.fixture
def copy_build_request():
    suffix = RandomData.get_username()
    return CopyBuildTypeRequest(
        sourceBuildTypeLocator="id:{suffix}",
        name=f"Copy {suffix}",
        id=f"Test_Copy_{suffix}",
        copyAllAssociatedSettings=True,
    )
