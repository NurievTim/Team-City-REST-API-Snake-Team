from typing import Generator, Any
from uuid import uuid4

import pytest

from framework.clients.team_city_api_client import TeamCityApiClient


@pytest.fixture()
def created_project(team_city_api_client: TeamCityApiClient, admin_headers: dict[str, str]) -> Generator[str, Any, None]:
    """
    Создаёт временный проект и удаляет его после теста.
    Возвращает external id созданного проекта.
    """
    project_id = f'AT_PRJ_{uuid4().hex[:8]}'
    payload = {
        'id': project_id,
        'name': f'AT Project {project_id}',
        'parentProject': {'locator': 'id:_Root'},
        'copyAllAssociatedSettings': False,
    }

    team_city_api_client.add_project(headers=admin_headers, data=payload)
    yield project_id

    team_city_api_client.delete_project(
        project_locator=f'id:{project_id}',
        headers=admin_headers
    )


@pytest.fixture()
def created_build_type(team_city_api_client: TeamCityApiClient, admin_headers: dict[str, str], created_project) \
        -> Generator[str, Any, None]:
    """
    Создаёт временный buildType и удаляет его после теста.
    Использует проект из TC_PROJECT_ID или TestProject по умолчанию.
    """
    build_type_id = f'AT_{uuid4().hex[:8]}'
    payload = {
        'id': build_type_id,
        'name': f'AT {build_type_id}',
        'project': {'id': created_project},
    }

    team_city_api_client.add_build_type(headers=admin_headers, data=payload)
    yield build_type_id

    team_city_api_client.delete_build_type(
        build_type_locator=f'id:{build_type_id}',
        headers=admin_headers
    )