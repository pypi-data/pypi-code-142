from dataclasses import dataclass
from typing import Generic

from bounden.axes import AxesT
from bounden.resolution.types import GetResolvedPoint, GetResolvedVolume


@dataclass
class RegionResolver(Generic[AxesT]):
    """
    Set of functions that fully resolve a region.
    """

    position: GetResolvedPoint[AxesT]
    """
    Function that resolves the region's position.
    """

    volume: GetResolvedVolume
    """
    Function that resolves the region's volume.
    """
