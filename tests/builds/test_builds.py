import allure
import pytest
import requests

from framework.checkers import check


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
            'comment': 'Cancelled by test #8',
            'readdIntoQueue': False
        }
        response = team_city_api_client.cancel_queued_build(
            data=payload,
            headers=admin_headers,
            queued_build_locator=f'id:{build_id}'
        )

        check.check_status_code(response=response, expected_status_code=requests.codes.ok)
        check.check_canceled_build_status(response=response, expected_status='Canceled')
