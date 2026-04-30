from dataclasses import dataclass
from enum import Enum
from typing import Optional

from src.models.base_model import BaseModel
from src.models.requests import (CreateProjectRequest, CreateBuildTypeRequest, QueueBuildRequest,
                                 CopyBuildTypeRequest, CreateVcsRootRequest,)
from src.models.responses import (ServerInfoResponse, CurrentUserResponse, ProjectResponse, ProjectsListResponse,
                                  BuildTypeResponse, QueueBuildResponse, AgentsListResponse, VcsRootResponse)


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

    GET_PROJECTS = EndpointConfig(
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

    QUEUE_BUILD = EndpointConfig(
        url='buildQueue',
        request_model=QueueBuildRequest,
        response_model=QueueBuildResponse,
    )

    GET_AGENTS = EndpointConfig(
        url='agents',
        request_model=None,
        response_model=AgentsListResponse,
    )

    COPY_BUILD_TYPE_TO_PROJECT = EndpointConfig(
        url='projects',
        request_model=CopyBuildTypeRequest,
        response_model=BuildTypeResponse,
    )

    CREATE_VCS_ROOT = EndpointConfig(
        url='vcs-roots',
        request_model=CreateVcsRootRequest,
        response_model=VcsRootResponse,
    )
