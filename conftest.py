import os

import pytest

from framework.clients.team_city_api_client import TeamCityApiClient
from framework.data.urls import URL


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
def admin_headers() -> dict[str, str]:
    return {"Authorization": f"Bearer {_env_or_skip('TC_ADMIN_TOKEN')}"}


@pytest.fixture(scope="session")
def no_auth_headers() -> dict[str, str]:
    """Request without Authorization header."""
    return {}


@pytest.fixture(scope="session")
def invalid_auth_headers() -> dict[str, str]:
    """Request with invalid bearer token."""
    return {"Authorization": "Bearer invalid_token"}


@pytest.fixture(scope="session")
def unauth_headers(no_auth_headers: dict[str, str]) -> dict[str, str]:
    """
    Backward-compatible alias.
    Kept for tests that already use `unauth_headers`.
    """
    return no_auth_headers