import logging
from typing import Any, List
import pytest

from src.classes.api_manager import ApiManager
from src.models.responses import ProjectResponse, BuildTypeResponse, AgentResponse


@pytest.fixture
def created_objects():
    objects: List[Any] = []
    yield objects

    cleanup_objects(objects)


def cleanup_objects(objects: List[Any]):    # Важно: порядок удаления имеет значение.
    api_manager = ApiManager(objects)
    for obj in objects:  # 1) BuildTypes
        if isinstance(obj, BuildTypeResponse):
            api_manager.build_steps.delete_build_type(obj.id)

    for obj in objects:
        if isinstance(obj, ProjectResponse):
            try:
                api_manager.project_steps.delete_project(obj.id)
            except Exception:
                pass

    for obj in objects:
        if isinstance(obj, ProjectResponse):
            try:
                api_manager.project_steps.delete_project(obj.id)
            except Exception:
                pass

    for obj in objects:  # 3) Agents (id строкой)
        if isinstance(obj, AgentResponse):
            api_manager.agent_steps.disable_agent(obj)

    for obj in objects:  # 4) Остальное — логируем
        if isinstance(obj, (BuildTypeResponse, ProjectResponse, str)):
            continue
        logging.warning(f'Cleanup is not implemented for object type: {type(obj)}')
