from src.steps.build_steps import BuildSteps
from src.steps.project_steps import ProjectSteps


class ApiManager:
    def __init__(self, created_objects: list):
        self.build_steps = BuildSteps(created_objects)
        self.project_steps = ProjectSteps(created_objects)