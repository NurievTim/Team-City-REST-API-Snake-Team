from dataclasses import dataclass
from enum import Enum
from typing import Optional

from src.models.base_model import BaseModel
from src.models.requests import (CreateProjectRequest, CreateBuildTypeRequest, QueueBuildRequest)
from src.models.responses import (ServerInfoResponse, CurrentUserResponse, ProjectResponse, ProjectsListResponse, BuildTypeResponse, QueueBuildResponse, AgentsListResponse)


@dataclass(frozen=True)
class EndpointConfig:
    url: str
    request_model: Optional[type[BaseModel]]
    response_model: Optional[type[BaseModel]]


class Endpoint(Enum):
    GET_SERVER_INFO = EndpointConfig(
        url='server',
        request_model=None,
        response_model=ServerInfoResponse,
    )

    GET_CURRENT_USER = EndpointConfig(
        url='users/current',
        request_model=None,
        response_model=CurrentUserResponse,
    )

    GET_PROJECT = EndpointConfig(
        url='projects',
        request_model=None,
        response_model=ProjectsListResponse,
    )

    CREATE_PROJECT = EndpointConfig(
        url='projects',
        request_model=CreateProjectRequest,
        response_model=ProjectResponse,
    )

    DELETE_PROJECT = EndpointConfig(
        url='projects',
        request_model=None,
        response_model=None,
    )

    CREATE_BUILD_TYPE = EndpointConfig(
        url='buildTypes',
        request_model=CreateBuildTypeRequest,
        response_model=BuildTypeResponse,
    )

    GET_BUILD_TYPE = EndpointConfig(
        url='buildTypes',
        request_model=None,
        response_model=BuildTypeResponse,
    )

    QUEUE_BUILD = EndpointConfig(
        url='buildQueue',
        request_model=QueueBuildRequest,
        response_model=QueueBuildResponse,
    )

    GET_QUEUED_BUILD = EndpointConfig(
        url='buildQueue',
        request_model=None,
        response_model=QueueBuildResponse,
    )

    GET_AGENT = EndpointConfig(
        url='agents',
        request_model=None,
        response_model=AgentsListResponse,
    )
