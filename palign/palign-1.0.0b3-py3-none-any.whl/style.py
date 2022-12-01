from dataclasses import dataclass
from typing import Any, Optional, TypeVar

from PIL.ImageFont import FreeTypeFont

from palign.enums import Horizontal, Vertical
from palign.types import Color


@dataclass
class Style:
    """
    Text style.

    `background_color` describes the background colour. A background will not
    be painted if this is omitted.

    `border_color` describes the border colour. Defaults to none.

    `border_radius` describes the border radius. Defaults to none.

    `border_width` describes the border width. Defaults to none.

    `color` describes the text colour. Text will not be painted if this is
    omitted.

    `font` describes the font. Pillow's default font will be used where
    possible if this is omitted, but many text operations will fail.

    `horizontal` describes the text's horizontal alignment within its bounds.
    Defaults to left.

    `tracking` describes the space to insert between each character. Defaults
    to none.

    `vertical` describes the text's vertical alignment within its bounds.
    Defaults to top.
    """

    background: Optional[Color] = None
    """
    Background colour.

    A background will not be painted if this is omitted.
    """

    border_color: Optional[Color] = None
    """
    Border colour.

    A border will not be painted if this is omitted.
    """

    border_radius: Optional[float] = None
    """
    Border radius.

    The border will be rounded if this is set.
    """

    border_width: Optional[float] = None
    """
    Border width.

    A border will not be painted if this is omitted.
    """

    color: Optional[Color] = None
    """
    Text colour.

    Text will not be painted if this is omitted.
    """

    font: Optional[FreeTypeFont] = None
    """
    Font.

    Pillow's default font will be used where possible if this is omitted, but
    many text operations will fail.
    """

    horizontal: Optional[Horizontal] = None
    """
    Horizontal alignment.
    """

    tracking: Optional[float] = None
    """
    Character tracking.
    """

    vertical: Optional[Vertical] = None
    """
    Vertical alignment.
    """

    def __add__(self, o: Any) -> "Style":
        if not isinstance(o, Style):
            raise TypeError("Can merge only Style to Style")

        V = TypeVar("V")

        def _or(a: V, b: V) -> V:
            return a if b is None else b

        return Style(
            background=_or(self.background, o.background),
            border_color=_or(self.border_color, o.border_color),
            border_radius=_or(self.border_radius, o.border_radius),
            border_width=_or(self.border_width, o.border_width),
            color=_or(self.color, o.color),
            font=_or(self.font, o.font),
            horizontal=_or(self.horizontal, o.horizontal),
            tracking=_or(self.tracking, o.tracking),
            vertical=_or(self.vertical, o.vertical),
        )
