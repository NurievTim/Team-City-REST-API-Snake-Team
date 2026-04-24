import os

import pytest

from framework.clients.team_city_api_client import TeamCityApiClient
from framework.data.urls import URL
from framework.steps.admin_steps import AdminSteps


def _env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise EnvironmentError(f"Required env variable '{name}' is not set")
    return value


def _env_or_skip(name: str) -> str:
    value = os.getenv(name)
    if not value:
        pytest.skip(f"Environment variable '{name}' is not set")
    return value


@pytest.fixture(scope="session")
def tc_url() -> str:
    return _env("TC_URL").rstrip("/") if os.getenv("TC_URL") else URL.rstrip("/")


@pytest.fixture(scope="session")
def team_city_api_client(tc_url: str) -> TeamCityApiClient:
    return TeamCityApiClient(tc_url=tc_url)


@pytest.fixture(scope="session")
def read_headers() -> dict[str, str]:
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


@pytest.fixture(scope="session")
def unauth_headers(no_auth_headers: dict[str, str]) -> dict[str, str]:
    return no_auth_headers


@pytest.fixture(scope="session")
def csrf_token(team_city_api_client: TeamCityApiClient, read_headers: dict) -> str:
    response = team_city_api_client.get_csrf_token(headers=read_headers, check_status=None)
    return response.text.strip()


@pytest.fixture(scope="session")
def write_headers(read_headers: dict, csrf_token: str) -> dict[str, str]:
    """Хедеры для POST / PUT запросов — Bearer + CSRF-токен."""
    return {**read_headers, "X-TC-CSRF-Token": csrf_token}


@pytest.fixture(scope="session")    # Создаёт проект
def project_with_build_type(request: pytest.FixtureRequest, admin_steps: AdminSteps) -> dict:
    project = admin_steps.create_unique_project()
    project_id = project["id"]
    build_type_id = f"{project_id}_Build"

    admin_steps.create_build_type(project_id=project_id, build_type_id=build_type_id)
    request.addfinalizer(lambda: admin_steps.delete_project(f"id:{project_id}"))
    return {"project_id": project_id, "build_type_id": build_type_id}


@pytest.fixture(scope='session')
def admin_steps(team_city_api_client: TeamCityApiClient, read_headers: dict, write_headers: dict) -> AdminSteps:
    return AdminSteps(client=team_city_api_client, read_headers=read_headers, write_headers=write_headers)

