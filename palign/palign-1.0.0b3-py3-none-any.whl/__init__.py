"""
Palign provides functions for aligning text to be rendered via Pillow.
"""

from importlib.resources import files

from palign.draw_text import draw_text
from palign.enums import Horizontal, Vertical
from palign.grid import Grid
from palign.region import Point, Region
from palign.style import Style

with files(__package__).joinpath("VERSION").open("r") as t:
    version = t.readline().strip()

__all__ = [
    "Grid",
    "Horizontal",
    "Point",
    "Region",
    "Style",
    "Vertical",
    "draw_text",
    "version",
]
