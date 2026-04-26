import os
import uuid
import pytest
import requests
import allure

from dotenv import load_dotenv

load_dotenv()


@pytest.mark.smoke
class TestBuilds:

    @allure.id("5")
    @allure.title("POST /buildQueue — поставить сборку в очередь, state=queued")
    def test_queue_build_state_is_queued(self):
        csrf_response = requests.get(
            url=f'http://localhost:8111/app/rest/csrf',
            headers={
                'Authorization': f'Bearer {os.getenv("TC_ADMIN_TOKEN")}',
                'Content-Type': 'application/json',
                'Accept': 'application/json',
            }
        )
        write_headers = {
            'Authorization': f'Bearer {os.getenv("TC_ADMIN_TOKEN")}',
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'X-TC-CSRF-Token': csrf_response.text.strip()
        }

        uid = uuid.uuid4().hex[:8].upper()
        project_id = f'SmokeProject{uid}'
        build_type_id = f'{project_id}_Build'

        requests.post(
            url=f'http://localhost:8111/app/rest/projects',
            headers=write_headers,
            json={
                'id': project_id,
                'name': f'Smoke Test Project {uid}',
                'parentProject': {'locator': '_Root'},
            },
        )

        requests.post(
            url=f'http://localhost:8111/app/rest/buildTypes',
            headers=write_headers,
            json={
                'id': build_type_id,
                'name': 'Smoke Build',
                'project': {'id': project_id},
            },
        )

        response = requests.post(
            url=f'http://localhost:8111/app/rest/buildQueue',
            headers=write_headers,
            json={'buildType': {'id': build_type_id}},
        )

        assert response.status_code == 200
        assert 'queued' in response.json().get('state', '')

        requests.delete(
            url=f'http://localhost:8111/app/rest/projects/id:{project_id}',
            headers=write_headers,
        )
