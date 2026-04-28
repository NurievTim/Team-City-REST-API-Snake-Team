from typing import Optional, Protocol
from src.models.base_model import BaseModel


class CrudEndpointInterface(Protocol):
    def post(self, model: BaseModel) -> BaseModel: ...

    def get(self, model: Optional[BaseModel] = None, locator: Optional[str] = None) -> BaseModel: ...

    def delete(self, locator: str) -> None: ...
