from pathlib import Path
from typing import List


class BaseDir:
    def __init__(self, reference, path: Path):
        """
        @param path:
        if the tool path contains subdirectories then it will add an attribute with the name of subdirectories.
        therefore we can access a subdirectory path like this :
        tool.vep.annotations
        if the tool path contains files then it will add an attribute with the name of file ('.' replaced by '_').
        Therefore, we can access a file path like this :
        tool.vep.annotations.dummy_annot -> tool/vep/annotations/dummy.annot
        """
        self.reference = reference
        self.path = path
        self.name = self.path.name
        if self.path.is_dir():
            self.files = [f for f in self.path.iterdir() if f.is_file()]
            for f in self.files:
                setattr(self, f"{f.name.replace('.', '_')}", f)
            for new_tool in self.available_tools:
                setattr(self, new_tool.name, new_tool)  # create attribute for each tool

    @property
    def available_tools(self) -> List:
        return [BaseDir(self.reference, path) for path in self.path.iterdir()]
