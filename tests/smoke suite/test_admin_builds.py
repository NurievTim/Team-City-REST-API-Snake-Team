import allure
import pytest

from framework.steps.admin_steps import AdminSteps


@pytest.mark.smoke
class TestBuilds:

    @allure.id("6")
    @allure.title("POST /buildQueue — поставить сборку в очередь, state=queued")
    def test_queue_build_state_is_queued(self, project_with_build_type: dict, admin_steps: AdminSteps) -> None:
        admin_steps.queue_build_and_assert_queued(build_type_id=project_with_build_type["build_type_id"])

