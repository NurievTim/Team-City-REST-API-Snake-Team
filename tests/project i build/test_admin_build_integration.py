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

    @allure.id("28")
    @allure.title("POST /buildTypes/{locator}/move — перемещение build configuration в другой проект")
    def test_move_build_configuration(self, api_manager: ApiManager, build_type, target_project):
        api_manager.build_steps.move_build_type_to_project(build_type.id, target_project.id)
        fetched = api_manager.build_steps.get_build_type_by_id(build_type.id)

        assert fetched.project.get("id") == target_project.id

    @allure.id("29.1")
    @allure.title("POST /projects — создание подпроекта с parentProject")
    def test_create_sub_project(self, api_manager: ApiManager, created_project, sub_project_request):
        created = api_manager.project_steps.create_project(sub_project_request)
        fetched = api_manager.project_steps.get_project_by_id(created.id)

        assert fetched.id == sub_project_request.id
        assert fetched.parentProjectId == created_project.id

    @allure.id("29")
    @allure.title("GET /buildTypes?locator=affectedProject — рекурсивный поиск build configs")
    def test_get_build_by_affected_project(self, api_manager: ApiManager, build_type, sub_build_type, created_project):
        build_types = api_manager.build_steps.get_build_by_affected_project(created_project.id)

        assert build_type.id in build_types.get_ids()
        assert sub_build_type.id in build_types.get_ids()
