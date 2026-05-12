import os
import pytest
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture()
def admin_username() -> str:
    return os.getenv("TC_ADMIN_USERNAME")


@pytest.fixture()
def admin_password() -> str:
    return os.getenv("TC_ADMIN_PASSWORD")
