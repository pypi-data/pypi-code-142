import typer
from rich import print

from memproc import core, utils

app = typer.Typer(
    add_completion=False,
    pretty_exceptions_enable=False,
    help='✨ Fancy display of memory usage.',
)


@app.command()
def run(
    version: bool = typer.Option(
        False,
        '--version',
        help='Show installed version.',
    ),
    update: bool = typer.Option(
        False,
        '--update',
        help='Update memproc to last version.',
    ),
    sort_by: str = typer.Option(
        'mem',
        '--sort',
        '-s',
        help='Sort results by criteria: pid name mem.',
    ),
    sort_reverse: bool = typer.Option(
        False,
        '--sort-reverse',
        '-r',
        help='Sort reverse by current criteria.',
    ),
    extended_info: bool = typer.Option(
        False,
        '--ext-info',
        '-e',
        help='Show extended info (command line) for each process.',
    ),
):
    if version:
        print(utils.get_memproc_version())
        return
    if update:
        utils.update_memproc()
        return
    core.display_memproc(sort_by, sort_reverse, extended_info)


if __name__ == "__main__":
    app()
