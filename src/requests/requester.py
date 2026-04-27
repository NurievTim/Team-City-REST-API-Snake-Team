import requests

from abc import ABC
from typing import Dict, Callable
from src.models.base_model import BaseModel


class BaseRequester(ABC):
    def __init__(self, request_spec: Dict[str, str], response_spec: Callable):
        self.headers = request_spec.get('headers')
        self.base_url = request_spec.get('base_url', 'http://localhost:8111/app/rest/')
        self.response_spec = response_spec

    def _get(self, path: str) -> requests.Response:
        response = requests.get(url=f'{self.base_url}{path}', headers=self.headers)
        self.response_spec(response)
        return response

    def _get_with_params(self, path: str, params: dict) -> requests.Response:
        response = requests.get(url=f'{self.base_url}{path}', headers=self.headers, params=params)
        self.response_spec(response)
        return response

    def _post(self, path: str, model: BaseModel) -> requests.Response:
        response = requests.post(url=f'{self.base_url}{path}', json=model.model_dump(), headers=self.headers)
        self.response_spec(response)
        return response

    def _delete(self, path: str) -> requests.Response:
        response = requests.delete(url=f'{self.base_url}{path}', headers=self.headers)
        self.response_spec(response)
        return response

