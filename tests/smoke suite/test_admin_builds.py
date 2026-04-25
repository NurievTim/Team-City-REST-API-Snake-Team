import allure
import pytest

from framework.checkers import check
from framework.steps.admin_steps import AdminSteps


@pytest.mark.smoke
class TestBuilds:

    @allure.id("5")
    @allure.title("POST /buildQueue — поставить сборку в очередь, state=queued")
    def test_queue_build_state_is_queued(self, project_with_build_type: dict, admin_steps: AdminSteps) -> None:
        response = admin_steps.queue_build(build_type_id=project_with_build_type["build_type_id"])

        check.check_build_state(response=response, expected_state='queued')

