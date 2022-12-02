# -*- coding: utf-8 -*-
import uuid as uuid
from datetime import datetime

from pydantic import BaseModel, UUID4, Field
from typing import Mapping, Optional, Any, Union


class TaskDecodeError(ValueError):
    """
    Received message cannot be decoded into task.
    """

    def __init__(self, payload: bytes, meta: Mapping, exc: Exception, handled: bool):
        """
        :param payload: Received payload
        :param meta:    Received meta
        :param exc:     Raised exception
        :param handled: True if exception has been handled by client and this is just a notification exception,
                        handled means that task is not lost on the queue. If False, this case is not handled
                        and worker should take care of logging and administrator notification in the same
                        way as other task processing messages are handled.
        """
        self.payload = payload
        self.meta = meta
        self.exception = exc
        self.is_handled = handled

    def __str__(self):
        return ("Handled" if self.is_handled else "Unhandled") + f" {self.__class__.__name__}({self.exception})"


class TaskMetadata(BaseModel):
    not_before: Optional[datetime]
    expires: Optional[datetime]
    max_retries: Optional[int]
    attempt: int = 0
    scheduled: Optional[datetime]
    received: Optional[datetime]
    queue_name: Optional[str]
    extra: Optional[Mapping[str, Union[int, float, bool, str, None]]]


class Task(BaseModel):
    uuid: UUID4 = Field(default_factory=uuid.uuid4)
    meta: TaskMetadata = TaskMetadata()
    task_type: str
    correlation_id: Optional[str]
    payload: Any
