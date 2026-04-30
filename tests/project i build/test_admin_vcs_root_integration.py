import allure
import pytest


@pytest.mark.projectIbuild
class TestVcsRootConfig:
    @allure.id("26")
    @allure.title("POST /vcs-roots — создание VCS Root")
    def test_create_vcs_root(self, vcs_root_requester, vcs_root_request):
        created_vcs_root = vcs_root_requester.create_vcs_root(vcs_root_request)

        assert created_vcs_root.id == vcs_root_request.id
        assert created_vcs_root.name == vcs_root_request.name

        vcs_root_requester.delete_vcs_root(vcs_root_request.id)
