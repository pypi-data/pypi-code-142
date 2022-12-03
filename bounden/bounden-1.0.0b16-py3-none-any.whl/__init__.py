"""
&copy; 2022 Cariad Eccleston and released under the MIT License.

For usage and support, see https://github.com/cariad/bounden.
"""

from importlib.resources import files

from bounden.axes import (
    AxisOperation,
    IntegerAxis,
    NoAxisForType,
    StringAxis,
    get_axis,
    register_axis,
)
from bounden.enums import Alignment
from bounden.points import Point, Point2
from bounden.regions import Region, Region2
from bounden.resolved import (
    ResolvedPoint,
    ResolvedRegion,
    ResolvedRegion2,
    ResolvedVolume,
)
from bounden.volumes import Percent, Volume, Volume2


def version() -> str:
    """
    Gets the package's version.
    """

    with files(__package__).joinpath("VERSION").open("r") as t:
        return t.readline().strip()


__all__ = [
    "Alignment",
    "AxisOperation",
    "IntegerAxis",
    "NoAxisForType",
    "Percent",
    "Point",
    "Point2",
    "Region",
    "Region2",
    "ResolvedPoint",
    "ResolvedRegion",
    "ResolvedRegion2",
    "ResolvedVolume",
    "StringAxis",
    "Volume",
    "Volume2",
    "get_axis",
    "register_axis",
    "version",
]
