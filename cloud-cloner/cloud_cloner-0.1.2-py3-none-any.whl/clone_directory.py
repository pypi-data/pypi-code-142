import os

import rclone
from rich import print

from cloud_cloner.bootstrap import app
from cloud_cloner.rclone_config import load_rclone_config


@app.command()
def clone_directory(remote_directory: str, destination_directory: str, rclone_config_path: str = "~/.rclone") -> None:
    rclone_config = load_rclone_config(rclone_config_path)

    print(f"Cloning {remote_directory} to {destination_directory}")
    rclone.with_config(rclone_config).copy(f"remote:{remote_directory}", destination_directory, flags=["-P"])
    print(f"Cloned {remote_directory} to {destination_directory}")
