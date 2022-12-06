from abc import ABC, abstractmethod
from typing import Optional

from . import exceptions
from .comms import BaseCommunication


class BaseSmartContract(ABC):
    def __init__(self, comm: Optional[BaseCommunication] = None) -> None:
        self.comm = comm

    @abstractmethod
    def compile(self):
        raise NotImplementedError("Need to implement for each chain.")

    @abstractmethod
    def run_test(self):
        raise NotImplementedError("Need to implement for each chain.")

    @abstractmethod
    def publish(self):
        if self.comm is None:
            raise exceptions.CommunicationError(
                "The communication object is not assgined"
            )

        raise NotImplementedError("Need to implement for each chain.")
