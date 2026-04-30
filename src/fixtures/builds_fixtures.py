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
def copy_build_request(build_requester, build_type_request):
    source_build = build_requester.create_build_type(build_type_request)
    uid = RandomData.get_name()
    request = CopyBuildTypeRequest(
        sourceBuildTypeLocator=f"id:{source_build.id}",
        name=f"Copy {uid}",
        id=f"{source_build.id}_Copy_{uid}",
        copyAllAssociatedSettings=True,
    )
    request._source_build_id = source_build.id
    return request


@pytest.fixture
def build_type_with_param(build_requester, build_type_request):
    uid = RandomData.get_name()
    created_build_type = build_requester.create_build_type(build_type_request)
    parameter_name = f"{uid}"
    build_requester.create_build_type_parameter(created_build_type.id, parameter_name, "old_value")
    return created_build_type, parameter_name

