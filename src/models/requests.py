from typing import Annotated

from pydantic import Field

from src.generators.generating_rule import GeneratingRule
from src.models.base_model import BaseModel


class ParentProject(BaseModel):
    locator: str = '_Root'


class CreateProjectRequest(BaseModel):
    id: str
    name: str
    parentProject: ParentProject = ParentProject()


class ProjectRef(BaseModel):
    id: str


class CreateBuildTypeRequest(BaseModel):
    id: Annotated[str, GeneratingRule(regex=r"^BuildTypeId_[a-z0-9]{4}$")]
    name: Annotated[str, GeneratingRule(regex=r"^BuildTypeName_[a-z0-9]{4}$")]
    project: ProjectRef = Field(default=None)


class BuildTypeRef(BaseModel):
    id: str


class QueueBuildRequest(BaseModel):
    buildType: BuildTypeRef


class CopyBuildTypeRequest(BaseModel):
    sourceBuildTypeLocator: str
    name: str
    id: str
    copyAllAssociatedSettings: bool = True


class VcsRootProjectRef(BaseModel):
    id: str


class VcsRootProperty(BaseModel):
    name: str
    value: str


class VcsRootProperties(BaseModel):
    property: list[VcsRootProperty]


class CreateVcsRootRequest(BaseModel):
    id: str
    name: str
    vcsName: str
    project: VcsRootProjectRef
    properties: VcsRootProperties


class BuildCancelRequest(BaseModel):
    comment: str
    readdIntoQueue: bool

