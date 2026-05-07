import pytest
from src.models.requests import CreateVcsRootRequest, VcsRootProjectRef, VcsRootProperties, VcsRootProperty
from src.generators.random_data import RandomData


@pytest.fixture()
def vcs_root_request(created_project) -> CreateVcsRootRequest:
    uid = RandomData.get_name()
    return CreateVcsRootRequest(
        id=f'{created_project.id}_Root{uid}',
        name=f'VcsRoot_{uid}',
        vcsName='jetbrains.git',
        project=VcsRootProjectRef(id=created_project.id),
        properties=VcsRootProperties(property=[
            VcsRootProperty(name='authMethod', value='ANONYMOUS'),
            VcsRootProperty(name='branch', value='refs/heads/main'),
            VcsRootProperty(name='url', value='https://github.com/JetBrains/teamcity-rest.git'),
        ])
    )
