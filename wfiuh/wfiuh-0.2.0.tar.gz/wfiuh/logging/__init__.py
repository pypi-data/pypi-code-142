import typing

import pandas as pd
import rich.traceback
from rich import print
from rich.console import RenderableType
from rich.padding import PaddingDimensions
from rich.panel import Panel
from rich.pretty import Pretty
from rich.style import Style
from rich.table import Table
from rich.text import Text

rich.traceback.install()
panel_title_style = Style(color="bright_blue", bold=True)


def print_panel(
    obj: RenderableType,
    *args,
    title: typing.Optional[str] = None,
    expand: bool = False,
    **kwargs,
) -> None:
    panel = Panel(
        obj,
        *args,
        title=Text(text=title, style=panel_title_style) if title else None,
        expand=expand,
        **kwargs,
    )
    print(panel)


def print_data_frame(
    data_frame: pd.DataFrame,
    *args,
    title: typing.Optional[str] = None,
    expand: bool = False,
    padding: PaddingDimensions = (0, 4),
    **kwargs,
) -> None:
    table = Table.grid(padding=padding)
    for key, values in data_frame.items():
        table.add_row(str(key), *map(Pretty, values))
    print_panel(table, *args, title=title, expand=expand, **kwargs)


def print_series(
    series: pd.Series,
    *args,
    title: typing.Optional[str] = None,
    expand: bool = False,
    padding: PaddingDimensions = (0, 4),
    **kwargs,
) -> None:
    table = Table.grid(padding=padding)
    for key, value in series.items():
        table.add_row(str(key), Pretty(value))
    print_panel(table, *args, title=title, expand=expand, **kwargs)


def print_dict(
    obj: dict,
    *args,
    title: typing.Optional[str] = None,
    expand: bool = False,
    padding: PaddingDimensions = (0, 4),
    **kwargs,
) -> None:
    series = pd.Series(obj)
    print_series(
        series=series, *args, title=title, expand=expand, padding=padding, **kwargs
    )
