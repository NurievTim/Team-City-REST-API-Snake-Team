import allure
import pytest

from src.steps.project_steps import ProjectSteps


@pytest.mark.smoke
class TestProjects:

    @allure.id("3")  # запрос без валидного токена возвращает 401
    @allure.title("GET /projects — HTTP 401 при невалидном токене")
    def test_get_projects_unauthorized(self):
        ProjectSteps().get_projects_unauthorized()

    @allure.id("4")  # есть хотя бы один проект
    @allure.title("GET /projects — HTTP 200, count >= 1")
    def test_get_projects_count(self):
        projects = ProjectSteps().get_projects()

        assert projects.count >= 1

    @allure.id("6")
    @allure.title("POST /projects — создать проект, count вырос")
    def test_create_project_increases_count(self, get_project_request):
        project_steps = ProjectSteps()
        count_before = project_steps.get_projects().count
        created_project = project_steps.create_project(get_project_request)
        project_steps.get_project_by_id(created_project.id)
        count_after = project_steps.get_projects().count
        assert count_after > count_before
