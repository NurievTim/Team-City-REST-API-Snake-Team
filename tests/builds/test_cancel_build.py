import allure
import pytest


@pytest.mark.integraion
@pytest.mark.builds
class TestCancelBuild:
    @allure.id("8")
    @allure.title("Отмена билда в очереди (queued)")
    def test_cancel_queued_build(self):
        ...