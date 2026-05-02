import pytest

from src.models.requests import (CreateBuildTypeRequest, ProjectRef, QueueBuildRequest, BuildTypeRef)


@pytest.fixture()
def build_type_request(created_project):
    return CreateBuildTypeRequest(
        id=f'{created_project.id}_Build',
        name='Smoke Build',
        project=ProjectRef(id=created_project.id),
    )


@pytest.fixture()
def queue_build_request(build_type_request):
    return QueueBuildRequest(buildType=BuildTypeRef(id=build_type_request.id))
