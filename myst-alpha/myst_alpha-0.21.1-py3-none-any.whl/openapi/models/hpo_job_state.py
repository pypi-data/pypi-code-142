from enum import Enum


class HPOJobState(str, Enum):
    PENDING = "PENDING"
    LOADING_DATA = "LOADING_DATA"
    RUNNING = "RUNNING"
    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"

    def __str__(self) -> str:
        return str(self.value)
