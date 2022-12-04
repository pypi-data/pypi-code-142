from __future__ import annotations

from typing import Any, Optional, Sequence, Type, TypeVar, cast

from bounden.axes import Axis, XAxisT, YAxisT
from bounden.enums import Alignment
from bounden.points import Point2
from bounden.region import Region, ResolvedRegion
from bounden.resolution import RegionResolver
from bounden.volumes import Percent


class Region2(Region[tuple[XAxisT, YAxisT]]):
    """
    A region of two-dimensional space.
    """

    @classmethod
    def new(
        cls: Type["Region2T"],
        x: Alignment | XAxisT,
        y: Alignment | YAxisT,
        width: float | int | Percent,
        height: float | int | Percent,
        axes: Optional[Sequence[Axis[Any]]] = None,
        within: Optional[RegionResolver] = None,
    ) -> "Region2T":
        """
        Creates a new `Region2`.
        """

        return cls(
            (x, y),
            (width, height),
            axes=axes,
            within=within,
        )

    @property
    def height(self) -> float | int | Percent:
        """
        Height.
        """

        return self.volume[1]

    @property
    def left(self) -> Alignment | XAxisT:
        """
        Left.
        """

        return self.x

    def point2(
        self,
        x: Alignment | XAxisT,
        y: Alignment | YAxisT,
    ) -> Point2[XAxisT, YAxisT]:
        """
        Creates a child point.
        """

        return Point2.new(
            x,
            y,
            axes=self._axes,
            origin_of=None,
            within=self._resolver,
        )

    def region2(
        self: "Region2T",
        x: Alignment | XAxisT,
        y: Alignment | YAxisT,
        width: float | int | Percent,
        height: float | int | Percent,
    ) -> "Region2T":
        """
        Creates a child region.
        """

        return self.__class__.new(
            x,
            y,
            width,
            height,
            axes=self._axes,
            within=self._resolver,
        )

    def resolve(self) -> ResolvedRegion2[XAxisT, YAxisT]:
        """
        Resolves the region.
        """

        return ResolvedRegion2(
            self._axes,
            self._position.resolve(),
            self._volume.resolve(),
        )

    @property
    def top(self) -> Alignment | YAxisT:
        """
        Top.
        """

        return self.y

    @property
    def width(self) -> float | int | Percent:
        """
        Width.
        """

        return self.volume[0]

    @property
    def x(self) -> Alignment | XAxisT:
        """
        X coordinate.
        """

        return self.position.coordinates[0]

    @property
    def y(self) -> Alignment | YAxisT:
        """
        Y coordinate.
        """

        return self.position.coordinates[1]


class ResolvedRegion2(ResolvedRegion[tuple[XAxisT, YAxisT]]):
    """
    A resolved region of two-dimensional space.
    """

    @property
    def bottom(self) -> YAxisT:
        """
        Bottom.
        """

        return self.y_axis.add(self.top, self.height)

    @property
    def height(self) -> float | int:
        """
        Height.
        """

        return self._volume[1]

    @property
    def left(self) -> XAxisT:
        """
        Left.
        """

        return self.x

    def region2(
        self,
        x: Alignment | XAxisT,
        y: Alignment | YAxisT,
        width: float | int | Percent,
        height: float | int | Percent,
    ) -> Region2[XAxisT, YAxisT]:
        """
        Creates and returns a new two-dimensional subregion.
        """

        return Region2.new(
            x,
            y,
            width,
            height,
            self._axes,
            within=RegionResolver(self._position, self._volume),
        )

    @property
    def right(self) -> XAxisT:
        """
        Right.
        """

        return self.x_axis.add(self.left, self.width)

    @property
    def top(self) -> YAxisT:
        """
        Top.
        """

        return self.y

    @property
    def width(self) -> float | int:
        """
        Width.
        """

        return self._volume[0]

    @property
    def x(self) -> XAxisT:
        """
        X coordinate.
        """

        return self._position.coordinates[0]

    @property
    def x_axis(self) -> Axis[XAxisT]:
        """
        X axis.
        """

        return cast(Axis[XAxisT], self._axes[0])

    @property
    def y(self) -> YAxisT:
        """
        Y coordinate.
        """

        return self._position.coordinates[1]

    @property
    def y_axis(self) -> Axis[YAxisT]:
        """
        Y axis.
        """

        return cast(Axis[YAxisT], self._axes[1])


Region2T = TypeVar("Region2T", bound=Region2[Any, Any])
