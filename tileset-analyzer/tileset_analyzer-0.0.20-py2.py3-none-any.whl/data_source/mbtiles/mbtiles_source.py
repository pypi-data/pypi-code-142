import abc
from collections import namedtuple
from sqlite3 import Connection
from typing import List
from tileset_analyzer.data_source.mbtiles.sqllite_utils import create_connection
from tileset_analyzer.data_source.tile_source import TileSource
from tileset_analyzer.entities.tileset_analysis_result import LevelCount, TilesetAnalysisResult
from tileset_analyzer.data_source.mbtiles.sql_queries import SQL_COUNT_TILES, SQL_COUNT_TILES_BY_Z


class MBTileSource(TileSource):
    def __init__(self, src_path: str):
        self.conn = create_connection(src_path)

    def count_tiles(self) -> int:
        cur = self.conn.cursor()
        cur.execute(SQL_COUNT_TILES)
        count = cur.fetchone()[0]
        return count

    def count_tiles_by_z(self) -> List[LevelCount]:
        cur = self.conn.cursor()
        cur.execute(SQL_COUNT_TILES_BY_Z)
        rows = cur.fetchall()
        result = []
        for row in rows:
            result.append(LevelCount(row[0], row[1]))
        return result

    def analyze(self) -> TilesetAnalysisResult:
        result = TilesetAnalysisResult()
        result.set_count_tiles_total(self.count_tiles())
        result.set_count_tiles_by_z(self.count_tiles_by_z())
        return result
