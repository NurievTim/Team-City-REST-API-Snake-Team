import os
import allure
import pytest
import requests
import uuid

from dotenv import load_dotenv

load_dotenv()


@pytest.mark.smoke
class TestProjects:

    @allure.id("3")  # запрос без валидного токена возвращает 401
    @allure.title("GET /projects — HTTP 401 при невалидном токене")
    def test_get_projects_unauthorized(self):
        response = requests.get(
            url=f'http://localhost:8111/app/rest/projects',
            headers={
                'Authorization': 'Bearer invalid_token',
                'Content-Type': 'application/json',
                'Accept': 'application/json',
            }
        )

        assert response.status_code == 401

    @allure.id("4")  # есть хотя бы один проект
    @allure.title("GET /projects — HTTP 200, count >= 1")
    def test_get_projects_count(self):
        response = requests.get(
            url=f'http://localhost:8111/app/rest/projects',
            headers={
                'Authorization': f'Bearer {os.getenv("TC_ADMIN_TOKEN")}',
                'Content-Type': 'application/json',
                'Accept': 'application/json',
            }
        )

        assert response.status_code == 200
        assert response.json().get('count') >= 1

    @allure.id("6")
    @allure.title("POST /projects — создать проект, count вырос")
    def test_create_project_increases_count(self):
        count_before = requests.get(
            url=f'http://localhost:8111/app/rest/projects',
            headers={
                'Authorization': f'Bearer {os.getenv("TC_ADMIN_TOKEN")}',
                'Content-Type': 'application/json',
                'Accept': 'application/json',
            }
        ).json().get('count', 0)

        uid = uuid.uuid4().hex[:8].upper()
        project_id = f'SmokeProject{uid}'

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

        create_response = requests.post(
            url=f'http://localhost:8111/app/rest/projects',
            headers=write_headers,
            json={
                'id': project_id,
                'name': f'Smoke Test Project {uid}',
                'parentProject': {'locator': '_Root'},
            },
        )

        assert create_response.status_code == 200

        count_after = requests.get(
            url=f'http://localhost:8111/app/rest/projects',
            headers={
                'Authorization': f'Bearer {os.getenv("TC_ADMIN_TOKEN")}',
                'Content-Type': 'application/json',
                'Accept': 'application/json',
            }
        ).json().get('count', 0)

        assert count_after > count_before

        requests.delete(
            url=f'http://localhost:8111/app/rest/projects/id:{project_id}',
            headers=write_headers,
        )
