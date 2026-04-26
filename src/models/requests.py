from pydantic import BaseModel


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

