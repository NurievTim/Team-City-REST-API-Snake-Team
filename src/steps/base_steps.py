from typing import Any


class BaseSteps:
    def __init__(self, created_objects: list[Any] = None):
        self.created_objects = created_objects or []
