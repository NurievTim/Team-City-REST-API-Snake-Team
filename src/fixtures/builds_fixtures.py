import pytest

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
    return CreateBuildTypeRequest(
        id=f'{created_project.id}_Build',
        name='Smoke Build',
        project=ProjectRef(id=created_project.id),
    )


@pytest.fixture()
def queue_build_request(build_type_request) -> QueueBuildRequest:
    return QueueBuildRequest(buildType=BuildTypeRef(id=build_type_request.id))


@pytest.fixture()
def copy_build_request(build_type_request) -> CopyBuildTypeRequest:
    uid = RandomData.get_name()
    return CopyBuildTypeRequest(
        sourceBuildTypeLocator=f'id:{build_type_request.id}',
        name=f'Copied Build {uid}',
        id=f'{build_type_request.id}_Copy{uid}',
        copyAllAssociatedSettings=True,
    )
