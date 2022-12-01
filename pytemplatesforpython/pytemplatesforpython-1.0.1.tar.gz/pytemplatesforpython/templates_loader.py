from typing import Callable, Optional, Union
from .file_template import FileTemplate
from pathlib import Path

class TemplatesLoader:
    templates: dict[str, FileTemplate]
    root_path = Path(".").absolute()

    def __init__(self):
        self.templates = {}

    def load_template(self, name: Union[str, Path]):
        self.templates[str(name)] = FileTemplate(name)

    def unload_template(self, name: str):
        del self.templates[name]

    def recursively_load_folder(self, path_str: str, pattern: str = "*", filter: Optional[Callable[[Path], bool]] = None):
        loaded: list[Path] = []
        for path in Path(path_str).rglob(pattern):
            try:
                path = path.absolute().relative_to(self.root_path)
            except ValueError as e:
                raise ValueError("Directory should be the child directory of the current working directory") from e
            if not filter or filter(path):
                self.load_template(path)
                loaded.append(path)
        return loaded
    
    def get_template(self, name: str):
        if name not in self.templates:
            self.load_template(name)
        return self.templates[name]
    




