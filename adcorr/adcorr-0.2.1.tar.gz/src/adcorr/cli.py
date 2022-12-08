import click

from . import __version__


@click.group(invoke_without_command=True)
@click.version_option(version=__version__, message="%(version)s")
@click.pass_context
def main(ctx: click.Context) -> None:
    """Area detector corrections as pure python functions.

    This project is intended to be used as a library, and thus has no CLI.
    """
    if ctx.invoked_subcommand is None:
        click.echo(main.get_help(ctx))
