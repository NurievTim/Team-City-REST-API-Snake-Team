import allure
import requests
from hamcrest import assert_that, equal_to, contains_string, greater_than_or_equal_to
from jsonschema import validate
from pydantic import BaseModel


@allure.step('Проверить, что модель ответа равна ожидаемой')
def check_json_schema(response: requests.Response | dict, schema: type[BaseModel] | dict) -> None:
    """Function to check json_schema for response"""
    if isinstance(response, requests.Response):
        response = response.json()
    if not isinstance(schema, dict):
        schema = schema.model_json_schema()
    validate(instance=response, schema=schema)


@allure.step('Проверить, что статус код равен {expected_status_code}')
def check_status_code(response: requests.Response, expected_status_code: int) -> None:
    """Function to check expected_status_code in response"""
    actual_status_code = response.status_code

    assert_that(
        actual_status_code,
        equal_to(expected_status_code),
        f"Response's status code was expected to be {expected_status_code}, but was {actual_status_code}! "
        f'Check out current response problem: \n'
        f'{response.content}',
    )

@allure.step('Проверить, что состояние билда равна {expected_state}')
def check_build_state(response: requests.Response | dict, expected_state: str) -> None:
    """Function to check state in response"""
    state = response.json().get('state')

    assert_that(state, contains_string(expected_state),
                f'State was expected to be {expected_state} but was {state}')


@allure.step('Проверить, что статус билда равен {expected_status}')
def check_build_status(response: requests.Response, expected_status: str) -> None:
    """Function to check status in response"""
    status = response.json().get('statusText')

    assert_that(status, contains_string(expected_status),
                f'State was expected to be {expected_status} but was {status}')


@allure.step('Проверить, что авторизованных агентов >= 1 ')
def check_agent_is_authorize(response: requests.Response) -> None:
    """Function to check authorized agents in response >= 1"""
    count = response.json().get('count')
    assert_that(count, greater_than_or_equal_to(1),
                f' {count} is False')