import requests

from task_helper.custom_logging import logger
from task_helper.model.task.pivotal_task import PivotalTask
from task_helper.repository.task_repository.errors import TaskNotFound
from task_helper.repository.task_repository.type import TaskRepository


class PivotalTaskRepository(TaskRepository):
    def __init__(self, project_id: str, token: str) -> None:
        self._project_id = project_id
        self._token = token

    def get(self, task_id: str) -> PivotalTask:
        logger.info(
            f"Getting story with id {task_id} from project {self._project_id}"
        )
        url = f"https://www.pivotaltracker.com/services/v5/projects/{self._project_id}/stories/{task_id}"
        story_res = requests.get(url, headers={"X-TrackerToken": self._token})

        if story_res.status_code != 200:
            raise TaskNotFound(story_res.text)

        story_json = story_res.json()

        return PivotalTask(
            id=story_json["id"],
            title=story_json["name"],
            type=story_json["story_type"],
            project_id=story_json["project_id"],
        )
