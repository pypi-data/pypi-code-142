from typing import Protocol

from task_helper.model.project import Project


class ProjectRepositoryP(Protocol):
    def find(self, project_id: int) -> Project:
        ...

    def store(self, project: Project) -> None:
        ...
