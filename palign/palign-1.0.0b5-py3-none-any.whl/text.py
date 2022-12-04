from typing import Optional

from bounden import Region2, ResolvedRegion2, ResolvedVolume2
from PIL.ImageDraw import ImageDraw

from palign.style import Style
from palign.text_lines import TextLines
from palign.types import Point, Region, ResolvedRegion


class Text:
    """
    Text renderer.

    `draw` is the Pillow drawing instance to render to.

    `style` is the optional default style to apply.
    """

    def __init__(self, draw: ImageDraw, style: Optional[Style] = None) -> None:
        self._draw = draw
        self._style = style or Style()

    def _render_text(
        self,
        lines: TextLines,
        style: Style,
        target: ResolvedRegion,
    ) -> None:
        lines_region = target.region2(
            0 if style.horizontal is None else style.horizontal,
            0 if style.vertical is None else style.vertical,
            lines.volume.width,
            lines.volume.height,
        ).resolve()

        for line_index, line in enumerate(lines):
            line_region = lines_region.region2(
                0 if style.horizontal is None else style.horizontal,
                0,
                line.width,
                lines.line_height,
            ).resolve()

            line_resolved = line_region + (
                0,
                lines.line_height * line_index,
            )

            for character in line:
                self._draw.text(
                    (line_resolved.left + character.x, line_resolved.top),
                    character.character,
                    fill=style.color,
                    font=style.font,
                )

    def draw_text(
        self,
        text: str,
        bounds: Region2[float, float] | ResolvedRegion | Point,
        style: Optional[Style] = None,
    ) -> None:
        """
        Draws `text` at/within `bounds` with optional `style`.
        """

        style = self._style if style is None else self._style + style
        lines = TextLines(text, style, self._draw.textlength)

        resolved = self.resolve(bounds, lines.volume)

        resolved_bounds = (
            None
            if resolved is None
            else (resolved.left, resolved.top, resolved.right, resolved.bottom)
        )

        if style.background is not None and resolved_bounds is not None:
            if style.border_radius is None:
                self._draw.rectangle(
                    resolved_bounds,
                    fill=style.background,
                )
            else:
                self._draw.rounded_rectangle(
                    resolved_bounds,
                    fill=style.background,
                    radius=style.border_radius,
                )

        if (
            style.border_color is not None
            and style.border_width is not None
            and resolved_bounds is not None
        ):
            if style.border_radius is None:
                self._draw.rectangle(
                    resolved_bounds,
                    outline=style.border_color,
                    width=style.border_width,
                )
            else:
                self._draw.rounded_rectangle(
                    resolved_bounds,
                    outline=style.border_color,
                    radius=style.border_radius,
                    width=style.border_width,
                )

        self._render_text(lines, style, resolved)

    @classmethod
    def resolve(
        cls,
        bounds: Point | Region2[float, float] | ResolvedRegion,
        fallback_volume: ResolvedVolume2,
    ) -> ResolvedRegion:
        """
        Attempts to resolve `bounds` to a region.
        """

        if isinstance(bounds, Region2):
            return bounds.resolve()

        if isinstance(bounds, ResolvedRegion2):
            return bounds

        return Region.new(
            bounds[0],
            bounds[1],
            fallback_volume.width,
            fallback_volume.height,
        ).resolve()
