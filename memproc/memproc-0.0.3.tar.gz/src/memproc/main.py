import typer
from rich import print

from memproc import core, utils

app = typer.Typer(
    add_completion=False,
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
        help='Sort results by criteria: [-]pid [-]name [-]mem',
    ),
):
    if version:
        print(utils.get_memproc_version())
        return
    if update:
        utils.update_memproc()
        return
    core.display_memproc(sort_by)


if __name__ == "__main__":
    app()
