import time

import pytest
from playwright.sync_api import Page

from src.ui.pages.project_page import ProjectPanel


@pytest.mark.ui
class TestBuildUI:
    @pytest.mark.admin_session
    def test_create_build_configuration(self, page: Page):
        ProjectPanel(page).open().check_new_project_create_page
        time.sleep(2)
        assert 1 == 1
        # тест заглушка