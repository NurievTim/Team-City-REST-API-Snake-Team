import pytest
from playwright.sync_api import Page

from src.api.models.requests import LoginUserRequest
from src.ui.pages.login_page import LoginPage


@pytest.fixture(autouse=True)
def admin_session_autologin(
    request: pytest.FixtureRequest,
    page: Page,
    admin_user_request: LoginUserRequest
):
    print(">>> Фикстура admin_session_autologin ВЫЗВАНА для теста", request.node.name)
    mark = request.node.get_closest_marker("admin_session")
    if not mark:
        print(">>> Маркер admin_session НЕ найден, выходим")
        return
    print(">>> Маркер найден, вызываем auth_as_admin")

    LoginPage(page).auth_as_admin(admin_user_request)