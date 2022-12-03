import os
from pathlib import Path
from typing import List

import rclone
import typer

from cloud_cloner.bootstrap import app
from cloud_cloner.config import load_config
from cloud_cloner.rclone_config import load_rclone_config


@app.command()
def clone(
    clones: List[str] = typer.Argument(None),
    base_dest_path: str = "./",
    config_path: str = "cloud_cloner.yaml",
    rclone_config_path: str = "~/.rclone",
    ignore_default: bool = False,
) -> None:
    config = load_config(config_path)
    rclone_config = load_rclone_config(rclone_config_path)

    for clone in config.clones:
        if (clone.default and not ignore_default) or clone.name in clones:
            print(f"Cloning {clone.name}...")
            for path in clone.paths:
                src_path = Path(config.base_path) / Path(path.src)
                dest_path = Path(base_dest_path) / Path(path.dest)
                dest_directory = dest_path if dest_path.is_dir() else dest_path.parent

                if not os.path.exists(dest_directory):
                    print(f"Making directory {dest_directory} for clone {clone.name}")
                    os.makedirs(dest_directory)

                print(f"Cloning {src_path} to {dest_path}...", end="\x1b[1K\r", flush=True)
                rclone.with_config(rclone_config).copy(f"remote:{src_path}", str(dest_path), flags=["--checksum"])
                print(f"Cloned {src_path} to {dest_path}")
            print()
