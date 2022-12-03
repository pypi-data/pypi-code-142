from typing import Any, List, Sequence, cast

from bounden.axes import AxesT, Axis, AxisOperation


def get_vector_length(vector: Any, dimension: int) -> float:
    """
    Gets the `vector` length of `dimension`.
    """

    if isinstance(vector, (float, int)):
        return vector

    if isinstance(vector, (list, tuple)):
        return cast(Sequence[float], vector)[dimension]

    raise ValueError(f"{repr(vector)} ({type(vector)}) is not a vector")


def transform_coordinates(
    axes: Sequence[Axis[Any]],
    coordinates: AxesT,
    vector: Any,
    operation: AxisOperation,
) -> AxesT:
    """
    Transforms `coordinates` by `operation` on `vector`.
    """

    translated_coords: List[Any] = []

    for index, point_coord in enumerate(coordinates):
        axis = axes[index]
        vector_coord = get_vector_length(vector, index)
        result = axis.operate(point_coord, vector_coord, operation)
        translated_coords.append(result)

    return cast(AxesT, tuple(translated_coords))
