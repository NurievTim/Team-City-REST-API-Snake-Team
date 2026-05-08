from typing import Annotated, Optional
from src.generators.generating_rule import GeneratingRule
from src.models.base_model import BaseModel


class CreateUserRequest(BaseModel):
    username: Annotated[str, GeneratingRule(regex=r"^[A-Za-z][A-Za-z0-9]{3,10}$")]
    password: Annotated[str, GeneratingRule(regex=r"^[A-Z]{2}[a-z]{3}[0-9]{2}[!@#]{1}$")]
    email: Annotated[Optional[str], GeneratingRule(skip=True)] = None
    name: Annotated[Optional[str], GeneratingRule(skip=True)] = None
