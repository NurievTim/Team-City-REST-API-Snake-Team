import logging
import os
from dotenv import load_dotenv

import requests

from src.models.requests import LoginUserRequest
from src.requests.skeleton.endpoint import Endpoint
from src.requests.skeleton.requesters.crud_requester import CrudRequester
from src.specs.response_spec import ResponseSpecs

load_dotenv()


class RequestSpecs:
    @staticmethod
    def default_req_headers():
        return {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }

    @staticmethod
    def unauth_spec():
        return RequestSpecs.default_req_headers()

    @staticmethod
    def admin_base_headers():
        headers = RequestSpecs.default_req_headers()
        headers['Authorization'] = f'Bearer {os.getenv("TC_ADMIN_TOKEN")}'
        return headers

    @staticmethod
    def auth_as_user(username, password):
        try:
            response: requests.Response = CrudRequester(
                RequestSpecs.unauth_spec(),
                Endpoint.LOGIN_USER,
                ResponseSpecs.request_return_ok()
            ).post(LoginUserRequest(username=username, password=password))
        except:
            logging.error(f"Authentication failed for {username}")
            raise Exception("Failed to authenticate user")
        else:
            auth_header = response.headers.get("Authorization")
            headers = RequestSpecs.default_req_headers()
            headers["Authorization"] = auth_header
            return headers
