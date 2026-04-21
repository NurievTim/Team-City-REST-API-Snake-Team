# TeamCity REST API — HandlerInfo registry
# Auto-generated from swagger.json (TeamCity 2025.11)

from __future__ import annotations
from dataclasses import dataclass

from framework.data.models import team_city_api_models as tc_models


@dataclass
class HandlerInfo:
    method: str
    path: str
    success_response_model: type | None
    request_model: type | None = None
    query_params: dict[str, bool] | None = None  # param_name -> required
    path_params: list[str] | None = None
    operation_id: str = ""


# ══════════ AGENT ═════════════════════════════════════════════

# Get all known agents.
get_all_agents = HandlerInfo(
    method='GET',
    path='/app/rest/agents',
    success_response_model=tc_models.Agents,
    query_params={'locator': False, 'fields': False},
    operation_id='getAllAgents',
)

# Get agent matching the locator.
get_agent = HandlerInfo(
    method='GET',
    path='/app/rest/agents/{agentLocator}',
    success_response_model=tc_models.Agent,
    query_params={'fields': False},
    path_params=['agentLocator'],
    operation_id='getAgent',
)

# Delete an inactive agent.
delete_agent = HandlerInfo(
    method='DELETE',
    path='/app/rest/agents/{agentLocator}',
    success_response_model=None,
    path_params=['agentLocator'],
    operation_id='deleteAgent',
)

# Get the authorization info of the matching agent.
get_authorized_info = HandlerInfo(
    method='GET',
    path='/app/rest/agents/{agentLocator}/authorizedInfo',
    success_response_model=tc_models.AuthorizedInfo,
    query_params={'fields': False},
    path_params=['agentLocator'],
    operation_id='getAuthorizedInfo',
)

# Update the authorization info of the matching agent.
set_authorized_info = HandlerInfo(
    method='PUT',
    path='/app/rest/agents/{agentLocator}/authorizedInfo',
    success_response_model=tc_models.AuthorizedInfo,
    request_model=tc_models.AuthorizedInfo,
    query_params={'fields': False},
    path_params=['agentLocator'],
    operation_id='setAuthorizedInfo',
)

# Get the build configuration run policy of the matching agent.
get_build_configuration_run_policy = HandlerInfo(
    method='GET',
    path='/app/rest/agents/{agentLocator}/compatibilityPolicy',
    success_response_model=tc_models.CompatibilityPolicy,
    query_params={'fields': False},
    path_params=['agentLocator'],
    operation_id='getBuildConfigurationRunPolicy',
)

# Update build configuration run policy of agent matching locator.
set_build_configuration_run_policy = HandlerInfo(
    method='PUT',
    path='/app/rest/agents/{agentLocator}/compatibilityPolicy',
    success_response_model=tc_models.CompatibilityPolicy,
    request_model=tc_models.CompatibilityPolicy,
    query_params={'fields': False},
    path_params=['agentLocator'],
    operation_id='setBuildConfigurationRunPolicy',
)

# Get build types compatible with the matching agent.
get_compatible_build_types = HandlerInfo(
    method='GET',
    path='/app/rest/agents/{agentLocator}/compatibleBuildTypes',
    success_response_model=tc_models.BuildTypes,
    query_params={'fields': False},
    path_params=['agentLocator'],
    operation_id='getCompatibleBuildTypes',
)

# Check if the matching agent is enabled.
get_enabled_info = HandlerInfo(
    method='GET',
    path='/app/rest/agents/{agentLocator}/enabledInfo',
    success_response_model=tc_models.EnabledInfo,
    query_params={'fields': False},
    path_params=['agentLocator'],
    operation_id='getEnabledInfo',
)

# Update the enablement status of the matching agent.
set_enabled_info = HandlerInfo(
    method='PUT',
    path='/app/rest/agents/{agentLocator}/enabledInfo',
    success_response_model=tc_models.EnabledInfo,
    request_model=tc_models.EnabledInfo,
    query_params={'fields': False},
    path_params=['agentLocator'],
    operation_id='setEnabledInfo',
)

# Get build types incompatible with the matching agent.
get_incompatible_build_types = HandlerInfo(
    method='GET',
    path='/app/rest/agents/{agentLocator}/incompatibleBuildTypes',
    success_response_model=tc_models.Compatibilities,
    query_params={'fields': False},
    path_params=['agentLocator'],
    operation_id='getIncompatibleBuildTypes',
)

# Get the agent pool of the matching agent.
get_agent_pool = HandlerInfo(
    method='GET',
    path='/app/rest/agents/{agentLocator}/pool',
    success_response_model=tc_models.AgentPool,
    query_params={'fields': False},
    path_params=['agentLocator'],
    operation_id='getAgentPool',
)

# Assign the matching agent to the specified agent pool.
set_agent_pool = HandlerInfo(
    method='PUT',
    path='/app/rest/agents/{agentLocator}/pool',
    success_response_model=tc_models.AgentPool,
    request_model=tc_models.AgentPool,
    query_params={'fields': False},
    path_params=['agentLocator'],
    operation_id='setAgentPool',
)

# Get a field of the matching agent.
get_agent_field = HandlerInfo(
    method='GET',
    path='/app/rest/agents/{agentLocator}/{field}',
    success_response_model=str,
    path_params=['agentLocator', 'field'],
    operation_id='getAgentField',
)

# Update a field of the matching agent.
set_agent_field = HandlerInfo(
    method='PUT',
    path='/app/rest/agents/{agentLocator}/{field}',
    success_response_model=str,
    request_model=str,
    path_params=['agentLocator', 'field'],
    operation_id='setAgentField',
)


# ══════════ AGENTPOOL ═════════════════════════════════════════

# Get all agent pools.
get_all_agent_pools = HandlerInfo(
    method='GET',
    path='/app/rest/agentPools',
    success_response_model=tc_models.AgentPools,
    query_params={'locator': False, 'fields': False},
    operation_id='getAllAgentPools',
)

# Create a new agent pool.
create_agent_pool = HandlerInfo(
    method='POST',
    path='/app/rest/agentPools',
    success_response_model=tc_models.AgentPool,
    request_model=tc_models.AgentPool,
    operation_id='createAgentPool',
)

# Get the agent pool matching the locator.
get_agent_pool_of_agent_pool = HandlerInfo(
    method='GET',
    path='/app/rest/agentPools/{agentPoolLocator}',
    success_response_model=tc_models.AgentPool,
    query_params={'fields': False},
    path_params=['agentPoolLocator'],
    operation_id='getAgentPoolOfAgentPool',
)

# Delete the agent pool matching the locator.
delete_agent_pool = HandlerInfo(
    method='DELETE',
    path='/app/rest/agentPools/{agentPoolLocator}',
    success_response_model=None,
    path_params=['agentPoolLocator'],
    operation_id='deleteAgentPool',
)

# Get the agent of the matching agent pool.
get_all_agents_from_agent_pool = HandlerInfo(
    method='GET',
    path='/app/rest/agentPools/{agentPoolLocator}/agents',
    success_response_model=tc_models.Agents,
    query_params={'locator': False, 'fields': False},
    path_params=['agentPoolLocator'],
    operation_id='getAllAgentsFromAgentPool',
)

# Assign the agent to the matching agent pool.
add_agent_to_agent_pool = HandlerInfo(
    method='POST',
    path='/app/rest/agentPools/{agentPoolLocator}/agents',
    success_response_model=tc_models.Agent,
    request_model=tc_models.Agent,
    query_params={'fields': False},
    path_params=['agentPoolLocator'],
    operation_id='addAgentToAgentPool',
)

# Generates one-time tokens that can be used by agents to be automatically authorized in the specified agent pool upon registration.
generate_automatic_agent_authorization_tokens = HandlerInfo(
    method='POST',
    path='/app/rest/agentPools/{agentPoolLocator}/authorizationTokens',
    success_response_model=tc_models.Items,
    request_model=tc_models.AuthorizationTokensRequirements,
    path_params=['agentPoolLocator'],
    operation_id='generateAutomaticAgentAuthorizationTokens',
)

# Get all projects of the matching agent pool.
get_all_projects_from_agent_pool = HandlerInfo(
    method='GET',
    path='/app/rest/agentPools/{agentPoolLocator}/projects',
    success_response_model=tc_models.Projects,
    query_params={'fields': False},
    path_params=['agentPoolLocator'],
    operation_id='getAllProjectsFromAgentPool',
)

# Assign the project to the matching agent pool.
add_project_to_agent_pool = HandlerInfo(
    method='POST',
    path='/app/rest/agentPools/{agentPoolLocator}/projects',
    success_response_model=tc_models.Project,
    request_model=tc_models.Project,
    path_params=['agentPoolLocator'],
    operation_id='addProjectToAgentPool',
)

# Update projects of the matching agent pool.
set_agent_pool_projects = HandlerInfo(
    method='PUT',
    path='/app/rest/agentPools/{agentPoolLocator}/projects',
    success_response_model=tc_models.Projects,
    request_model=tc_models.Projects,
    path_params=['agentPoolLocator'],
    operation_id='setAgentPoolProjects',
)

# Unassign all projects from the matching agent pool.
delete_all_projects_from_agent_pool = HandlerInfo(
    method='DELETE',
    path='/app/rest/agentPools/{agentPoolLocator}/projects',
    success_response_model=None,
    path_params=['agentPoolLocator'],
    operation_id='deleteAllProjectsFromAgentPool',
)

# Unassign the project from the matching agent pool.
delete_project_from_agent_pool = HandlerInfo(
    method='DELETE',
    path='/app/rest/agentPools/{agentPoolLocator}/projects/{projectLocator}',
    success_response_model=None,
    path_params=['agentPoolLocator', 'projectLocator'],
    operation_id='deleteProjectFromAgentPool',
)

# Get a field of the matching agent pool.
get_field_from_agent_pool = HandlerInfo(
    method='GET',
    path='/app/rest/agentPools/{agentPoolLocator}/{field}',
    success_response_model=str,
    path_params=['agentPoolLocator', 'field'],
    operation_id='getFieldFromAgentPool',
)

# Update a field of the matching agent pool.
set_agent_pool_field = HandlerInfo(
    method='PUT',
    path='/app/rest/agentPools/{agentPoolLocator}/{field}',
    success_response_model=str,
    request_model=str,
    path_params=['agentPoolLocator', 'field'],
    operation_id='setAgentPoolField',
)


# ══════════ AGENTTYPE ═════════════════════════════════════════

# Get agent type matching the locator.
get_agent_type = HandlerInfo(
    method='GET',
    path='/app/rest/agentTypes/{agentTypeLocator}',
    success_response_model=tc_models.AgentType,
    query_params={'fields': False},
    path_params=['agentTypeLocator'],
    operation_id='getAgentType',
)


# ══════════ AUDIT ═════════════════════════════════════════════

# Get all audit events.
get_all_audit_events = HandlerInfo(
    method='GET',
    path='/app/rest/audit',
    success_response_model=tc_models.AuditEvents,
    query_params={'locator': False, 'fields': False},
    operation_id='getAllAuditEvents',
)

# Get audit event matching the locator.
get_audit_event = HandlerInfo(
    method='GET',
    path='/app/rest/audit/{auditEventLocator}',
    success_response_model=tc_models.AuditEvent,
    query_params={'fields': False},
    path_params=['auditEventLocator'],
    operation_id='getAuditEvent',
)


# ══════════ AVATAR ════════════════════════════════════════════

# Update a users avatar
put_avatar = HandlerInfo(
    method='PUT',
    path='/app/rest/avatars/{userLocator}',
    success_response_model=None,
    path_params=['userLocator'],
    operation_id='putAvatar',
)

# Delete a users avatar
delete_avatar = HandlerInfo(
    method='DELETE',
    path='/app/rest/avatars/{userLocator}',
    success_response_model=None,
    path_params=['userLocator'],
    operation_id='deleteAvatar',
)

# Get a users avatar
get_avatar = HandlerInfo(
    method='GET',
    path='/app/rest/avatars/{userLocator}/{size}/avatar.png',
    success_response_model=None,
    path_params=['userLocator', 'size'],
    operation_id='getAvatar',
)

# Get a users avatar
get_avatar_with_hash = HandlerInfo(
    method='GET',
    path='/app/rest/avatars/{userLocator}/{size}/avatar.{hash}.png',
    success_response_model=None,
    path_params=['userLocator', 'size', 'hash'],
    operation_id='getAvatarWithHash',
)


# ══════════ BUILD ═════════════════════════════════════════════

# Get all builds.
get_all_builds = HandlerInfo(
    method='GET',
    path='/app/rest/builds',
    success_response_model=tc_models.Builds,
    query_params={'locator': False, 'fields': False},
    operation_id='getAllBuilds',
)

# Get the build status of aggregated matching builds.
get_aggregated_build_status = HandlerInfo(
    method='GET',
    path='/app/rest/builds/aggregated/{buildLocator}/status',
    success_response_model=str,
    path_params=['buildLocator'],
    operation_id='getAggregatedBuildStatus',
)

# Get the status icon (in specified format) of aggregated matching builds.
get_aggregated_build_status_icon = HandlerInfo(
    method='GET',
    path='/app/rest/builds/aggregated/{buildLocator}/statusIcon{suffix}',
    success_response_model=None,
    path_params=['buildLocator', 'suffix'],
    operation_id='getAggregatedBuildStatusIcon',
)

# Get multiple builds matching the locator.
get_multiple_builds = HandlerInfo(
    method='GET',
    path='/app/rest/builds/multiple/{buildLocator}',
    success_response_model=tc_models.Builds,
    query_params={'fields': False},
    path_params=['buildLocator'],
    operation_id='getMultipleBuilds',
)

# cancelMultipleBuilds
cancel_multiple = HandlerInfo(
    method='POST',
    path='/app/rest/builds/multiple/{buildLocator}',
    success_response_model=tc_models.MultipleOperationResult,
    request_model=tc_models.BuildCancelRequest,
    query_params={'fields': False},
    path_params=['buildLocator'],
    operation_id='cancelMultiple',
)

# Delete multiple builds matching the locator.
delete_multiple_builds = HandlerInfo(
    method='DELETE',
    path='/app/rest/builds/multiple/{buildLocator}',
    success_response_model=tc_models.MultipleOperationResult,
    query_params={'fields': False},
    path_params=['buildLocator'],
    operation_id='deleteMultipleBuilds',
)

# Update comments in multiple matching builds.
set_multiple_build_comments = HandlerInfo(
    method='PUT',
    path='/app/rest/builds/multiple/{buildLocator}/comment',
    success_response_model=tc_models.MultipleOperationResult,
    request_model=str,
    query_params={'fields': False},
    path_params=['buildLocator'],
    operation_id='setMultipleBuildComments',
)

# Delete comments of multiple matching builds.
delete_multiple_build_comments = HandlerInfo(
    method='DELETE',
    path='/app/rest/builds/multiple/{buildLocator}/comment',
    success_response_model=tc_models.MultipleOperationResult,
    query_params={'fields': False},
    path_params=['buildLocator'],
    operation_id='deleteMultipleBuildComments',
)

# Pin multiple matching builds.
pin_multiple_builds = HandlerInfo(
    method='PUT',
    path='/app/rest/builds/multiple/{buildLocator}/pinInfo',
    success_response_model=tc_models.MultipleOperationResult,
    request_model=tc_models.PinInfo,
    query_params={'fields': False},
    path_params=['buildLocator'],
    operation_id='pinMultipleBuilds',
)

# Add tags to multiple matching builds.
add_tags_to_multiple_builds = HandlerInfo(
    method='POST',
    path='/app/rest/builds/multiple/{buildLocator}/tags',
    success_response_model=tc_models.MultipleOperationResult,
    request_model=tc_models.Tags,
    query_params={'fields': False},
    path_params=['buildLocator'],
    operation_id='addTagsToMultipleBuilds',
)

# Remove tags from multiple matching builds.
remove_multiple_build_tags = HandlerInfo(
    method='DELETE',
    path='/app/rest/builds/multiple/{buildLocator}/tags',
    success_response_model=tc_models.MultipleOperationResult,
    request_model=tc_models.Tags,
    query_params={'fields': False},
    path_params=['buildLocator'],
    operation_id='removeMultipleBuildTags',
)

# Get build matching the locator.
get_build = HandlerInfo(
    method='GET',
    path='/app/rest/builds/{buildLocator}',
    success_response_model=tc_models.Build,
    query_params={'fields': False},
    path_params=['buildLocator'],
    operation_id='getBuild',
)

# cancelBuild
cancel_build = HandlerInfo(
    method='POST',
    path='/app/rest/builds/{buildLocator}',
    success_response_model=tc_models.Build,
    request_model=tc_models.BuildCancelRequest,
    query_params={'fields': False},
    path_params=['buildLocator'],
    operation_id='cancelBuild',
)

# Delete build matching the locator.
delete_build = HandlerInfo(
    method='DELETE',
    path='/app/rest/builds/{buildLocator}',
    success_response_model=None,
    path_params=['buildLocator'],
    operation_id='deleteBuild',
)

# Get artifact dependency changes of the matching build.
get_artifact_dependency_changes = HandlerInfo(
    method='GET',
    path='/app/rest/builds/{buildLocator}/artifactDependencyChanges',
    success_response_model=tc_models.BuildChanges,
    query_params={'fields': False},
    path_params=['buildLocator'],
    operation_id='getArtifactDependencyChanges',
)

# List all files.
get_files_list_of_build = HandlerInfo(
    method='GET',
    path='/app/rest/builds/{buildLocator}/artifacts',
    success_response_model=tc_models.Files,
    query_params={'basePath': False, 'locator': False, 'fields': False, 'resolveParameters': False, 'logBuildUsage': False},
    path_params=['buildLocator'],
    operation_id='getFilesListOfBuild',
)

# Get specific file zipped.
get_zipped_file_of_build = HandlerInfo(
    method='GET',
    path='/app/rest/builds/{buildLocator}/artifacts/archived{path}',
    success_response_model=None,
    query_params={'basePath': False, 'locator': False, 'name': False, 'resolveParameters': False, 'logBuildUsage': False},
    path_params=['buildLocator', 'path'],
    operation_id='getZippedFileOfBuild',
)

# Download specific file.
download_file_of_build = HandlerInfo(
    method='GET',
    path='/app/rest/builds/{buildLocator}/artifacts/files{path}',
    success_response_model=None,
    query_params={'resolveParameters': False, 'logBuildUsage': False},
    path_params=['buildLocator', 'path'],
    operation_id='downloadFileOfBuild',
)

