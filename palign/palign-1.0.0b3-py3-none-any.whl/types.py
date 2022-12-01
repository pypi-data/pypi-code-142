from typing import Callable, Optional, Tuple, Union

from PIL.ImageFont import FreeTypeFont

Color = Union[
    Tuple[int, int, int],
    Tuple[int, int, int, int],
]

GetTextLength = Callable[[str, Optional[FreeTypeFont]], float]
