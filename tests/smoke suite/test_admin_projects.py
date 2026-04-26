import os
import allure
import pytest
import requests
import uuid

from dotenv import load_dotenv
from src.specs.request_spec import RequestSpecs
from src.models.requests import CreateProjectRequest, ParentProject
from src.models.responses import ProjectsListResponse, ProjectResponse

load_dotenv()


@pytest.mark.smoke
class TestProjects:

    @allure.id("3")  # запрос без валидного токена возвращает 401
    @allure.title("GET /projects — HTTP 401 при невалидном токене")
    def test_get_projects_unauthorized(self):
        response = requests.get(
            url=f'{RequestSpecs.BASE_URL}projects',
            headers=RequestSpecs.unauth_spec()['headers']
        )

        assert response.status_code == 401

    @allure.id("4")  # есть хотя бы один проект
    @allure.title("GET /projects — HTTP 200, count >= 1")
    def test_get_projects_count(self):
        response = requests.get(
            url=f'{RequestSpecs.BASE_URL}projects',
            headers=RequestSpecs.admin_base_headers()['headers']
        )

        assert response.status_code == 200
        body = ProjectsListResponse(**response.json())
        assert body.count >= 1

    @allure.id("6")
    @allure.title("POST /projects — создать проект, count вырос")
    def test_create_project_increases_count(self):
        count_before = ProjectsListResponse(**requests.get(
            url=f'{RequestSpecs.BASE_URL}projects',
            headers=RequestSpecs.admin_base_headers()['headers'],
        ).json()).count

        uid = uuid.uuid4().hex[:8].upper()
        project = CreateProjectRequest(
            id=f'SmokeProject{uid}',
            name=f'Smoke Test Project {uid}',
            parentProject=ParentProject(locator='_Root'),
        )

        csrf_token = requests.get(
            url=f'{RequestSpecs.BASE_URL}csrf',
            headers=RequestSpecs.admin_base_headers()['headers']
        ).text.strip()
        write_headers = {**RequestSpecs.admin_base_headers()['headers'], 'X-TC-CSRF-Token': csrf_token}

        create_response = requests.post(
            url=f'{RequestSpecs.BASE_URL}projects',
            headers=write_headers,
            json=project.model_dump(),
        )

        assert create_response.status_code == 200
        created = ProjectResponse(**create_response.json())
        assert created.id == project.id

        count_after = ProjectsListResponse(**requests.get(
            url=f'{RequestSpecs.BASE_URL}projects',
            headers=RequestSpecs.admin_base_headers()['headers'],
        ).json()).count

        assert count_after > count_before

        requests.delete(
            url=f'{RequestSpecs.BASE_URL}projects/id:{project.id}',
            headers=write_headers,
        )
