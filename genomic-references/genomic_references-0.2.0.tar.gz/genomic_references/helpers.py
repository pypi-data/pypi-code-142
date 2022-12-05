from pathlib import Path
from typing import List


def uniq_file(file_paths: List[Path]) -> Path:
    if len(file_paths) != 1:
        raise FileExistsError(f"Multiples files found where only one in expected : {file_paths}")
    return existing_file(file_paths[0])


def existing_file(file_path: Path) -> Path:
    if not file_path.is_file():
        raise FileNotFoundError(f"{file_path} does not exist")
    return file_path


def existing_dir(dir_path: Path) -> Path:
    if not dir_path.is_dir():
        raise NotADirectoryError(f"{dir_path} does not exist")
    return dir_path


def depends(*attributes):
    def inner(f):
        def wrapper(self, *args, **kwargs):
            for attribute in attributes:
                ref_cls = self
                if hasattr(self, "reference"):
                    ref_cls = self.reference
                if getattr(ref_cls, attribute) is None:
                    raise AttributeError("{arg} is not defined.")
                return f(self, *args, **kwargs)

        return wrapper

    return inner
