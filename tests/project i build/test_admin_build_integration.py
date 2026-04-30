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
        copy_request = CopyBuildTypeRequest(
            sourceBuildTypeLocator=f"id:{source_build.id}",
            name=f"Copy {RandomData.get_name()}",
            id=f"{source_build.id}_Copy_{RandomData.get_name()}",
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

    @allure.id("24")
    @allure.title("PUT /buildTypes/{buildTypeLocator}/paused — приостановка build configuration")
    def test_pause_build_configuration(self, build_requester, build_type_request):
        created_build_type = build_requester.create_build_type(build_type_request)

        try:
            assert build_requester.get_build_type_paused(created_build_type.id) is False

            build_requester.set_build_type_paused(created_build_type.id, True)

            assert build_requester.get_build_type_paused(created_build_type.id) is True
        finally:
            build_requester.set_build_type_paused(created_build_type.id, False)
            build_requester.delete_build_type(created_build_type.id)

    @allure.id("25")
    @allure.title("PUT /buildTypes/{buildTypeLocator}/parameters/{name} — изменение параметра build configuration")
    def test_update_build_configuration_parameter(self, build_requester, build_type_request):
        created_build_type = build_requester.create_build_type(build_type_request)
        parameter_name = "myTestParam"
        old_value = "old_value"
        new_value = "new_value_025"

        try:
            build_requester.create_build_type_parameter(created_build_type.id, parameter_name, old_value)
            build_requester.set_build_type_parameter(created_build_type.id, parameter_name, new_value)
            parameter = build_requester.get_build_type_parameter(created_build_type.id, parameter_name)

            assert parameter.get("value") == new_value
        finally:
            build_requester.delete_build_type_parameter(created_build_type.id, parameter_name)
            build_requester.delete_build_type(created_build_type.id)
