import os
from envyaml import EnvYAML
from pathlib import Path


def get_project_root() -> Path:
    return Path(__file__).parent


ROOT_DIR = get_project_root()
config_file_path = os.path.join(ROOT_DIR, 'conf.yaml')
env = EnvYAML(config_file_path)


def get_from_env(str_path: str):
    try:
        return env[str_path]
    except Exception as e:
        raise Exception(f"Wrong environment path {str_path}: {e}")

