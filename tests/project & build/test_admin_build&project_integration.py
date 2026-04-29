import allure
import pytest


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
    def test_delete_project_and_get_404_after(self, get_project_requester, get_project_request):
        created = get_project_requester.create_project(get_project_request)
        get_project_requester.delete_project(get_project_request.id)
        ProjectRequester(
            RequestSpecs.admin_base_headers(),
            ResponseSpecs.entity_was_not_found(),
        ).get(
            endpoint=Endpoint.GET_PROJECTS,
            locator=f"id:{payload.id}",
        )