import pytest
from src.generators.random_model_generator import RandomModelGenerator
from src.models.requests import CreateUserRequest, LoginUserRequest


@pytest.fixture()
def user_request() -> CreateUserRequest:
    return RandomModelGenerator.generate(CreateUserRequest)


@pytest.fixture()
def created_user(user_request, api_manager):
    return api_manager.user_steps.admin_create_user(user_request)


@pytest.fixture
def admin_user_request(admin_username, admin_password):
    return LoginUserRequest(username=admin_username, password=admin_password)
