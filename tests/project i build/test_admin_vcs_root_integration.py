import allure
import pytest

from src.classes.api_manager import ApiManager


@pytest.mark.projectIbuild
class TestVcsRootConfig:
    @allure.id("26")
    @allure.title("POST /vcs-roots — создание VCS Root")
    def test_create_vcs_root(self, api_manager: ApiManager, vcs_root_request):
        created = api_manager.vcsroot_steps.create_vcs_root(vcs_root_request)
        fetched = api_manager.vcsroot_steps.get_vcs_root_by_id(created.id)

        assert fetched.id == vcs_root_request.id
        assert fetched.name == vcs_root_request.name
        assert fetched.vcsName == vcs_root_request.vcsName

