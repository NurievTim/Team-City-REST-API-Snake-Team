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
    archived: Optional[bool] = None


class ProjectsListResponse(BaseModel):
    count: int
    project: Optional[list] = None


class BuildTypeResponse(BaseModel):
    id: str
    name: str
    project: Optional[dict] = None

class Comment(BaseModel):
    text: str

class QueueBuildResponse(BaseModel):
    id: int
    state: str
    buildType: Optional[dict] = None
    status: Optional[str] = None
    comment : Optional[Comment] = None


class AgentResponse(BaseModel):
    id: int
    name: str
    connected: Optional[bool] = None
    enabled: Optional[bool] = None
    authorized: Optional[bool] = None


class AgentsListResponse(BaseModel):
    count: int
    agent: list[AgentResponse]


class VcsRootResponse(BaseModel):
    id: str
    name: str
    vcsName: Optional[str] = None
    project: Optional[dict] = None