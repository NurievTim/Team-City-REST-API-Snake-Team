import logging
import os

import requests
from dotenv import load_dotenv

from src.api.models.requests import LoginUserRequest
from src.api.requests.skeleton.endpoint import Endpoint
from src.api.requests.skeleton.requesters.crud_requester import CrudRequester
from src.api.specs.response_spec import ResponseSpecs

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
            requester = CrudRequester(
                request_spec=RequestSpecs.unauth_spec(),
                endpoint=Endpoint.LOGIN_USER,
                response_spec=ResponseSpecs.request_return_ok()
            )
            response = requester.post(LoginUserRequest(username=username, password=password))
            return response

        except Exception as e:
            logging.error(f"Authentication failed for {username}: {e}")
            raise Exception("Failed to authenticate user") from e