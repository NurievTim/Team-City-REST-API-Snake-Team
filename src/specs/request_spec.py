import os
from src.configs.config import Config


class RequestSpecs:
    @staticmethod
    def default_req_headers():
        return {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }

    @staticmethod
    def unauth_spec():
        return {
            'headers': RequestSpecs.default_req_headers(),
            'base_url': Config.get('baseurl')
        }

    @staticmethod
    def admin_base_headers():
        headers = RequestSpecs.default_req_headers()
        headers['Authorization'] = f'Bearer {os.getenv("TC_ADMIN_TOKEN")}'
        return {
            'headers': headers,
            'base_url': Config.get('baseurl')
        }