# Get metadata of specific file.
get_file_metadata_of_build = HandlerInfo(
    method='GET',
    path='/app/rest/builds/{buildLocator}/artifacts/metadata{path}',
    success_response_model=tc_models.File,
    query_params={'fields': False, 'resolveParameters': False, 'logBuildUsage': False},
    path_params=['buildLocator', 'path'],
    operation_id='getFileMetadataOfBuild',
)

# List files under this path.
get_files_list_for_subpath_of_build = HandlerInfo(
    method='GET',
    path='/app/rest/builds/{buildLocator}/artifacts/{path}',
    success_response_model=tc_models.Files,
    query_params={'basePath': False, 'locator': False, 'fields': False, 'resolveParameters': False, 'logBuildUsage': False},
    path_params=['buildLocator', 'path'],
    operation_id='getFilesListForSubpathOfBuild',
)

# Get the artifacts' directory of the matching build.
get_artifacts_directory = HandlerInfo(
    method='GET',
    path='/app/rest/builds/{buildLocator}/artifactsDirectory',
    success_response_model=str,
    path_params=['buildLocator'],
    operation_id='getArtifactsDirectory',
)

# Remove build parameters from the matching build.
reset_build_finish_properties = HandlerInfo(
    method='DELETE',
    path='/app/rest/builds/{buildLocator}/caches/finishProperties',
    success_response_model=None,
    path_params=['buildLocator'],
    operation_id='resetBuildFinishProperties',
)

# Check if the matching build is canceled.
get_canceled_info = HandlerInfo(
    method='GET',
    path='/app/rest/builds/{buildLocator}/canceledInfo',
    success_response_model=tc_models.Comment,
    query_params={'fields': False},
    path_params=['buildLocator'],
    operation_id='getCanceledInfo',
)

# Update the comment on the matching build.
set_build_comment = HandlerInfo(
    method='PUT',
    path='/app/rest/builds/{buildLocator}/comment',
    success_response_model=None,
    request_model=str,
    path_params=['buildLocator'],
    operation_id='setBuildComment',
)

# Remove the build comment matching the locator.
delete_build_comment = HandlerInfo(
    method='DELETE',
    path='/app/rest/builds/{buildLocator}/comment',
    success_response_model=None,
    path_params=['buildLocator'],
    operation_id='deleteBuildComment',
)

# Marks the running build as finished by passing agent the current time of the build to finish.
set_finished_time = HandlerInfo(
    method='PUT',
    path='/app/rest/builds/{buildLocator}/finish',
    success_response_model=str,
    path_params=['buildLocator'],
    operation_id='setFinishedTime',
)

# Get the finish date of the matching build.
get_build_finish_date = HandlerInfo(
    method='GET',
    path='/app/rest/builds/{buildLocator}/finishDate',
    success_response_model=str,
    path_params=['buildLocator'],
    operation_id='getBuildFinishDate',
)

# Marks the running build as finished by passing agent the current time of the build to finish.
set_build_finish_date = HandlerInfo(
    method='PUT',
    path='/app/rest/builds/{buildLocator}/finishDate',
    success_response_model=str,
    request_model=str,
    path_params=['buildLocator'],
    operation_id='setBuildFinishDate',
)

# Adds a message to the build log. Service messages are accepted.
add_log_message_to_build = HandlerInfo(
    method='POST',
    path='/app/rest/builds/{buildLocator}/log',
    success_response_model=None,
    request_model=str,
    query_params={'fields': False},
    path_params=['buildLocator'],
    operation_id='addLogMessageToBuild',
)

# Get the number of the matching build.
get_build_number = HandlerInfo(
    method='GET',
    path='/app/rest/builds/{buildLocator}/number',
    success_response_model=str,
    path_params=['buildLocator'],
    operation_id='getBuildNumber',
)

# Update the number of the matching build.
set_build_number = HandlerInfo(
    method='PUT',
    path='/app/rest/builds/{buildLocator}/number',
    success_response_model=str,
    request_model=str,
    path_params=['buildLocator'],
    operation_id='setBuildNumber',
)

# Get output parameters published by the build.
get_build_output_parameters_of_build = HandlerInfo(
    method='GET',
    path='/app/rest/builds/{buildLocator}/output-parameters',
    success_response_model=tc_models.Properties,
    query_params={'fields': False},
    path_params=['buildLocator'],
    operation_id='getBuildOutputParametersOfBuild',
)

# Returns the value of a build output parameter.
get_build_output_parameters = HandlerInfo(
    method='GET',
    path='/app/rest/builds/{buildLocator}/output-parameters/{propertyName}',
    success_response_model=str,
    path_params=['buildLocator', 'propertyName'],
    operation_id='getBuildOutputParameters',
)

# Check if the matching build is pinned.
get_build_pin_info = HandlerInfo(
    method='GET',
    path='/app/rest/builds/{buildLocator}/pinInfo',
    success_response_model=tc_models.PinInfo,
    query_params={'fields': False},
    path_params=['buildLocator'],
    operation_id='getBuildPinInfo',
)

# Update the pin info of the matching build.
set_build_pin_info = HandlerInfo(
    method='PUT',
    path='/app/rest/builds/{buildLocator}/pinInfo',
    success_response_model=tc_models.PinInfo,
    request_model=tc_models.PinInfo,
    query_params={'fields': False},
    path_params=['buildLocator'],
    operation_id='setBuildPinInfo',
)

# Get build problems of the matching build.
get_build_problems = HandlerInfo(
    method='GET',
    path='/app/rest/builds/{buildLocator}/problemOccurrences',
    success_response_model=tc_models.ProblemOccurrences,
    query_params={'fields': False},
    path_params=['buildLocator'],
    operation_id='getBuildProblems',
)

# Add a build problem to the matching build.
add_problem_to_build = HandlerInfo(
    method='POST',
    path='/app/rest/builds/{buildLocator}/problemOccurrences',
    success_response_model=tc_models.ProblemOccurrence,
    request_model=str,
    query_params={'fields': False},
    path_params=['buildLocator'],
    operation_id='addProblemToBuild',
)

# Get related issues of the matching build.
get_build_related_issues = HandlerInfo(
    method='GET',
    path='/app/rest/builds/{buildLocator}/relatedIssues',
    success_response_model=tc_models.IssuesUsages,
    query_params={'fields': False},
    path_params=['buildLocator'],
    operation_id='getBuildRelatedIssues',
)

# Get the resolvement status of the matching build.
get_build_resolved = HandlerInfo(
    method='GET',
    path='/app/rest/builds/{buildLocator}/resolved/{value}',
    success_response_model=str,
    path_params=['buildLocator', 'value'],
    operation_id='getBuildResolved',
)

# Get actual build parameters of the matching build.
get_build_actual_parameters = HandlerInfo(
    method='GET',
    path='/app/rest/builds/{buildLocator}/resulting-properties',
    success_response_model=tc_models.Properties,
    query_params={'fields': False},
    path_params=['buildLocator'],
    operation_id='getBuildActualParameters',
)

# Returns the final value that a given parameter had after the build finished.
get_build_resulting_properties = HandlerInfo(
    method='GET',
    path='/app/rest/builds/{buildLocator}/resulting-properties/{propertyName}',
    success_response_model=str,
    path_params=['buildLocator', 'propertyName'],
    operation_id='getBuildResultingProperties',
)

# Starts the queued build as an agent-less build and returns the corresponding running build.
mark_build_as_running = HandlerInfo(
    method='PUT',
    path='/app/rest/builds/{buildLocator}/runningData',
    success_response_model=tc_models.Build,
    request_model=str,
    query_params={'fields': False},
    path_params=['buildLocator'],
    operation_id='markBuildAsRunning',
)

# Get a source file of the matching build.
get_build_source_file = HandlerInfo(
    method='GET',
    path='/app/rest/builds/{buildLocator}/sources/files/{fileName}',
    success_response_model=None,
    path_params=['buildLocator', 'fileName'],
    operation_id='getBuildSourceFile',
)

# Get all statistical values of the matching build.
get_build_statistic_values = HandlerInfo(
    method='GET',
    path='/app/rest/builds/{buildLocator}/statistics',
    success_response_model=tc_models.Properties,
    query_params={'fields': False},
    path_params=['buildLocator'],
    operation_id='getBuildStatisticValues',
)

# Get a statistical value of the matching build.
get_build_statistic_value = HandlerInfo(
    method='GET',
    path='/app/rest/builds/{buildLocator}/statistics/{name}',
    success_response_model=str,
    path_params=['buildLocator', 'name'],
    operation_id='getBuildStatisticValue',
)

# Get status of the matching build.
get_build_status = HandlerInfo(
    method='GET',
    path='/app/rest/builds/{buildLocator}/status',
    success_response_model=str,
    path_params=['buildLocator'],
    operation_id='getBuildStatus',
)

# Change status of the build.
set_build_status = HandlerInfo(
    method='POST',
    path='/app/rest/builds/{buildLocator}/status',
    success_response_model=None,
    request_model=tc_models.BuildStatusUpdate,
    query_params={'fields': False},
    path_params=['buildLocator'],
    operation_id='setBuildStatus',
)

# Get the status icon (in specified format) of the matching build.
get_build_status_icon = HandlerInfo(
    method='GET',
    path='/app/rest/builds/{buildLocator}/statusIcon{suffix}',
    success_response_model=None,
    path_params=['buildLocator', 'suffix'],
    operation_id='getBuildStatusIcon',
)

# Get the build status text of the matching build.
get_build_status_text = HandlerInfo(
    method='GET',
    path='/app/rest/builds/{buildLocator}/statusText',
    success_response_model=str,
    path_params=['buildLocator'],
    operation_id='getBuildStatusText',
)

# Update the build status of the matching build.
set_build_status_text = HandlerInfo(
    method='PUT',
    path='/app/rest/builds/{buildLocator}/statusText',
    success_response_model=str,
    request_model=str,
    path_params=['buildLocator'],
    operation_id='setBuildStatusText',
)

# Get tags of the matching build.
get_build_tags = HandlerInfo(
    method='GET',
    path='/app/rest/builds/{buildLocator}/tags',
    success_response_model=tc_models.Tags,
    query_params={'locator': False, 'fields': False},
    path_params=['buildLocator'],
    operation_id='getBuildTags',
)

# Add tags to the matching build.
add_tags_to_build = HandlerInfo(
    method='POST',
    path='/app/rest/builds/{buildLocator}/tags',
    success_response_model=tc_models.Tags,
    request_model=tc_models.Tags,
    query_params={'fields': False},
    path_params=['buildLocator'],
    operation_id='addTagsToBuild',
)

# Update tags of the matching build.
set_build_tags = HandlerInfo(
    method='PUT',
    path='/app/rest/builds/{buildLocator}/tags',
    success_response_model=tc_models.Tags,
    request_model=tc_models.Tags,
    query_params={'locator': False, 'fields': False},
    path_params=['buildLocator'],
    operation_id='setBuildTags',
)

# Get test occurrences of the matching build.
get_build_test_occurrences = HandlerInfo(
    method='GET',
    path='/app/rest/builds/{buildLocator}/testOccurrences',
    success_response_model=tc_models.TestOccurrences,
    query_params={'fields': False},
    path_params=['buildLocator'],
    operation_id='getBuildTestOccurrences',
)

# Get VCS labels of the matching build.
get_build_vcs_labels = HandlerInfo(
    method='GET',
    path='/app/rest/builds/{buildLocator}/vcsLabels',
    success_response_model=tc_models.VcsLabels,
    query_params={'fields': False},
    path_params=['buildLocator'],
    operation_id='getBuildVcsLabels',
)

# Add a VCS label to the matching build.
add_build_vcs_label = HandlerInfo(
    method='POST',
    path='/app/rest/builds/{buildLocator}/vcsLabels',
    success_response_model=tc_models.VcsLabels,
    request_model=str,
    query_params={'locator': False, 'fields': False},
    path_params=['buildLocator'],
    operation_id='addBuildVcsLabel',
)

# Get a field of the matching build.
get_build_field = HandlerInfo(
    method='GET',
    path='/app/rest/builds/{buildLocator}/{field}',
    success_response_model=str,
    path_params=['buildLocator', 'field'],
    operation_id='getBuildField',
)


# ══════════ BUILDQUEUE ════════════════════════════════════════

# Get all queued builds.
get_all_queued_builds = HandlerInfo(
    method='GET',
    path='/app/rest/buildQueue',
    success_response_model=tc_models.Builds,
    query_params={'locator': False, 'fields': False},
    operation_id='getAllQueuedBuilds',
)

# Add a new build to the queue.
add_build_to_queue = HandlerInfo(
    method='POST',
    path='/app/rest/buildQueue',
    success_response_model=tc_models.Build,
    request_model=tc_models.Build,
    query_params={'moveToTop': False},
    operation_id='addBuildToQueue',
)

# Delete all queued builds.
delete_all_queued_builds = HandlerInfo(
    method='DELETE',
    path='/app/rest/buildQueue',
    success_response_model=None,
    query_params={'locator': False, 'fields': False},
    operation_id='deleteAllQueuedBuilds',
)

# Update the build queue order.
set_queued_builds_order = HandlerInfo(
    method='PUT',
    path='/app/rest/buildQueue/order',
    success_response_model=tc_models.Builds,
    request_model=tc_models.Builds,
    query_params={'fields': False},
    operation_id='setQueuedBuildsOrder',
)

# Get the queue position of a queued matching build.
get_queued_build_position = HandlerInfo(
    method='GET',
    path='/app/rest/buildQueue/order/{queuePosition}',
    success_response_model=tc_models.Build,
    query_params={'fields': False},
    path_params=['queuePosition'],
    operation_id='getQueuedBuildPosition',
)

# Update the queue position of a queued matching build.
set_queued_build_position = HandlerInfo(
    method='PUT',
    path='/app/rest/buildQueue/order/{queuePosition}',
    success_response_model=tc_models.Build,
    request_model=tc_models.Build,
    query_params={'fields': False},
    path_params=['queuePosition'],
    operation_id='setQueuedBuildPosition',
)

# Get approval info of a queued matching build.
get_approval_info = HandlerInfo(
    method='GET',
    path='/app/rest/buildQueue/{buildLocator}/approvalInfo',
    success_response_model=tc_models.ApprovalInfo,
    query_params={'fields': False},
    path_params=['buildLocator'],
    operation_id='getApprovalInfo',
)

# Approve queued build with approval feature enabled.
approve_queued_build = HandlerInfo(
    method='POST',
    path='/app/rest/buildQueue/{buildLocator}/approve',
    success_response_model=tc_models.ApprovalInfo,
    request_model=str,
    query_params={'fields': False, 'approveAll': False},
    path_params=['buildLocator'],
    operation_id='approveQueuedBuild',
)

# Get tags of the queued matching build.
get_queued_build_tags = HandlerInfo(
    method='GET',
    path='/app/rest/buildQueue/{buildLocator}/tags',
    success_response_model=tc_models.Tags,
    query_params={'locator': False, 'fields': False},
    path_params=['buildLocator'],
    operation_id='getQueuedBuildTags',
)

# Add tags to the matching build.
add_tags_to_build_of_build_queue = HandlerInfo(
    method='POST',
    path='/app/rest/buildQueue/{buildLocator}/tags',
    success_response_model=None,
    request_model=tc_models.Tags,
    path_params=['buildLocator'],
    operation_id='addTagsToBuildOfBuildQueue',
)

# Get a queued matching build.
get_queued_build = HandlerInfo(
    method='GET',
    path='/app/rest/buildQueue/{queuedBuildLocator}',
    success_response_model=tc_models.Build,
    query_params={'fields': False},
    path_params=['queuedBuildLocator'],
    operation_id='getQueuedBuild',
)

# Cancel a queued matching build.
cancel_queued_build = HandlerInfo(
    method='POST',
    path='/app/rest/buildQueue/{queuedBuildLocator}',
    success_response_model=tc_models.Build,
    request_model=tc_models.BuildCancelRequest,
    path_params=['queuedBuildLocator'],
    operation_id='cancelQueuedBuild',
)

# Delete a queued matching build.
delete_queued_build = HandlerInfo(
    method='DELETE',
    path='/app/rest/buildQueue/{queuedBuildLocator}',
    success_response_model=None,
    path_params=['queuedBuildLocator'],
    operation_id='deleteQueuedBuild',
)

# Get compatible agents for a queued matching build.
get_compatible_agents_for_build = HandlerInfo(
    method='GET',
    path='/app/rest/buildQueue/{queuedBuildLocator}/compatibleAgents',
    success_response_model=tc_models.Agents,
    query_params={'fields': False},
    path_params=['queuedBuildLocator'],
    operation_id='getCompatibleAgentsForBuild',
)


# ══════════ BUILDTYPE ═════════════════════════════════════════

# Get all build configurations.
get_all_build_types = HandlerInfo(
    method='GET',
    path='/app/rest/buildTypes',
    success_response_model=tc_models.BuildTypes,
    query_params={'locator': False, 'fields': False},
    operation_id='getAllBuildTypes',
)

# Create a new build configuration.
create_build_type = HandlerInfo(
    method='POST',
    path='/app/rest/buildTypes',
    success_response_model=tc_models.BuildType,
    request_model=tc_models.BuildType,
    query_params={'fields': False},
    operation_id='createBuildType',
)

# Get build configuration matching the locator.
get_build_type = HandlerInfo(
    method='GET',
    path='/app/rest/buildTypes/{btLocator}',
    success_response_model=tc_models.BuildType,
    query_params={'fields': False},
    path_params=['btLocator'],
    operation_id='getBuildType',
)

# Delete build configuration matching the locator.
delete_build_type = HandlerInfo(
    method='DELETE',
    path='/app/rest/buildTypes/{btLocator}',
    success_response_model=None,
    path_params=['btLocator'],
    operation_id='deleteBuildType',
)

# Get all agent requirements of the matching build configuration.
get_all_agent_requirements = HandlerInfo(
    method='GET',
    path='/app/rest/buildTypes/{btLocator}/agent-requirements',
    success_response_model=tc_models.AgentRequirements,
    query_params={'fields': False},
    path_params=['btLocator'],
    operation_id='getAllAgentRequirements',
)

