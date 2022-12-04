from __future__ import annotations

from typing import Any, Generic, Optional, Sequence, TypeVar

from bounden.axes import AxesT, Axis, get_axis
from bounden.points import Point
from bounden.resolution import RegionResolver
from bounden.resolved.resolved_point import ResolvedPoint
from bounden.resolved.resolved_volume import ResolvedVolume
from bounden.volumes import Percent, Volume


class Region(Generic[AxesT]):
    """
    A region of n-dimensional space.
    """

    def __init__(
        self,
        coordinates: AxesT,
        volume: Sequence[float | int | Percent],
        axes: Optional[Sequence[Axis[Any]]] = None,
        within: Optional[RegionResolver] = None,
    ) -> None:
        if len(coordinates) != len(volume):
            raise ValueError(
                f"Coordinates count ({len(coordinates)}) "
                f"!= lengths count ({len(volume)})"
            )

        self._axes = axes or tuple(get_axis(c) for c in coordinates)

        self._volume = Volume(
            *volume,
            within=within.volume if within else None,
        )

        self._position = Point[AxesT](
            coordinates,
            axes=self._axes,
            within=within,
            origin_of=self._volume.resolve,
        )

        self._resolver = RegionResolver(
            self._position.resolve,
            self._volume.resolve,
        )

        self._within = within

    def __add__(self: "RegionT", other: Any) -> "RegionT":
        return self.__class__(
            tuple(self._position + other),
            tuple(self._volume),
            axes=self._axes,
            within=self._within,
        )

    def __eq__(self, other: Any) -> bool:
        return (
            isinstance(other, Region)
            and self.position == other.position
            and self.volume == other.volume
        )

    def __repr__(self) -> str:
        return f"{self._position} x {self._volume}"

    def point(self, coordinates: Any) -> Point[AxesT]:
        """
        Creates a child point.
        """

        return Point(
            coordinates,
            axes=self._axes,
            within=self._resolver,
        )

    @property
    def position(self) -> Point[AxesT]:
        """
        Position.
        """

        return self._position

    def resolve(self) -> ResolvedRegion[AxesT]:
        """
        Resolves the region.
        """

        return ResolvedRegion(
            self._axes,
            self._position.resolve(),
            self._volume.resolve(),
        )

    def region(
        self: "RegionT",
        coordinates: Sequence[Any],
        volume: Sequence[float | int | Percent],
    ) -> "RegionT":
        """
        Creates a child region.
        """

        return self.__class__(
            coordinates,
            volume,
            axes=self._axes,
            within=self._resolver,
        )

    @property
    def volume(self) -> Volume:
        """
        Volume.
        """

        return self._volume


class ResolvedRegion(Generic[AxesT]):
    """
    A resolved region of n-dimensional space.
    """

    def __init__(
        self,
        axes: Sequence[Axis[Any]],
        position: ResolvedPoint[AxesT],
        volume: ResolvedVolume,
    ) -> None:
        self._axes = axes
        self._position = position
        self._volume = volume

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, ResolvedRegion):
            return (
                self.position == other.position and self.volume == other.volume
            )

        if isinstance(other, (list, tuple)):
            return bool(
                len(other) == 2
                and self._position == other[0]
                and self._volume == other[1]
            )

        return False

    def __add__(self: "ResolvedRegionT", other: Any) -> "ResolvedRegionT":
        return self.__class__(self._axes, self._position + other, self._volume)

    def __repr__(self) -> str:
        return f"{self._position} x {self._volume}"

    def expand(
        self: "ResolvedRegionT",
        length: float | int,
    ) -> "ResolvedRegionT":
        """
        Returns a new resolved region expanded by `length` about its centre.

        Pass a negative length to contract.
        """

        coords = self._position - (length / 2)
        position = self._position.__class__(self._axes, coords)

        lengths = [vl + length for vl in self._volume]
        volume = self._volume.__class__(*lengths)

        return self.__class__(self._axes, position, volume)

    @property
    def position(self) -> ResolvedPoint[AxesT]:
        """
        Position.
        """

        return self._position

    def region(
        self,
        coordinates: AxesT,
        volume: Sequence[float | int | Percent],
    ) -> Region[AxesT]:
        """
        Creates and returns a new subregion.
        """

        return Region(
            coordinates,
            volume,
            self._axes,
            within=RegionResolver(self._position, self._volume),
        )

    @property
    def volume(self) -> ResolvedVolume:
        """
        Volume.
        """

        return self._volume


RegionT = TypeVar("RegionT", bound=Region[Any])
ResolvedRegionT = TypeVar("ResolvedRegionT", bound=ResolvedRegion[Any])
