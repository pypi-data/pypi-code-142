from .type import Task


class PivotalTask(Task):
    def __init__(
        self, id: str, title: str, type: str, project_id: str
    ) -> None:
        self.id = id
        self.title = title
        self.type = type
        self.project_id = project_id
