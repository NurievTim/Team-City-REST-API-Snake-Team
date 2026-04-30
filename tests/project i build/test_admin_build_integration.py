import allure
import pytest

from src.generators.random_data import RandomData
from src.models.requests import CopyBuildTypeRequest


@pytest.mark.projectIbuild
class TestBuildConfig:
    @allure.id("22")
    @allure.title("POST /buildTypes — создать build configuration")
    def test_create_build_configuration(self, build_requester, build_type_request):
        created_build_type = build_requester.create_build_type(build_type_request)

        assert created_build_type.id == build_type_request.id
        assert created_build_type.name == build_type_request.name
        build_requester.delete_build_type(build_type_request.id)

    @allure.id("23")
    @allure.title("POST /projects/{projectLocator}/buildTypes — копирование build configuration")
    def test_copy_build_configuration(self, build_requester, build_type_request, created_project):
        source_build = build_requester.create_build_type(build_type_request)
        suffix = RandomData.get_username()
        copy_request = CopyBuildTypeRequest(
            sourceBuildTypeLocator=f"id:{source_build.id}",
            name=f"Copy {suffix}",
            id=f"{source_build.id}_Copy_{suffix}",
            copyAllAssociatedSettings=True,
        )

        try:
            copied = build_requester.copy_build_type_to_project(created_project.id, copy_request)

            assert copied.id == copy_request.id
            assert copied.project is not None
            assert copied.project.get("id") == created_project.id
        finally:
            build_requester.delete_build_type(copy_request.id)
            build_requester.delete_build_type(source_build.id)
