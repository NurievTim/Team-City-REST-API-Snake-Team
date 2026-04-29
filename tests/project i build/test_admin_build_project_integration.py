import allure
import pytest

from http import HTTPStatus


@pytest.mark.smoke
class TestProjectsIBuildConfig:
    @allure.id("20")  # запрос с жёсткими данными
    @allure.title("POST /projects — создать проект с заданными атрибутами")
    def test_create_project_with_expected_attributes(self, get_project_requester, tc20_project_request):
        created = get_project_requester.create_project(tc20_project_request)

        assert created.id == tc20_project_request.id
        assert created.name == tc20_project_request.name
        get_project_requester.delete_project(tc20_project_request.id)

    @allure.id("21")
    @allure.title("DELETE /projects/{locator} — удалить проект, повторный GET возвращает 404")
    def test_delete_project_and_get_404(self, get_project_requester, get_project_request, project_not_found):
        created = get_project_requester.create_project(get_project_request)
        assert created.id == get_project_request.id

        get_project_requester.delete_project(get_project_request.id)
        response = project_not_found.get(locator=f"id:{get_project_request.id}")
        assert response.status_code == HTTPStatus.NOT_FOUND

    @allure.id("22")
    @allure.title("POST /buildTypes — создать build configuration")
    def test_create_build_configuration(self, build_requester, build_type_request):
        created_build_type = build_requester.create_build_type(build_type_request)

        assert created_build_type.id == build_type_request.id
        assert created_build_type.name == build_type_request.name
        build_requester.delete_build_type(build_type_request.id)

