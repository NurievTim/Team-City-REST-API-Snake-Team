import allure
import pytest

from src.classes.api_manager import ApiManager
from src.enums import BuildState
from src.models.requests import BuildCancelRequest, QueueBuildRequest
from src.models.responses import QueueBuildResponse


@pytest.mark.integraion
@pytest.mark.builds
class TestCancelBuild:
    @allure.id("8")
    @allure.title("Отмена билда в очереди (queued)")
    @pytest.mark.usefixtures('queue_build', 'api_manager', 'queued_build_cancel_request')
    def test_cancel_queued_build(
            self,
            api_manager: ApiManager,
            queue_build: QueueBuildResponse,
            queued_build_cancel_request: BuildCancelRequest
    ):
        api_manager.build_steps.cancel_queued_build(queued_build_cancel_request, queue_build.id)

    @allure.id("9")
    @allure.title("Отмена запущенного билда (running)")
    @pytest.mark.usefixtures('enable_agent', 'api_manager', 'queue_build', 'running_build_cancel_request')
    def test_cancel_running_build(
            self,
            api_manager: ApiManager,
            queue_build: QueueBuildResponse,
            running_build_cancel_request: BuildCancelRequest
    ):
        api_manager.build_steps.cancel_running_build(running_build_cancel_request, queue_build.id)
