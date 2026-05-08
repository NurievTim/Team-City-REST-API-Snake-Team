import allure
import pytest

from src.classes.api_manager import ApiManager
from src.models.requests import QueueBuildRequest


@pytest.mark.integraion
@pytest.mark.builds
class TestStartBuild:
    @allure.id("10")
    @allure.title("Запуск custom build (параметры, ветка, агент)")
    @pytest.mark.usefixtures('enable_agent', 'api_manager', 'custom_build_request')
    def test_start_custom_build(
            self,
            api_manager: ApiManager,
            custom_build_request: QueueBuildRequest,
    ):
        response = api_manager.build_steps.add_build_to_queue(custom_build_request)

        assert response.comment.text == custom_build_request.comment.text
