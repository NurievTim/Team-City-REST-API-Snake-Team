import pytest
import allure

from src.models.comparison.model_assertions import ModelAssertions
from src.models.requests import (QueueBuildRequest, BuildTypeRef)


@pytest.mark.smoke
class TestBuilds:
    @allure.id("5.1")
    @allure.title("POST /buildTypes — создать build configs, id и name совпадают")
    def test_create_build_type(self, build_requester, build_type_request):
        build_type = build_requester.create_build_type(build_type_request)
        ModelAssertions(build_type_request, build_type).match()

    @allure.id("5")
    @allure.title("POST /buildQueue — поставить сборку в очередь, state=queued")
    def test_queue_build_state_is_queued(self, build_requester, build_type_request):
        build_requester.create_build_type(build_type_request)
        queue_response = build_requester.queue_build(
            QueueBuildRequest(buildType=BuildTypeRef(id=build_type_request.id)))
        assert queue_response.state == 'queued'
