import base64
import os
import pytest

from typing import Any, Generator
from dotenv import load_dotenv
from framework.clients.team_city_api_client import TeamCityApiClient
from framework.data.entities.users import PROJECT_ADMIN, TestUser
from framework.data.urls import URL
from framework.steps.admin_steps import AdminSteps

pytest_plugins = [
    'framework.data.fixtures.api_fixtures'
]


def pytest_configure():
    load_dotenv(".env")


def _env(name: str) -> str:
    value = os.environ[f'{name}']
    if not value:
        raise EnvironmentError(f"Required env variable '{name}' is not set")
    return value


def _env_or_skip(name: str) -> str:
    value = os.environ[f'{name}']
    if not value:
        pytest.skip(f"Environment variable '{name}' is not set")
    return value


def basic_headers(username: str, password: str) -> dict[str, str]:
    raw = f"{username}:{password}".encode("utf-8")
    encoded = base64.b64encode(raw).decode("ascii")
    return {"Authorization": f"Basic {encoded}"}


@pytest.fixture(scope="session")
def tc_url() -> str:
    return _env("TC_URL").rstrip("/") if os.getenv("TC_URL") else URL.rstrip("/")


@pytest.fixture(scope="session")
def team_city_api_client(tc_url: str) -> TeamCityApiClient:
    return TeamCityApiClient(tc_url=tc_url)


@pytest.fixture(scope="session")
def admin_headers() -> dict[str, str]:
    return {
        "Authorization": f"Bearer {_env_or_skip('TC_ADMIN_TOKEN')}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }


@pytest.fixture(scope="session")
def no_auth_headers() -> dict[str, str]:
    return {}


@pytest.fixture(scope="session")
def invalid_auth_headers() -> dict[str, str]:
    return {"Authorization": "Bearer invalid_token"}


def proj_admin_user() -> TestUser:
    """Данные проектного администратора из entities."""
    return PROJECT_ADMIN


@pytest.fixture(scope="session")
def unauth_headers(no_auth_headers: dict[str, str]) -> dict[str, str]:
    return no_auth_headers


@pytest.fixture(scope="session")
def csrf_token(team_city_api_client: TeamCityApiClient, admin_headers: dict) -> str:
    response = team_city_api_client.get_csrf_token(headers=admin_headers, check_status=None)
    return response.text.strip()


@pytest.fixture(scope="session")
def write_headers(admin_headers: dict, csrf_token: str) -> dict[str, str]:
    """Хедеры для POST / PUT запросов — Bearer + CSRF-токен."""
    return {**admin_headers, "X-TC-CSRF-Token": csrf_token}


@pytest.fixture(scope="session")    # Создаёт проект
def project_with_build_type(request: pytest.FixtureRequest, admin_steps: AdminSteps) -> dict:
    project = admin_steps.create_unique_project()
    project_id = project["id"]
    build_type_id = f"{project_id}_Build"

    admin_steps.create_build_type(project_id=project_id, build_type_id=build_type_id)
    request.addfinalizer(lambda: admin_steps.delete_project(f"id:{project_id}"))
    return {"project_id": project_id, "build_type_id": build_type_id}


@pytest.fixture(scope='session')
def admin_steps(team_city_api_client: TeamCityApiClient, admin_headers: dict, write_headers: dict) -> AdminSteps:
    return AdminSteps(client=team_city_api_client, admin_headers=admin_headers, write_headers=write_headers)


def proj_admin(team_city_api_client: TeamCityApiClient, proj_admin_user: TestUser, admin_headers) \
        -> Generator[None, Any, None]:
    payload = {
        'username': proj_admin_user.username,
        'password': proj_admin_user.password,
    }
    team_city_api_client.add_user(data=payload, check_status=None, headers=admin_headers)

    team_city_api_client.add_role_to_user(
        user_locator=proj_admin_user.locator,
        role_id=proj_admin_user.role_id,
        scope=proj_admin_user.role_scope,
        headers=admin_headers,
        check_status=None,
    )
    PROJECT_ADMIN.token = basic_headers(proj_admin_user.username, proj_admin_user.password)
    yield
    team_city_api_client.session.cookies.clear()
    team_city_api_client.guest_session.cookies.clear()
    team_city_api_client.delete_user(user_locator=proj_admin_user.locator, headers=admin_headers)


@pytest.fixture(scope='session')
def proj_admin_headers(proj_admin) -> dict[str, str]:
    return PROJECT_ADMIN.token



