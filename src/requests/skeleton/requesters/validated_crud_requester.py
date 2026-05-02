from typing import TypeVar, Optional

import requests
from pydantic import TypeAdapter

from src.models.base_model import BaseModel
from src.requests.skeleton.http_request import HttpRequest
from src.requests.skeleton.requesters.crud_requester import CrudRequester

T = TypeVar('T', bound=BaseModel)


class ValidatedCrudRequester(HttpRequest):
    def __init__(self, request_spec, endpoint, response_spec):
        super().__init__(request_spec, endpoint, response_spec)
        self.crud_requester = CrudRequester(
            request_spec=request_spec,
            endpoint=endpoint,
            response_spec=response_spec
        )
        self._adapter = TypeAdapter(self.endpoint.value.response_model)

    def post(self, model: Optional[T] = None, locator: Optional[str] = None):
        response = self.crud_requester.post(model, locator)
        return self._adapter.validate_python(response.json())

    def get(self, id: int):
        response = self.crud_requester.get(id)
        return self._adapter.validate_python(response.json())

    def get_all(self) -> requests.Response:
        response = self.crud_requester.get_all()
        return response

    def update(self, id: int): ...
    def delete(self, id: int): ...
