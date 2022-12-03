import re

from task_helper.model.task.type import Task
from task_helper.repository.project_repository.type import ProjectRepositoryP
from task_helper.repository.task_repository.type import TaskRepository
from task_helper.repository.vcs_repository.type import VCSRepository


class PivotalVCSService:
    _BRANCH_NAME_FORMAT = "{project_name}/{task_type}/{task_id}-{task_title}"

    def __init__(
        self,
        vcs_repo: VCSRepository,
        task_repo: TaskRepository,
        project_repo: ProjectRepositoryP,
    ) -> None:
        self._vcs_repo = vcs_repo
        self._task_repo = task_repo
        self._project_repo = project_repo

    def make_branch(self, task_id: int) -> None:
        task = self._task_repo.get(task_id)
        project_name = self._project_repo.find(task.project_id).name

        self._vcs_repo.create_branch(
            self._format_branch_name(task, project_name)
        )

    def _format_branch_name(self, task: Task, project_name: str) -> str:
        return self._sanitize_branch_name(
            self._BRANCH_NAME_FORMAT.format(
                project_name=project_name,
                task_type=task.type,
                task_id=task.id,
                task_title=task.title,
            )
        )

    def _sanitize_branch_name(self, string: str) -> str:
        """Make a valid branch name

        Args:
            string (str): _description_

        Returns:
            str: Valid branch name
        """
        string = string.lower()
        string = re.sub(r"[\[\]\'\"]", "", string)
        string = re.sub(r"\s+|:+|_+|=+", "-", string)

        return string
