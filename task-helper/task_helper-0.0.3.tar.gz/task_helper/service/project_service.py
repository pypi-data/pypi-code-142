from task_helper.model.project import Project
from task_helper.repository.project_repository.type import ProjectRepositoryP


class ProjectService:
    def __init__(self, repo: ProjectRepositoryP):
        self._repo = repo

    def register(self, project_id: int, name: str):
        project = Project(project_id, name)

        self._repo.store(project)
