#!/usr/bin/env python3

# Standard libraries
from os.path import expanduser
from pathlib import Path, PurePosixPath
from typing import Union

# Components
from ..system.platform import Platform
from .environment import Environment

# Paths class
class Paths:

    # Basename
    @staticmethod
    def basename(data: str) -> str:

        # POSIX path
        path = PurePosixPath(data)

        # Result
        return str(path.name)

    # Expand
    @staticmethod
    def expand(path: str, env: bool = True, home: bool = True) -> str:

        # Expand environment
        if env:
            path = Environment.expand(path)

        # Expand home
        if home:
            path = expanduser(path)

        # Result
        return path

    # Getter
    @staticmethod
    def get(data: Union[PurePosixPath, str]) -> str:

        # POSIX path
        path = PurePosixPath(data)

        # Result
        return str(path)

    # Home
    @staticmethod
    def home(user: str) -> str:

        # Expand home
        path: str = expanduser(f'~{user}')
        if path[0:1] != '~':
            return path

        # Default root
        if user == 'root': # pragma: no cover
            return '/root'

        # Default user
        return f'/home/{user}'

    # Resolver
    @staticmethod
    def resolve(data: Union[Path, str]) -> str:

        # Resolve path
        path = str(Path(data).resolve())

        # Linux, macOS or Windows path
        if Platform.IS_LINUX or Platform.IS_MAC_OS or Platform.IS_WINDOWS:
            path = str(path)

        # Result
        return path

    # Translator
    @staticmethod
    def translate(data: str) -> str:

        # Double backslash translation
        if data[0:1] == '\\': # pragma: no cover
            data = f'/{data[1:]}'

        # Double slash translation
        if data[0:2] == '//': # pragma: no cover
            data = data[1:]

        # Result
        return data
