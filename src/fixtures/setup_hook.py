import pytest
from playwright.sync_api import Page

from src.models.requests import LoginUserRequest
from src.ui_pages.login_page import LoginPage


@pytest.fixture(autouse=True)
def admin_session_autologin(
    request: pytest.FixtureRequest,
    page: Page,
    admin_user_request: LoginUserRequest
):
    mark = request.node.get_closest_marker("admin_session")
    if not mark:
        return

    LoginPage(page).auth_as_user(admin_user_request)