# Add an agent requirement to the matching build configuration.
add_agent_requirement_to_build_type = HandlerInfo(
    method='POST',
    path='/app/rest/buildTypes/{btLocator}/agent-requirements',
    success_response_model=tc_models.AgentRequirement,
    request_model=tc_models.AgentRequirement,
    query_params={'fields': False},
    path_params=['btLocator'],
    operation_id='addAgentRequirementToBuildType',
)

# Update all agent requirements of the matching build configuration.
replace_all_agent_requirements = HandlerInfo(
    method='PUT',
    path='/app/rest/buildTypes/{btLocator}/agent-requirements',
    success_response_model=tc_models.AgentRequirements,
    request_model=tc_models.AgentRequirements,
    query_params={'fields': False},
    path_params=['btLocator'],
    operation_id='replaceAllAgentRequirements',
)

# Get an agent requirement of the matching build configuration.
get_agent_requirement = HandlerInfo(
    method='GET',
    path='/app/rest/buildTypes/{btLocator}/agent-requirements/{agentRequirementLocator}',
    success_response_model=tc_models.AgentRequirement,
    query_params={'fields': False},
    path_params=['btLocator', 'agentRequirementLocator'],
    operation_id='getAgentRequirement',
)

# Update an agent requirement of the matching build configuration.
replace_agent_requirement = HandlerInfo(
    method='PUT',
    path='/app/rest/buildTypes/{btLocator}/agent-requirements/{agentRequirementLocator}',
    success_response_model=tc_models.AgentRequirement,
    request_model=tc_models.AgentRequirement,
    query_params={'fields': False},
    path_params=['btLocator', 'agentRequirementLocator'],
    operation_id='replaceAgentRequirement',
)

# Remove an agent requirement of the matching build configuration.
delete_agent_requirement = HandlerInfo(
    method='DELETE',
    path='/app/rest/buildTypes/{btLocator}/agent-requirements/{agentRequirementLocator}',
    success_response_model=None,
    path_params=['btLocator', 'agentRequirementLocator'],
    operation_id='deleteAgentRequirement',
)

# Get a setting of an agent requirement of the matching build configuration.
get_agent_requirement_parameter = HandlerInfo(
    method='GET',
    path='/app/rest/buildTypes/{btLocator}/agent-requirements/{agentRequirementLocator}/{fieldName}',
    success_response_model=str,
    path_params=['btLocator', 'agentRequirementLocator', 'fieldName'],
    operation_id='getAgentRequirementParameter',
)

# Update a parameter of an agent requirement of the matching build configuration.
set_agent_requirement_parameter = HandlerInfo(
    method='PUT',
    path='/app/rest/buildTypes/{btLocator}/agent-requirements/{agentRequirementLocator}/{fieldName}',
    success_response_model=str,
    request_model=str,
    path_params=['btLocator', 'agentRequirementLocator', 'fieldName'],
    operation_id='setAgentRequirementParameter',
)

# Get external IDs of the matching build configuration.
get_aliases = HandlerInfo(
    method='GET',
    path='/app/rest/buildTypes/{btLocator}/aliases',
    success_response_model=tc_models.Items,
    query_params={'field': False},
    path_params=['btLocator'],
    operation_id='getAliases',
)

# Get all artifact dependencies of the matching build configuration.
get_all_artifact_dependencies = HandlerInfo(
    method='GET',
    path='/app/rest/buildTypes/{btLocator}/artifact-dependencies',
    success_response_model=tc_models.ArtifactDependencies,
    query_params={'fields': False},
    path_params=['btLocator'],
    operation_id='getAllArtifactDependencies',
)

# Add an artifact dependency to the matching build configuration.
add_artifact_dependency_to_build_type = HandlerInfo(
    method='POST',
    path='/app/rest/buildTypes/{btLocator}/artifact-dependencies',
    success_response_model=tc_models.ArtifactDependency,
    request_model=tc_models.ArtifactDependency,
    query_params={'fields': False},
    path_params=['btLocator'],
    operation_id='addArtifactDependencyToBuildType',
)

# Update all artifact dependencies of the matching build configuration.
replace_all_artifact_dependencies = HandlerInfo(
    method='PUT',
    path='/app/rest/buildTypes/{btLocator}/artifact-dependencies',
    success_response_model=tc_models.ArtifactDependencies,
    request_model=tc_models.ArtifactDependencies,
    query_params={'fields': False},
    path_params=['btLocator'],
    operation_id='replaceAllArtifactDependencies',
)

# Get an artifact dependency of the matching build configuration.
get_artifact_dependency = HandlerInfo(
    method='GET',
    path='/app/rest/buildTypes/{btLocator}/artifact-dependencies/{artifactDepLocator}',
    success_response_model=tc_models.ArtifactDependency,
    query_params={'fields': False},
    path_params=['btLocator', 'artifactDepLocator'],
    operation_id='getArtifactDependency',
)

# Update an artifact dependency of the matching build configuration.
replace_artifact_dependency = HandlerInfo(
    method='PUT',
    path='/app/rest/buildTypes/{btLocator}/artifact-dependencies/{artifactDepLocator}',
    success_response_model=tc_models.ArtifactDependency,
    request_model=tc_models.ArtifactDependency,
    query_params={'fields': False},
    path_params=['btLocator', 'artifactDepLocator'],
    operation_id='replaceArtifactDependency',
)

# Remove an artifact dependency from the matching build configuration.
delete_artifact_dependency = HandlerInfo(
    method='DELETE',
    path='/app/rest/buildTypes/{btLocator}/artifact-dependencies/{artifactDepLocator}',
    success_response_model=None,
    path_params=['btLocator', 'artifactDepLocator'],
    operation_id='deleteArtifactDependency',
)

# Get a parameter of an artifact dependency of the matching build configuration.
get_artifact_dependency_parameter = HandlerInfo(
    method='GET',
    path='/app/rest/buildTypes/{btLocator}/artifact-dependencies/{artifactDepLocator}/{fieldName}',
    success_response_model=str,
    path_params=['btLocator', 'artifactDepLocator', 'fieldName'],
    operation_id='getArtifactDependencyParameter',
)

# Update a parameter of an artifact dependency of the matching build configuration.
set_artifact_dependency_parameter = HandlerInfo(
    method='PUT',
    path='/app/rest/buildTypes/{btLocator}/artifact-dependencies/{artifactDepLocator}/{fieldName}',
    success_response_model=str,
    request_model=str,
    path_params=['btLocator', 'artifactDepLocator', 'fieldName'],
    operation_id='setArtifactDependencyParameter',
)

# Get all branches of the matching build configuration.
get_all_branches_of_build_type = HandlerInfo(
    method='GET',
    path='/app/rest/buildTypes/{btLocator}/branches',
    success_response_model=tc_models.Branches,
    query_params={'locator': False, 'fields': False},
    path_params=['btLocator'],
    operation_id='getAllBranchesOfBuildType',
)

# Get tags of builds of the matching build configuration.
get_build_type_build_tags = HandlerInfo(
    method='GET',
    path='/app/rest/buildTypes/{btLocator}/buildTags',
    success_response_model=tc_models.Tags,
    query_params={'field': False},
    path_params=['btLocator'],
    operation_id='getBuildTypeBuildTags',
)

# Get builds of the matching build configuration.
get_build_type_builds = HandlerInfo(
    method='GET',
    path='/app/rest/buildTypes/{btLocator}/builds',
    success_response_model=tc_models.Builds,
    query_params={'fields': False},
    path_params=['btLocator'],
    operation_id='getBuildTypeBuilds',
)

# Get all build features of the matching build configuration.
get_all_build_features = HandlerInfo(
    method='GET',
    path='/app/rest/buildTypes/{btLocator}/features',
    success_response_model=tc_models.Features,
    query_params={'fields': False},
    path_params=['btLocator'],
    operation_id='getAllBuildFeatures',
)

# Add build feature to the matching build configuration.
add_build_feature_to_build_type = HandlerInfo(
    method='POST',
    path='/app/rest/buildTypes/{btLocator}/features',
    success_response_model=tc_models.Feature,
    request_model=tc_models.Feature,
    query_params={'fields': False},
    path_params=['btLocator'],
    operation_id='addBuildFeatureToBuildType',
)

# Update all build features of the matching build configuration.
replace_all_build_features = HandlerInfo(
    method='PUT',
    path='/app/rest/buildTypes/{btLocator}/features',
    success_response_model=tc_models.Features,
    request_model=tc_models.Features,
    query_params={'fields': False},
    path_params=['btLocator'],
    operation_id='replaceAllBuildFeatures',
)

# Get a build feature of the matching build configuration.
get_build_feature = HandlerInfo(
    method='GET',
    path='/app/rest/buildTypes/{btLocator}/features/{featureId}',
    success_response_model=tc_models.Feature,
    query_params={'fields': False},
    path_params=['btLocator', 'featureId'],
    operation_id='getBuildFeature',
)

# Update a build feature of the matching build configuration.
replace_build_feature = HandlerInfo(
    method='PUT',
    path='/app/rest/buildTypes/{btLocator}/features/{featureId}',
    success_response_model=tc_models.Feature,
    request_model=tc_models.Feature,
    query_params={'fields': False},
    path_params=['btLocator', 'featureId'],
    operation_id='replaceBuildFeature',
)

# Remove a build feature of the matching build configuration.
delete_feature_of_build_type = HandlerInfo(
    method='DELETE',
    path='/app/rest/buildTypes/{btLocator}/features/{featureId}',
    success_response_model=None,
    path_params=['btLocator', 'featureId'],
    operation_id='deleteFeatureOfBuildType',
)

# Get all parameters of a build feature of the matching build configuration.
get_all_build_feature_parameters = HandlerInfo(
    method='GET',
    path='/app/rest/buildTypes/{btLocator}/features/{featureId}/parameters',
    success_response_model=tc_models.Properties,
    query_params={'fields': False},
    path_params=['btLocator', 'featureId'],
    operation_id='getAllBuildFeatureParameters',
)

# Update a parameter of a build feature of the matching build configuration.
replace_build_feature_parameters = HandlerInfo(
    method='PUT',
    path='/app/rest/buildTypes/{btLocator}/features/{featureId}/parameters',
    success_response_model=tc_models.Properties,
    request_model=tc_models.Properties,
    query_params={'fields': False},
    path_params=['btLocator', 'featureId'],
    operation_id='replaceBuildFeatureParameters',
)

# Get a parameter of a build feature of the matching build configuration.
get_build_feature_parameter = HandlerInfo(
    method='GET',
    path='/app/rest/buildTypes/{btLocator}/features/{featureId}/parameters/{parameterName}',
    success_response_model=str,
    path_params=['btLocator', 'featureId', 'parameterName'],
    operation_id='getBuildFeatureParameter',
)

# Update build feature parameter for the matching build configuration.
add_parameter_to_build_feature = HandlerInfo(
    method='PUT',
    path='/app/rest/buildTypes/{btLocator}/features/{featureId}/parameters/{parameterName}',
    success_response_model=str,
    request_model=str,
    path_params=['btLocator', 'featureId', 'parameterName'],
    operation_id='addParameterToBuildFeature',
)

# Get the setting of a build feature of the matching build configuration.
get_build_feature_setting = HandlerInfo(
    method='GET',
    path='/app/rest/buildTypes/{btLocator}/features/{featureId}/{name}',
    success_response_model=str,
    path_params=['btLocator', 'featureId', 'name'],
    operation_id='getBuildFeatureSetting',
)

# Update a parameter of a build feature of the matching build configuration.
set_build_feature_parameter = HandlerInfo(
    method='PUT',
    path='/app/rest/buildTypes/{btLocator}/features/{featureId}/{name}',
    success_response_model=str,
    request_model=str,
    path_params=['btLocator', 'featureId', 'name'],
    operation_id='setBuildFeatureParameter',
)

# Get all investigations of the matching build configuration.
get_all_investigations_of_build_type = HandlerInfo(
    method='GET',
    path='/app/rest/buildTypes/{btLocator}/investigations',
    success_response_model=tc_models.Investigations,
    query_params={'fields': False},
    path_params=['btLocator'],
    operation_id='getAllInvestigationsOfBuildType',
)

# Move build type to another project.
move_build_type = HandlerInfo(
    method='POST',
    path='/app/rest/buildTypes/{btLocator}/move',
    success_response_model=None,
    query_params={'targetProjectId': False},
    path_params=['btLocator'],
    operation_id='moveBuildType',
)

# Get build parameters.
get_build_parameters_of_build_type = HandlerInfo(
    method='GET',
    path='/app/rest/buildTypes/{btLocator}/output-parameters',
    success_response_model=tc_models.Properties,
    query_params={'locator': False, 'fields': False},
    path_params=['btLocator'],
    operation_id='getBuildParametersOfBuildType',
)

# Create a build parameter.
create_build_parameter_of_build_type = HandlerInfo(
    method='POST',
    path='/app/rest/buildTypes/{btLocator}/output-parameters',
    success_response_model=tc_models.Property,
    request_model=tc_models.Property,
    query_params={'fields': False},
    path_params=['btLocator'],
    operation_id='createBuildParameterOfBuildType',
)

# Update build parameters.
update_build_parameters_of_build_type = HandlerInfo(
    method='PUT',
    path='/app/rest/buildTypes/{btLocator}/output-parameters',
    success_response_model=tc_models.Properties,
    request_model=tc_models.Properties,
    query_params={'fields': False},
    path_params=['btLocator'],
    operation_id='updateBuildParametersOfBuildType',
)

# Delete all build parameters.
delete_build_parameters_of_build_type = HandlerInfo(
    method='DELETE',
    path='/app/rest/buildTypes/{btLocator}/output-parameters',
    success_response_model=None,
    path_params=['btLocator'],
    operation_id='deleteBuildParametersOfBuildType',
)

# Get build parameter.
get_build_parameter_of_build_type = HandlerInfo(
    method='GET',
    path='/app/rest/buildTypes/{btLocator}/output-parameters/{name}',
    success_response_model=tc_models.Property,
    query_params={'fields': False},
    path_params=['btLocator', 'name'],
    operation_id='getBuildParameterOfBuildType',
)

# Update build parameter.
update_build_parameter_of_build_type = HandlerInfo(
    method='PUT',
    path='/app/rest/buildTypes/{btLocator}/output-parameters/{name}',
    success_response_model=tc_models.Property,
    request_model=tc_models.Property,
    query_params={'fields': False},
    path_params=['btLocator', 'name'],
    operation_id='updateBuildParameterOfBuildType',
)

# Delete build parameter.
delete_build_parameter_of_build_type = HandlerInfo(
    method='DELETE',
    path='/app/rest/buildTypes/{btLocator}/output-parameters/{name}',
    success_response_model=None,
    path_params=['btLocator', 'name'],
    operation_id='deleteBuildParameterOfBuildType',
)

# Get value of build parameter.
get_build_parameter_value_of_build_type = HandlerInfo(
    method='GET',
    path='/app/rest/buildTypes/{btLocator}/output-parameters/{name}/value',
    success_response_model=str,
    path_params=['btLocator', 'name'],
    operation_id='getBuildParameterValueOfBuildType',
)

# Update value of build parameter.
update_build_parameter_value_of_build_type = HandlerInfo(
    method='PUT',
    path='/app/rest/buildTypes/{btLocator}/output-parameters/{name}/value',
    success_response_model=str,
    request_model=str,
    path_params=['btLocator', 'name'],
    operation_id='updateBuildParameterValueOfBuildType',
)

# Get build parameters.
get_build_parameters_of_build_type = HandlerInfo(
    method='GET',
    path='/app/rest/buildTypes/{btLocator}/parameters',
    success_response_model=tc_models.Properties,
    query_params={'locator': False, 'fields': False},
    path_params=['btLocator'],
    operation_id='getBuildParametersOfBuildType',
)

# Create a build parameter.
create_build_parameter_of_build_type = HandlerInfo(
    method='POST',
    path='/app/rest/buildTypes/{btLocator}/parameters',
    success_response_model=tc_models.Property,
    request_model=tc_models.Property,
    query_params={'fields': False},
    path_params=['btLocator'],
    operation_id='createBuildParameterOfBuildType',
)

# Update build parameters.
update_build_parameters_of_build_type = HandlerInfo(
    method='PUT',
    path='/app/rest/buildTypes/{btLocator}/parameters',
    success_response_model=tc_models.Properties,
    request_model=tc_models.Properties,
    query_params={'fields': False},
    path_params=['btLocator'],
    operation_id='updateBuildParametersOfBuildType',
)

# Delete all build parameters.
delete_build_parameters_of_build_type = HandlerInfo(
    method='DELETE',
    path='/app/rest/buildTypes/{btLocator}/parameters',
    success_response_model=None,
    path_params=['btLocator'],
    operation_id='deleteBuildParametersOfBuildType',
)

# Get build parameter.
get_build_parameter_of_build_type = HandlerInfo(
    method='GET',
    path='/app/rest/buildTypes/{btLocator}/parameters/{name}',
    success_response_model=tc_models.Property,
    query_params={'fields': False},
    path_params=['btLocator', 'name'],
    operation_id='getBuildParameterOfBuildType',
)

# Update build parameter.
update_build_parameter_of_build_type = HandlerInfo(
    method='PUT',
    path='/app/rest/buildTypes/{btLocator}/parameters/{name}',
    success_response_model=tc_models.Property,
    request_model=tc_models.Property,
    query_params={'fields': False},
    path_params=['btLocator', 'name'],
    operation_id='updateBuildParameterOfBuildType',
)

# Delete build parameter.
delete_build_parameter_of_build_type = HandlerInfo(
    method='DELETE',
    path='/app/rest/buildTypes/{btLocator}/parameters/{name}',
    success_response_model=None,
    path_params=['btLocator', 'name'],
    operation_id='deleteBuildParameterOfBuildType',
)

# Get type of build parameter.
get_build_parameter_type_of_build_type = HandlerInfo(
    method='GET',
    path='/app/rest/buildTypes/{btLocator}/parameters/{name}/type',
    success_response_model=tc_models.Type,
    path_params=['btLocator', 'name'],
    operation_id='getBuildParameterTypeOfBuildType',
)

# Update type of build parameter.
update_build_parameter_type_of_build_type = HandlerInfo(
    method='PUT',
    path='/app/rest/buildTypes/{btLocator}/parameters/{name}/type',
    success_response_model=tc_models.Type,
    request_model=tc_models.Type,
    path_params=['btLocator', 'name'],
    operation_id='updateBuildParameterTypeOfBuildType',
)

