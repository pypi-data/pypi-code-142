from typing import Optional

from bounden import Region2
from nvalues import Volume
from PIL.ImageDraw import ImageDraw

from palign.cell import Cell
from palign.style import Style
from palign.text import Text
from palign.types import AnyRegion


class Grid:
    """
    Text grid.

    `columns` is the number of columns.

    `rows` is the number of rows.

    `region` is the region to render the grid within.

    `style` is the optional base style to apply to each cell.
    """

    def __init__(
        self,
        columns: int,
        rows: int,
        region: AnyRegion,
        style: Optional[Style] = None,
    ) -> None:
        def validate_key(key: tuple[int, int]) -> None:
            x = key[0]
            if x < 0 or x >= columns:
                raise IndexError(f"No column {x}; grid has {columns}")

            y = key[1]
            if y < 0 or y >= rows:
                raise IndexError(f"No row {y}; grid has {rows}")

        self._columns = columns

        self._region = (
            region.resolve() if isinstance(region, Region2) else region
        )

        self._rows = rows

        def make_cell(_: tuple[int, int]) -> Cell:
            return Cell(style=Style())

        self._cells = Volume[tuple[int, int], Cell](
            default_maker=make_cell,
            key_validator=validate_key,
        )

        self._default_style = style or Style()

    def __delitem__(self, key: tuple[int, int]) -> None:
        del self._cells[key]

    def __getitem__(self, key: tuple[int, int]) -> Cell:
        return self._cells[key]

    def _cell_bounds(self, x: int, y: int) -> Region2[float, float]:
        column_width = int(self._region.width / self._columns)
        row_height = int(self._region.height / self._rows)

        return self._region.region2(
            x * column_width,
            y * row_height,
            column_width,
            row_height,
        )

    def draw(self, draw: ImageDraw) -> None:
        """
        Draws the grid.
        """

        renderer = Text(draw, self._default_style)

        for x in range(self._columns):
            for y in range(self._rows):
                cell = self[x, y]
                renderer.draw_text(
                    cell.text or "",
                    self._cell_bounds(x, y),
                    style=cell.style,
                )
