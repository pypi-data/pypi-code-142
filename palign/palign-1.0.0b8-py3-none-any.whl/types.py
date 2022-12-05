from typing import Callable, Optional, Tuple, Union

from bounden import Region2, ResolvedRegion2
from PIL.ImageFont import FreeTypeFont

Color = Union[
    Tuple[int, int, int],
    Tuple[int, int, int, int],
]

GetTextLength = Callable[[str, Optional[FreeTypeFont]], float]

Point = tuple[int, int]
Region = Region2[float, float]
ResolvedRegion = ResolvedRegion2[float, float]

AnyRegion = Region | ResolvedRegion
