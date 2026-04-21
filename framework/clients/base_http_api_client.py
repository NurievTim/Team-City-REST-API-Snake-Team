import json
import logging
import curlify
import requests
from pydantic import BaseModel

from framework.reporting.log_to_allure import attach_request, attach_response

logger = logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s [%(levelname)s] %(name)s: %(message)s')
logger.setLevel(logging.INFO)


class BaseHttpApiClient:
    """
    Class with base http api client logic.
    ALl http api client classes must be inherited from this one.
    """

    base_url: str
    session: requests.Session
    timeout: int = 10

    def __init__(
            self,
            base_url: str,
            headers: dict | None = None,
            session: requests.Session | None = None,
            guest_session: requests.Session | None = None,
    ):
        """
        Initialize the BaseHttpApiClient.

        :param base_url: Base URL for all requests
        :param headers: Default headers to be included in all requests
        :param session: Custom session object to use instead of creating a new one
        :param guest_session: Custom guest session object to use instead of creating a new one
        """
        self.base_url = base_url
        self.session = session or requests.Session()
        self.guest_session = guest_session or requests.Session()

        default_headers = {
                              'Content-Type': 'application/json',
                              'Accept': 'application/json',
                          } | (headers or {})

        self.session.headers.update(default_headers)
        self.guest_session.headers.update(default_headers)

    def write_log_for_monitoring(
            self,
            method: str,
            uri: str,
            headers: dict | None = None,
            data: str | None = None,
            params: dict | None = None,
    ) -> None:
        """Compatibility hook for external monitoring integrations."""
        logger.debug(
            "HTTP %s %s headers=%s params=%s body=%s",
            method.upper(),
            uri,
            headers,
            params,
            data,
        )

    def request(
            self,
            method: str,
            uri: str,
            headers: dict | BaseModel | None = None,
            data: dict | BaseModel | str | None = None,
            params: dict | BaseModel | None = None,
            need_log: bool = False,
            need_allure_log: bool = True,
            check_status: int | None = requests.codes.ok,
            to_json: bool = False,
            verify: bool = False,
            timeout: int = timeout,
            files: dict | None = None,
            use_guest_session: bool = False,
    ) -> requests.Response | dict:
        """
        Override of the default method to call any api request with the ability to specify which session to use
        :param method: method type ('POST', 'GET', etc.)
        :param uri: method's uri ('/api/v1/product')
        :param headers: request's headers
        :param data: request's body
        :param params: request's query params
        :param need_log: set with True if logging is needed
        :param need_allure_log: True if logging to allure report is needed
        :param check_status: set with needed status code from requests.codes
        :param to_json: is need convert response to json
        :param verify: is need verify SSl certificate
        :param timeout: how long to wait for the server to send data before giving up
        :param files: files for upload
        :param use_guest_session: if True, use guest_session instead of session
        :return: requests.Response object or dictionary with response body
        """
        url = f'{self.base_url}{uri}'
        headers = headers or {}

        current_session = self.guest_session if use_guest_session else self.session

        if isinstance(headers, BaseModel):
            headers = headers.model_dump(by_alias=True, exclude_none=True)

        current_session.headers.update(headers)

        non_encoded_data = None
        if isinstance(data, BaseModel):
            non_encoded_data = data.model_dump_json(by_alias=True, exclude_none=True)
            data = non_encoded_data.encode('utf-8')

        elif isinstance(data, dict):
            data = json.dumps(data)

        if isinstance(params, BaseModel):
            params = params.model_dump(by_alias=True, exclude_none=True)

        if files:
            current_session.headers['Content-Type'] = None

        self.write_log_for_monitoring(
            method, uri, headers=current_session.headers, data=non_encoded_data, params=params
        )

        prepared_request = current_session.prepare_request(
            requests.Request(method=method, url=url, headers=current_session.headers, data=data, params=params,
                             files=files)
        )
        if need_allure_log:
            attach_request(prepared_request)

        response = current_session.send(request=prepared_request, verify=verify, timeout=timeout or self.timeout)

        if need_allure_log:
            attach_response(response)

        if need_log and not files:
            logger.info(f'{method} {url} REQUEST CURL IS LIKE: %s\n\n', curlify.to_curl(response.request))
            logger.info(f'STATUS CODE FOR {method} {url} IS LIKE: %s\n\n', response.status_code)
            logger.info(f'RESPONSE CONTENT FOR {method} {url} IS LIKE: %s\n\n', response.json())

        if need_log and files:
            logger.info(f'CAN NOT CREATE CURL OF {method} {url} CAUSE OF files arg\n\n')
            logger.info(f'STATUS CODE FOR {method} {url} IS LIKE: %s\n\n', response.status_code)
            logger.info(f'RESPONSE CONTENT FOR {method} {url} IS LIKE: %s\n\n', response.json())

        if check_status:
            if response.status_code != check_status:
                raise requests.HTTPError(f'There must be status code {check_status}, but was {response.status_code}!')

        if to_json:
            response = response.json()

        return response