import allure
import pytest

from http import HTTPStatus

from src.steps.project_steps import ProjectSteps


@pytest.mark.projectIbuild
class TestProjectsConfig:
    @allure.id("20")  # запрос с жёсткими данными
    @allure.title("POST /projects — создать проект с заданными атрибутами")
    def test_create_project_with_expected_attributes(self, project_steps: ProjectSteps, get_project_request):
        created = project_steps.create_project(get_project_request)
        fetched = project_steps.get_project_by_id(created.id)

        assert fetched.id == get_project_request.id
        assert fetched.name == get_project_request.name

        project_steps.delete_project(created.id)

    @allure.id("21")
    @allure.title("DELETE /projects/{locator} — удалить проект, повторный GET возвращает 404")
    def test_delete_project_and_get_404(self, project_steps: ProjectSteps, get_project_request, project_not_found):
        created = project_steps.create_project(get_project_request)
        fetched = project_steps.get_project_by_id(created.id)
        assert fetched.id == created.id

        project_steps.delete_project(created.id)

        response = project_not_found.get(locator=f"id:{created.id}")
        assert response.status_code == HTTPStatus.NOT_FOUND

    @allure.id("27")
    @allure.title("PUT /projects/{projectLocator}/archived — архивация проекта")
    def test_archive_project(self, project_steps: ProjectSteps, get_project_request, archive_project):
        created = project_steps.create_project(get_project_request)
        fetched_before = project_steps.get_project_by_id(created.id)
        assert fetched_before.archived is not True

        archive_project(created.id, True)
        fetched_archived = project_steps.get_project_by_id(created.id)
        assert fetched_archived.archived is True

        archive_project(created.id, False)
        project_steps.delete_project(created.id)
