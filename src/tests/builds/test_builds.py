import allure
import pytest
import requests

from framework.checkers import check
from framework.helpers import build_helper


@pytest.mark.integration
@pytest.mark.builds
class TestBuilds:
    @allure.id('8')
    @allure.title('Отмена билда в очереди (queued)')
    def test_cancel_build_in_queue(self, team_city_api_client, admin_headers, created_build_type):
        add_build_response = team_city_api_client.add_build_to_queue(
            data={'buildType': {'id': created_build_type}},
            headers=admin_headers
        )
        build_data = add_build_response.json()
        build_id = build_data.get('id')
        if not build_id:
            pytest.fail("В ответе add_build_to_queue отсутствует поле id")

        payload = {
            'comment': 'Cancelled queued by test #8',
            'readdIntoQueue': False
        }
        response = team_city_api_client.cancel_queued_build(
            data=payload,
            headers=admin_headers,
            queued_build_locator=f'id:{build_id}',
            need_log=True
        )

        check.check_status_code(response=response, expected_status_code=requests.codes.ok)
        check.check_build_state(response=response, expected_state='finished')

    @allure.id('9')
    @allure.title('Отмена запущенного билда (running)')
    def test_cancel_running_build(self, team_city_api_client, admin_headers, created_build_type):
        add_build_response = team_city_api_client.add_build_to_queue(
            data={'buildType': {'id': created_build_type}},
            headers=admin_headers
        )
        build_data = add_build_response.json()
        build_id = build_data.get('id')
        if not build_id:
            pytest.fail("В ответе add_build_to_queue отсутствует поле id")
        build_helper.wait_for_build_state(
            client=team_city_api_client,
            headers=admin_headers,
            build_id=build_id,
            target_state='running'
        )
        payload = {
            'comment': 'Cancelled running build by test #9',
            'readdIntoQueue': False
        }
        response = team_city_api_client.cancel_running_build(
            build_locator=f'id:{build_id}',
            headers=admin_headers,
            data=payload
        )

        check.check_status_code(response=response, expected_status_code=requests.codes.ok)
        check.check_build_state(response=response, expected_state='running')
        check.check_build_status(response=response, expected_status='Canceled')
