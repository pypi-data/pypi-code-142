from typing import Optional

from nvalues import Volume
from PIL.ImageDraw import ImageDraw

from palign.cell import Cell
from palign.draw_text import draw_text
from palign.region import Region
from palign.style import Style


class Grid:
    """
    Text grid.

    `columns` is the number of columns.

    `rows` is the number of rows.

    `default_style` is the optional style to apply to each cell that isn't
    given its own explicit style.
    """

    def __init__(
        self,
        columns: int,
        rows: int,
        region: Region,
        default_style: Optional[Style] = None,
    ) -> None:
        def validate_key(key: tuple[int, int]) -> None:
            x = key[0]
            if x < 0 or x >= columns:
                raise ValueError(f"No column {x} (grid has {columns})")

            y = key[1]
            if y < 0 or y >= rows:
                raise ValueError(f"No row {y} (grid has {rows})")

        self._columns = columns
        self._region = region
        self._rows = rows

        def make_cell(_: tuple[int, int]) -> Cell:
            return Cell(style=Style())

        self._cells = Volume[tuple[int, int], Cell](
            default_maker=make_cell,
            key_validator=validate_key,
        )

        self._default_style = default_style

    def __delitem__(self, key: tuple[int, int]) -> None:
        del self._cells[key]

    def __getitem__(self, key: tuple[int, int]) -> Cell:
        return self._cells[key]

    def __setitem__(self, key: tuple[int, int], value: Cell) -> None:
        self._cells[key] = value

    def _cell_bounds(self, x: int, y: int) -> Region:
        column_width = int(self._region.width / self._columns)
        row_height = int(self._region.height / self._rows)

        return self._region.pregion(
            x * column_width,
            y * row_height,
            column_width,
            row_height,
        )

    def render(self, draw: ImageDraw) -> None:
        """
        Renders the grid.
        """

        for x in range(self._columns):
            for y in range(self._rows):
                cell_bounds = self._cell_bounds(x, y)
                cell = self[x, y]

                style = (
                    self._default_style + cell.style
                    if self._default_style
                    else cell.style
                )
                draw_text(cell.text, draw, style, cell_bounds)
