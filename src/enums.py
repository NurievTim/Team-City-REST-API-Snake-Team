from enum import StrEnum


class BuildState(StrEnum):
    QUEUED = 'queued'
    FINISHED = 'finished'
    RUNNING = 'running'
    DELETED = 'deleted'
    UNKNOWN = 'unknown'


class Comment(StrEnum):
    CANCELING_QUEUED_BUILD = 'Canceling a queued build'
    CANCELING_RUNNING_BUILD = 'Canceling a running build'


class BuildStatus(StrEnum):
    NULL = 'null'           # for queued builds.
    SUCCESS = 'SUCCESS'     # for builds that have successfully finished or still running without errors.
    FAILURE = 'FAILURE'     # for builds that failed to start or failed during their run.
    UNKNOWN = 'UNKNOWN'     # for canceled builds.