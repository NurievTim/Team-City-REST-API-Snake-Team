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
    id: str
    name: str
    project: ProjectRef


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

