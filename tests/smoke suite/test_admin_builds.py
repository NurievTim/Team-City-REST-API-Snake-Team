import allure
import pytest

from src.steps.build_steps import BuildSteps


@pytest.mark.smoke
class TestBuilds:
    @allure.id("5.1")
    @allure.title("POST /buildTypes — создать build configs, id и name совпадают")
    def test_create_build_type(self, build_steps: BuildSteps, build_type_request):
        created_build_type = build_steps.create_build_type(build_type_request)
        fetched_build_type = build_steps.get_build_type_by_id(created_build_type.id)

        assert fetched_build_type.id == build_type_request.id
        assert fetched_build_type.name == build_type_request.name

        build_steps.delete_build_type(created_build_type.id)

    @allure.id("5")
    @allure.title("POST /buildQueue — поставить сборку в очередь, state=queued")
    def test_queue_build_state_is_queued(self, build_steps: BuildSteps, build_type_request, queue_build_request):
        created_build_type = build_steps.create_build_type(build_type_request)
        fetched_build_type = build_steps.get_build_type_by_id(created_build_type.id)
        assert fetched_build_type.id == build_type_request.id

        queued_build = build_steps.add_build_to_queue(queue_build_request)
        fetched_queued_build = build_steps.get_queued_build_by_id(queued_build.id)
        assert fetched_queued_build.state == 'queued'

        build_steps.cancel_queued_build(queued_build.id)
        build_steps.delete_build_type(created_build_type.id)
