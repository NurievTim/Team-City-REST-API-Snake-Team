from src.models.base_model import BaseModel
from typing import Optional


class ServerInfoResponse(BaseModel):
    version: str
    buildDate: Optional[str] = None
    buildNumber: Optional[str] = None


class CurrentUserResponse(BaseModel):
    username: str
    id: Optional[int] = None
    name: Optional[str] = None


class ProjectResponse(BaseModel):
    id: str
    name: str


class ProjectsListResponse(BaseModel):
    count: int
    project: Optional[list] = None


class BuildTypeResponse(BaseModel):
    id: str
    name: str
    project: Optional[dict] = None


class QueueBuildResponse(BaseModel):
    id: int
    state: str
    buildType: Optional[dict] = None
    status: str


class AgentsListResponse(BaseModel):
    count: int
    agent: Optional[list] = None


class VcsRootResponse(BaseModel):
    id: str
    name: str
    vcsName: Optional[str] = None
    project: Optional[dict] = None

