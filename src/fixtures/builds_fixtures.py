import pytest

from src.enums import Comment
from src.models.requests import (CreateBuildTypeRequest, ProjectRef, QueueBuildRequest, BuildTypeRef,
                                 BuildCancelRequest)
from src.models.responses import QueueBuildResponse, BuildTypeResponse


@pytest.fixture()
def build_type_request(created_project) -> CreateBuildTypeRequest:
    return CreateBuildTypeRequest(
        id=f'{created_project.id}_Build',
        name='Smoke Build',
        project=ProjectRef(id=created_project.id),
    )
# наверное надо через генератор создавать данные


@pytest.fixture()
def build_type(build_type_request, api_manager) -> BuildTypeResponse:
    return api_manager.build_steps.create_build_type(build_type_request)


@pytest.fixture()
def queue_build_request(build_type) -> QueueBuildRequest:
    return QueueBuildRequest(buildType=BuildTypeRef(id=build_type.id))


@pytest.fixture()
def queue_build(queue_build_request, api_manager) -> QueueBuildResponse:
    return api_manager.build_steps.add_build_to_queue(queue_build_request)


@pytest.fixture()
def build_cancel_request() -> BuildCancelRequest:
    return BuildCancelRequest(comment=Comment.CANCELING_QUEUED_BUILD, readdIntoQueue=False)
