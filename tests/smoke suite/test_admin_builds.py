import uuid
import pytest
import allure

from dotenv import load_dotenv
from src.specs.response_spec import ResponseSpecs
from src.requests.build_requester import BuildRequester
from src.requests.project_requester import ProjectRequester
from src.specs.request_spec import RequestSpecs
from src.models.requests import (CreateProjectRequest, ParentProject, CreateBuildTypeRequest,
                                 ProjectRef, QueueBuildRequest, BuildTypeRef)

load_dotenv()


@pytest.mark.smoke
class TestBuilds:
    @allure.id("5.1")
    @allure.title("POST /buildTypes — создать build configs, id и name совпадают")
    def test_create_build_type(self):
        uid = uuid.uuid4().hex[:8].upper()
        project_request = CreateProjectRequest(
            id=f'SmokeProject{uid}',
            name=f'Smoke Test Project {uid}',
            parentProject=ParentProject(locator='_Root'),
        )

        project_requester = ProjectRequester(
            RequestSpecs.admin_base_headers(),
            ResponseSpecs.request_return_ok(),
        )
        project_requester.create_project(project_request)

        build_type_request = CreateBuildTypeRequest(
            id=f'{project_request.id}_Build',
            name='Smoke Build',
            project=ProjectRef(id=project_request.id),
        )

        build_type = BuildRequester(
            RequestSpecs.admin_base_headers(),
            ResponseSpecs.request_return_ok(),
        ).create_build_type(build_type_request)

        assert build_type.id == build_type_request.id
        assert build_type.name == build_type_request.name
        project_requester.delete_project(project_request.id)

    @allure.id("5")
    @allure.title("POST /buildQueue — поставить сборку в очередь, state=queued")
    def test_queue_build_state_is_queued(self):
        uid = uuid.uuid4().hex[:8].upper()

        project_request = CreateProjectRequest(
            id=f'SmokeProject{uid}',
            name=f'Smoke Test Project {uid}',
            parentProject=ParentProject(locator='_Root'),
        )

        project_requester = ProjectRequester(
            RequestSpecs.admin_base_headers(),
            ResponseSpecs.request_return_ok(),
        )
        project_requester.create_project(project_request)

        build_type_request = CreateBuildTypeRequest(
            id=f'{project_request.id}_Build',
            name='Smoke Build',
            project=ProjectRef(id=project_request.id),
        )

        build_requester = BuildRequester(
            RequestSpecs.admin_base_headers(),
            ResponseSpecs.request_return_ok(),
        )
        build_requester.create_build_type(build_type_request)

        queue_response = build_requester.queue_build(
            QueueBuildRequest(buildType=BuildTypeRef(id=build_type_request.id))
        )

        assert queue_response.state == 'queued'
        project_requester.delete_project(project_request.id)
