import allure
import pytest
import requests

from hamcrest import assert_that, greater_than_or_equal_to
from framework.checkers import check
from framework.steps.admin_steps import AdminSteps


@pytest.mark.smoke
class TestProjects:

    @allure.id("3")    # запрос без валидного токена возвращает 401
    @allure.title("GET /projects — HTTP 401 при невалидном токене")
    def test_get_projects_unauthorized(self, admin_steps: AdminSteps, invalid_auth_headers: dict) -> None:
        response = admin_steps.get_projects_unauthorized(invalid_headers=invalid_auth_headers)

        check.check_status_code(response=response, expected_status_code=requests.codes.unauthorized)

    @allure.id("4")   # есть хотя бы один проект
    @allure.title("GET /projects — HTTP 200, count >= 1")
    def test_get_projects_count(self, admin_steps: AdminSteps) -> None:
        count = admin_steps.assert_projects_count_gte_one()

        assert_that(count, greater_than_or_equal_to(1), "count >= 1")

    @allure.id("6")
    @allure.title("POST /projects — создать проект, count вырос")
    def test_create_project_increases_count(self, request: pytest.FixtureRequest, admin_steps: AdminSteps) -> None:
        count_before = admin_steps.get_projects_count()
        project = admin_steps.create_unique_project()
        project_id = project["id"]
        request.addfinalizer(lambda: admin_steps.delete_project(f"id:{project_id}"))
        admin_steps.assert_projects_count_increased(count_before=count_before)

