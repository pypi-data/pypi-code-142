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
    name_level: int = typer.Option(
        1,
        '--name-level',
        '-n',
        help='1: Name | 2: Executable | 3: Command line',
    ),
):
    if version:
        print(utils.get_memproc_version())
        return
    if update:
        utils.update_memproc()
        return
    core.display_memproc(name_level, sort_by, sort_reverse)


if __name__ == "__main__":
    app()
