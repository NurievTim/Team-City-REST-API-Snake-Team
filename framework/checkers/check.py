import allure
import pytest
import requests
from hamcrest import assert_that, equal_to
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

def check_canceled_build_status(response: requests.Response, expected_status: str) -> None:
    """Function to check expected_status in response"""
    status_text = response.json().get('statusText')

    assert_that(status_text, equal_to(expected_status), f'statusText was expected to be {expected_status} but was {status_text}')