# Get build parameter specification.
get_build_parameter_specification_of_build_type = HandlerInfo(
    method='GET',
    path='/app/rest/buildTypes/{btLocator}/parameters/{name}/type/rawValue',
    success_response_model=str,
    path_params=['btLocator', 'name'],
    operation_id='getBuildParameterSpecificationOfBuildType',
)

# Update build parameter specification.
update_build_parameter_specification_of_build_type = HandlerInfo(
    method='PUT',
    path='/app/rest/buildTypes/{btLocator}/parameters/{name}/type/rawValue',
    success_response_model=str,
    request_model=str,
    path_params=['btLocator', 'name'],
    operation_id='updateBuildParameterSpecificationOfBuildType',
)

# Get value of build parameter.
get_build_parameter_value_of_build_type = HandlerInfo(
    method='GET',
    path='/app/rest/buildTypes/{btLocator}/parameters/{name}/value',
    success_response_model=str,
    path_params=['btLocator', 'name'],
    operation_id='getBuildParameterValueOfBuildType',
)

# Update value of build parameter.
update_build_parameter_value_of_build_type = HandlerInfo(
    method='PUT',
    path='/app/rest/buildTypes/{btLocator}/parameters/{name}/value',
    success_response_model=str,
    request_model=str,
    path_params=['btLocator', 'name'],
    operation_id='updateBuildParameterValueOfBuildType',
)

# Get the settings file of the matching build configuration.
get_build_type_settings_file = HandlerInfo(
    method='GET',
    path='/app/rest/buildTypes/{btLocator}/settingsFile',
    success_response_model=str,
    path_params=['btLocator'],
    operation_id='getBuildTypeSettingsFile',
)

# Get all snapshot dependencies of the matching build configuration.
get_all_snapshot_dependencies = HandlerInfo(
    method='GET',
    path='/app/rest/buildTypes/{btLocator}/snapshot-dependencies',
    success_response_model=tc_models.SnapshotDependencies,
    query_params={'fields': False},
    path_params=['btLocator'],
    operation_id='getAllSnapshotDependencies',
)

# Add a snapshot dependency to the matching build configuration.
add_snapshot_dependency_to_build_type = HandlerInfo(
    method='POST',
    path='/app/rest/buildTypes/{btLocator}/snapshot-dependencies',
    success_response_model=tc_models.SnapshotDependency,
    request_model=tc_models.SnapshotDependency,
    query_params={'fields': False},
    path_params=['btLocator'],
    operation_id='addSnapshotDependencyToBuildType',
)

# Update all snapshot dependencies of the matching build configuration.
replace_all_snapshot_dependencies = HandlerInfo(
    method='PUT',
    path='/app/rest/buildTypes/{btLocator}/snapshot-dependencies',
    success_response_model=tc_models.SnapshotDependencies,
    request_model=tc_models.SnapshotDependencies,
    query_params={'fields': False},
    path_params=['btLocator'],
    operation_id='replaceAllSnapshotDependencies',
)

# Get a snapshot dependency of the matching build configuration.
get_snapshot_dependency = HandlerInfo(
    method='GET',
    path='/app/rest/buildTypes/{btLocator}/snapshot-dependencies/{snapshotDepLocator}',
    success_response_model=tc_models.SnapshotDependency,
    query_params={'fields': False},
    path_params=['btLocator', 'snapshotDepLocator'],
    operation_id='getSnapshotDependency',
)

# Update a snapshot dependency of the matching build configuration.
replace_snapshot_dependency = HandlerInfo(
    method='PUT',
    path='/app/rest/buildTypes/{btLocator}/snapshot-dependencies/{snapshotDepLocator}',
    success_response_model=tc_models.SnapshotDependency,
    request_model=tc_models.SnapshotDependency,
    query_params={'fields': False},
    path_params=['btLocator', 'snapshotDepLocator'],
    operation_id='replaceSnapshotDependency',
)

# Delete a snapshot dependency of the matching build configuration.
delete_snapshot_dependency = HandlerInfo(
    method='DELETE',
    path='/app/rest/buildTypes/{btLocator}/snapshot-dependencies/{snapshotDepLocator}',
    success_response_model=None,
    path_params=['btLocator', 'snapshotDepLocator'],
    operation_id='deleteSnapshotDependency',
)

# Get all build steps of the matching build configuration.
get_all_build_steps = HandlerInfo(
    method='GET',
    path='/app/rest/buildTypes/{btLocator}/steps',
    success_response_model=tc_models.Steps,
    query_params={'fields': False},
    path_params=['btLocator'],
    operation_id='getAllBuildSteps',
)

# Add a build step to the matching build configuration.
add_build_step_to_build_type = HandlerInfo(
    method='POST',
    path='/app/rest/buildTypes/{btLocator}/steps',
    success_response_model=tc_models.Step,
    request_model=tc_models.Step,
    query_params={'fields': False},
    path_params=['btLocator'],
    operation_id='addBuildStepToBuildType',
)

# Update all build steps of the matching build configuration.
replace_all_build_steps = HandlerInfo(
    method='PUT',
    path='/app/rest/buildTypes/{btLocator}/steps',
    success_response_model=tc_models.Steps,
    request_model=tc_models.Steps,
    query_params={'fields': False},
    path_params=['btLocator'],
    operation_id='replaceAllBuildSteps',
)

# Get a build step of the matching build configuration.
get_build_step = HandlerInfo(
    method='GET',
    path='/app/rest/buildTypes/{btLocator}/steps/{stepId}',
    success_response_model=tc_models.Step,
    query_params={'fields': False},
    path_params=['btLocator', 'stepId'],
    operation_id='getBuildStep',
)

# Replace a build step of the matching build configuration.
replace_build_step = HandlerInfo(
    method='PUT',
    path='/app/rest/buildTypes/{btLocator}/steps/{stepId}',
    success_response_model=tc_models.Step,
    request_model=tc_models.Step,
    query_params={'fields': False},
    path_params=['btLocator', 'stepId'],
    operation_id='replaceBuildStep',
)

# Delete a build step of the matching build configuration.
delete_build_step = HandlerInfo(
    method='DELETE',
    path='/app/rest/buildTypes/{btLocator}/steps/{stepId}',
    success_response_model=None,
    path_params=['btLocator', 'stepId'],
    operation_id='deleteBuildStep',
)

# Get all parameters of a build step of the matching build configuration.
get_all_build_step_parameters = HandlerInfo(
    method='GET',
    path='/app/rest/buildTypes/{btLocator}/steps/{stepId}/parameters',
    success_response_model=tc_models.Properties,
    query_params={'fields': False},
    path_params=['btLocator', 'stepId'],
    operation_id='getAllBuildStepParameters',
)

# Update a parameter of a build step of the matching build configuration.
delete_build_step_parameters = HandlerInfo(
    method='PUT',
    path='/app/rest/buildTypes/{btLocator}/steps/{stepId}/parameters',
    success_response_model=tc_models.Properties,
    request_model=tc_models.Properties,
    query_params={'fields': False},
    path_params=['btLocator', 'stepId'],
    operation_id='deleteBuildStepParameters',
)

# Get a parameter of a build step of the matching build configuration.
get_build_step_parameter = HandlerInfo(
    method='GET',
    path='/app/rest/buildTypes/{btLocator}/steps/{stepId}/parameters/{parameterName}',
    success_response_model=str,
    path_params=['btLocator', 'stepId', 'parameterName'],
    operation_id='getBuildStepParameter',
)

# Add a parameter to a build step of the matching build configuration.
add_parameter_to_build_step = HandlerInfo(
    method='PUT',
    path='/app/rest/buildTypes/{btLocator}/steps/{stepId}/parameters/{parameterName}',
    success_response_model=str,
    request_model=str,
    path_params=['btLocator', 'stepId', 'parameterName'],
    operation_id='addParameterToBuildStep',
)

# Get the setting of a build step of the matching build configuration.
get_build_step_setting = HandlerInfo(
    method='GET',
    path='/app/rest/buildTypes/{btLocator}/steps/{stepId}/{fieldName}',
    success_response_model=str,
    path_params=['btLocator', 'stepId', 'fieldName'],
    operation_id='getBuildStepSetting',
)

# Update a parameter of a build step of the matching build configuration.
set_build_step_parameter = HandlerInfo(
    method='PUT',
    path='/app/rest/buildTypes/{btLocator}/steps/{stepId}/{fieldName}',
    success_response_model=str,
    request_model=str,
    path_params=['btLocator', 'stepId', 'fieldName'],
    operation_id='setBuildStepParameter',
)

# Get all build templates of the matching build configuration.
get_all_build_templates = HandlerInfo(
    method='GET',
    path='/app/rest/buildTypes/{btLocator}/templates',
    success_response_model=tc_models.BuildTypes,
    query_params={'fields': False},
    path_params=['btLocator'],
    operation_id='getAllBuildTemplates',
)

# Add a build template to the matching build configuration.
add_build_template = HandlerInfo(
    method='POST',
    path='/app/rest/buildTypes/{btLocator}/templates',
    success_response_model=tc_models.BuildType,
    request_model=tc_models.BuildType,
    query_params={'optimizeSettings': False, 'fields': False},
    path_params=['btLocator'],
    operation_id='addBuildTemplate',
)

# Update all templates of the matching build configuration.
set_build_type_templates = HandlerInfo(
    method='PUT',
    path='/app/rest/buildTypes/{btLocator}/templates',
    success_response_model=tc_models.BuildTypes,
    request_model=tc_models.BuildTypes,
    query_params={'optimizeSettings': False, 'fields': False},
    path_params=['btLocator'],
    operation_id='setBuildTypeTemplates',
)

# Detach all templates from the matching build configuration.
remove_all_templates = HandlerInfo(
    method='DELETE',
    path='/app/rest/buildTypes/{btLocator}/templates',
    success_response_model=None,
    query_params={'inlineSettings': False},
    path_params=['btLocator'],
    operation_id='removeAllTemplates',
)

# Get a template of the matching build configuration.
get_build_template = HandlerInfo(
    method='GET',
    path='/app/rest/buildTypes/{btLocator}/templates/{templateLocator}',
    success_response_model=tc_models.BuildType,
    query_params={'fields': False},
    path_params=['btLocator', 'templateLocator'],
    operation_id='getBuildTemplate',
)

# Detach a template from the matching build configuration.
remove_template = HandlerInfo(
    method='DELETE',
    path='/app/rest/buildTypes/{btLocator}/templates/{templateLocator}',
    success_response_model=None,
    query_params={'inlineSettings': False},
    path_params=['btLocator', 'templateLocator'],
    operation_id='removeTemplate',
)

# Get all triggers of the matching build configuration.
get_all_triggers = HandlerInfo(
    method='GET',
    path='/app/rest/buildTypes/{btLocator}/triggers',
    success_response_model=tc_models.Triggers,
    query_params={'fields': False},
    path_params=['btLocator'],
    operation_id='getAllTriggers',
)

# Add a trigger to the matching build configuration.
add_trigger_to_build_type = HandlerInfo(
    method='POST',
    path='/app/rest/buildTypes/{btLocator}/triggers',
    success_response_model=tc_models.Trigger,
    request_model=tc_models.Trigger,
    query_params={'fields': False},
    path_params=['btLocator'],
    operation_id='addTriggerToBuildType',
)

# Update all triggers of the matching build configuration.
replace_all_triggers = HandlerInfo(
    method='PUT',
    path='/app/rest/buildTypes/{btLocator}/triggers',
    success_response_model=tc_models.Triggers,
    request_model=tc_models.Triggers,
    query_params={'fields': False},
    path_params=['btLocator'],
    operation_id='replaceAllTriggers',
)

# Get a trigger of the matching build configuration.
get_trigger = HandlerInfo(
    method='GET',
    path='/app/rest/buildTypes/{btLocator}/triggers/{triggerLocator}',
    success_response_model=tc_models.Trigger,
    query_params={'fields': False},
    path_params=['btLocator', 'triggerLocator'],
    operation_id='getTrigger',
)

# Update a trigger of the matching build configuration.
replace_trigger = HandlerInfo(
    method='PUT',
    path='/app/rest/buildTypes/{btLocator}/triggers/{triggerLocator}',
    success_response_model=tc_models.Trigger,
    request_model=tc_models.Trigger,
    query_params={'fields': False},
    path_params=['btLocator', 'triggerLocator'],
    operation_id='replaceTrigger',
)

# Delete a trigger of the matching build configuration.
delete_trigger = HandlerInfo(
    method='DELETE',
    path='/app/rest/buildTypes/{btLocator}/triggers/{triggerLocator}',
    success_response_model=None,
    path_params=['btLocator', 'triggerLocator'],
    operation_id='deleteTrigger',
)

# Get a parameter of a trigger of the matching build configuration.
get_trigger_parameter = HandlerInfo(
    method='GET',
    path='/app/rest/buildTypes/{btLocator}/triggers/{triggerLocator}/{fieldName}',
    success_response_model=str,
    path_params=['btLocator', 'triggerLocator', 'fieldName'],
    operation_id='getTriggerParameter',
)

# Update a parameter of a trigger of the matching build configuration.
set_trigger_parameter = HandlerInfo(
    method='PUT',
    path='/app/rest/buildTypes/{btLocator}/triggers/{triggerLocator}/{fieldName}',
    success_response_model=str,
    request_model=str,
    path_params=['btLocator', 'triggerLocator', 'fieldName'],
    operation_id='setTriggerParameter',
)

# Get all VCS roots of the matching build configuration.
get_all_vcs_roots_of_build_type = HandlerInfo(
    method='GET',
    path='/app/rest/buildTypes/{btLocator}/vcs-root-entries',
    success_response_model=tc_models.VcsRootEntries,
    query_params={'fields': False},
    path_params=['btLocator'],
    operation_id='getAllVcsRootsOfBuildType',
)

# Add a VCS root to the matching build.
add_vcs_root_to_build_type = HandlerInfo(
    method='POST',
    path='/app/rest/buildTypes/{btLocator}/vcs-root-entries',
    success_response_model=tc_models.VcsRootEntry,
    request_model=tc_models.VcsRootEntry,
    query_params={'fields': False},
    path_params=['btLocator'],
    operation_id='addVcsRootToBuildType',
)

# Update all VCS roots of the matching build configuration.
replace_all_vcs_roots = HandlerInfo(
    method='PUT',
    path='/app/rest/buildTypes/{btLocator}/vcs-root-entries',
    success_response_model=tc_models.VcsRootEntries,
    request_model=tc_models.VcsRootEntries,
    query_params={'fields': False},
    path_params=['btLocator'],
    operation_id='replaceAllVcsRoots',
)

# Get a VCS root of the matching build configuration.
get_vcs_root = HandlerInfo(
    method='GET',
    path='/app/rest/buildTypes/{btLocator}/vcs-root-entries/{vcsRootLocator}',
    success_response_model=tc_models.VcsRootEntry,
    query_params={'fields': False},
    path_params=['btLocator', 'vcsRootLocator'],
    operation_id='getVcsRoot',
)

# Update a VCS root of the matching build configuration.
update_build_type_vcs_root = HandlerInfo(
    method='PUT',
    path='/app/rest/buildTypes/{btLocator}/vcs-root-entries/{vcsRootLocator}',
    success_response_model=tc_models.VcsRootEntry,
    request_model=tc_models.VcsRootEntry,
    query_params={'fields': False},
    path_params=['btLocator', 'vcsRootLocator'],
    operation_id='updateBuildTypeVcsRoot',
)

# Remove a VCS root of the matching build configuration.
delete_vcs_root_of_build_type = HandlerInfo(
    method='DELETE',
    path='/app/rest/buildTypes/{btLocator}/vcs-root-entries/{vcsRootLocator}',
    success_response_model=None,
    path_params=['btLocator', 'vcsRootLocator'],
    operation_id='deleteVcsRootOfBuildType',
)

# Get checkout rules of a VCS root of the matching build configuration.
get_vcs_root_checkout_rules = HandlerInfo(
    method='GET',
    path='/app/rest/buildTypes/{btLocator}/vcs-root-entries/{vcsRootLocator}/checkout-rules',
    success_response_model=str,
    path_params=['btLocator', 'vcsRootLocator'],
    operation_id='getVcsRootCheckoutRules',
)

# Update checkout rules of a VCS root of the matching build configuration.
update_build_type_vcs_root_checkout_rules = HandlerInfo(
    method='PUT',
    path='/app/rest/buildTypes/{btLocator}/vcs-root-entries/{vcsRootLocator}/checkout-rules',
    success_response_model=str,
    request_model=str,
    path_params=['btLocator', 'vcsRootLocator'],
    operation_id='updateBuildTypeVcsRootCheckoutRules',
)

# List all files.
get_files_list_of_build_type = HandlerInfo(
    method='GET',
    path='/app/rest/buildTypes/{btLocator}/vcs/files/latest',
    success_response_model=tc_models.Files,
    query_params={'basePath': False, 'locator': False, 'fields': False, 'resolveParameters': False},
    path_params=['btLocator'],
    operation_id='getFilesListOfBuildType',
)

# Get specific file zipped.
get_zipped_file_of_build_type = HandlerInfo(
    method='GET',
    path='/app/rest/buildTypes/{btLocator}/vcs/files/latest/archived{path}',
    success_response_model=None,
    query_params={'basePath': False, 'locator': False, 'name': False, 'resolveParameters': False},
    path_params=['btLocator', 'path'],
    operation_id='getZippedFileOfBuildType',
)

# Download specific file.
download_file_of_build_type = HandlerInfo(
    method='GET',
    path='/app/rest/buildTypes/{btLocator}/vcs/files/latest/files{path}',
    success_response_model=None,
    query_params={'resolveParameters': False},
    path_params=['btLocator', 'path'],
    operation_id='downloadFileOfBuildType',
)

# Get metadata of specific file.
get_file_metadata_of_build_type = HandlerInfo(
    method='GET',
    path='/app/rest/buildTypes/{btLocator}/vcs/files/latest/metadata{path}',
    success_response_model=tc_models.File,
    query_params={'fields': False, 'resolveParameters': False},
    path_params=['btLocator', 'path'],
    operation_id='getFileMetadataOfBuildType',
)

