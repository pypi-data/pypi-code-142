"""Main configuration class for easy-aoc."""
from __future__ import annotations

import os

import attrs
import yarl

from easy_aoc import exceptions


@attrs.define(frozen=True)  # pylint: disable-next=too-few-public-methods
class Configuration:
    """Class with configuration for the easy-aoc tools."""

    session_key: str = attrs.field(repr=lambda key: "[hidden]")
    base_url: yarl.URL = attrs.field(default=yarl.URL("https://adventofcode.com"))

    @classmethod
    def from_environment(cls) -> Configuration:
        """Create a Configuration instance from environment variables.

        :return: An instance of Configuration
        """
        return cls(session_key=_get_from_env("AOC_SESSION"))


def _get_from_env(name: str) -> str:
    """Get a value from the environment by the variable name.

    :param name: The name of the variable
    :return: The value associated with the name
    :raises MissingEnvironmentVariable: if the variable isn't found
    """
    try:
        return os.environ[name]
    except KeyError as exc:  # pragma: nocover
        raise exceptions.MissingEnvironmentVariable(name=name) from exc
