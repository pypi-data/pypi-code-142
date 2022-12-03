#!/usr/bin/env python3

# Standard libraries
from argparse import Namespace
from enum import Enum
from typing import List

# Components
from .docker import Docker
from .podman import Podman

# Backend enumeration
class Backend(Enum):
    DOCKER = 1
    PODMAN = 2
    UNKNOWN = 3

# Names enumeration, pylint: disable=too-few-public-methods
class Names:

    # Constants
    AUTO: str = 'auto'
    DOCKER: str = 'docker'
    PODMAN: str = 'podman'

    # Defaults
    DEFAULTS: List[str] = [
        PODMAN,
        DOCKER,
    ]

    # Getter
    @staticmethod
    def get(override: str) -> List[str]:

        # Adapt override
        override = override.lower() if override else ''

        # Handle engine overrides
        if override:
            auto: bool = False
            names: List[str] = []
            overrides: List[str] = override.split(',')
            for item in overrides:
                if item:
                    if Names.AUTO == item:
                        auto = True
                    else:
                        names += [name for name in Names.DEFAULTS if name == item]
            if auto or override[-1] == ',':
                names = names + Names.DEFAULTS
            names = list(dict.fromkeys(names))

        # Use engine defaults
        else:
            names = Names.DEFAULTS

        # Result
        return names

# Supported engines
def supported() -> List[str]:
    return [Names.AUTO] + Names.DEFAULTS

# Engine class
class Engine:

    # Members
    __engine = None
    __name: str = ''

    # Constructor
    def __init__(self, options: Namespace) -> None:

        # Acquire engine names
        names: List[str] = Names.get(options.engine)

        # Iterate through names
        for name in names:

            # Detect Docker engine
            if name == Names.DOCKER:
                try:
                    self.__engine = Docker()
                    self.__name = Names.DOCKER
                    break
                except (KeyboardInterrupt, ModuleNotFoundError):
                    self.__engine = None

            # Detect Podman engine
            elif name == Names.PODMAN:
                try:
                    self.__engine = Podman()
                    self.__name = Names.PODMAN
                    break
                except (KeyboardInterrupt, ModuleNotFoundError):
                    self.__engine = None

        # Unknown engine fallback
        if not self.__engine:
            raise NotImplementedError('Unknown or unsupported container engine...')

    # Command exec
    def cmd_exec(self) -> str:
        return self.__engine.cmd_exec()

    # Container
    @property
    def container(self) -> str:
        return self.__engine.container

    # Exec
    def exec(self, command): # pragma: no cover
        return self.__engine.exec(command)

    # Get
    def get(self, image: str) -> None:
        self.__engine.get(image)

    # Logs
    def logs(self):
        return self.__engine.logs()

    # Name
    @property
    def name(self) -> str:
        return self.__name

    # Pull
    def pull(self, image: str, force: bool = False) -> None:
        self.__engine.pull(image, force=force)

    # Remove
    def remove(self) -> None:
        self.__engine.remove()

    # Remove image
    def rmi(self, image: str) -> None:
        self.__engine.rmi(image)

    # Run, pylint: disable=too-many-arguments
    def run(self, image: str, command, entrypoint: str, variables, network: str,
            option_sockets: bool, services: bool, volumes, directory: str,
            temp_folder: str):
        return self.__engine.run(
            image=image,
            command=command,
            entrypoint=entrypoint,
            variables=variables,
            network=network,
            option_sockets=option_sockets,
            services=services,
            volumes=volumes,
            directory=directory,
            temp_folder=temp_folder,
        )

    # Stop
    def stop(self, timeout: int) -> None:
        self.__engine.stop(timeout)

    # Supports
    def supports(self, binary: str) -> bool:
        return self.__engine.supports(binary)

    # Wait
    def wait(self) -> bool:
        return self.__engine.wait()
