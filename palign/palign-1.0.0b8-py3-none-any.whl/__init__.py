"""
Palign provides functions for aligning text to be rendered via Pillow.
"""

from importlib.resources import files

from bounden import Alignment, Percent

from palign.grid import Grid
from palign.image_region import ResolvedImageRegion, make_image_region
from palign.style import Style, StyledText, StyledTextLineFragment
from palign.text import Text
from palign.types import (
    AnyRegion,
    Color,
    GetTextLength,
    Point,
    Region,
    ResolvedRegion,
)

with files(__package__).joinpath("VERSION").open("r") as t:
    version = t.readline().strip()

__all__ = [
    "Alignment",
    "AnyRegion",
    "Color",
    "GetTextLength",
    "Grid",
    "Percent",
    "Point",
    "Region",
    "ResolvedImageRegion",
    "ResolvedRegion",
    "Style",
    "StyledText",
    "StyledTextLineFragment",
    "Text",
    "make_image_region",
    "version",
]
