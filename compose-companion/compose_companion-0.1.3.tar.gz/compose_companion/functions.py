from os import system as run

from rich.panel import Panel
from rich.table import Table
from rich import print

from compose_companion.configurations import Configurations


def container_up(container: str, recreate: bool, build: bool):
    scripts = Configurations().scripts
    compose_file = Configurations().compose_file

    if scripts.get("x-before-up", {}).get(container):
        for script in scripts["x-before-up"]["before-each"]:
            run(script)
        for script in scripts["x-before-up"][container]:
            run(script)

    run(
        f"docker compose -f {compose_file} up -d --remove-orphans {container} --force-recreate={recreate} --build={build}"
    )

    if scripts.get("x-after-up", {}).get(container):
        for script in scripts["x-after-up"]["after-each"]:
            run(script)
        for script in scripts["x-after-up"][container]:
            run(script)


def container_down(container: str, volumes: bool):
    scripts = Configurations().scripts
    compose_file = Configurations().compose_file

    if scripts.get("x-before-down", {}).get(container):
        for script in scripts["x-before-down"][container]:
            run(script)

    run(f"docker compose -f {compose_file} rm -sf -v={volumes} {container}")

    if scripts.get("x-after-down", {}).get(container):
        for script in scripts["x-after-down"][container]:
            run(script)


def container_stop(container: str):
    compose_file = Configurations().compose_file
    run(f"docker compose -f {compose_file} stop {container}")


def container_pause(container: str):
    compose_file = Configurations().compose_file
    run(f"docker compose -f {compose_file} pause {container}")


def container_start(container: str):
    compose_file = Configurations().compose_file
    run(f"docker compose -f {compose_file} start {container}")


def print_config():
    [config_keys, get_config] = [Configurations().config_keys, Configurations().get_config]

    grid = Table.grid(expand=True)
    grid.add_column("Key", style="cyan")
    grid.add_column("Value", style="magenta")
    for key in config_keys:
        grid.add_row(
            key,
            get_config(key),
        )

    panel = Panel(
        grid,
        title="Configurations",
        title_align="left",
        border_style="dim",
    )
    
    print(panel)