import base64
import os
from typing import Any, Generator

import pytest
from dotenv import load_dotenv

from framework.clients.team_city_api_client import TeamCityApiClient
from framework.data.entities.users import PROJECT_ADMIN, TestUser
from framework.data.urls import URL

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
    return {"Authorization": f"Bearer {_env_or_skip('TC_ADMIN_TOKEN')}"}


@pytest.fixture(scope="session")
def no_auth_headers() -> dict[str, str]:
    """Request without Authorization header."""
    return {}


@pytest.fixture(scope="session")
def proj_admin_user() -> TestUser:
    """Данные проектного администратора из entities."""
    return PROJECT_ADMIN


@pytest.fixture(scope="session")
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
    team_city_api_client.delete_user(
        user_locator=proj_admin_user.locator,
        headers=admin_headers
    )

@pytest.fixture(scope='session')
def proj_admin_headers(proj_admin) -> dict[str, str]:
    return PROJECT_ADMIN.token