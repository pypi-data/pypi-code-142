import os
import shutil
from pathlib import Path

import click
import uvicorn
from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax

from mappi import config
from mappi.server import create_app
from mappi.utils import logger, read_configuration

console = Console(highlight=False)
error_console = Console(stderr=True)


def panel(message: str):
    error_console.print(Panel(message, expand=False))


@click.group(invoke_without_command=True)
@click.version_option(message="mappi, version %(version)s")
@click.pass_context
@click.option(
    "-c",
    "--config",
    "config_filepath",
    type=click.Path(exists=False),
)
def cli(ctx, config_filepath):
    if config_filepath is None:
        config_filepath = config.MAPPI_CONFIG_FILENAME
        logger.debug(f"Using default {config.MAPPI_CONFIG_FILENAME} config file")
        if not Path(config_filepath).exists():
            panel(config.CONFIG_MISSING_MESSAGE)
            shutil.copy(config.DEFAULT_CONFIG_FILEPATH, config.MAPPI_CONFIG_FILENAME)

    if not Path(config_filepath).exists():
        raise click.BadArgumentUsage(
            f"Provided config file {config_filepath} does not exist"
        )

    if ctx.invoked_subcommand is None:
        run(config_filepath)


@cli.command(name="config", short_help="Generate sample configuration")
@click.option("--full", is_flag=True, default=False)
def generate_config(full: bool):
    filename = "config-full.yml" if full else "config-basic.yml"
    config_filepath = config.DATA_DIR / filename
    panel(config.CONFIG_MESSAGE)

    with open(config_filepath) as f:
        console.print(Syntax(f.read(), "yaml"))


def run(config_filepath: Path):
    mappi_config = read_configuration(config_filepath)
    app = create_app(mappi_config.routes)
    port = mappi_config.server.port
    server_config = uvicorn.Config(
        app,
        port=port,
        log_level="info",
        server_header=False,
        log_config=config.LOGGING_CONFIG,
    )
    server = uvicorn.Server(server_config)
    console.print(config.MAPPI_LOGO, style="yellow")
    message = f"Started mappi process [{click.style('%d', fg='cyan')}]"
    logger.info(message, os.getpid())
    endpoint = click.style(f"http://127.0.0.1:{port}", fg="green")
    logger.info(f"Running on {endpoint} (Press CTRL+C to quit)")
    server.run()


if __name__ == "__main__":
    cli()
