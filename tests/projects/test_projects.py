import allure
import pytest
import requests

from framework.checkers import check


@pytest.mark.smoke
class TestProjectsSmoke:
    @allure.id('3')
    @allure.title('GET /projects без токена, 401')
    def test_get_projects_without_token(self, team_city_api_client, no_auth_headers):
        response = team_city_api_client.get_projects(headers=no_auth_headers, check_status=None)
        check.check_status_code(response=response, expected_status_code=requests.codes.unauthorized)
