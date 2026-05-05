import uuid
import pytest

from src.generators.random_model_generator import RandomModelGenerator
from src.models.project_models.create_project_request import CreateProjectRequest


@pytest.fixture()
def get_project_request():
    project_data: CreateProjectRequest = RandomModelGenerator.generate(CreateProjectRequest)
    return project_data

@pytest.fixture()
def created_project(get_project_request, api_manager):
    project = api_manager.project_steps.create_project(get_project_request)
    return project