# List files under this path.
get_files_list_for_subpath_of_build_type = HandlerInfo(
    method='GET',
    path='/app/rest/buildTypes/{btLocator}/vcs/files/latest/{path}',
    success_response_model=tc_models.Files,
    query_params={'basePath': False, 'locator': False, 'fields': False, 'resolveParameters': False},
    path_params=['btLocator', 'path'],
    operation_id='getFilesListForSubpathOfBuildType',
)

# Get all VCS root instances of the matching build configuration.
get_vcs_root_instances_of_build_type = HandlerInfo(
    method='GET',
    path='/app/rest/buildTypes/{btLocator}/vcsRootInstances',
    success_response_model=tc_models.VcsRootInstances,
    query_params={'fields': False},
    path_params=['btLocator'],
    operation_id='getVcsRootInstancesOfBuildType',
)

# Get a field of the matching build configuration.
get_build_type_field = HandlerInfo(
    method='GET',
    path='/app/rest/buildTypes/{btLocator}/{field}',
    success_response_model=str,
    path_params=['btLocator', 'field'],
    operation_id='getBuildTypeField',
)

# Update a field of the matching build configuration.
set_build_type_field = HandlerInfo(
    method='PUT',
    path='/app/rest/buildTypes/{btLocator}/{field}',
    success_response_model=str,
    request_model=str,
    path_params=['btLocator', 'field'],
    operation_id='setBuildTypeField',
)


# ══════════ CHANGE ════════════════════════════════════════════

# Get all changes.
get_all_changes = HandlerInfo(
    method='GET',
    path='/app/rest/changes',
    success_response_model=tc_models.Changes,
    query_params={'locator': False, 'fields': False},
    operation_id='getAllChanges',
)

# Get change matching the locator.
get_change = HandlerInfo(
    method='GET',
    path='/app/rest/changes/{changeLocator}',
    success_response_model=tc_models.Change,
    query_params={'fields': False},
    path_params=['changeLocator'],
    operation_id='getChange',
)

# Get attributes of the matching change.
get_change_attributes = HandlerInfo(
    method='GET',
    path='/app/rest/changes/{changeLocator}/attributes',
    success_response_model=tc_models.Entries,
    query_params={'fields': False},
    path_params=['changeLocator'],
    operation_id='getChangeAttributes',
)

# Get duplicates of the matching change.
get_change_duplicates = HandlerInfo(
    method='GET',
    path='/app/rest/changes/{changeLocator}/duplicates',
    success_response_model=tc_models.Changes,
    query_params={'fields': False},
    path_params=['changeLocator'],
    operation_id='getChangeDuplicates',
)

# Get first builds of the matching change.
get_change_first_builds = HandlerInfo(
    method='GET',
    path='/app/rest/changes/{changeLocator}/firstBuilds',
    success_response_model=tc_models.Builds,
    query_params={'fields': False},
    path_params=['changeLocator'],
    operation_id='getChangeFirstBuilds',
)

# Get issues of the matching change.
get_change_issue = HandlerInfo(
    method='GET',
    path='/app/rest/changes/{changeLocator}/issues',
    success_response_model=tc_models.Issues,
    path_params=['changeLocator'],
    operation_id='getChangeIssue',
)

# Get parent changes of the matching change.
get_change_parent_changes = HandlerInfo(
    method='GET',
    path='/app/rest/changes/{changeLocator}/parentChanges',
    success_response_model=tc_models.Changes,
    query_params={'fields': False},
    path_params=['changeLocator'],
    operation_id='getChangeParentChanges',
)

# Get parent revisions of the matching change.
get_change_parent_revisions = HandlerInfo(
    method='GET',
    path='/app/rest/changes/{changeLocator}/parentRevisions',
    success_response_model=tc_models.Items,
    path_params=['changeLocator'],
    operation_id='getChangeParentRevisions',
)

# Get a VCS root instance of the matching change.
get_change_vcs_root = HandlerInfo(
    method='GET',
    path='/app/rest/changes/{changeLocator}/vcsRootInstance',
    success_response_model=tc_models.VcsRootInstance,
    query_params={'fields': False},
    path_params=['changeLocator'],
    operation_id='getChangeVcsRoot',
)

# Get a field of the matching change.
get_change_field = HandlerInfo(
    method='GET',
    path='/app/rest/changes/{changeLocator}/{field}',
    success_response_model=str,
    path_params=['changeLocator', 'field'],
    operation_id='getChangeField',
)


# ══════════ CLOUDINSTANCE ═════════════════════════════════════

# Get all cloud images.
get_all_cloud_images = HandlerInfo(
    method='GET',
    path='/app/rest/cloud/images',
    success_response_model=tc_models.CloudImages,
    query_params={'locator': False, 'fields': False},
    operation_id='getAllCloudImages',
)

# Get cloud image matching the locator.
get_cloud_image = HandlerInfo(
    method='GET',
    path='/app/rest/cloud/images/{imageLocator}',
    success_response_model=tc_models.CloudImage,
    query_params={'fields': False},
    path_params=['imageLocator'],
    operation_id='getCloudImage',
)

# Get all cloud instances.
get_all_cloud_instances = HandlerInfo(
    method='GET',
    path='/app/rest/cloud/instances',
    success_response_model=tc_models.CloudInstances,
    query_params={'locator': False, 'fields': False},
    operation_id='getAllCloudInstances',
)

# Start a new cloud instance.
start_instance = HandlerInfo(
    method='POST',
    path='/app/rest/cloud/instances',
    success_response_model=None,
    request_model=tc_models.CloudInstance,
    query_params={'fields': False},
    operation_id='startInstance',
)

# Get cloud instance matching the locator.
get_cloud_instance = HandlerInfo(
    method='GET',
    path='/app/rest/cloud/instances/{instanceLocator}',
    success_response_model=tc_models.CloudInstance,
    query_params={'fields': False},
    path_params=['instanceLocator'],
    operation_id='getCloudInstance',
)

# Stop cloud instance matching the locator.
stop_instance = HandlerInfo(
    method='DELETE',
    path='/app/rest/cloud/instances/{instanceLocator}',
    success_response_model=None,
    path_params=['instanceLocator'],
    operation_id='stopInstance',
)

# Terminates existing cloud instance immediately
forse_terminate_instance = HandlerInfo(
    method='POST',
    path='/app/rest/cloud/instances/{instanceLocator}/actions/forceStop',
    success_response_model=None,
    path_params=['instanceLocator'],
    operation_id='forseTerminateInstance',
)

# Schedules existing cloud instance for termination
terminate_instance = HandlerInfo(
    method='POST',
    path='/app/rest/cloud/instances/{instanceLocator}/actions/stop',
    success_response_model=None,
    path_params=['instanceLocator'],
    operation_id='terminateInstance',
)

# Get all cloud profiles.
get_all_cloud_profiles = HandlerInfo(
    method='GET',
    path='/app/rest/cloud/profiles',
    success_response_model=tc_models.CloudProfiles,
    query_params={'locator': False, 'fields': False},
    operation_id='getAllCloudProfiles',
)

# Get cloud profile matching the locator.
get_cloud_profile = HandlerInfo(
    method='GET',
    path='/app/rest/cloud/profiles/{profileLocator}',
    success_response_model=tc_models.CloudProfile,
    query_params={'fields': False},
    path_params=['profileLocator'],
    operation_id='getCloudProfile',
)


# ══════════ DEPLOYMENTDASHBOARD ═══════════════════════════════

# Get all deployment dashboards.
get_all_dashboards = HandlerInfo(
    method='GET',
    path='/app/rest/deploymentDashboards',
    success_response_model=tc_models.DeploymentDashboards,
    query_params={'locator': False, 'fields': False},
    operation_id='getAllDashboards',
)

# Create a new deployment dashboard.
create_dashboard = HandlerInfo(
    method='POST',
    path='/app/rest/deploymentDashboards',
    success_response_model=tc_models.DeploymentDashboard,
    request_model=tc_models.DeploymentDashboard,
    operation_id='createDashboard',
)

# Get the deployment dashboard matching the locator.
get_dashboard = HandlerInfo(
    method='GET',
    path='/app/rest/deploymentDashboards/{deploymentDashboardLocator}',
    success_response_model=tc_models.DeploymentDashboard,
    query_params={'fields': False},
    path_params=['deploymentDashboardLocator'],
    operation_id='getDashboard',
)

# Delete the deployment dashboard matching the locator.
delete_dashboard = HandlerInfo(
    method='DELETE',
    path='/app/rest/deploymentDashboards/{deploymentDashboardLocator}',
    success_response_model=None,
    path_params=['deploymentDashboardLocator'],
    operation_id='deleteDashboard',
)

# Get deployment instances for a given deployment dashboard.
get_instances = HandlerInfo(
    method='GET',
    path='/app/rest/deploymentDashboards/{deploymentDashboardLocator}/instances',
    success_response_model=tc_models.DeploymentInstances,
    query_params={'locator': False, 'fields': False},
    path_params=['deploymentDashboardLocator'],
    operation_id='getInstances',
)

# Create a new deployment instance.
create_instance = HandlerInfo(
    method='POST',
    path='/app/rest/deploymentDashboards/{deploymentDashboardLocator}/instances',
    success_response_model=tc_models.DeploymentInstance,
    request_model=tc_models.DeploymentInstance,
    path_params=['deploymentDashboardLocator'],
    operation_id='createInstance',
)

# Get the deployment instance matching the locator.
get_instance = HandlerInfo(
    method='GET',
    path='/app/rest/deploymentDashboards/{deploymentDashboardLocator}/instances/{deploymentInstanceLocator}',
    success_response_model=tc_models.DeploymentInstance,
    query_params={'fields': False},
    path_params=['deploymentDashboardLocator', 'deploymentInstanceLocator'],
    operation_id='getInstance',
)

# Report a new deployment for instance.
report_new_deployment_for_instance = HandlerInfo(
    method='POST',
    path='/app/rest/deploymentDashboards/{deploymentDashboardLocator}/instances/{deploymentInstanceLocator}',
    success_response_model=tc_models.DeploymentInstance,
    request_model=tc_models.DeploymentStateEntry,
    path_params=['deploymentDashboardLocator', 'deploymentInstanceLocator'],
    operation_id='reportNewDeploymentForInstance',
)

# Delete the deployment instance matching the locator.
delete_instance = HandlerInfo(
    method='DELETE',
    path='/app/rest/deploymentDashboards/{deploymentDashboardLocator}/instances/{deploymentInstanceLocator}',
    success_response_model=None,
    path_params=['deploymentDashboardLocator', 'deploymentInstanceLocator'],
    operation_id='deleteInstance',
)


# ══════════ GLOBAL SERVER SETTINGS ════════════════════════════

# Get global settings.
get_global_settings = HandlerInfo(
    method='GET',
    path='/app/rest/server/globalSettings',
    success_response_model=tc_models.ServerGlobalSettings,
    operation_id='getGlobalSettings',
)

# Set global settings.
set_global_settings = HandlerInfo(
    method='PUT',
    path='/app/rest/server/globalSettings',
    success_response_model=tc_models.ServerGlobalSettings,
    request_model=tc_models.ServerGlobalSettings,
    operation_id='setGlobalSettings',
)


# ══════════ GROUP ═════════════════════════════════════════════

# Get all user groups.
get_all_groups = HandlerInfo(
    method='GET',
    path='/app/rest/userGroups',
    success_response_model=tc_models.Groups,
    query_params={'fields': False},
    operation_id='getAllGroups',
)

# Add a new user group.
add_group = HandlerInfo(
    method='POST',
    path='/app/rest/userGroups',
    success_response_model=tc_models.Group,
    request_model=tc_models.Group,
    query_params={'fields': False},
    operation_id='addGroup',
)

# Get user group matching the locator.
get_user_group_of_group = HandlerInfo(
    method='GET',
    path='/app/rest/userGroups/{groupLocator}',
    success_response_model=tc_models.Group,
    query_params={'fields': False},
    path_params=['groupLocator'],
    operation_id='getUserGroupOfGroup',
)

# Delete user group matching the locator.
delete_group = HandlerInfo(
    method='DELETE',
    path='/app/rest/userGroups/{groupLocator}',
    success_response_model=None,
    path_params=['groupLocator'],
    operation_id='deleteGroup',
)

# Get parent groups of the matching user group.
get_group_parent_groups = HandlerInfo(
    method='GET',
    path='/app/rest/userGroups/{groupLocator}/parent-groups',
    success_response_model=tc_models.Groups,
    query_params={'fields': False},
    path_params=['groupLocator'],
    operation_id='getGroupParentGroups',
)

# Update parent groups of the matching user group.
set_group_parent_groups = HandlerInfo(
    method='PUT',
    path='/app/rest/userGroups/{groupLocator}/parent-groups',
    success_response_model=tc_models.Groups,
    request_model=tc_models.Groups,
    query_params={'fields': False},
    path_params=['groupLocator'],
    operation_id='setGroupParentGroups',
)

# Get properties of the matching user group.
get_group_properties = HandlerInfo(
    method='GET',
    path='/app/rest/userGroups/{groupLocator}/properties',
    success_response_model=tc_models.Properties,
    query_params={'fields': False},
    path_params=['groupLocator'],
    operation_id='getGroupProperties',
)

# Get a property of the matching user group.
get_group_property = HandlerInfo(
    method='GET',
    path='/app/rest/userGroups/{groupLocator}/properties/{name}',
    success_response_model=str,
    path_params=['groupLocator', 'name'],
    operation_id='getGroupProperty',
)

# Update a property of the matching user group.
set_group_property = HandlerInfo(
    method='PUT',
    path='/app/rest/userGroups/{groupLocator}/properties/{name}',
    success_response_model=str,
    request_model=str,
    path_params=['groupLocator', 'name'],
    operation_id='setGroupProperty',
)

# Remove a property of the matching user group.
remove_group_property = HandlerInfo(
    method='DELETE',
    path='/app/rest/userGroups/{groupLocator}/properties/{name}',
    success_response_model=None,
    path_params=['groupLocator', 'name'],
    operation_id='removeGroupProperty',
)

# Get all roles of the matching user group.
get_group_roles = HandlerInfo(
    method='GET',
    path='/app/rest/userGroups/{groupLocator}/roles',
    success_response_model=tc_models.RoleAssignments,
    path_params=['groupLocator'],
    operation_id='getGroupRoles',
)

# Add a role to the matching user group.
add_role_to_group = HandlerInfo(
    method='POST',
    path='/app/rest/userGroups/{groupLocator}/roles',
    success_response_model=tc_models.RoleAssignment,
    request_model=tc_models.RoleAssignment,
    path_params=['groupLocator'],
    operation_id='addRoleToGroup',
)

# Update roles of the matching user group.
set_group_roles = HandlerInfo(
    method='PUT',
    path='/app/rest/userGroups/{groupLocator}/roles',
    success_response_model=tc_models.RoleAssignments,
    request_model=tc_models.RoleAssignments,
    path_params=['groupLocator'],
    operation_id='setGroupRoles',
)

# Get a role with the specific scope of the matching user group.
get_group_role_at_scope = HandlerInfo(
    method='GET',
    path='/app/rest/userGroups/{groupLocator}/roles/{roleId}/{scope}',
    success_response_model=tc_models.RoleAssignment,
    path_params=['groupLocator', 'roleId', 'scope'],
    operation_id='getGroupRoleAtScope',
)

# Add a role with the specific scope to the matching user group.
add_role_at_scope_to_group = HandlerInfo(
    method='POST',
    path='/app/rest/userGroups/{groupLocator}/roles/{roleId}/{scope}',
    success_response_model=tc_models.RoleAssignment,
    path_params=['groupLocator', 'roleId', 'scope'],
    operation_id='addRoleAtScopeToGroup',
)

# Remove a role with the specific scope from the matching user group.
remove_role_at_scope_from_group = HandlerInfo(
    method='DELETE',
    path='/app/rest/userGroups/{groupLocator}/roles/{roleId}/{scope}',
    success_response_model=None,
    path_params=['groupLocator', 'roleId', 'scope'],
    operation_id='removeRoleAtScopeFromGroup',
)


# ══════════ INVESTIGATION ═════════════════════════════════════

# Get all investigations.
get_all_investigations = HandlerInfo(
    method='GET',
    path='/app/rest/investigations',
    success_response_model=tc_models.Investigations,
    query_params={'locator': False, 'fields': False},
    operation_id='getAllInvestigations',
)

# Create a new investigation.
add_investigation = HandlerInfo(
    method='POST',
    path='/app/rest/investigations',
    success_response_model=tc_models.Investigation,
    request_model=tc_models.Investigation,
    query_params={'fields': False},
    operation_id='addInvestigation',
)

# Create multiple new investigations.
add_multiple_investigations = HandlerInfo(
    method='POST',
    path='/app/rest/investigations/multiple',
    success_response_model=tc_models.Investigations,
    request_model=tc_models.Investigations,
    query_params={'fields': False},
    operation_id='addMultipleInvestigations',
)

# Get investigation matching the locator.
get_investigation = HandlerInfo(
    method='GET',
    path='/app/rest/investigations/{investigationLocator}',
    success_response_model=tc_models.Investigation,
    query_params={'fields': False},
    path_params=['investigationLocator'],
    operation_id='getInvestigation',
)

# Update investigation matching the locator.
replace_investigation = HandlerInfo(
    method='PUT',
    path='/app/rest/investigations/{investigationLocator}',
    success_response_model=tc_models.Investigation,
    request_model=tc_models.Investigation,
    query_params={'fields': False},
    path_params=['investigationLocator'],
    operation_id='replaceInvestigation',
)

# Delete investigation matching the locator.
delete_investigation = HandlerInfo(
    method='DELETE',
    path='/app/rest/investigations/{investigationLocator}',
    success_response_model=None,
    path_params=['investigationLocator'],
    operation_id='deleteInvestigation',
)


# ══════════ MUTE ══════════════════════════════════════════════

# Get all muted tests.
get_all_muted_tests = HandlerInfo(
    method='GET',
    path='/app/rest/mutes',
    success_response_model=tc_models.Mutes,
    query_params={'locator': False, 'fields': False},
    operation_id='getAllMutedTests',
)

# Mute a test.
mute_test = HandlerInfo(
    method='POST',
    path='/app/rest/mutes',
    success_response_model=tc_models.Mute,
    request_model=tc_models.Mute,
    query_params={'fields': False},
    operation_id='muteTest',
)

