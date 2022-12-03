from typing import Any, Optional, Type, TypeVar

from bounden.axes import Axis, XAxisT, YAxisT
from bounden.enums import Alignment
from bounden.points import Point2
from bounden.regions import Region
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
        axes: Optional[tuple[Axis[Any], ...]] = None,
        within: Optional[RegionResolver[tuple[XAxisT, YAxisT]]] = None,
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


Region2T = TypeVar("Region2T", bound=Region2[Any, Any])
