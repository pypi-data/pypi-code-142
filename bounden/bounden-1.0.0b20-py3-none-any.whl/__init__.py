"""
&copy; 2022 Cariad Eccleston and released under the MIT License.

For usage and support, see https://github.com/cariad/bounden.
"""

from importlib.resources import files

from bounden.axes import (
    AxesT,
    Axis,
    AxisOperation,
    FloatAxis,
    IntegerAxis,
    NoAxisForType,
    StringAxis,
    XAxisT,
    YAxisT,
    get_axis,
    register_axis,
)
from bounden.enums import Alignment
from bounden.points import Point, Point2
from bounden.region import Region, RegionT, ResolvedRegion, ResolvedRegionT
from bounden.region2 import Region2, Region2T, ResolvedRegion2
from bounden.resolved import ResolvedPoint, ResolvedVolume
from bounden.volume2 import (
    ResolvedVolume2,
    ResolvedVolume2T,
    Volume2,
    Volume2T,
)
from bounden.volumes import Percent, Volume, VolumeT


def version() -> str:
    """
    Gets the package's version.
    """

    with files(__package__).joinpath("VERSION").open("r") as t:
        return t.readline().strip()


__all__ = [
    "Alignment",
    "Axis",
    "AxisOperation",
    "AxesT",
    "IntegerAxis",
    "FloatAxis",
    "NoAxisForType",
    "Percent",
    "Point",
    "Point2",
    "Region",
    "Region2",
    "Region2T",
    "RegionT",
    "ResolvedPoint",
    "ResolvedRegion",
    "ResolvedRegion2",
    "ResolvedRegionT",
    "ResolvedVolume",
    "ResolvedVolume2",
    "ResolvedVolume2T",
    "StringAxis",
    "Volume",
    "Volume2",
    "Volume2T",
    "VolumeT",
    "XAxisT",
    "YAxisT",
    "get_axis",
    "register_axis",
    "version",
]