# Mute multiple tests.
mute_multiple_tests = HandlerInfo(
    method='POST',
    path='/app/rest/mutes/multiple',
    success_response_model=tc_models.Mutes,
    request_model=tc_models.Mutes,
    query_params={'fields': False},
    operation_id='muteMultipleTests',
)

# Unmute multiple tests.
unmute_multiple_tests = HandlerInfo(
    method='DELETE',
    path='/app/rest/mutes/multiple',
    success_response_model=None,
    request_model=tc_models.Mutes,
    query_params={'fields': False},
    operation_id='unmuteMultipleTests',
)

# Get a muted test.
get_muted_test = HandlerInfo(
    method='GET',
    path='/app/rest/mutes/{muteLocator}',
    success_response_model=tc_models.Mute,
    query_params={'fields': False},
    path_params=['muteLocator'],
    operation_id='getMutedTest',
)

# Unmute the matching test.
unmute_test = HandlerInfo(
    method='DELETE',
    path='/app/rest/mutes/{muteLocator}',
    success_response_model=None,
    request_model=str,
    path_params=['muteLocator'],
    operation_id='unmuteTest',
)


# ══════════ NODE ══════════════════════════════════════════════

# Get all TeamCity nodes.
get_all_nodes = HandlerInfo(
    method='GET',
    path='/app/rest/server/nodes',
    success_response_model=tc_models.Nodes,
    query_params={'locator': False, 'fields': False},
    operation_id='getAllNodes',
)

# Get a node matching the locator.
get_node = HandlerInfo(
    method='GET',
    path='/app/rest/server/nodes/{nodeLocator}',
    success_response_model=tc_models.Node,
    query_params={'fields': False},
    path_params=['nodeLocator'],
    operation_id='getNode',
)

# Get all effective responsibilities for a node matching the locator.
get_disabled_responsibilities = HandlerInfo(
    method='GET',
    path='/app/rest/server/nodes/{nodeLocator}/disabledResponsibilities',
    success_response_model=tc_models.DisabledResponsibilities,
    query_params={'fields': False},
    path_params=['nodeLocator'],
    operation_id='getDisabledResponsibilities',
)

# Get all effective responsibilities for a node matching the locator.
get_effective_responsibilities = HandlerInfo(
    method='GET',
    path='/app/rest/server/nodes/{nodeLocator}/effectiveResponsibilities',
    success_response_model=tc_models.EffectiveResponsibilities,
    query_params={'fields': False},
    path_params=['nodeLocator'],
    operation_id='getEffectiveResponsibilities',
)

# Get all enabled responsibilities for a node matching the locator.
get_enabled_responsibilities = HandlerInfo(
    method='GET',
    path='/app/rest/server/nodes/{nodeLocator}/enabledResponsibilities',
    success_response_model=tc_models.EnabledResponsibilities,
    query_params={'fields': False},
    path_params=['nodeLocator'],
    operation_id='getEnabledResponsibilities',
)

# Enables or disables responsibility for a node.
change_node_responsibility = HandlerInfo(
    method='PUT',
    path='/app/rest/server/nodes/{nodeLocator}/enabledResponsibilities/{name}',
    success_response_model=tc_models.EnabledResponsibilities,
    request_model=str,
    path_params=['nodeLocator', 'name'],
    operation_id='changeNodeResponsibility',
)


# ══════════ PROBLEM ═══════════════════════════════════════════

# Get all build problems.
get_all_build_problems = HandlerInfo(
    method='GET',
    path='/app/rest/problems',
    success_response_model=tc_models.Problems,
    query_params={'locator': False, 'fields': False},
    operation_id='getAllBuildProblems',
)

# Get a matching build problem.
get_build_problem = HandlerInfo(
    method='GET',
    path='/app/rest/problems/{problemLocator}',
    success_response_model=tc_models.Problem,
    query_params={'fields': False},
    path_params=['problemLocator'],
    operation_id='getBuildProblem',
)


# ══════════ PROBLEMOCCURRENCE ═════════════════════════════════

# Get all build problem occurrences.
get_all_build_problem_occurrences = HandlerInfo(
    method='GET',
    path='/app/rest/problemOccurrences',
    success_response_model=tc_models.ProblemOccurrences,
    query_params={'locator': False, 'fields': False},
    operation_id='getAllBuildProblemOccurrences',
)

# Get a matching build problem occurrence.
get_build_problem_occurrence = HandlerInfo(
    method='GET',
    path='/app/rest/problemOccurrences/{problemLocator}',
    success_response_model=tc_models.ProblemOccurrence,
    query_params={'fields': False},
    path_params=['problemLocator'],
    operation_id='getBuildProblemOccurrence',
)


# ══════════ PROJECT ═══════════════════════════════════════════

# Get all projects.
get_all_projects = HandlerInfo(
    method='GET',
    path='/app/rest/projects',
    success_response_model=tc_models.Projects,
    query_params={'locator': False, 'fields': False},
    operation_id='getAllProjects',
)

# Create a new project.
add_project = HandlerInfo(
    method='POST',
    path='/app/rest/projects',
    success_response_model=tc_models.Project,
    request_model=tc_models.NewProjectDescription,
    operation_id='addProject',
)

# Get project matching the locator.
get_project = HandlerInfo(
    method='GET',
    path='/app/rest/projects/{projectLocator}',
    success_response_model=tc_models.Project,
    query_params={'fields': False},
    path_params=['projectLocator'],
    operation_id='getProject',
)

# Delete project matching the locator.
delete_project = HandlerInfo(
    method='DELETE',
    path='/app/rest/projects/{projectLocator}',
    success_response_model=None,
    path_params=['projectLocator'],
    operation_id='deleteProject',
)

# Get agent pools appointed to the matching project.
get_agent_pools_project = HandlerInfo(
    method='GET',
    path='/app/rest/projects/{projectLocator}/agentPools',
    success_response_model=tc_models.AgentPools,
    query_params={'fields': False},
    path_params=['projectLocator'],
    operation_id='getAgentPoolsProject',
)

# Assign the matching project to the agent pool.
add_agent_pools_project = HandlerInfo(
    method='POST',
    path='/app/rest/projects/{projectLocator}/agentPools',
    success_response_model=tc_models.AgentPool,
    request_model=tc_models.AgentPool,
    path_params=['projectLocator'],
    operation_id='addAgentPoolsProject',
)

# Update agent pools apppointed to the matching project.
set_agent_pools_project = HandlerInfo(
    method='PUT',
    path='/app/rest/projects/{projectLocator}/agentPools',
    success_response_model=tc_models.AgentPools,
    request_model=tc_models.AgentPools,
    query_params={'fields': False},
    path_params=['projectLocator'],
    operation_id='setAgentPoolsProject',
)

# Unassign a project from the matching agent pool.
remove_project_from_agent_pool = HandlerInfo(
    method='DELETE',
    path='/app/rest/projects/{projectLocator}/agentPools/{agentPoolLocator}',
    success_response_model=None,
    path_params=['projectLocator', 'agentPoolLocator'],
    operation_id='removeProjectFromAgentPool',
)

# Get all branches of the matching project.
get_all_branches = HandlerInfo(
    method='GET',
    path='/app/rest/projects/{projectLocator}/branches',
    success_response_model=tc_models.Branches,
    query_params={'locator': False, 'fields': False},
    path_params=['projectLocator'],
    operation_id='getAllBranches',
)

# Add a build configuration to the matching project.
add_build_type = HandlerInfo(
    method='POST',
    path='/app/rest/projects/{projectLocator}/buildTypes',
    success_response_model=tc_models.BuildType,
    request_model=tc_models.NewBuildTypeDescription,
    query_params={'fields': False},
    path_params=['projectLocator'],
    operation_id='addBuildType',
)

# Get the default template of the matching project.
get_default_template = HandlerInfo(
    method='GET',
    path='/app/rest/projects/{projectLocator}/defaultTemplate',
    success_response_model=tc_models.BuildType,
    query_params={'fields': False},
    path_params=['projectLocator'],
    operation_id='getDefaultTemplate',
)

# Update the default template of the matching project.
set_default_template = HandlerInfo(
    method='PUT',
    path='/app/rest/projects/{projectLocator}/defaultTemplate',
    success_response_model=tc_models.BuildType,
    request_model=tc_models.BuildType,
    query_params={'fields': False},
    path_params=['projectLocator'],
    operation_id='setDefaultTemplate',
)

# Remove the default template from the matching project.
remove_default_template = HandlerInfo(
    method='DELETE',
    path='/app/rest/projects/{projectLocator}/defaultTemplate',
    success_response_model=None,
    query_params={'fields': False},
    path_params=['projectLocator'],
    operation_id='removeDefaultTemplate',
)

# getDefaultValueSets
get_default_value_sets = HandlerInfo(
    method='GET',
    path='/app/rest/projects/{projectLocator}/defaultValueSets',
    success_response_model=tc_models.TypedValueSets,
    query_params={'fields': False},
    path_params=['projectLocator'],
    operation_id='getDefaultValueSets',
)

# getDeploymentDashboardsInProjet
get_deployment_dashboards_in_project = HandlerInfo(
    method='GET',
    path='/app/rest/projects/{projectLocator}/deploymentDashboards',
    success_response_model=tc_models.DeploymentDashboards,
    query_params={'fields': False},
    path_params=['projectLocator'],
    operation_id='getDeploymentDashboardsInProject',
)

# getDeploymentDashboardInProject
get_deployment_dashboard_in_project = HandlerInfo(
    method='GET',
    path='/app/rest/projects/{projectLocator}/deploymentDashboards/{dashboardLocator}',
    success_response_model=tc_models.DeploymentDashboard,
    query_params={'fields': False},
    path_params=['projectLocator', 'dashboardLocator'],
    operation_id='getDeploymentDashboardInProject',
)

# Get all build configurations from the matching project, with custom ordering applied.
get_all_build_types_ordered = HandlerInfo(
    method='GET',
    path='/app/rest/projects/{projectLocator}/order/buildTypes',
    success_response_model=tc_models.BuildTypes,
    query_params={'field': False},
    path_params=['projectLocator'],
    operation_id='getAllBuildTypesOrdered',
)

# Update custom ordering of build configurations of the matching project.
set_build_types_order = HandlerInfo(
    method='PUT',
    path='/app/rest/projects/{projectLocator}/order/buildTypes',
    success_response_model=tc_models.BuildTypes,
    request_model=tc_models.BuildTypes,
    query_params={'field': False},
    path_params=['projectLocator'],
    operation_id='setBuildTypesOrder',
)

# Get all subprojects of the matching project, with custom ordering applied.
get_all_subprojects_ordered = HandlerInfo(
    method='GET',
    path='/app/rest/projects/{projectLocator}/order/projects',
    success_response_model=tc_models.Projects,
    query_params={'field': False},
    path_params=['projectLocator'],
    operation_id='getAllSubprojectsOrdered',
)

# Update custom ordering of subprojects of the matching project.
set_subprojects_order = HandlerInfo(
    method='PUT',
    path='/app/rest/projects/{projectLocator}/order/projects',
    success_response_model=tc_models.Projects,
    request_model=tc_models.Projects,
    query_params={'field': False},
    path_params=['projectLocator'],
    operation_id='setSubprojectsOrder',
)

# Get build parameters.
get_build_parameters = HandlerInfo(
    method='GET',
    path='/app/rest/projects/{projectLocator}/parameters',
    success_response_model=tc_models.Properties,
    query_params={'locator': False, 'fields': False},
    path_params=['projectLocator'],
    operation_id='getBuildParameters',
)

# Create a build parameter.
create_build_parameter = HandlerInfo(
    method='POST',
    path='/app/rest/projects/{projectLocator}/parameters',
    success_response_model=tc_models.Property,
    request_model=tc_models.Property,
    query_params={'fields': False},
    path_params=['projectLocator'],
    operation_id='createBuildParameter',
)

# Update build parameters.
update_build_parameters = HandlerInfo(
    method='PUT',
    path='/app/rest/projects/{projectLocator}/parameters',
    success_response_model=tc_models.Properties,
    request_model=tc_models.Properties,
    query_params={'fields': False},
    path_params=['projectLocator'],
    operation_id='updateBuildParameters',
)

# Delete all build parameters.
delete_build_parameters = HandlerInfo(
    method='DELETE',
    path='/app/rest/projects/{projectLocator}/parameters',
    success_response_model=None,
    path_params=['projectLocator'],
    operation_id='deleteBuildParameters',
)

# Get build parameter.
get_build_parameter = HandlerInfo(
    method='GET',
    path='/app/rest/projects/{projectLocator}/parameters/{name}',
    success_response_model=tc_models.Property,
    query_params={'fields': False},
    path_params=['projectLocator', 'name'],
    operation_id='getBuildParameter',
)

# Update build parameter.
update_build_parameter = HandlerInfo(
    method='PUT',
    path='/app/rest/projects/{projectLocator}/parameters/{name}',
    success_response_model=tc_models.Property,
    request_model=tc_models.Property,
    query_params={'fields': False},
    path_params=['projectLocator', 'name'],
    operation_id='updateBuildParameter',
)

# Delete build parameter.
delete_build_parameter = HandlerInfo(
    method='DELETE',
    path='/app/rest/projects/{projectLocator}/parameters/{name}',
    success_response_model=None,
    path_params=['projectLocator', 'name'],
    operation_id='deleteBuildParameter',
)

# Get type of build parameter.
get_build_parameter_type = HandlerInfo(
    method='GET',
    path='/app/rest/projects/{projectLocator}/parameters/{name}/type',
    success_response_model=tc_models.Type,
    path_params=['projectLocator', 'name'],
    operation_id='getBuildParameterType',
)

# Update type of build parameter.
update_build_parameter_type = HandlerInfo(
    method='PUT',
    path='/app/rest/projects/{projectLocator}/parameters/{name}/type',
    success_response_model=tc_models.Type,
    request_model=tc_models.Type,
    path_params=['projectLocator', 'name'],
    operation_id='updateBuildParameterType',
)

# Get build parameter specification.
get_build_parameter_specification = HandlerInfo(
    method='GET',
    path='/app/rest/projects/{projectLocator}/parameters/{name}/type/rawValue',
    success_response_model=str,
    path_params=['projectLocator', 'name'],
    operation_id='getBuildParameterSpecification',
)

# Update build parameter specification.
update_build_parameter_specification = HandlerInfo(
    method='PUT',
    path='/app/rest/projects/{projectLocator}/parameters/{name}/type/rawValue',
    success_response_model=str,
    request_model=str,
    path_params=['projectLocator', 'name'],
    operation_id='updateBuildParameterSpecification',
)

# Get value of build parameter.
get_build_parameter_value = HandlerInfo(
    method='GET',
    path='/app/rest/projects/{projectLocator}/parameters/{name}/value',
    success_response_model=str,
    path_params=['projectLocator', 'name'],
    operation_id='getBuildParameterValue',
)

# Update value of build parameter.
update_build_parameter_value = HandlerInfo(
    method='PUT',
    path='/app/rest/projects/{projectLocator}/parameters/{name}/value',
    success_response_model=str,
    request_model=str,
    path_params=['projectLocator', 'name'],
    operation_id='updateBuildParameterValue',
)

# Get the parent project of the matching project.
get_project_parent_project = HandlerInfo(
    method='GET',
    path='/app/rest/projects/{projectLocator}/parentProject',
    success_response_model=tc_models.Project,
    query_params={'fields': False},
    path_params=['projectLocator'],
    operation_id='getProjectParentProject',
)

# Update the parent project of the matching project.
set_parent_project = HandlerInfo(
    method='PUT',
    path='/app/rest/projects/{projectLocator}/parentProject',
    success_response_model=tc_models.Project,
    request_model=tc_models.Project,
    query_params={'fields': False},
    path_params=['projectLocator'],
    operation_id='setParentProject',
)

# Get all features.
get_features = HandlerInfo(
    method='GET',
    path='/app/rest/projects/{projectLocator}/projectFeatures',
    success_response_model=dict,
    query_params={'locator': False, 'fields': False},
    path_params=['projectLocator'],
    operation_id='getFeatures',
)

# Add a feature.
add_feature = HandlerInfo(
    method='POST',
    path='/app/rest/projects/{projectLocator}/projectFeatures',
    success_response_model=dict,
    request_model=tc_models.ProjectFeature,
    query_params={'fields': False},
    path_params=['projectLocator'],
    operation_id='addFeature',
)

# Update all features.
update_features = HandlerInfo(
    method='PUT',
    path='/app/rest/projects/{projectLocator}/projectFeatures',
    success_response_model=dict,
    request_model=tc_models.ProjectFeatures,
    query_params={'fields': False},
    path_params=['projectLocator'],
    operation_id='updateFeatures',
)

# Get a matching feature.
get_feature = HandlerInfo(
    method='GET',
    path='/app/rest/projects/{projectLocator}/projectFeatures/{featureLocator}',
    success_response_model=dict,
    query_params={'fields': False},
    path_params=['projectLocator', 'featureLocator'],
    operation_id='getFeature',
)

# Update a matching feature.
update_feature = HandlerInfo(
    method='PUT',
    path='/app/rest/projects/{projectLocator}/projectFeatures/{featureLocator}',
    success_response_model=dict,
    request_model=tc_models.ProjectFeature,
    query_params={'fields': False},
    path_params=['projectLocator', 'featureLocator'],
    operation_id='updateFeature',
)

# Delete a matching feature.
delete_feature = HandlerInfo(
    method='DELETE',
    path='/app/rest/projects/{projectLocator}/projectFeatures/{featureLocator}',
    success_response_model=None,
    path_params=['projectLocator', 'featureLocator'],
    operation_id='deleteFeature',
)

# Creates a new [secure token](https://www.jetbrains.com/help/teamcity/storing-project-settings-in-version-control.html#Managing+Tokens) to store the sensitive value passed in the request body. Returns the scrambled value that is the new token name. This operation is available only for users with the EDIT_PROJECT permission (included in the Project Administrator role by default).
add_secure_token = HandlerInfo(
    method='POST',
    path='/app/rest/projects/{projectLocator}/secure/tokens',
    success_response_model=str,
    request_model=str,
    path_params=['projectLocator'],
    operation_id='addSecureToken',
)

# Returns the value of the given [secure token](https://www.jetbrains.com/help/teamcity/storing-project-settings-in-version-control.html#Managing+Tokens).This operation is available only for users with the CHANGE_SERVER_SETTINGS permission (included only in System Administrator role by default).
get_secure_value = HandlerInfo(
    method='GET',
    path='/app/rest/projects/{projectLocator}/secure/values/{token}',
    success_response_model=str,
    path_params=['projectLocator', 'token'],
    operation_id='getSecureValue',
)

