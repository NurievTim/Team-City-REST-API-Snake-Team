import allure
import pytest
import uuid

from dotenv import load_dotenv
from src.requests.project_requester import ProjectRequester
from src.specs.request_spec import RequestSpecs
from src.models.requests import CreateProjectRequest, ParentProject
from src.specs.response_spec import ResponseSpecs

load_dotenv()


@pytest.mark.smoke
class TestProjects:

    @allure.id("3")  # запрос без валидного токена возвращает 401
    @allure.title("GET /projects — HTTP 401 при невалидном токене")
    def test_get_projects_unauthorized(self):
        ProjectRequester(
            RequestSpecs.unauth_spec(),
            ResponseSpecs.request_return_unauth(),
        ).get_projects()

    @allure.id("4")  # есть хотя бы один проект
    @allure.title("GET /projects — HTTP 200, count >= 1")
    def test_get_projects_count(self):
        projects = ProjectRequester(
            RequestSpecs.admin_base_headers(),
            ResponseSpecs.request_return_ok(),
        ).get_projects()

        assert projects.count >= 1

    @allure.id("6")
    @allure.title("POST /projects — создать проект, count вырос")
    def test_create_project_increases_count(self):
        requester = ProjectRequester(
            RequestSpecs.admin_base_headers(),
            ResponseSpecs.request_return_ok(),
        )
        count_before = requester.get_projects().count

        uid = uuid.uuid4().hex[:8].upper()
        project_request = CreateProjectRequest(
            id=f'SmokeProject{uid}',
            name=f'Smoke Test Project {uid}',
            parentProject=ParentProject(locator='_Root'),
        )
        created = requester.create_project(project_request)
        assert created.id == project_request.id

        count_after = requester.get_projects().count
        assert count_after > count_before
        requester.delete_project(project_request.id)

