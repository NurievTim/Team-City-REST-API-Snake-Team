import uuid
import allure
import pytest
import requests

from hamcrest import assert_that, equal_to, greater_than, greater_than_or_equal_to, not_none
from framework.checkers import check
from framework.clients.team_city_api_client import TeamCityApiClient


class AdminSteps:
    def __init__(self, client: TeamCityApiClient, read_headers: dict, write_headers: dict) -> None:
        self._client = client
        self._read = read_headers  # GET / DELETE
        self._write = write_headers  # POST / PUT (с CSRF-токеном)

    # Server / User
    @allure.step("Получить информацию о сервере и убедиться, что поле version присутствует")
    def get_server_info_with_version(self) -> dict:
        """GET /app/rest/server → возвращает тело ответа."""
        response = self._client.get_server_info(headers=self._read, check_status=None)
        check.check_status_code(response=response, expected_status_code=requests.codes.ok)
        body = response.json()
        assert_that(body.get("version"), not_none(), "Поле version отсутствует в ответе")
        return body

    @allure.step("Получить текущего пользователя и проверить username = '{expected_username}'")
    def get_current_user_and_check_username(self, expected_username: str) -> dict:
        """GET /app/rest/users/current → проверяет username."""
        response = self._client.get_current_user(headers=self._read, check_status=None)
        check.check_status_code(response=response, expected_status_code=requests.codes.ok)
        body = response.json()
        actual = body.get("username")
        assert_that(actual, equal_to(expected_username), f'username ожидался «{expected_username}», получен «{actual}»')
        return body

    # Projects
    @allure.step("Получить список проектов и вернуть текущий count")
    def get_projects_count(self) -> int:
        """GET /app/rest/projects → возвращает поле count."""
        response = self._client.get_projects(headers=self._read, check_status=None)
        check.check_status_code(response=response, expected_status_code=requests.codes.ok)
        return response.json().get("count", 0)

    @allure.step("Получить список проектов без токена и ожидать 401")
    def get_projects_unauthorized(self, invalid_headers: dict) -> None:
        """GET /app/rest/projects с невалидным токеном → 401."""
        response = self._client.get_projects(headers=invalid_headers, check_status=None)
        check.check_status_code(response=response, expected_status_code=requests.codes.unauthorized)

    @allure.step("Убедиться, что список проектов содержит хотя бы 1 проект")
    def assert_projects_count_gte_one(self) -> None:
        """GET /app/rest/projects → count >= 1."""
        count = self.get_projects_count()
        assert_that(count, greater_than_or_equal_to(1), "count >= 1")

    @allure.step("Создать проект с уникальным ID в _Root")
    def create_unique_project(self) -> dict:
        uid = uuid.uuid4().hex[:8].upper()
        project_id = f"SmokeProject{uid}"
        response = self._client.add_project(
            headers=self._write,
            data={
                "id": project_id,
                "name": f"Smoke Test Project {uid}",
                "parentProject": {"locator": "_Root"},
            },
            check_status=None,
        )
        check.check_status_code(response=response, expected_status_code=requests.codes.ok)
        return response.json()

    @allure.step("Удалить проект с locator='{project_locator}'")
    def delete_project(self, project_locator: str) -> None:
        self._client.delete_project(project_locator=project_locator, headers=self._write )

    # Build Types
    @allure.step("Создать build configuration '{build_type_id}' внутри проекта '{project_id}'")
    def create_build_type(self, project_id: str, build_type_id: str) -> dict:
        response = self._client.add_build_type(
            headers=self._write,
            data={
                "id": build_type_id,
                "name": "Smoke Build",
                "project": {"id": project_id},
            },
            check_status=None,
        )
        check.check_status_code(response=response, expected_status_code=requests.codes.ok)
        return response.json()

    # Build Queue

    @allure.step("Поставить сборку '{build_type_id}' в очередь и убедиться, что state=queued")
    def queue_build_and_assert_queued(self, build_type_id: str) -> int:
        response = self._client.add_build_to_queue(headers=self._write, data={"buildType": {"id": build_type_id}}, check_status=None )
        check.check_status_code(response=response, expected_status_code=requests.codes.ok)
        body = response.json()
        assert_that(body.get("state"), equal_to("queued"), 'state должен быть «queued»')
        return body.get("id")

    @allure.step("Убедиться, что count проектов вырос: было {count_before}")
    def assert_projects_count_increased(self, count_before: int) -> None:
        count_after = self.get_projects_count()
        assert_that(count_after, greater_than(count_before), f"count вырос: было {count_before}, стало {count_after}")

    # Builds

    @allure.step("Получить сборку id={build_id} и проверить state=running")
    def get_build_and_assert_running(self, build_id: int | str) -> dict:
        response = self._client.get_build(build_locator=f"id:{build_id}", headers=self._read, check_status=None)
        check.check_status_code(response=response, expected_status_code=requests.codes.ok)
        body = response.json()
        actual_state = body.get("state")
        assert_that(actual_state, equal_to("running"), f'state должен быть «running», получен «{actual_state}»')
        return body

    # Agents

    @allure.step("Получить авторизованные агенты и убедиться, что их >= 1")
    def get_authorized_agents_and_assert(self) -> int:
        response = self._client.get_agents(headers=self._read, params={"locator": "authorized:true"}, check_status=None)
        check.check_status_code(response=response, expected_status_code=requests.codes.ok)
        count = response.json().get("count", 0)
        if count == 0:
            pytest.skip("Нет авторизованных агентов в окружении — тест пропущен")
        assert_that(count, greater_than_or_equal_to(1))
        return count