# Get the settings file of the matching build configuration.
get_project_settings_file = HandlerInfo(
    method='GET',
    path='/app/rest/projects/{projectLocator}/settingsFile',
    success_response_model=str,
    path_params=['projectLocator'],
    operation_id='getProjectSettingsFile',
)

# Get all templates of the matching project.
get_project_templates = HandlerInfo(
    method='GET',
    path='/app/rest/projects/{projectLocator}/templates',
    success_response_model=tc_models.BuildTypes,
    query_params={'fields': False},
    path_params=['projectLocator'],
    operation_id='getProjectTemplates',
)

# Add a build configuration template to the matching project.
add_template = HandlerInfo(
    method='POST',
    path='/app/rest/projects/{projectLocator}/templates',
    success_response_model=tc_models.BuildType,
    request_model=tc_models.NewBuildTypeDescription,
    query_params={'fields': False},
    path_params=['projectLocator'],
    operation_id='addTemplate',
)

# Get a field of the matching project.
get_project_field = HandlerInfo(
    method='GET',
    path='/app/rest/projects/{projectLocator}/{field}',
    success_response_model=str,
    path_params=['projectLocator', 'field'],
    operation_id='getProjectField',
)

# Update a field of the matching project.
set_project_field = HandlerInfo(
    method='PUT',
    path='/app/rest/projects/{projectLocator}/{field}',
    success_response_model=str,
    request_model=str,
    path_params=['projectLocator', 'field'],
    operation_id='setProjectField',
)


# ══════════ ROLE ══════════════════════════════════════════════

# Get all roles.
get_roles = HandlerInfo(
    method='GET',
    path='/app/rest/roles',
    success_response_model=tc_models.Roles,
    query_params={'fields': False},
    operation_id='getRoles',
)

# Create a new role.
create_role = HandlerInfo(
    method='POST',
    path='/app/rest/roles',
    success_response_model=tc_models.Role,
    request_model=tc_models.Role,
    query_params={'fields': False},
    operation_id='createRole',
)

# Get a role with specified id.
get_role = HandlerInfo(
    method='GET',
    path='/app/rest/roles/id:{id}',
    success_response_model=tc_models.Role,
    query_params={'fields': False},
    path_params=['id'],
    operation_id='getRole',
)

# Delete a role matching the id.
delete_role = HandlerInfo(
    method='DELETE',
    path='/app/rest/roles/id:{id}',
    success_response_model=None,
    path_params=['id'],
    operation_id='deleteRole',
)

# Add an included role.
add_included_role = HandlerInfo(
    method='PUT',
    path='/app/rest/roles/id:{roleId}/included/{includedId}',
    success_response_model=tc_models.Role,
    query_params={'fields': False},
    path_params=['roleId', 'includedId'],
    operation_id='addIncludedRole',
)

# Remove an included role.
remove_included_role = HandlerInfo(
    method='DELETE',
    path='/app/rest/roles/id:{roleId}/included/{includedId}',
    success_response_model=tc_models.Role,
    query_params={'fields': False},
    path_params=['roleId', 'includedId'],
    operation_id='removeIncludedRole',
)

# Add a permission to a role.
add_permission = HandlerInfo(
    method='PUT',
    path='/app/rest/roles/id:{roleId}/permissions/{permissionId}',
    success_response_model=tc_models.Role,
    query_params={'fields': False},
    path_params=['roleId', 'permissionId'],
    operation_id='addPermission',
)

# Remove a permission from a role.
remove_permission = HandlerInfo(
    method='DELETE',
    path='/app/rest/roles/id:{roleId}/permissions/{permissionId}',
    success_response_model=tc_models.Role,
    query_params={'fields': False},
    path_params=['roleId', 'permissionId'],
    operation_id='removePermission',
)


# ══════════ ROOT ══════════════════════════════════════════════

# Get root endpoints.
get_root_endpoints_of_root = HandlerInfo(
    method='GET',
    path='/app/rest',
    success_response_model=str,
    operation_id='getRootEndpointsOfRoot',
)

# Get the API version.
get_api_version = HandlerInfo(
    method='GET',
    path='/app/rest/apiVersion',
    success_response_model=str,
    operation_id='getApiVersion',
)

# Get the plugin info.
get_plugin_info = HandlerInfo(
    method='GET',
    path='/app/rest/info',
    success_response_model=tc_models.Plugin,
    query_params={'fields': False},
    operation_id='getPluginInfo',
)

# Get the TeamCity server version.
get_version = HandlerInfo(
    method='GET',
    path='/app/rest/version',
    success_response_model=str,
    operation_id='getVersion',
)


# ══════════ SERVER ════════════════════════════════════════════

# Get the server info.
get_server_info = HandlerInfo(
    method='GET',
    path='/app/rest/server',
    success_response_model=tc_models.Server,
    query_params={'fields': False},
    operation_id='getServerInfo',
)

# Get the latest backup status.
get_backup_status = HandlerInfo(
    method='GET',
    path='/app/rest/server/backup',
    success_response_model=str,
    operation_id='getBackupStatus',
)

# Start a new backup.
start_backup = HandlerInfo(
    method='POST',
    path='/app/rest/server/backup',
    success_response_model=str,
    query_params={'fileName': False, 'addTimestamp': False, 'includeConfigs': False, 'includeDatabase': False, 'includeBuildLogs': False, 'includePersonalChanges': False, 'includeRunningBuilds': False, 'includeSupplimentaryData': False},
    operation_id='startBackup',
)

# Get clean-up settings.
get_cleanup_settings = HandlerInfo(
    method='GET',
    path='/app/rest/server/cleanup',
    success_response_model=tc_models.Cleanup,
    operation_id='getCleanupSettings',
)

# Set clean-up settings.
set_cleanup_settings = HandlerInfo(
    method='PUT',
    path='/app/rest/server/cleanup',
    success_response_model=tc_models.Cleanup,
    request_model=tc_models.Cleanup,
    operation_id='setCleanupSettings',
)

# List all files.
get_files_list_of_server = HandlerInfo(
    method='GET',
    path='/app/rest/server/files/{areaId}',
    success_response_model=tc_models.Files,
    query_params={'basePath': False, 'locator': False, 'fields': False},
    path_params=['areaId'],
    operation_id='getFilesListOfServer',
)

# Get specific file zipped.
get_zipped_file_of_server = HandlerInfo(
    method='GET',
    path='/app/rest/server/files/{areaId}/archived{path}',
    success_response_model=None,
    query_params={'basePath': False, 'locator': False, 'name': False},
    path_params=['areaId', 'path'],
    operation_id='getZippedFileOfServer',
)

# Download specific file.
download_file_of_server = HandlerInfo(
    method='GET',
    path='/app/rest/server/files/{areaId}/files{path}',
    success_response_model=None,
    path_params=['areaId', 'path'],
    operation_id='downloadFileOfServer',
)

# Get metadata of specific file.
get_file_metadata_of_server = HandlerInfo(
    method='GET',
    path='/app/rest/server/files/{areaId}/metadata{path}',
    success_response_model=tc_models.File,
    query_params={'fields': False},
    path_params=['areaId', 'path'],
    operation_id='getFileMetadataOfServer',
)

# List files under this path.
get_files_list_for_subpath_of_server = HandlerInfo(
    method='GET',
    path='/app/rest/server/files/{areaId}/{path}',
    success_response_model=tc_models.Files,
    query_params={'basePath': False, 'locator': False, 'fields': False},
    path_params=['areaId', 'path'],
    operation_id='getFilesListForSubpathOfServer',
)

# Get the licensing data.
get_licensing_data = HandlerInfo(
    method='GET',
    path='/app/rest/server/licensingData',
    success_response_model=tc_models.LicensingData,
    query_params={'fields': False},
    operation_id='getLicensingData',
)

# Get all license keys.
get_license_keys = HandlerInfo(
    method='GET',
    path='/app/rest/server/licensingData/licenseKeys',
    success_response_model=tc_models.LicenseKeys,
    query_params={'fields': False},
    operation_id='getLicenseKeys',
)

# Add license keys.
add_license_keys = HandlerInfo(
    method='POST',
    path='/app/rest/server/licensingData/licenseKeys',
    success_response_model=tc_models.LicenseKeys,
    request_model=str,
    query_params={'fields': False},
    operation_id='addLicenseKeys',
)

# Get a license key.
get_license_key = HandlerInfo(
    method='GET',
    path='/app/rest/server/licensingData/licenseKeys/{licenseKey}',
    success_response_model=tc_models.LicenseKey,
    query_params={'fields': False},
    path_params=['licenseKey'],
    operation_id='getLicenseKey',
)

# Delete a license key.
delete_license_key = HandlerInfo(
    method='DELETE',
    path='/app/rest/server/licensingData/licenseKeys/{licenseKey}',
    success_response_model=None,
    path_params=['licenseKey'],
    operation_id='deleteLicenseKey',
)

# Get metrics.
get_all_metrics = HandlerInfo(
    method='GET',
    path='/app/rest/server/metrics',
    success_response_model=tc_models.Metrics,
    query_params={'fields': False},
    operation_id='getAllMetrics',
)

# Get all plugins.
get_all_plugins = HandlerInfo(
    method='GET',
    path='/app/rest/server/plugins',
    success_response_model=tc_models.Plugins,
    query_params={'fields': False, 'locator': False},
    operation_id='getAllPlugins',
)

# Get a field of the server info.
get_server_field = HandlerInfo(
    method='GET',
    path='/app/rest/server/{field}',
    success_response_model=str,
    path_params=['field'],
    operation_id='getServerField',
)


# ══════════ SERVER AUTHENTICATION SETTINGS ════════════════════

# Get authentication settings.
get_auth_settings = HandlerInfo(
    method='GET',
    path='/app/rest/server/authSettings',
    success_response_model=tc_models.ServerAuthSettings,
    operation_id='getAuthSettings',
)

# Set authentication settings.
set_auth_settings = HandlerInfo(
    method='PUT',
    path='/app/rest/server/authSettings',
    success_response_model=tc_models.ServerAuthSettings,
    request_model=tc_models.ServerAuthSettings,
    operation_id='setAuthSettings',
)


# ══════════ TEST ══════════════════════════════════════════════

# Get all tests.
get_tests = HandlerInfo(
    method='GET',
    path='/app/rest/tests',
    success_response_model=tc_models.Tests,
    query_params={'locator': False, 'fields': False},
    operation_id='getTests',
)

# Get a matching test.
get_test = HandlerInfo(
    method='GET',
    path='/app/rest/tests/{testLocator}',
    success_response_model=tc_models.Test,
    query_params={'fields': False},
    path_params=['testLocator'],
    operation_id='getTest',
)


# ══════════ TESTOCCURRENCE ════════════════════════════════════

# Get all test occurrences.
get_all_test_occurrences = HandlerInfo(
    method='GET',
    path='/app/rest/testOccurrences',
    success_response_model=tc_models.TestOccurrences,
    query_params={'locator': False, 'fields': False},
    operation_id='getAllTestOccurrences',
)

# Get a matching test occurrence.
get_test_occurrence = HandlerInfo(
    method='GET',
    path='/app/rest/testOccurrences/{testLocator}',
    success_response_model=tc_models.TestOccurrence,
    query_params={'fields': False},
    path_params=['testLocator'],
    operation_id='getTestOccurrence',
)


# ══════════ USER ══════════════════════════════════════════════

# Get all users.
get_all_users = HandlerInfo(
    method='GET',
    path='/app/rest/users',
    success_response_model=tc_models.Users,
    query_params={'locator': False, 'fields': False},
    operation_id='getAllUsers',
)

# Create a new user.
add_user = HandlerInfo(
    method='POST',
    path='/app/rest/users',
    success_response_model=tc_models.User,
    request_model=tc_models.User,
    query_params={'fields': False},
    operation_id='addUser',
)

# Get user matching the locator.
get_user = HandlerInfo(
    method='GET',
    path='/app/rest/users/{userLocator}',
    success_response_model=tc_models.User,
    query_params={'fields': False},
    path_params=['userLocator'],
    operation_id='getUser',
)

# Update user matching the locator.
replace_user = HandlerInfo(
    method='PUT',
    path='/app/rest/users/{userLocator}',
    success_response_model=tc_models.User,
    request_model=tc_models.User,
    query_params={'fields': False},
    path_params=['userLocator'],
    operation_id='replaceUser',
)

# Delete user matching the locator.
delete_user = HandlerInfo(
    method='DELETE',
    path='/app/rest/users/{userLocator}',
    success_response_model=None,
    path_params=['userLocator'],
    operation_id='deleteUser',
)

# Remove the RememberMe data of the matching user.
remove_user_remember_me = HandlerInfo(
    method='DELETE',
    path='/app/rest/users/{userLocator}/debug/rememberMe',
    success_response_model=None,
    path_params=['userLocator'],
    operation_id='removeUserRememberMe',
)

# Get all groups of the matching user.
get_all_user_groups = HandlerInfo(
    method='GET',
    path='/app/rest/users/{userLocator}/groups',
    success_response_model=tc_models.Groups,
    query_params={'fields': False},
    path_params=['userLocator'],
    operation_id='getAllUserGroups',
)

# Update groups of the matching user.
set_user_groups = HandlerInfo(
    method='PUT',
    path='/app/rest/users/{userLocator}/groups',
    success_response_model=tc_models.Groups,
    request_model=tc_models.Groups,
    query_params={'fields': False},
    path_params=['userLocator'],
    operation_id='setUserGroups',
)

# Get a user group of the matching user.
get_user_group = HandlerInfo(
    method='GET',
    path='/app/rest/users/{userLocator}/groups/{groupLocator}',
    success_response_model=tc_models.Group,
    query_params={'fields': False},
    path_params=['userLocator', 'groupLocator'],
    operation_id='getUserGroup',
)

# Remove the matching user from the specific group.
remove_user_from_group = HandlerInfo(
    method='DELETE',
    path='/app/rest/users/{userLocator}/groups/{groupLocator}',
    success_response_model=None,
    query_params={'fields': False},
    path_params=['userLocator', 'groupLocator'],
    operation_id='removeUserFromGroup',
)

# Terminate all current sessions of the matching user.
logout_user = HandlerInfo(
    method='POST',
    path='/app/rest/users/{userLocator}/logout',
    success_response_model=None,
    path_params=['userLocator'],
    operation_id='logoutUser',
)

# Get all permissions effective for the matching user.
get_user_permissions = HandlerInfo(
    method='GET',
    path='/app/rest/users/{userLocator}/permissions',
    success_response_model=tc_models.PermissionAssignments,
    query_params={'locator': False, 'fields': False},
    path_params=['userLocator'],
    operation_id='getUserPermissions',
)

# Get all properties of the matching user.
get_user_properties = HandlerInfo(
    method='GET',
    path='/app/rest/users/{userLocator}/properties',
    success_response_model=tc_models.Properties,
    query_params={'fields': False},
    path_params=['userLocator'],
    operation_id='getUserProperties',
)

# Get a property of the matching user.
get_user_property = HandlerInfo(
    method='GET',
    path='/app/rest/users/{userLocator}/properties/{name}',
    success_response_model=str,
    path_params=['userLocator', 'name'],
    operation_id='getUserProperty',
)

# Update a property of the matching user.
set_user_property = HandlerInfo(
    method='PUT',
    path='/app/rest/users/{userLocator}/properties/{name}',
    success_response_model=str,
    request_model=str,
    path_params=['userLocator', 'name'],
    operation_id='setUserProperty',
)

# Remove a property of the matching user.
remove_user_property = HandlerInfo(
    method='DELETE',
    path='/app/rest/users/{userLocator}/properties/{name}',
    success_response_model=None,
    path_params=['userLocator', 'name'],
    operation_id='removeUserProperty',
)

# Get all user roles of the matching user.
get_all_user_roles = HandlerInfo(
    method='GET',
    path='/app/rest/users/{userLocator}/roles',
    success_response_model=tc_models.RoleAssignments,
    path_params=['userLocator'],
    operation_id='getAllUserRoles',
)

# Add a role to the matching user.
add_role_to_user = HandlerInfo(
    method='POST',
    path='/app/rest/users/{userLocator}/roles',
    success_response_model=tc_models.RoleAssignment,
    request_model=tc_models.RoleAssignment,
    path_params=['userLocator'],
    operation_id='addRoleToUser',
)

# Update user roles of the matching user.
set_user_roles = HandlerInfo(
    method='PUT',
    path='/app/rest/users/{userLocator}/roles',
    success_response_model=tc_models.RoleAssignments,
    request_model=tc_models.RoleAssignments,
    path_params=['userLocator'],
    operation_id='setUserRoles',
)

# Get a user role with the specific scope from the matching user.
get_user_roles_at_scope = HandlerInfo(
    method='GET',
    path='/app/rest/users/{userLocator}/roles/{roleId}/{scope}',
    success_response_model=tc_models.RoleAssignment,
    path_params=['userLocator', 'roleId', 'scope'],
    operation_id='getUserRolesAtScope',
)

# Add a role with the specific scope to the matching user.
add_role_to_user_at_scope = HandlerInfo(
    method='PUT',
    path='/app/rest/users/{userLocator}/roles/{roleId}/{scope}',
    success_response_model=tc_models.RoleAssignment,
    path_params=['userLocator', 'roleId', 'scope'],
    operation_id='addRoleToUserAtScope',
)

# Remove a role with the specific scope from the matching user.
remove_user_role_at_scope = HandlerInfo(
    method='DELETE',
    path='/app/rest/users/{userLocator}/roles/{roleId}/{scope}',
    success_response_model=None,
    path_params=['userLocator', 'roleId', 'scope'],
    operation_id='removeUserRoleAtScope',
)

# Get all authentication tokens of the matching user.
get_user_tokens = HandlerInfo(
    method='GET',
    path='/app/rest/users/{userLocator}/tokens',
    success_response_model=tc_models.Tokens,
    query_params={'fields': False},
    path_params=['userLocator'],
    operation_id='getUserTokens',
)

# Create a new authentication token for the matching user.
add_user_token = HandlerInfo(
    method='POST',
    path='/app/rest/users/{userLocator}/tokens',
    success_response_model=tc_models.Token,
    request_model=tc_models.Token,
    query_params={'fields': False},
    path_params=['userLocator'],
    operation_id='addUserToken',
)

