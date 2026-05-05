import pytest

from src.enums import Comment
from src.generators.random_model_generator import RandomModelGenerator
from src.models.requests import BuildCancelRequest
from src.models.responses import QueueBuildResponse, BuildTypeResponse


from src.generators.random_data import RandomData
from src.models.requests import CreateBuildTypeRequest, ProjectRef, QueueBuildRequest, BuildTypeRef, \
    CopyBuildTypeRequest
from src.steps.build_steps import BuildSteps


@pytest.fixture()
def build_steps() -> BuildSteps:
    return BuildSteps()


def _make_uid() -> str:
    return RandomData.get_name()


@pytest.fixture()
def build_type_request(created_project) -> CreateBuildTypeRequest:
    build_type_data: CreateBuildTypeRequest = RandomModelGenerator.generate(CreateBuildTypeRequest)
    build_type_data.project = ProjectRef(id=created_project.id)
    return build_type_data
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


@pytest.fixture()
def copy_build_request(build_type_request) -> CopyBuildTypeRequest:
    uid = RandomData.get_name()
    return CopyBuildTypeRequest(
        sourceBuildTypeLocator=f'id:{build_type_request.id}',
        name=f'Copied Build {uid}',
        id=f'{build_type_request.id}_Copy{uid}',
        copyAllAssociatedSettings=True,
    )
