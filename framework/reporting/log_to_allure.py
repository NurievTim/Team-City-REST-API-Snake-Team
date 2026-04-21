import allure
import requests


def attach_request(prepared_request: requests.PreparedRequest) -> None:
    request_dump = (
        f"{prepared_request.method} {prepared_request.url}\n"
        f"Headers: {dict(prepared_request.headers)}\n"
        f"Body: {prepared_request.body}"
    )
    allure.attach(request_dump, name="request", attachment_type=allure.attachment_type.TEXT)


def attach_response(response: requests.Response) -> None:
    response_dump = (
        f"Status: {response.status_code}\n"
        f"Headers: {dict(response.headers)}\n"
        f"Body: {response.text}"
    )
    allure.attach(response_dump, name="response", attachment_type=allure.attachment_type.TEXT)
