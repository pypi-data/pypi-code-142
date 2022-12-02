import subprocess
from pathlib import Path
from typing import Optional

import typer


def clone(
    dépôt: str = typer.Argument(...),
    répertoire: Optional[Path] = typer.Argument(None),
    dénudé: bool = typer.Option(False),
    miroir: bool = typer.Option(False),
    profondeur: Optional[int] = typer.Option(None),
):
    options: list[str] = []
    if dénudé:
        options.append("--bare")
    if miroir:
        options.append("--mirror")
    if profondeur is not None:
        options.extend(["--depth", str(profondeur)])
    subprocess.call(["git", "clone", *options, dépôt, str(répertoire)])
