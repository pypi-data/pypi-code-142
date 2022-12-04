from os import system as run
from typing import List, Optional

import typer
from rich import print
from rich.console import Console

from compose_companion.configurations import Configurations

from compose_companion.functions import (
    container_down,
    container_stop,
    container_start,
    container_pause,
    container_up,
    print_config
)


app = typer.Typer()
err_console = Console(stderr=True)


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    """
    A companion for Docker Compose.
    """
    if not ctx.invoked_subcommand:
        ctx.get_help()
    else:
        Configurations()


@app.command()
def up(
    targets: Optional[List[str]] = typer.Argument(
        None,
        help="Containers in which to run the command. If no targets are passed, runs for all containers.",
    ),
    recreate: bool = typer.Option(
        False,
        "--recreate",
        "-r",
        help="Recreates containers even if their configuration and image haven't changed. Toggles docker compose --force-recreate option.",
    ),
    build: bool = typer.Option(
        False,
        "--build",
        "-b",
        help="Build images before starting containers. Toggles docker compose --build option.",
    ),
):
    """
    Starts up targeted containers.
    If no target is defined, starts all containers.
    Calls to `docker compose up -d --remove-orphans`.
    """
    services = Configurations().services
    if not targets:
        for container in services:
            container_up(container, recreate, build)
        return
    for container in targets:
        container_up(container, recreate, build)
    return


@app.command()
def start(
    targets: Optional[List[str]] = typer.Argument(
        None,
        help="Containers in which to run the command. If no targets are passed, runs for all containers.",
    ),
):
    """
    Starts targeted containers.
    If no target is defined, starts all containers.
    Equivalent to `docker compose start`.
    """
    services = Configurations().services
    if not targets:
        for container in services:
            container_start(container)
        return
    for container in targets:
        container_start(container)


@app.command()
def pause(
    targets: Optional[List[str]] = typer.Argument(
        None,
        help="Containers in which to run the command. If no targets are passed, runs for all containers.",
    ),
):
    """
    Pauses targeted containers.
    If no target is defined, pauses all containers.
    Equivalent to `docker compose pause`.
    """
    services = Configurations().services
    if not targets:
        for container in services:
            container_pause(container)
        return
    for container in targets:
        container_pause(container)


@app.command()
def stop(
    targets: Optional[List[str]] = typer.Argument(
        None,
        help="Containers in which to run the command. If no targets are passed, runs for all containers.",
    ),
):
    """
    Stops targeted containers.
    If no target is defined, stops all containers.
    Equivalent to `docker compose stop`.
    """
    services = Configurations().services
    if not targets:
        for container in services:
            container_stop(container)
        return
    for container in targets:
        container_stop(container)


@app.command()
def down(
    targets: Optional[List[str]] = typer.Argument(
        None,
        help="Containers in which to run the command. If no targets are passed, runs for all containers.",
    ),
    remove_volumes: Optional[bool] = typer.Option(
        False,
        "--remove-volumes",
        help="Remove any anonymous volumes attached to the containers. Equivalent do docker compose -v/--volumes option.",
    ),
    confirmation: bool = typer.Option(
        False,
        "-f",
        "--force",
        prompt="You're about to shut down your containers. Are you sure?",
        help="Skip confirmation prompt and run.",
    ),
):
    """
    Shuts down target containers.
    If no target is defined, shuts down all containers.
    Equivalent to `docker compose rm -sf`.
    """
    services = Configurations().services

    if not confirmation:
        return
    if not targets:
        for container in services:
            container_down(container, remove_volumes)
        return
    for container in targets:
        container_down(container, remove_volumes)


@app.command()
def logs(
    targets: Optional[List[str]] = typer.Argument(
        None,
        help="Containers in which to run the command. If no targets are passed, runs for all containers.",
    ),
    detach: bool = typer.Option(
        False,
        "--detach",
        "-d",
        help="Print logs without following. Negates docker compose --follow/-f flag, which is used by default.",
    ),
    timestamps: bool = typer.Option(
        False,
        "--timestamps",
        "-t",
        help="Show timestamps. Toggles docker compose --timestamps/-t flag.",
    ),
):
    """
    Prints logs for target containers.
    If no target is defined, prints for all running ones.
    Equivalent to `docker compose logs -f`
    """
    compose_file = Configurations().compose_file

    if not targets:
        run(f"docker compose -f {compose_file} logs -f={not detach} -t={timestamps}")
        return
    run(
        f"docker compose -f {compose_file} logs {' '.join(targets)} -f={not detach} -t={timestamps}"
    )


@app.command()
def exec(
    target: str = typer.Argument(
        ...,
        help="The target container.",
    ),
    detach: Optional[bool] = typer.Option(
        False,
        "-d",
        "--detach",
        help="Detached mode: Run command in the background. Equivalent to docker compose -d flag.",
    ),
    command: Optional[List[str]] = typer.Argument(
        None,
        help="Command to be run. By default, runs `sh`.",
    ),
):
    """
    Runs command on the container.
    Equivalent to `docker compose exec`.
    """
    compose_file = Configurations().compose_file

    if not command:
        run(f"docker compose -f {compose_file} exec -d={detach} {target} sh")
        return
    run(
        f"docker compose -f {compose_file} exec -d={detach} {target} {' '.join(command)}"
    )


@app.command()
def ps(
    targets: Optional[List[str]] = typer.Argument(
        None,
        help="Containers in which to run the command. If no targets are passed, runs for all containers.",
    ),
    include_stopped: Optional[bool] = typer.Option(
        False,
        "-a",
        "--all",
        help="Show all, including stopped containers. Equivalent to docker compose -a/--all option.",
    ),
):
    """
    Lists containers.
    If no target is defined, lists all containers.
    Equivalent to `docker compose ps`.
    """
    compose_file = Configurations().compose_file

    if not targets:
        run(f"docker compose -f {compose_file} ps")
        return
    run(
        f"docker compose -f {compose_file} ps {' '.join(targets)} -a={include_stopped}"
    )


@app.command()
def config(
    key: Optional[str] = typer.Argument(
        None,
        help="Configuration key to view/set. If left blank, prints all the conf.",
    ),
    value: Optional[str] = typer.Argument(
        None,
        help="Value to set on the key. If key is passed but not value, current value for the config will be printed.",
    ),
):
    """
    View or change configurations.
    """
    conf = Configurations()

    if key and key in conf.config_keys:
        if (key == 'compose_file' and value):
            conf.compose_file = value
        elif (key == 'companion_file' and value):
            conf.companion_file = value
        print(conf.get_config(key))
        return

    if key and key not in conf.config_keys:
        err_console.print(
            "Invalid Key. Here are the available keys:\n"
        )

    print_config()


if __name__ == "__main__":
    app()
