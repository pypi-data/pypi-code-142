import inspect
import json
from pathlib import Path
from typing import Any


def get_resource_path(*path_components: str) -> Path:
    invoking_frame = inspect.stack()[1]
    invoking_module = inspect.getmodule(invoking_frame[0])
    return Path(invoking_module.__file__).parent.joinpath(*path_components)


def load_resource(*path_components: str) -> Any:
    invoking_frame = inspect.stack()[1]
    invoking_module = inspect.getmodule(invoking_frame[0])
    pkg_resource_file_path = Path(invoking_module.__file__).parent.joinpath(*path_components)
    if pkg_resource_file_path.suffix == ".json":
        return json.loads(pkg_resource_file_path.read_text())
