from typing import Annotated

from generators.generating_rule import GeneratingRule
from models.base_model import BaseModel
from models.requests import ParentProject


class CreateProjectRequest(BaseModel):
    id: Annotated[str, GeneratingRule(regex=r"^ProjectId_[a-z0-9]{4}$")]
    name: Annotated[str, GeneratingRule(regex=r"^Project_name_[a-z0-9]{4}$")]
    parentProject: ParentProject = ParentProject()