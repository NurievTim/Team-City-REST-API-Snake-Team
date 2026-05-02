import allure
import pytest

from src.models.comparison.model_assertions import ModelAssertions
from src.specs.request_spec import RequestSpecs
from src.specs.response_spec import ResponseSpecs


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
    def test_create_project_increases_count(self, get_project_requester, get_project_request, factory_created_project):
        count_before = get_project_requester.get_projects().count
        created = factory_created_project()
        ModelAssertions(get_project_request, created).match()
        count_after = get_project_requester.get_projects().count

        assert count_after > count_before

