from typing import Any, Generic, Optional, Sequence, TypeVar

from bounden.axes import AxesT, Axis, get_axis
from bounden.points import Point
from bounden.resolution import RegionResolver
from bounden.resolved import ResolvedRegion
from bounden.volumes import Percent, Volume


class Region(Generic[AxesT]):
    """
    A region of n-dimensional space.
    """

    def __init__(
        self,
        coordinates: AxesT,
        volume: Sequence[float | int | Percent],
        axes: Optional[tuple[Axis[Any], ...]] = None,
        within: Optional[RegionResolver[AxesT]] = None,
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


RegionT = TypeVar("RegionT", bound=Region[Any])
