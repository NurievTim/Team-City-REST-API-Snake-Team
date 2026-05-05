import logging
from typing import Any, List
import pytest

from src.classes.api_manager import ApiManager
from src.models.responses import ProjectResponse, BuildTypeResponse


@pytest.fixture
def created_objects():
    objects: List[Any] = []
    yield objects

    cleanup_objects(objects)


def cleanup_objects(objects: List[Any]):
    api_manager = ApiManager(objects)
    for obj in objects:
        if isinstance(obj, ProjectResponse):
            api_manager.project_steps.delete_project(obj.id)
        else:
            logging.warning(f'Object type: {type(obj)} is not deleted')