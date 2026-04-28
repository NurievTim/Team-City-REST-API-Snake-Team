from typing import Dict, Callable
from src.models.base_model import BaseModel
from src.requests.skeleton.endpoint import Endpoint


class HttpRequest:
    def __init__(self, request_spec: Dict[str, str], endpoint: Endpoint, response_spec: Callable):
        self.headers = request_spec.get('headers')
        self.base_url = request_spec.get('base_url', 'http://localhost:8111/app/rest/')
        self.endpoint = endpoint
        self.response_spec = response_spec

