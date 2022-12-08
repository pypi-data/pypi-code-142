from __future__ import annotations

from math import pow  # pylint: disable=redefined-builtin
from math import acos, asin, atan2, cos, radians, sin, sqrt
from typing import Tuple

__all__ = (
    "spherical_law_of_cosines_formula",
    "haversine_formula",
    "vincenty_formula",
)
__version__ = "0.1.0rc1"

_EARTH_RADIUS = 6372795  # meters


def _coords_to_radians(
    coords: Tuple[float, float],
) -> Tuple[float, float]:
    return radians(coords[0]), radians(coords[1])


def haversine_formula(
    from_coords: Tuple[float, float],
    to_coords: Tuple[float, float],
) -> float:
    from_radians = _coords_to_radians(from_coords)
    to_radians = _coords_to_radians(to_coords)

    delta_longitudes = to_radians[1] - from_radians[1]

    angle_degrees = 2 * asin(
        sqrt(
            pow(sin((to_radians[0] - from_radians[0]) / 2), 2)
            + cos(from_radians[0])
            * cos(to_radians[0])
            * pow(sin(delta_longitudes / 2), 2)
        )
    )

    return angle_degrees * _EARTH_RADIUS


def spherical_law_of_cosines_formula(
    from_coords: Tuple[float, float],
    to_coords: Tuple[float, float],
) -> float:
    from_radians = _coords_to_radians(from_coords)
    to_radians = _coords_to_radians(to_coords)

    cos_latitudes = [cos(from_radians[0]), cos(to_radians[0])]
    sin_latitudes = [sin(from_radians[0]), sin(to_radians[0])]
    delta_longitudes = to_radians[1] - from_radians[1]

    angle_degrees = acos(
        sin_latitudes[0] * sin_latitudes[1]
        + cos_latitudes[0] * cos_latitudes[1] * cos(delta_longitudes)
    )

    return angle_degrees * _EARTH_RADIUS


def vincenty_formula(
    from_coords: Tuple[float, float],
    to_coords: Tuple[float, float],
) -> float:
    from_radians = _coords_to_radians(from_coords)
    to_radians = _coords_to_radians(to_coords)

    cos_latitudes = [cos(from_radians[0]), cos(to_radians[0])]
    sin_latitudes = [sin(from_radians[0]), sin(to_radians[0])]
    delta_longitudes = to_radians[1] - from_radians[1]

    numerator = sqrt(
        pow(cos_latitudes[1] * sin(delta_longitudes), 2)
        + pow(
            cos_latitudes[0] * sin_latitudes[1]
            - sin_latitudes[0] * cos_latitudes[1] * cos(delta_longitudes),
            2,
        )
    )
    denominator = sin_latitudes[0] * sin_latitudes[1] + cos_latitudes[
        0
    ] * cos_latitudes[1] * cos(delta_longitudes)

    angle_degrees = atan2(numerator, denominator)

    return angle_degrees * _EARTH_RADIUS
