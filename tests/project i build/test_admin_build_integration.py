import allure
import pytest

from src.models.requests import CopyBuildTypeRequest
from src.steps.build_steps import BuildSteps


@pytest.mark.projectIbuild
class TestBuildConfig:

    @allure.id("22")
    @allure.title("POST /buildTypes — создать build configuration")
    def test_create_build_configuration(self, build_steps: BuildSteps, build_type_request):
        created = build_steps.create_build_type(build_type_request)
        fetched = build_steps.get_build_type_by_id(created.id)

        assert fetched.id == build_type_request.id
        assert fetched.name == build_type_request.name
        build_steps.delete_build_type(created.id)

    @allure.id("23")
    @allure.title("POST /projects/{projectLocator}/buildTypes — копирование build configuration")
    def test_copy_build_configuration(self, build_steps: BuildSteps, build_type_request, copy_build_request,
                                      created_project):
        source = build_steps.create_build_type(build_type_request)
        fetched_source = build_steps.get_build_type_by_id(source.id)
        assert fetched_source.id == source.id
        assert fetched_source.name == build_type_request.name

        copied = build_steps.copy_build_type_to_project(created_project.id, copy_build_request)
        fetched_copy = build_steps.get_build_type_by_id(copied.id)
        assert fetched_copy.id == copy_build_request.id
        assert fetched_copy.project is not None
        assert fetched_copy.project.get("id") == created_project.id

        build_steps.delete_build_type(copied.id)
        build_steps.delete_build_type(source.id)

    @allure.id("24")
    @allure.title("PUT /buildTypes/{buildTypeLocator}/paused — приостановка build configuration")
    def test_pause_build_configuration(self, build_steps: BuildSteps, build_type_request):
        created = build_steps.create_build_type(build_type_request)
        fetched = build_steps.get_build_type_by_id(created.id)

        assert fetched.id == build_type_request.id
        assert build_steps.get_build_type_paused(fetched.id) is False

        build_steps.set_build_type_paused(fetched.id, True)
        assert build_steps.get_build_type_paused(fetched.id) is True

        build_steps.set_build_type_paused(fetched.id, False)
        build_steps.delete_build_type(created.id)

    @allure.id("25")
    @allure.title("PUT /buildTypes/{buildTypeLocator}/parameters/{name} — изменение параметра build configuration")
    def test_update_build_configuration_parameter(self, build_steps: BuildSteps, build_type_request):
        created = build_steps.create_build_type(build_type_request)
        fetched = build_steps.get_build_type_by_id(created.id)
        assert fetched.id == build_type_request.id

        parameter_name = 'env.SMOKE_PARAM'
        new_value = 'NEW_parameter'
        build_steps.set_build_type_parameter(fetched.id, parameter_name, new_value)
        parameter = build_steps.get_build_type_parameter(fetched.id, parameter_name)
        assert parameter.get("value") == new_value

        build_steps.delete_build_type_parameter(fetched.id, parameter_name)
        build_steps.delete_build_type(created.id)
