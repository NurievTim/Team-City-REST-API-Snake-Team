import allure
import pytest


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
    def test_copy_build_configuration(self, build_requester, copy_build_request, created_project):
        copied = build_requester.copy_build_type_to_project(created_project.id, copy_build_request)

        assert copied.id == copy_build_request.id
        assert copied.project is not None
        assert copied.project.get("id") == created_project.id

        build_requester.delete_build_type(copy_build_request.id)
        build_requester.delete_build_type(copy_build_request._source_build_id)

    @allure.id("24")
    @allure.title("PUT /buildTypes/{buildTypeLocator}/paused — приостановка build configuration")
    def test_pause_build_configuration(self, build_requester, build_type_request):
        created_build_type = build_requester.create_build_type(build_type_request)
        assert build_requester.get_build_type_paused(created_build_type.id) is False

        build_requester.set_build_type_paused(created_build_type.id, True)
        assert build_requester.get_build_type_paused(created_build_type.id) is True

        build_requester.set_build_type_paused(created_build_type.id, False)
        build_requester.delete_build_type(created_build_type.id)

    @allure.id("25")
    @allure.title("PUT /buildTypes/{buildTypeLocator}/parameters/{name} — изменение параметра build configuration")
    def test_update_build_configuration_parameter(self, build_requester, build_type_with_param ):
        created_build_type, parameter_name = build_type_with_param
        new_value = "NEW_parameter"

        build_requester.set_build_type_parameter(created_build_type.id, parameter_name, new_value)
        parameter = build_requester.get_build_type_parameter(created_build_type.id, parameter_name)

        assert parameter.get("value") == new_value
        build_requester.delete_build_type_parameter(created_build_type.id, parameter_name)
        build_requester.delete_build_type(created_build_type.id)
