import requests

from src.configs.config import Config
from src.models.base_model import BaseModel
from src.requests.skeleton.endpoint import Endpoint
from src.requests.skeleton.http_request import HttpRequest
from src.requests.skeleton.interfaces.crud_end_interface import CrudEndpointInterface


class CrudRequester(HttpRequest, CrudEndpointInterface):

    @property
    def base_url(self) -> str:
        return f"{Config.get('baseurl')}"

    def post(self, model: BaseModel, endpoint: Endpoint = None) -> requests.Response:
        ep = endpoint or self.endpoint
        url = f'{self.base_url}{ep.value.url}'
        response = requests.post(url=url, json=model.model_dump(), headers=self.headers)
        self.response_spec(response)
        return response

    def get(self, endpoint: Endpoint = None, locator: str = None, params: dict = None) -> requests.Response:
        ep = endpoint or self.endpoint
        url = f'{self.base_url}{ep.value.url}'
        if locator:
            url = f'{url}/{locator}'
        response = requests.get(url=url, headers=self.headers, params=params)
        self.response_spec(response)
        return response

    def delete(self, locator: str, endpoint: Endpoint = None) -> requests.Response:
        ep = endpoint or self.endpoint
        url = f'{self.base_url}{ep.value.url}/{locator}'
        response = requests.delete(url=url, headers=self.headers)
        self.response_spec(response)
        return response
