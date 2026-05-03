import uuid
import pytest

from src.models.requests import CreateProjectRequest, ParentProject
from src.steps.project_steps import ProjectSteps


@pytest.fixture()
def get_project_request():
    uid = uuid.uuid4().hex[:8].upper()
    return CreateProjectRequest(
        id=f'SmokeProject{uid}',
        name=f'Smoke Test Project {uid}',
        parentProject=ParentProject(locator='_Root'),
    )

@pytest.fixture()
def created_project(get_project_request):
    project_steps = ProjectSteps()
    project = project_steps.create_project(get_project_request)
    yield project
    project_steps.delete_project(project.id)
