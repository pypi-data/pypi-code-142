import os


def load_rclone_config(rclone_config_path: str) -> str:
    print(f"Loading rclone config from {rclone_config_path}\n")
    with open(os.path.expanduser(rclone_config_path), "r") as config_file:
        return config_file.read()
