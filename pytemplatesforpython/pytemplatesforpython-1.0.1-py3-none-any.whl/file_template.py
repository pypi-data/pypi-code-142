from pathlib import Path
from typing import Union
from .abstract_template import AbstractTemplate

class FileTemplate(AbstractTemplate):
    def __init__(self, filename: Union[str, Path]):
        file = open(filename, "r")
        self._string = file.read()
        self.name = str(filename)
        super().__init__()