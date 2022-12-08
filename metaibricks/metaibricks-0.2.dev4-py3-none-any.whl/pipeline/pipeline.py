from typing import List, Union

from pydantic import Field

from metaibricks.base import TaskBase
from metaibricks.settings import Logger
from metaibricks.extraction import FTPFiles, FTPDir, HTTPFiles, HTTPDir

LOGGER = Logger(name="pipeline.base")

Tasks = Union[HTTPFiles, HTTPDir, FTPFiles, FTPDir, TaskBase]


class Pipeline(TaskBase):
    """Class for gathering and running sequentially tasks

    Attrs:
        tasks (List[Tasks]): List of tasks to launch sequentially
    """

    kind: str = Field("Pipeline", const=True)
    tasks: List[Tasks]

    def run(self) -> bool:
        """Runs all the tasks one after after the other.

        Returns:
            bool: Whether the tasks have run correctly
        """
        LOGGER.info(f"Launching {self.desc}")

        for task in self.tasks:
            LOGGER.info(f"Launching Task {task.desc}")
            status = task.run()
            if not status:
                LOGGER.error(f"Task {task.desc} failed !. Ending pipeline.")
                return False
            LOGGER.info(f"Task {task.desc} done.")

        LOGGER.info(f"{self.desc} done.")
        return True