# Remove an authentication token from the matching user.
delete_user_token = HandlerInfo(
    method='DELETE',
    path='/app/rest/users/{userLocator}/tokens/{name}',
    success_response_model=None,
    path_params=['userLocator', 'name'],
    operation_id='deleteUserToken',
)

# Get a field of the matching user.
get_user_field = HandlerInfo(
    method='GET',
    path='/app/rest/users/{userLocator}/{field}',
    success_response_model=str,
    path_params=['userLocator', 'field'],
    operation_id='getUserField',
)

# Update a field of the matching user.
set_user_field = HandlerInfo(
    method='PUT',
    path='/app/rest/users/{userLocator}/{field}',
    success_response_model=str,
    request_model=str,
    path_params=['userLocator', 'field'],
    operation_id='setUserField',
)

# Remove a property of the matching user.
delete_user_field = HandlerInfo(
    method='DELETE',
    path='/app/rest/users/{userLocator}/{field}',
    success_response_model=None,
    path_params=['userLocator', 'field'],
    operation_id='deleteUserField',
)


# ══════════ VCSROOT ═══════════════════════════════════════════

# Get all VCS roots.
get_all_vcs_roots = HandlerInfo(
    method='GET',
    path='/app/rest/vcs-roots',
    success_response_model=tc_models.VcsRoots,
    query_params={'locator': False, 'fields': False},
    operation_id='getAllVcsRoots',
)

# Add a new VCS root.
add_vcs_root = HandlerInfo(
    method='POST',
    path='/app/rest/vcs-roots',
    success_response_model=tc_models.VcsRoot,
    request_model=tc_models.VcsRoot,
    query_params={'fields': False},
    operation_id='addVcsRoot',
)

# Get root endpoints.
get_root_endpoints = HandlerInfo(
    method='GET',
    path='/app/rest/vcs-roots/{vcsRootLocator}',
    success_response_model=tc_models.VcsRoot,
    query_params={'fields': False},
    path_params=['vcsRootLocator'],
    operation_id='getRootEndpoints',
)

# Remove VCS root matching the locator.
delete_vcs_root = HandlerInfo(
    method='DELETE',
    path='/app/rest/vcs-roots/{vcsRootLocator}',
    success_response_model=None,
    path_params=['vcsRootLocator'],
    operation_id='deleteVcsRoot',
)

# Get all VCS root instances of the matching VCS root.
get_vcs_root_instances = HandlerInfo(
    method='GET',
    path='/app/rest/vcs-roots/{vcsRootLocator}/instances',
    success_response_model=tc_models.VcsRootInstances,
    query_params={'fields': False},
    path_params=['vcsRootLocator'],
    operation_id='getVcsRootInstances',
)

# Get all properties of the matching VCS root.
get_all_vcs_root_properties = HandlerInfo(
    method='GET',
    path='/app/rest/vcs-roots/{vcsRootLocator}/properties',
    success_response_model=tc_models.Properties,
    query_params={'fields': False},
    path_params=['vcsRootLocator'],
    operation_id='getAllVcsRootProperties',
)

# Update all properties of the matching VCS root.
set_vcs_root_properties = HandlerInfo(
    method='PUT',
    path='/app/rest/vcs-roots/{vcsRootLocator}/properties',
    success_response_model=tc_models.Properties,
    request_model=tc_models.Properties,
    query_params={'fields': False},
    path_params=['vcsRootLocator'],
    operation_id='setVcsRootProperties',
)

# Delete all properties of the matching VCS root.
delete_all_vcs_root_properties = HandlerInfo(
    method='DELETE',
    path='/app/rest/vcs-roots/{vcsRootLocator}/properties',
    success_response_model=None,
    path_params=['vcsRootLocator'],
    operation_id='deleteAllVcsRootProperties',
)

# Get a property on the matching VCS root.
get_vcs_root_property = HandlerInfo(
    method='GET',
    path='/app/rest/vcs-roots/{vcsRootLocator}/properties/{name}',
    success_response_model=str,
    path_params=['vcsRootLocator', 'name'],
    operation_id='getVcsRootProperty',
)

# Update a property of the matching VCS root.
set_vcs_root_property = HandlerInfo(
    method='PUT',
    path='/app/rest/vcs-roots/{vcsRootLocator}/properties/{name}',
    success_response_model=str,
    request_model=str,
    path_params=['vcsRootLocator', 'name'],
    operation_id='setVcsRootProperty',
)

# Delete a property of the matching VCS root.
delete_vcs_root_property = HandlerInfo(
    method='DELETE',
    path='/app/rest/vcs-roots/{vcsRootLocator}/properties/{name}',
    success_response_model=None,
    path_params=['vcsRootLocator', 'name'],
    operation_id='deleteVcsRootProperty',
)

# Get the settings file of the matching VCS root.
get_vcs_root_settings_file = HandlerInfo(
    method='GET',
    path='/app/rest/vcs-roots/{vcsRootLocator}/settingsFile',
    success_response_model=str,
    path_params=['vcsRootLocator'],
    operation_id='getVcsRootSettingsFile',
)

# Get a field of the matching VCS root.
get_vcs_root_field = HandlerInfo(
    method='GET',
    path='/app/rest/vcs-roots/{vcsRootLocator}/{field}',
    success_response_model=str,
    path_params=['vcsRootLocator', 'field'],
    operation_id='getVcsRootField',
)

# Update a field of the matching VCS root.
set_vcs_root_field = HandlerInfo(
    method='PUT',
    path='/app/rest/vcs-roots/{vcsRootLocator}/{field}',
    success_response_model=str,
    request_model=str,
    path_params=['vcsRootLocator', 'field'],
    operation_id='setVcsRootField',
)


# ══════════ VCSROOTINSTANCE ═══════════════════════════════════

# Get all VCS root instances.
get_all_vcs_root_instances = HandlerInfo(
    method='GET',
    path='/app/rest/vcs-root-instances',
    success_response_model=tc_models.VcsRootInstances,
    query_params={'locator': False, 'fields': False},
    operation_id='getAllVcsRootInstances',
)

# Check for the pending changes for all VCS root instances.
request_pending_changes_check = HandlerInfo(
    method='POST',
    path='/app/rest/vcs-root-instances/checkingForChangesQueue',
    success_response_model=tc_models.VcsRootInstances,
    query_params={'locator': False, 'requestor': False, 'fields': False},
    operation_id='requestPendingChangesCheck',
)

# Send the commit hook notification.
trigger_commit_hook_notification = HandlerInfo(
    method='POST',
    path='/app/rest/vcs-root-instances/commitHookNotification',
    success_response_model=None,
    query_params={'locator': False, 'okOnNothingFound': False},
    operation_id='triggerCommitHookNotification',
)

# Get VCS root instance matching the locator.
get_vcs_root_instance = HandlerInfo(
    method='GET',
    path='/app/rest/vcs-root-instances/{vcsRootInstanceLocator}',
    success_response_model=tc_models.VcsRootInstance,
    query_params={'fields': False},
    path_params=['vcsRootInstanceLocator'],
    operation_id='getVcsRootInstance',
)

# List all files.
get_files_list = HandlerInfo(
    method='GET',
    path='/app/rest/vcs-root-instances/{vcsRootInstanceLocator}/files/latest',
    success_response_model=tc_models.Files,
    query_params={'basePath': False, 'locator': False, 'fields': False},
    path_params=['vcsRootInstanceLocator'],
    operation_id='getFilesList',
)

# Get specific file zipped.
get_zipped_file = HandlerInfo(
    method='GET',
    path='/app/rest/vcs-root-instances/{vcsRootInstanceLocator}/files/latest/archived{path}',
    success_response_model=None,
    query_params={'basePath': False, 'locator': False, 'name': False},
    path_params=['vcsRootInstanceLocator', 'path'],
    operation_id='getZippedFile',
)

# Download specific file.
download_file = HandlerInfo(
    method='GET',
    path='/app/rest/vcs-root-instances/{vcsRootInstanceLocator}/files/latest/files{path}',
    success_response_model=None,
    path_params=['vcsRootInstanceLocator', 'path'],
    operation_id='downloadFile',
)

# Get metadata of specific file.
get_file_metadata = HandlerInfo(
    method='GET',
    path='/app/rest/vcs-root-instances/{vcsRootInstanceLocator}/files/latest/metadata{path}',
    success_response_model=tc_models.File,
    query_params={'fields': False},
    path_params=['vcsRootInstanceLocator', 'path'],
    operation_id='getFileMetadata',
)

# List files under this path.
get_files_list_for_subpath = HandlerInfo(
    method='GET',
    path='/app/rest/vcs-root-instances/{vcsRootInstanceLocator}/files/latest/{path}',
    success_response_model=tc_models.Files,
    query_params={'basePath': False, 'locator': False, 'fields': False},
    path_params=['vcsRootInstanceLocator', 'path'],
    operation_id='getFilesListForSubpath',
)

# Get all properties of the matching VCS root instance.
get_vcs_root_instance_properties = HandlerInfo(
    method='GET',
    path='/app/rest/vcs-root-instances/{vcsRootInstanceLocator}/properties',
    success_response_model=tc_models.Properties,
    query_params={'fields': False},
    path_params=['vcsRootInstanceLocator'],
    operation_id='getVcsRootInstanceProperties',
)

# Get the repository state of the matching VCS root instance.
get_vcs_root_instance_repository_state = HandlerInfo(
    method='GET',
    path='/app/rest/vcs-root-instances/{vcsRootInstanceLocator}/repositoryState',
    success_response_model=tc_models.Entries,
    query_params={'fields': False},
    path_params=['vcsRootInstanceLocator'],
    operation_id='getVcsRootInstanceRepositoryState',
)

# Update the repository state of the matching VCS root instance.
set_vcs_root_instance_repository_state = HandlerInfo(
    method='PUT',
    path='/app/rest/vcs-root-instances/{vcsRootInstanceLocator}/repositoryState',
    success_response_model=tc_models.Entries,
    request_model=tc_models.Entries,
    query_params={'fields': False},
    path_params=['vcsRootInstanceLocator'],
    operation_id='setVcsRootInstanceRepositoryState',
)

# Delete the last repository state of the matching VCS root instance.
delete_vcs_root_instance_repository_state = HandlerInfo(
    method='DELETE',
    path='/app/rest/vcs-root-instances/{vcsRootInstanceLocator}/repositoryState',
    success_response_model=None,
    path_params=['vcsRootInstanceLocator'],
    operation_id='deleteVcsRootInstanceRepositoryState',
)

# Get the creation date of the matching VCS root instance.
get_vcs_root_instance_creation_date = HandlerInfo(
    method='GET',
    path='/app/rest/vcs-root-instances/{vcsRootInstanceLocator}/repositoryState/creationDate',
    success_response_model=str,
    path_params=['vcsRootInstanceLocator'],
    operation_id='getVcsRootInstanceCreationDate',
)

# Get a field of the matching VCS root instance.
get_vcs_root_instance_field = HandlerInfo(
    method='GET',
    path='/app/rest/vcs-root-instances/{vcsRootInstanceLocator}/{field}',
    success_response_model=str,
    path_params=['vcsRootInstanceLocator', 'field'],
    operation_id='getVcsRootInstanceField',
)

# Get a field of the matching VCS root instance.
set_vcs_root_instance_field = HandlerInfo(
    method='PUT',
    path='/app/rest/vcs-root-instances/{vcsRootInstanceLocator}/{field}',
    success_response_model=str,
    request_model=str,
    path_params=['vcsRootInstanceLocator', 'field'],
    operation_id='setVcsRootInstanceField',
)

# Remove a field of the matching VCS root instance.
delete_vcs_root_instance_field = HandlerInfo(
    method='DELETE',
    path='/app/rest/vcs-root-instances/{vcsRootInstanceLocator}/{field}',
    success_response_model=None,
    path_params=['vcsRootInstanceLocator', 'field'],
    operation_id='deleteVcsRootInstanceField',
)


# ══════════ VERSIONEDSETTINGS ═════════════════════════════════

# Get a list of projects that are affected by Load Settings from VCS action.
get_versioned_settings_projects_to_load = HandlerInfo(
    method='GET',
    path='/app/rest/projects/{locator}/versionedSettings/affectedProjects',
    success_response_model=tc_models.Projects,
    query_params={'fields': False},
    path_params=['locator'],
    operation_id='getVersionedSettingsProjectsToLoad',
)

# Check for changes in Versioned Settings.
check_for_versioned_settings_changes = HandlerInfo(
    method='POST',
    path='/app/rest/projects/{locator}/versionedSettings/checkForChanges',
    success_response_model=None,
    path_params=['locator'],
    operation_id='checkForVersionedSettingsChanges',
)

# Perform Versioned Settings action: Commit current settings to VCS.
commit_current_settings = HandlerInfo(
    method='POST',
    path='/app/rest/projects/{locator}/versionedSettings/commitCurrentSettings',
    success_response_model=None,
    path_params=['locator'],
    operation_id='commitCurrentSettings',
)

# Get Versioned Settings config.
get_versioned_settings_config = HandlerInfo(
    method='GET',
    path='/app/rest/projects/{locator}/versionedSettings/config',
    success_response_model=tc_models.VersionedSettingsConfig,
    query_params={'fields': False},
    path_params=['locator'],
    operation_id='getVersionedSettingsConfig',
)

# Set Verseioned Settings config.
set_versioned_settings_config = HandlerInfo(
    method='PUT',
    path='/app/rest/projects/{locator}/versionedSettings/config',
    success_response_model=tc_models.VersionedSettingsConfig,
    request_model=tc_models.VersionedSettingsConfig,
    query_params={'fields': False},
    path_params=['locator'],
    operation_id='setVersionedSettingsConfig',
)

# Get Versioned Settings config parameter value.
get_versioned_settings_config_parameter = HandlerInfo(
    method='GET',
    path='/app/rest/projects/{locator}/versionedSettings/config/parameters/{name}',
    success_response_model=str,
    path_params=['locator', 'name'],
    operation_id='getVersionedSettingsConfigParameter',
)

# Set Versioned Settings config parameter value.
set_versioned_settings_config_parameter = HandlerInfo(
    method='PUT',
    path='/app/rest/projects/{locator}/versionedSettings/config/parameters/{name}',
    success_response_model=str,
    request_model=str,
    path_params=['locator', 'name'],
    operation_id='setVersionedSettingsConfigParameter',
)

# Delete Versioned Settings config parameter value.
delete_versioned_settings_config_parameter = HandlerInfo(
    method='DELETE',
    path='/app/rest/projects/{locator}/versionedSettings/config/parameters/{name}',
    success_response_model=None,
    path_params=['locator', 'name'],
    operation_id='deleteVersionedSettingsConfigParameter',
)

# Get Versioned Settings Context Parameters.
get_versioned_settings_context_parameters = HandlerInfo(
    method='GET',
    path='/app/rest/projects/{locator}/versionedSettings/contextParameters',
    success_response_model=tc_models.VersionedSettingsContextParameters,
    path_params=['locator'],
    operation_id='getVersionedSettingsContextParameters',
)

# Set Versioned Settings Context Parameters.
set_versioned_settings_context_parameters = HandlerInfo(
    method='PUT',
    path='/app/rest/projects/{locator}/versionedSettings/contextParameters',
    success_response_model=tc_models.VersionedSettingsContextParameters,
    request_model=tc_models.VersionedSettingsContextParameters,
    path_params=['locator'],
    operation_id='setVersionedSettingsContextParameters',
)

# Perform Versioned Settings action: Load Setting from VCS.
load_settings_from_vcs = HandlerInfo(
    method='POST',
    path='/app/rest/projects/{locator}/versionedSettings/loadSettings',
    success_response_model=tc_models.Projects,
    query_params={'fields': False},
    path_params=['locator'],
    operation_id='loadSettingsFromVCS',
)

# Get current status of Versioned Settings.
get_versioned_settings_status = HandlerInfo(
    method='GET',
    path='/app/rest/projects/{locator}/versionedSettings/status',
    success_response_model=tc_models.VersionedSettingsStatus,
    query_params={'fields': False},
    path_params=['locator'],
    operation_id='getVersionedSettingsStatus',
)

# Get Versioned Settings Tokens.
get_versioned_settings_tokens = HandlerInfo(
    method='GET',
    path='/app/rest/projects/{locator}/versionedSettings/tokens',
    success_response_model=tc_models.VersionedSettingsTokens,
    query_params={'status': False},
    path_params=['locator'],
    operation_id='getVersionedSettingsTokens',
)

# Add Versioned Settings Tokens.
add_versioned_settings_tokens = HandlerInfo(
    method='POST',
    path='/app/rest/projects/{locator}/versionedSettings/tokens',
    success_response_model=tc_models.VersionedSettingsTokens,
    request_model=tc_models.VersionedSettingsTokens,
    path_params=['locator'],
    operation_id='addVersionedSettingsTokens',
)

# Delete Versioned Settings Tokens.
delete_versioned_settings_tokens = HandlerInfo(
    method='DELETE',
    path='/app/rest/projects/{locator}/versionedSettings/tokens',
    success_response_model=tc_models.VersionedSettingsTokens,
    request_model=tc_models.VersionedSettingsTokens,
    path_params=['locator'],
    operation_id='deleteVersionedSettingsTokens',
)


# ══════════ HEALTH ════════════════════════════════════════════

get_health_items = HandlerInfo(
    method='GET',
    path='/app/rest/health',
    success_response_model=tc_models.HealthStatusItems,
    query_params={'locator': False, 'fields': False},
    operation_id='getHealthItems',
)

get_categories = HandlerInfo(
    method='GET',
    path='/app/rest/health/category',
    success_response_model=tc_models.HealthCategories,
    query_params={'locator': False, 'fields': False},
    operation_id='getCategories',
)

get_single_category = HandlerInfo(
    method='GET',
    path='/app/rest/health/category/{locator}',
    success_response_model=tc_models.HealthCategory,
    query_params={'fields': False},
    path_params=['locator'],
    operation_id='getSingleCategory',
)

get_single_health_item = HandlerInfo(
    method='GET',
    path='/app/rest/health/{locator}',
    success_response_model=tc_models.HealthItem,
    query_params={'fields': False},
    path_params=['locator'],
    operation_id='getSingleHealthItem',
)