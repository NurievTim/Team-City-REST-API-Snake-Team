from src.main.configs.config import Config


class RequestSpecs:
    @staticmethod
    def _base_url() -> str:
        return f"{Config.get('server')}{Config.get('apiVersion')}"

    @staticmethod
    def default_req_headers() -> dict[str, str]:
        return {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

    @staticmethod
    def unauth_spec() -> dict[str, str]:
        return RequestSpecs.default_req_headers()

    @staticmethod
    def admin_auth_spec() -> dict[str, str]:
        headers = RequestSpecs.default_req_headers()
        headers["Authorization"] = Config.get("TC_ADMIN_TOKEN")
        return headers
