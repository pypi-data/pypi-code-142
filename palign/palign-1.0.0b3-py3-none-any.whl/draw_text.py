from logging import getLogger
from typing import Optional

from PIL.ImageDraw import ImageDraw

from palign.enums import Horizontal, Vertical
from palign.region import Point, Region
from palign.style import Style
from palign.text import Text

DEFAULT_FONT_SIZE = 21

log = getLogger("palign")


def _render_text(
    text: str,
    draw: ImageDraw,
    style: Style,
    b: Point | Region | tuple[float, float],
) -> None:
    lh = style.font.size if style.font else DEFAULT_FONT_SIZE

    if not isinstance(b, Region) and (style.horizontal or style.vertical):
        log.warning("Text will not be aligned when bounds are a position")

    t = Text(text, style, draw.textlength)

    for index, line in enumerate(t):
        match style.horizontal:
            case Horizontal.Center if isinstance(b, Region):
                x = float(b.left) + (b.width / 2) - (line.width / 2)

            case Horizontal.Right if isinstance(b, Region):
                x = float(b.left) + b.width - line.width

            case _ if isinstance(b, tuple):
                x = b[0]

            case _:
                x = float(b.left)

        match style.vertical:
            case Vertical.Center if isinstance(b, Region):
                y = b.top + (b.height / 2) - (t.height / 2) + (lh * index)

            case Vertical.Bottom if isinstance(b, Region):
                y = b.top + b.height - t.height + (lh * index)

            case _ if isinstance(b, tuple):
                y = b[1] + (lh * index)

            case _:
                y = b.top + (lh * index)

        for character in line:
            draw.text(
                (float(x + character.x), float(y)),
                character.character,
                fill=style.color,
                font=style.font,
            )


def draw_text(
    text: Optional[str],
    draw: ImageDraw,
    style: Style,
    bounds: Point | Region | tuple[float, float],
) -> None:
    if isinstance(bounds, Region):
        bounds = bounds.absolute

    if style.background is not None:
        if isinstance(bounds, Region):
            pb = (
                float(bounds.left),
                float(bounds.top.coordinate),
                float(bounds.right.coordinate),
                float(bounds.bottom.coordinate),
            )

            if style.border_radius is None:
                draw.rectangle(pb, fill=style.background)
            else:
                draw.rounded_rectangle(
                    pb,
                    outline=style.border_color,
                    radius=style.border_radius,
                )
        else:
            log.warning("Will not draw background when bounds is a position")

    if style.border_color is not None and style.border_width is not None:
        if isinstance(bounds, Region):
            pb = (
                float(bounds.left),
                float(bounds.top.coordinate),
                float(bounds.right.coordinate),
                float(bounds.bottom.coordinate),
            )

            if style.border_radius is None:
                draw.rectangle(
                    pb,
                    outline=style.border_color,
                    width=style.border_width,
                )
            else:
                draw.rounded_rectangle(
                    pb,
                    outline=style.border_color,
                    radius=style.border_radius,
                    width=style.border_width,
                )
        else:
            log.warning("Will not draw border when bounds is a position")

    if text:
        _render_text(text, draw, style, bounds)
