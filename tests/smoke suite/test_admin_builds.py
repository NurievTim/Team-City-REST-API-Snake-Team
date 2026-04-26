import os
import uuid
import pytest
import requests
import allure

from dotenv import load_dotenv
from src.specs.request_spec import RequestSpecs
from src.models.requests import CreateProjectRequest, ParentProject, CreateBuildTypeRequest, ProjectRef, QueueBuildRequest, BuildTypeRef
from src.models.responses import QueueBuildResponse

load_dotenv()


@pytest.mark.smoke
class TestBuilds:

    @allure.id("5")
    @allure.title("POST /buildQueue — поставить сборку в очередь, state=queued")
    def test_queue_build_state_is_queued(self):
        csrf_token = requests.get(
            url=f'{RequestSpecs.BASE_URL}csrf',
            headers=RequestSpecs.admin_base_headers()['headers'],
        ).text.strip()
        write_headers = {**RequestSpecs.admin_base_headers()['headers'], 'X-TC-CSRF-Token': csrf_token}

        uid = uuid.uuid4().hex[:8].upper()
        project = CreateProjectRequest(
            id=f'SmokeProject{uid}',
            name=f'Smoke Test Project {uid}',
            parentProject=ParentProject(locator='_Root'),
        )

        requests.post(
            url=f'{RequestSpecs.BASE_URL}projects',
            headers=write_headers,
            json=project.model_dump(),
        )

        build_type = CreateBuildTypeRequest(
            id=f'{project.id}_Build',
            name='Smoke Build',
            project=ProjectRef(id=project.id),
        )

        requests.post(
            url=f'{RequestSpecs.BASE_URL}buildTypes',
            headers=write_headers,
            json=build_type.model_dump(),
        )

        queue_request = QueueBuildRequest(
            buildType=BuildTypeRef(id=build_type.id)
        )

        response = requests.post(
            url=f'{RequestSpecs.BASE_URL}buildQueue',
            headers=write_headers,
            json=queue_request.model_dump(),
        )

        assert response.status_code == 200
        body = QueueBuildResponse(**response.json())
        assert body.state == 'queued'

        requests.delete(
            url=f'{RequestSpecs.BASE_URL}projects/id:{project.id}',
            headers=write_headers,
        )

