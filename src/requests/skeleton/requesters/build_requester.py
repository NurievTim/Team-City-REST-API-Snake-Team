import requests

from src.models.requests import CreateBuildTypeRequest, QueueBuildRequest, CopyBuildTypeRequest
from src.models.responses import BuildTypeResponse, QueueBuildResponse
from src.requests.skeleton.endpoint import Endpoint
from src.requests.skeleton.requesters.crud_requester import CrudRequester
from src.specs.response_spec import ResponseSpecs


class BuildRequester(CrudRequester):

    def create_build_type(self, create_build_type_request: CreateBuildTypeRequest) -> BuildTypeResponse:
        response = self.post(model=create_build_type_request, endpoint=Endpoint.CREATE_BUILD_TYPE)
        return BuildTypeResponse(**response.json())

    def queue_build(self, queue_build_request: QueueBuildRequest) -> QueueBuildResponse:
        response = self.post(model=queue_build_request, endpoint=Endpoint.QUEUE_BUILD)
        return QueueBuildResponse(**response.json())

    def delete_build_type(self, build_type_id: str) -> None:
        previous_spec = self.response_spec
        try:
            self.response_spec = ResponseSpecs.entity_was_deleted()
            self.delete(locator=f'id:{build_type_id}', endpoint=Endpoint.CREATE_BUILD_TYPE)
        finally:
            self.response_spec = previous_spec

    def copy_build_type_to_project(self, project_id: str, copy_request: CopyBuildTypeRequest) -> BuildTypeResponse:
        response = self.post(
            model=copy_request,
            endpoint=Endpoint.COPY_BUILD_TYPE_TO_PROJECT,
            locator=f"id:{project_id}",
            suffix="buildTypes",
        )
        return BuildTypeResponse(**response.json())

    def set_build_type_paused(self, build_type_id: str, paused: bool) -> None:
        headers = dict(self.headers)
        headers["Content-Type"] = "text/plain"
        headers["Accept"] = "text/plain"
        response = requests.put(
            url=f"{self.base_url}{Endpoint.CREATE_BUILD_TYPE.value.url}/id:{build_type_id}/paused",
            data=str(paused).lower(),
            headers=headers,
        )
        self.response_spec(response)

    def get_build_type_paused(self, build_type_id: str) -> bool:
        headers = dict(self.headers)
        headers["Accept"] = "text/plain"
        response = requests.get(
            url=f"{self.base_url}{Endpoint.CREATE_BUILD_TYPE.value.url}/id:{build_type_id}/paused",
            headers=headers,
        )
        self.response_spec(response)
        return response.text.strip().lower() == "true"

    def create_build_type_parameter(self, build_type_id: str, name: str, value: str) -> None:
        response = requests.post(
            url=f"{self.base_url}{Endpoint.CREATE_BUILD_TYPE.value.url}/id:{build_type_id}/parameters",
            json={"name": name, "value": value},
            headers=self.headers,
        )
        self.response_spec(response)

    def set_build_type_parameter(self, build_type_id: str, name: str, value: str) -> None:
        headers = dict(self.headers)
        headers["Content-Type"] = "text/plain"
        headers["Accept"] = "text/plain"
        response = requests.put(
            url=f"{self.base_url}{Endpoint.CREATE_BUILD_TYPE.value.url}/id:{build_type_id}/parameters/{name}",
            data=value,
            headers=headers,
        )
        self.response_spec(response)

    def get_build_type_parameter(self, build_type_id: str, name: str) -> dict:
        response = requests.get(
            url=f"{self.base_url}{Endpoint.CREATE_BUILD_TYPE.value.url}/id:{build_type_id}/parameters/{name}",
            headers=self.headers,
        )
        self.response_spec(response)
        return response.json()

    def delete_build_type_parameter(self, build_type_id: str, name: str) -> None:
        previous_spec = self.response_spec
        try:
            self.response_spec = ResponseSpecs.entity_was_deleted()
            response = requests.delete(
                url=f"{self.base_url}{Endpoint.CREATE_BUILD_TYPE.value.url}/id:{build_type_id}/parameters/{name}",
                headers=self.headers,
            )
            self.response_spec(response)
        finally:
            self.response_spec = previous_spec
