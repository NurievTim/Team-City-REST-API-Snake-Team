from dataclasses import dataclass
from enum import Enum

from src.main.models.base_model import BaseModel


@dataclass(frozen=True)
class EndpointConfig:
    url: str
    request_model: BaseModel
    response_model: BaseModel


class Endpoint(Enum):

    ADD_PROJECT = EndpointConfig(
        url='/app/rest/projects',
        request_model=CreateUserRequest,
        response_model=CreateUserResponse
    )