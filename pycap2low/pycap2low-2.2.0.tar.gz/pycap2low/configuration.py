import os

from pathlib import Path


class ConfigExcept:
    @staticmethod
    def load(path) -> iter:
        if not os.path.exists(path):
            raise ValueError('Invalid directory path')

        with open(path) as f:
            for ln in f:
                i = ln.find(' ')
                attrs = ln[:i].strip()
                _path = ln[i + 1:].strip()
                if 'r' in attrs:
                    cfg_excp = ConfigExcept(str(Path(_path).resolve()), recursive=True)
                else:
                    cfg_excp = ConfigExcept(str(Path(_path).resolve()), recursive=False)
                yield cfg_excp

    __slots__ = '__path', '__recursive'
    def __init__(self, path, recursive=True) -> None:
        if not os.path.exists(path):
            raise ValueError('Invalid directory path')

        self.__path = path
        self.__recursive = recursive

    def __str__(self):
        return self.path

    def __eq__(self, other):
        return self.path == other.path

    def __ne__(self, other):
        return self.path != other.path

    def __lt__(self, other):
        return self.path < other.path

    def __le__(self, other):
        return self.path <= other.path

    def __gt__(self, other):
        return self.path > other.path

    def __ge__(self, other):
        return self.path >= other.path

    def __hash__(self) -> int:
        return hash(self.path)

    @property
    def path(self):
        return self.__path

    @property
    def recursive(self):
        return self.__recursive