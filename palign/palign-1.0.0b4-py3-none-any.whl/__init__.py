"""
Palign provides functions for aligning text to be rendered via Pillow.
"""

from importlib.resources import files

from bounden import Alignment, Percent

from palign.grid import Grid
from palign.image_region import make_image_region
from palign.style import Style
from palign.text_renderer import TextRenderer
from palign.types import AnyRegion, Region, ResolvedRegion

with files(__package__).joinpath("VERSION").open("r") as t:
    version = t.readline().strip()

__all__ = [
    "Alignment",
    "AnyRegion",
    "Grid",
    "Percent",
    "Region",
    "ResolvedRegion",
    "Style",
    "TextRenderer",
    "make_image_region",
    "version",
]
