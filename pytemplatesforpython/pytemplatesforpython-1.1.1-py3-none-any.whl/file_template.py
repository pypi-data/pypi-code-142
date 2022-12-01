from pathlib import Path
from typing import Optional, Union
from .abstract_template import AbstractTemplate

class FileTemplate(AbstractTemplate):
    def __init__(self, filename: Union[str, Path], name: Optional[str] = None):
        with open(filename, "r") as file:
            self._string = file.read()
        if name is None:
            self.name = str(filename)
        else:
            self.name = name
        super().__init__()