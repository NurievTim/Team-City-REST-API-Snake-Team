import allure
import requests

from framework.clients.base_http_api_client import BaseHttpApiClient


class TeamCityApiClient(BaseHttpApiClient):
    """Class with TeamCityApiClient api client logic"""

    def __init__(self, tc_url: str, **kwargs):
        super().__init__(tc_url)

    @allure.step('GET /app/rest/projects')
    def get_projects(self, headers: dict, **kwargs) -> requests.Response | dict:
        """Method /app/rest/projects"""
        uri = '/app/rest/projects'
        return self.request('get', uri, headers=headers, **kwargs)

    @allure.step('GET /app/rest/server')
    def get_server_info(self, headers: dict, **kwargs) -> requests.Response | dict:
        """Method /app/rest/server"""
        uri = '/app/rest/server'
        return self.request('get', uri, headers=headers, **kwargs)

    @allure.step('GET /app/rest/users/current')
    def get_current_user(self, headers: dict, **kwargs) -> requests.Response | dict:
        """Method /app/rest/users/current"""
        uri = '/app/rest/users/current'
        return self.request('get', uri, headers=headers, **kwargs)

    @allure.step('GET /app/rest/agents')
    def get_agents(self, headers: dict, **kwargs) -> requests.Response | dict:
        """Method /app/rest/agents"""
        uri = '/app/rest/agents'
        return self.request('get', uri, headers=headers, **kwargs)

    @allure.step('POST /app/rest/buildQueue')
    def add_build_to_queue(self, headers: dict, data: dict | None = None, **kwargs) -> requests.Response | dict:
        """Method /app/rest/buildQueue"""
        uri = '/app/rest/buildQueue'
        return self.request('post', uri, headers=headers, data=data, **kwargs)

    @allure.step('POST /app/rest/buildQueue/{queuedBuildLocator}')
    def cancel_queued_build(self, queued_build_locator: str, headers: dict, data: dict | None = None, **kwargs) -> requests.Response | dict:
        """Method /app/rest/buildQueue/{queuedBuildLocator}"""
        uri = f'/app/rest/buildQueue/{queued_build_locator}'
        return self.request('post', uri, headers=headers, data=data, **kwargs)

    @allure.step('POST /app/rest/builds/{buildLocator}')
    def cancel_running_build(self, build_locator: str, headers: dict, data: dict | None = None, **kwargs) -> requests.Response | dict:
        """Method /app/rest/builds/{buildLocator}"""
        uri = f'/app/rest/builds/{build_locator}'
        return self.request('post', uri, headers=headers, data=data, **kwargs)

    @allure.step('GET /app/rest/builds/{buildLocator}')
    def get_build(self, build_locator: str, headers: dict, **kwargs) -> requests.Response | dict:
        """Method /app/rest/builds/{buildLocator}"""
        uri = f'/app/rest/builds/{build_locator}'
        return self.request('get', uri, headers=headers, **kwargs)

    @allure.step('GET /app/rest/builds')
    def get_builds(self, headers: dict, **kwargs) -> requests.Response | dict:
        """Method /app/rest/builds"""
        uri = '/app/rest/builds'
        return self.request('get', uri, headers=headers, **kwargs)

    @allure.step('GET /app/rest/builds/{buildLocator}/resulting-properties')
    def get_build_resulting_properties(self, build_locator: str, headers: dict, **kwargs) -> requests.Response | dict:
        """Method /app/rest/builds/{buildLocator}/resulting-properties"""
        uri = f'/app/rest/builds/{build_locator}/resulting-properties'
        return self.request('get', uri, headers=headers, **kwargs)

    @allure.step('GET /app/rest/builds/{buildLocator}/artifacts/files/{path}')
    def download_build_artifact(self, build_locator: str, path: str, headers: dict, **kwargs) -> requests.Response | dict:
        """Method /app/rest/builds/{buildLocator}/artifacts/files/{path}"""
        uri = f'/app/rest/builds/{build_locator}/artifacts/files/{path}'
        return self.request('get', uri, headers=headers, **kwargs)

    @allure.step('GET /app/rest/builds/{buildLocator}/statistics')
    def get_build_statistics(self, build_locator: str, headers: dict, **kwargs) -> requests.Response | dict:
        """Method /app/rest/builds/{buildLocator}/statistics"""
        uri = f'/app/rest/builds/{build_locator}/statistics'
        return self.request('get', uri, headers=headers, **kwargs)

    @allure.step('GET /app/rest/changes')
    def get_changes(self, headers: dict, **kwargs) -> requests.Response | dict:
        """Method /app/rest/changes"""
        uri = '/app/rest/changes'
        return self.request('get', uri, headers=headers, **kwargs)

    @allure.step('POST /app/rest/projects')
    def add_project(self, headers: dict, data: dict, **kwargs) -> requests.Response | dict:
        """Method /app/rest/projects"""
        uri = '/app/rest/projects'
        return self.request('post', uri, headers=headers, data=data, **kwargs)

    @allure.step('GET /app/rest/projects/{projectLocator}')
    def get_project(self, project_locator: str, headers: dict, **kwargs) -> requests.Response | dict:
        """Method /app/rest/projects/{projectLocator}"""
        uri = f'/app/rest/projects/{project_locator}'
        return self.request('get', uri, headers=headers, **kwargs)

    @allure.step('DELETE /app/rest/projects/{projectLocator}')
    def delete_project(self, project_locator: str, headers: dict, **kwargs) -> requests.Response | dict:
        """Method /app/rest/projects/{projectLocator}"""
        uri = f'/app/rest/projects/{project_locator}'
        return self.request('delete', uri, headers=headers, check_status=None, **kwargs)

    @allure.step('PUT /app/rest/projects/{projectLocator}/archived')
    def set_project_archived(self, project_locator: str, headers: dict, data: str | dict, **kwargs) -> requests.Response | dict:
        """Method /app/rest/projects/{projectLocator}/archived"""
        uri = f'/app/rest/projects/{project_locator}/archived'
        return self.request('put', uri, headers=headers, data=data, **kwargs)

    @allure.step('POST /app/rest/buildTypes')
    def add_build_type(self, headers: dict, data: dict, **kwargs) -> requests.Response | dict:
        """Method /app/rest/buildTypes"""
        uri = '/app/rest/buildTypes'
        return self.request('post', uri, headers=headers, data=data, **kwargs)

    @allure.step('GET /app/rest/buildTypes')
    def get_build_types(self, headers: dict, **kwargs) -> requests.Response | dict:
        """Method /app/rest/buildTypes"""
        uri = '/app/rest/buildTypes'
        return self.request('get', uri, headers=headers, **kwargs)

    @allure.step('GET /app/rest/buildTypes/{buildTypeLocator}/triggers')
    def get_build_type_triggers(self, build_type_locator: str, headers: dict, **kwargs) -> requests.Response | dict:
        """Method /app/rest/buildTypes/{buildTypeLocator}/triggers"""
        uri = f'/app/rest/buildTypes/{build_type_locator}/triggers'
        return self.request('get', uri, headers=headers, **kwargs)

    @allure.step('PUT /app/rest/buildTypes/{buildTypeLocator}/paused')
    def set_build_type_paused(self, build_type_locator: str, headers: dict, data: str | dict, **kwargs) -> requests.Response | dict:
        """Method /app/rest/buildTypes/{buildTypeLocator}/paused"""
        uri = f'/app/rest/buildTypes/{build_type_locator}/paused'
        return self.request('put', uri, headers=headers, data=data, **kwargs)

    @allure.step('PUT /app/rest/buildTypes/{buildTypeLocator}/parameters/{name}')
    def set_build_type_parameter(self, build_type_locator: str, name: str, headers: dict, data: str | dict, **kwargs) -> requests.Response | dict:
        """Method /app/rest/buildTypes/{buildTypeLocator}/parameters/{name}"""
        uri = f'/app/rest/buildTypes/{build_type_locator}/parameters/{name}'
        return self.request('put', uri, headers=headers, data=data, **kwargs)

    @allure.step('GET /app/rest/buildTypes/{buildTypeLocator}/parameters/{name}')
    def get_build_type_parameter(self, build_type_locator: str, name: str, headers: dict, **kwargs) -> requests.Response | dict:
        """Method /app/rest/buildTypes/{buildTypeLocator}/parameters/{name}"""
        uri = f'/app/rest/buildTypes/{build_type_locator}/parameters/{name}'
        return self.request('get', uri, headers=headers, **kwargs)

    @allure.step('POST /app/rest/buildTypes/{buildTypeLocator}/move')
    def move_build_type(self, build_type_locator: str, headers: dict, **kwargs) -> requests.Response | dict:
        """Method /app/rest/buildTypes/{buildTypeLocator}/move"""
        uri = f'/app/rest/buildTypes/{build_type_locator}/move'
        return self.request('post', uri, headers=headers, **kwargs)

    @allure.step('POST /app/rest/projects/{projectLocator}/buildTypes')
    def copy_build_type_to_project(self, project_locator: str, headers: dict, data: dict, **kwargs) -> requests.Response | dict:
        """Method /app/rest/projects/{projectLocator}/buildTypes"""
        uri = f'/app/rest/projects/{project_locator}/buildTypes'
        return self.request('post', uri, headers=headers, data=data, **kwargs)

    @allure.step('POST /app/rest/vcs-roots')
    def add_vcs_root(self, headers: dict, data: dict, **kwargs) -> requests.Response | dict:
        """Method /app/rest/vcs-roots"""
        uri = '/app/rest/vcs-roots'
        return self.request('post', uri, headers=headers, data=data, **kwargs)

    @allure.step('DELETE /app/rest/vcs-roots/{vcsRootLocator}')
    def delete_vcs_root(self, vcs_root_locator: str, headers: dict, **kwargs) -> requests.Response | dict:
        """Method /app/rest/vcs-roots/{vcsRootLocator}"""
        uri = f'/app/rest/vcs-roots/{vcs_root_locator}'
        return self.request('delete', uri, headers=headers, check_status=None, **kwargs)

    @allure.step('GET /app/rest/vcs-root-instances')
    def get_vcs_root_instances(self, headers: dict, **kwargs) -> requests.Response | dict:
        """Method /app/rest/vcs-root-instances"""
        uri = '/app/rest/vcs-root-instances'
        return self.request('get', uri, headers=headers, **kwargs)

    @allure.step('POST /app/rest/agentPools')
    def add_agent_pool(self, headers: dict, data: dict, **kwargs) -> requests.Response | dict:
        """Method /app/rest/agentPools"""
        uri = '/app/rest/agentPools'
        return self.request('post', uri, headers=headers, data=data, **kwargs)

    @allure.step('DELETE /app/rest/agentPools/{agentPoolLocator}')
    def delete_agent_pool(self, agent_pool_locator: str, headers: dict, **kwargs) -> requests.Response | dict:
        """Method /app/rest/agentPools/{agentPoolLocator}"""
        uri = f'/app/rest/agentPools/{agent_pool_locator}'
        return self.request('delete', uri, headers=headers, check_status=None, **kwargs)

    @allure.step('GET /app/rest/agentPools/{agentPoolLocator}/agents')
    def get_agent_pool_agents(self, agent_pool_locator: str, headers: dict, **kwargs) -> requests.Response | dict:
        """Method /app/rest/agentPools/{agentPoolLocator}/agents"""
        uri = f'/app/rest/agentPools/{agent_pool_locator}/agents'
        return self.request('get', uri, headers=headers, **kwargs)

    @allure.step('PUT /app/rest/agents/{agentLocator}/enabledInfo')
    def set_agent_enabled_info(self, agent_locator: str, headers: dict, data: dict, **kwargs) -> requests.Response | dict:
        """Method /app/rest/agents/{agentLocator}/enabledInfo"""
        uri = f'/app/rest/agents/{agent_locator}/enabledInfo'
        return self.request('put', uri, headers=headers, data=data, **kwargs)

    @allure.step('PUT /app/rest/agents/{agentLocator}/authorizedInfo')
    def set_agent_authorized_info(self, agent_locator: str, headers: dict, data: dict, **kwargs) -> requests.Response | dict:
        """Method /app/rest/agents/{agentLocator}/authorizedInfo"""
        uri = f'/app/rest/agents/{agent_locator}/authorizedInfo'
        return self.request('put', uri, headers=headers, data=data, **kwargs)

    @allure.step('POST /app/rest/users')
    def add_user(self, headers: dict, data: dict, **kwargs) -> requests.Response | dict:
        """Method /app/rest/users"""
        uri = '/app/rest/users'
        return self.request('post', uri, headers=headers, data=data, **kwargs)

    @allure.step('DELETE /app/rest/users/{userLocator}')
    def delete_user(self, user_locator: str, headers: dict, **kwargs) -> requests.Response | dict:
        """Method /app/rest/users/{userLocator}"""
        uri = f'/app/rest/users/{user_locator}'
        return self.request('delete', uri, headers=headers, check_status=None, **kwargs)

    @allure.step('PUT /app/rest/users/{userLocator}/roles/{roleId}/{scope}')
    def add_role_to_user(self, user_locator: str, role_id: str, scope: str, headers: dict, **kwargs) -> requests.Response | dict:
        """Method /app/rest/users/{userLocator}/roles/{roleId}/{scope}"""
        uri = f'/app/rest/users/{user_locator}/roles/{role_id}/{scope}'
        return self.request('put', uri, headers=headers, **kwargs)

    @allure.step('POST /app/rest/users/{userLocator}/tokens/{name}')
    def add_user_token(self, user_locator: str, name: str, headers: dict, **kwargs) -> requests.Response | dict:
        """Method /app/rest/users/{userLocator}/tokens/{name}"""
        uri = f'/app/rest/users/{user_locator}/tokens/{name}'
        return self.request('post', uri, headers=headers, **kwargs)

    @allure.step('DELETE /app/rest/users/{userLocator}/tokens/{name}')
    def delete_user_token(self, user_locator: str, name: str, headers: dict, **kwargs) -> requests.Response | dict:
        """Method /app/rest/users/{userLocator}/tokens/{name}"""
        uri = f'/app/rest/users/{user_locator}/tokens/{name}'
        return self.request('delete', uri, headers=headers, check_status=None, **kwargs)

    @allure.step('GET /app/rest/userGroups')
    def get_user_groups(self, headers: dict, **kwargs) -> requests.Response | dict:
        """Method /app/rest/userGroups"""
        uri = '/app/rest/userGroups'
        return self.request('get', uri, headers=headers, **kwargs)

    @allure.step('GET /app/rest/investigations')
    def get_investigations(self, headers: dict, **kwargs) -> requests.Response | dict:
        """Method /app/rest/investigations"""
        uri = '/app/rest/investigations'
        return self.request('get', uri, headers=headers, **kwargs)

    @allure.step('POST /app/rest/mutes')
    def add_mute(self, headers: dict, data: dict, **kwargs) -> requests.Response | dict:
        """Method /app/rest/mutes"""
        uri = '/app/rest/mutes'
        return self.request('post', uri, headers=headers, data=data, **kwargs)

    @allure.step('GET /app/rest/testOccurrences')
    def get_test_occurrences(self, headers: dict, **kwargs) -> requests.Response | dict:
        """Method /app/rest/testOccurrences"""
        uri = '/app/rest/testOccurrences'
        return self.request('get', uri, headers=headers, **kwargs)

    @allure.step('GET /app/rest/problemOccurrences')
    def get_problem_occurrences(self, headers: dict, **kwargs) -> requests.Response | dict:
        """Method /app/rest/problemOccurrences"""
        uri = '/app/rest/problemOccurrences'
        return self.request('get', uri, headers=headers, **kwargs)

    @allure.step('POST /app/rest/builds/{buildLocator}/tags')
    def add_build_tag(self, build_locator: str, headers: dict, data: dict | None = None, **kwargs) -> requests.Response | dict:
        """Method /app/rest/builds/{buildLocator}/tags"""
        uri = f'/app/rest/builds/{build_locator}/tags'
        return self.request('post', uri, headers=headers, data=data, **kwargs)

    @allure.step('GET /app/rest/$help')
    def get_rest_help(self, headers: dict, **kwargs) -> requests.Response | dict:
        """Method /app/rest/$help"""
        uri = '/app/rest/$help'
        return self.request('get', uri, headers=headers, **kwargs)