import git

from task_helper.repository.vcs_repository.type import VCSRepository


class GitVCSRepository(VCSRepository):
    def __init__(self, repo_path: str) -> None:
        self._repo = git.Repo(repo_path)

    def create_branch(self, branch_name: str) -> None:
        self._repo.git.checkout("-b", branch_name)
