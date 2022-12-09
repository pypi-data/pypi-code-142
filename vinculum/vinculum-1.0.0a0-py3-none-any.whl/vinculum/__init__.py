"""
&copy; 2022 Cariad Eccleston and released under the MIT License.
"""

from importlib.resources import files


def version() -> str:
    """
    Gets the package's version.
    """

    with files(__package__).joinpath("VERSION").open("r") as t:
        return t.readline().strip()


__all__ = [
    "version",
]
