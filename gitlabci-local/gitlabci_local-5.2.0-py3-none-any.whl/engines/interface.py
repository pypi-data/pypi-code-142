#!/usr/bin/env python3

# Standard libraries
from abc import ABC, abstractmethod

# Interface class
class Interface(ABC): # pragma: no cover

    # Command exec
    @abstractmethod
    def cmd_exec(self) -> str:
        pass

    # Container
    @property
    @abstractmethod
    def container(self) -> str:
        pass

    # Exec
    @abstractmethod
    def exec(self, command):
        pass

    # Get
    @abstractmethod
    def get(self, image):
        pass

    # Logs
    @abstractmethod
    def logs(self):
        pass

    # Pull
    @abstractmethod
    def pull(self, image, force=False) -> None:
        pass

    # Remove
    @abstractmethod
    def remove(self) -> None:
        pass

    # Remove image
    @abstractmethod
    def rmi(self, image) -> None:
        pass

    # Run, pylint: disable=too-many-arguments
    @abstractmethod
    def run(self, image, command, entrypoint, variables, network, option_sockets,
            services, volumes, directory, temp_folder):
        pass

    # Stop
    @abstractmethod
    def stop(self, timeout) -> None:
        pass

    # Supports
    @abstractmethod
    def supports(self, binary) -> bool:
        pass

    # Wait
    @abstractmethod
    def wait(self) -> bool:
        pass
