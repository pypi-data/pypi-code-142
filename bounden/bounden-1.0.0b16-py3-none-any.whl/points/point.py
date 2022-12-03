from typing import (
    Any,
    Generic,
    Iterator,
    List,
    Optional,
    Sequence,
    TypeVar,
    cast,
)

from bounden.axes import AxesT, Axis, AxisOperation, get_axis
from bounden.enums import Alignment
from bounden.log import log
from bounden.resolution import GetResolvedVolume, RegionResolver
from bounden.resolved import ResolvedPoint


class Point(Generic[AxesT]):
    """
    A point in n-dimensional space.
    """

    def __init__(
        self,
        coordinates: AxesT,
        axes: Optional[tuple[Axis[Any], ...]] = None,
        origin_of: Optional[GetResolvedVolume] = None,
        within: Optional[RegionResolver[AxesT]] = None,
    ) -> None:
        self._axes = axes or tuple(get_axis(c) for c in coordinates)
        self._coordinates = coordinates
        self._origin_of = origin_of
        self._within = within

    def __add__(self: "PointT", other: Any) -> "PointT":
        return self._operate(other, AxisOperation.Add)

    def __eq__(self, other: Any) -> bool:
        return list(self) == list(other)

    def __iter__(self) -> Iterator[Any]:
        return iter(self.coordinates)

    def __len__(self) -> int:
        return len(self._coordinates)

    def __repr__(self) -> str:
        return str(self._coordinates)

    def __sub__(self, other: Any) -> "Point[AxesT]":
        return self._operate(other, AxisOperation.Subtract)

    def _operate(self: "PointT", vector: Any, op: AxisOperation) -> "PointT":
        """
        Returns a new point based on the `op` between this and `vector`.
        """

        translated_coords: List[Any] = []

        for index, point_coord in enumerate(self._coordinates):
            axis = self._axes[index]
            vector_coord = self._vector(vector, index)
            result = axis.operate(point_coord, vector_coord, op)
            translated_coords.append(result)

        coordinates = cast(AxesT, tuple(translated_coords))

        return self.__class__(
            coordinates,
            axes=self._axes,
            origin_of=self._origin_of,
            within=self._within,
        )

    def _vector(self, vector: Any, dimension: int) -> float:
        """
        Gets the `vector` force of `dimension`.
        """

        if isinstance(vector, (float, int)):
            return vector

        if isinstance(vector, (list, tuple)):
            return cast(Sequence[float], vector)[dimension]

        raise ValueError(f"{repr(vector)} ({type(vector)}) is not a vector")

    @property
    def coordinates(self) -> AxesT:
        """
        Coordinates.
        """

        return self._coordinates

    def resolve(self) -> ResolvedPoint[AxesT]:
        translated_coords: List[Any] = []

        for dimension, coordinate in enumerate(self._coordinates):
            if isinstance(coordinate, Alignment):
                if self._within is None:
                    raise ValueError(
                        f"{self.__class__.__name__} cannot resolve alignment "
                        f"{coordinate.name} without a parent region"
                    )

                within_offset = self._within.position()[dimension]

                match coordinate.value:
                    case Alignment.Near:
                        translated_coords.append(within_offset)

                    case Alignment.Center:
                        axis = self._axes[dimension]
                        distance = axis.to_decimal(within_offset)

                        within_len = self._within.volume()[dimension]
                        distance += within_len / 2

                        if self._origin_of is not None:
                            distance -= self._origin_of()[dimension] / 2

                        translated_coords.append(axis.to_value(distance))

                    case Alignment.Far:
                        axis = self._axes[dimension]
                        distance = axis.to_decimal(within_offset)

                        within_len = self._within.volume()[dimension]
                        distance += within_len

                        if self._origin_of:
                            distance -= self._origin_of()[dimension]

                        translated_coords.append(axis.to_value(distance))

                    case _:
                        m = f"Unrecognised alignment {repr(coordinate.value)}"
                        raise ValueError(m)

            else:
                translated = coordinate

                if self._within is not None:
                    axis = self._axes[dimension]
                    within_origin = self._within.position()
                    translated = axis.add(coordinate, within_origin[dimension])

                translated_coords.append(translated)

        resolved_point = cast(AxesT, tuple(translated_coords))
        log.debug("Resolved %s to %s", self, resolved_point)
        return ResolvedPoint(resolved_point)


PointT = TypeVar("PointT", bound=Point[Any])
