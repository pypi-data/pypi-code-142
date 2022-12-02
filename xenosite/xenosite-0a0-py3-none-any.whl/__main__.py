import typer
from rich.logging import RichHandler
from importlib.metadata import entry_points
import logging
from rich import print

logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    datefmt="[%X]",
    handlers=[
        RichHandler(rich_tracebacks=True, tracebacks_suppress=[typer], markup=True)
    ],
)

app = typer.Typer(
    name="xenosite",
    no_args_is_help=True,
)


@app.command()
def about():
    print("This is the XenoSite commandline interface.")


commands = {(e.load(), e.name) for e in entry_points().get("xenosite_command", [])}


for c in commands:
    app.add_typer(c[0], name=c[1])


if __name__ == "__main__":
    app()
