import allure
import pytest

from src.classes.api_manager import ApiManager
from src.enums import BuildParams
from src.models.requests import CopyBuildTypeRequest


@pytest.mark.projectIbuild
class TestBuildConfig:

    @allure.id("22")
    @allure.title("POST /buildTypes — создать build configuration")
    def test_create_build_configuration(self, api_manager: ApiManager, build_type_request):
        created = api_manager.build_steps.create_build_type(build_type_request)
        fetched = api_manager.build_steps.get_build_type_by_id(created.id)

        assert fetched.id == build_type_request.id
        assert fetched.name == build_type_request.name

    @allure.id("23")
    @allure.title("POST /projects/{projectLocator}/buildTypes — копирование build configuration")
    def test_copy_build_configuration(self, api_manager: ApiManager, build_type, copy_build_request, created_project):
        copied = api_manager.build_steps.copy_build_type_to_project(created_project.id, copy_build_request)
        fetched_copy = api_manager.build_steps.get_build_type_by_id(copied.id)

        assert fetched_copy.id == copy_build_request.id
        assert fetched_copy.project is not None
        assert fetched_copy.project.get("id") == created_project.id

    @allure.id("24")
    @allure.title("PUT /buildTypes/{buildTypeLocator}/paused — приостановка build configuration")
    def test_pause_build_configuration(self, api_manager: ApiManager, build_type):
        assert api_manager.build_steps.get_build_type_paused(build_type.id) is False

        api_manager.build_steps.set_build_type_paused(build_type.id, True)
        assert api_manager.build_steps.get_build_type_paused(build_type.id) is True

    @allure.id("25")
    @allure.title("PUT /buildTypes/{buildTypeLocator}/parameters/{name} — изменение параметра build configuration")
    def test_update_build_configuration_parameter(self, api_manager: ApiManager, build_type):
        api_manager.build_steps.set_build_type_parameter(build_type.id, BuildParams.PARAM_NAME, BuildParams.PARAM_VALUE)
        parameter = api_manager.build_steps.get_build_type_parameter(build_type.id, BuildParams.PARAM_NAME)
        assert parameter.get("value") == BuildParams.PARAM_VALUE
