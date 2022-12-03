from typing import Protocol


class VCSRepository(Protocol):
    def create_branch(self, branch_name: str) -> str:
        ...
