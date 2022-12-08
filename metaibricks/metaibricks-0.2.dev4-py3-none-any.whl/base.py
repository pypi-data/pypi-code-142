from __future__ import annotations

import os
import abc
import json
from typing import Optional

from pydantic import BaseModel, Field


class TaskBase(BaseModel, abc.ABC):
    """Abstract class for defining a task

    Args:
        kind (str): Task's kind

    Method:
        run (None -> bool): Runs the task and returns the execution status.
    """

    kind: str
    name: Optional[str] = None

    class Config:
        underscore_attrs_are_private = True

    @abc.abstractmethod
    def run(self) -> bool:
        """Abstract extraction method used by the extractor.

        Returns:
            bool: Whether the extraction is alright or not.
        """
        pass

    @classmethod
    def load(cls, filename: str) -> TaskBase:
        """Class method for loading a JSON configuration file as a cls object.

        Args:
            filename (str): JSON configuration file's name.

        Returns:
            TaskBase: cls object
        """
        with open(filename, "r") as fp:
            config = json.load(fp)
        return cls(**config)

    def dump(self, filename: str, **kwargs) -> bool:
        """Method for dumping an object to a JSON file.

        Args:
            filename (str): JSON file's name.

        Returns:
            bool: Whether the file has correctly been created or not.
        """
        with open(filename, "w") as fp:
            json.dump(json.loads(self.json()), fp, **kwargs)
        return os.path.isfile(filename)

    @property
    def desc(self) -> str:
        """Description property."""
        return f"{self.kind}(name={self.name})"


class ParallelTaskBase(TaskBase):
    """Abstract class for difining a task with a multiprocessing execution.

    Inherits:
        TaskBase

    Args:
        n_workers (Optional[int]): Numbers of workers to use to parallelize the
            extraction.
    """

    n_workers: int = Field(1, gt=0, lt=os.cpu_count() + 1)
