from typing import List, Optional, Sequence

from bounden import Region2, ResolvedRegion2, ResolvedVolume2
from PIL.ImageDraw import ImageDraw

from palign.style import Style, StyledText
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

        next_line_top = 0

        for line in lines:
            region = lines_region.region2(
                0 if style.horizontal is None else style.horizontal,
                next_line_top,
                line.width,
                line.height,
            ).resolve()

            next_line_top += line.height

            for character in line:
                self._draw.text(
                    (region.left + character.x, region.top),
                    character.character,
                    fill=character.style.color,
                    font=character.style.font,
                )

    def draw(
        self,
        text: str | StyledText | Sequence[str | StyledText],
        bounds: Region2[float, float] | ResolvedRegion | Point,
        style: Optional[Style] = None,
    ) -> None:
        """
        Draws `text` at/within `bounds` with optional `style`.
        """

        style = self._style if style is None else self._style + style

        many_fragments: List[StyledText] = []

        if isinstance(text, (str, StyledText)):
            text = [text]

        for t in text:
            if isinstance(t, StyledText):
                t.rebase_style(style)
                many_fragments.append(t)
            else:
                many_fragments.append(style.text(t))

        lines = TextLines(many_fragments, self._draw.textlength)

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
