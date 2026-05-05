import allure
import pytest

from src.enums import BuildStatus, BuildState


@pytest.mark.integraion
@pytest.mark.builds
class TestCancelBuild:
    @allure.id("8")
    @allure.title("Отмена билда в очереди (queued)")
    @pytest.mark.usefixtures('api_manager', 'queue_build')
    def test_cancel_queued_build(self, api_manager, queue_build, build_cancel_request):
        response = api_manager.build_steps.cancel_queued_build(build_cancel_request, queue_build.id)

        assert response.status == BuildStatus.UNKNOWN
        assert response.state == BuildState.FINISHED

    # @allure.id("9")
    # @allure.title("Отмена запущенного билда (running)")
    # @pytest.mark.usefixtures('api_manager', 'queue_build')
    # def test_cancel_queued_build(self, api_manager, queue_build, build_cancel_request):
    #     response = api_manager.build_steps.cancel_queued_build(build_cancel_request, queue_build.id)
    #
    #     assert response.status == BuildStatus.UNKNOWN
    #     assert response.state == BuildState.FINISHED