from typing import Protocol


class Task(Protocol):
    id: str
    type: str
    title: str
    project_id: str
