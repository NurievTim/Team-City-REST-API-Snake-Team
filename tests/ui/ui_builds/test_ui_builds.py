import time

import pytest
from playwright.sync_api import Page

from src.ui_pages.project_page import ProjectPanel


@pytest.mark.ui
class TestBuildUI:
    @pytest.mark.admin_session
    def test_create_build_configuration(self, page: Page):
        create_project = ProjectPanel(page).open()
        time.sleep(2)
        # except(create_project.favorite_projects_text.to_be_visible())