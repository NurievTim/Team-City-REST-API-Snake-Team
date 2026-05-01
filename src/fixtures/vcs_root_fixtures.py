import pytest

from src.generators.random_data import RandomData
from src.models.requests import (CreateVcsRootRequest, VcsRootProjectRef, VcsRootProperties, VcsRootProperty)
from src.requests.skeleton.endpoint import Endpoint
from src.requests.skeleton.requesters.vcs_root_requester import VcsRootRequester
from src.specs.request_spec import RequestSpecs
from src.specs.response_spec import ResponseSpecs


@pytest.fixture
def vcs_root_requester():
    return VcsRootRequester(
        request_spec=RequestSpecs.admin_base_headers(),
        endpoint=Endpoint.CREATE_VCS_ROOT,
        response_spec=ResponseSpecs.request_return_ok(),
    )


@pytest.fixture
def vcs_root_request(created_project):
    uid = RandomData.get_name()
    return CreateVcsRootRequest(
        id=f"{created_project.id}_TC26Root_{uid}",
        name=f"TC26 Test Root {uid}",
        vcsName="jetbrains.git",
        project=VcsRootProjectRef(id=created_project.id),
        properties=VcsRootProperties(
            property=[
                VcsRootProperty(name="authMethod", value="SUPPERADMIN"),
                VcsRootProperty(name="branch", value="refs/heads/main"),
                VcsRootProperty(name="url", value="https://github.com/JetBrains/teamcity-rest.git"),
            ]
        ),
    )

