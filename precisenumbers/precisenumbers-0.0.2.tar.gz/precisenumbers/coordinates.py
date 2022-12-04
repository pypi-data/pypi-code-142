from dataclasses import dataclass
from typing import Optional, Tuple, Union

from precisenumbers import PreciseNumber, parse_number


class Longitude(PreciseNumber):
    """PreciseNumber to represent a longitude value"""

    MAXIMUM_PRECISION = 7
    MAXIMUM = 180
    MINIMUM = -180


class Latitude(PreciseNumber):
    """PreciseNumber to represent a latitude value"""

    MAXIMUM_PRECISION = 7
    MAXIMUM = 90
    MINIMUM = -90


@dataclass
class Coordinate:
    """Representation of a coordinate on the globe (i.e., a lon/lat pair) using PreciseNumbers"""

    longitude: Longitude
    latitude: Latitude

    def __init__(
        self,
        longitude: Union[float, int, str],
        latitude: Union[float, int, str],
        precision: Optional[int] = None,
        same_precision: bool = True,
    ):
        if precision and not same_precision:
            raise ValueError('`precision` cannot be set if `same_precision=False`')

        if same_precision and not precision:
            _, _, _, inferred_lon_precision = parse_number(longitude)
            _, _, _, inferred_lat_precision = parse_number(latitude)
            precision = max(inferred_lat_precision, inferred_lon_precision)

        self.longitude = Longitude(number=longitude, precision=precision)
        self.latitude = Latitude(number=latitude, precision=precision)
