import abc
from sqlite3 import Connection
from typing import List
from entities.level_count import LevelCount
from entities.tileset_analysis_result import TilesetAnalysisResult


class TileSource(abc.ABC):
    @abc.abstractmethod
    def __init__(self, src_path: str):
        pass

    @abc.abstractmethod
    def count_tiles(self) -> int:
        pass

    @abc.abstractmethod
    def count_tiles_by_z(self) -> List[LevelCount]:
        pass

    @abc.abstractmethod
    def analyze(self) -> TilesetAnalysisResult:
        pass
