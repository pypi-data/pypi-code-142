from typing import Callable, Optional, Union
from .file_template import FileTemplate
from pathlib import Path

class TemplatesLoader:
    templates: dict[str, FileTemplate]
    root_path: Path

    def __init__(self, path_str = "."):
        self.templates = {}
        self.root_path = Path(path_str).absolute()

    def load_template(self, name: Union[str, Path]):
        if isinstance(name, str):
            name = Path(name)
        global_path = self.root_path / name
        self.templates[str(name)] = FileTemplate(global_path, str(name))

    def unload_template(self, name: str):
        del self.templates[name]

    def recursively_load_folder(self, path_str: str, pattern: str = "*", filter: Optional[Callable[[Path], bool]] = None):
        loaded: list[Path] = []
        path: Path = Path(path_str)
        global_path: Path = self.root_path / path
        if not global_path.exists():
            global_path_str = str(global_path)
            raise FileNotFoundError(f"No such file or directory: '{global_path_str}'")
        for path in global_path.rglob(pattern):
            if not filter or filter(path):
                try:
                    path = path.relative_to(self.root_path)
                except ValueError as e:
                    raise ValueError("directory should be the child directory of the current working directory or of the directory you've specified") from e
                self.load_template(path)
                loaded.append(path)
        return loaded
    
    def get_template(self, name: str):
        if name not in self.templates:
            self.load_template(name)
        return self.templates[name]
    




