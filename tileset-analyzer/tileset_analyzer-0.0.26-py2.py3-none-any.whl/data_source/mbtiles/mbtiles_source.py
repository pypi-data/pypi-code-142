import abc
from collections import namedtuple
from sqlite3 import Connection
from typing import List
from tileset_analyzer.data_source.mbtiles.sqllite_utils import create_connection
from tileset_analyzer.data_source.tile_source import TileSource
from tileset_analyzer.entities.level_size import LevelSize
from tileset_analyzer.entities.tileset_analysis_result import LevelCount, TilesetAnalysisResult
from tileset_analyzer.data_source.mbtiles.sql_queries import SQL_COUNT_TILES, SQL_COUNT_TILES_BY_Z, \
    SQL_SUM_TILE_SIZES_BY_Z, SQL_MIN_TILE_SIZES_BY_Z, SQL_MAX_TILE_SIZES_BY_Z, SQL_AVG_TILE_SIZES_BY_Z


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
        result: List[LevelCount] = []
        for row in rows:
            result.append(LevelCount(row[0], row[1]))
        return result

    def _get_agg_tile_size_z(self, agg_type: str) -> List[LevelSize]:
        sql = None
        if agg_type == 'SUM':
            sql = SQL_SUM_TILE_SIZES_BY_Z
        elif agg_type == 'MIN':
            sql = SQL_MIN_TILE_SIZES_BY_Z
        elif agg_type == 'MAX':
            sql = SQL_MAX_TILE_SIZES_BY_Z
        elif agg_type == 'AVG':
            sql = SQL_AVG_TILE_SIZES_BY_Z
        else:
            raise 'UNKNOWN AGG TYPE'

        cur = self.conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        result: List[LevelSize] = []
        for row in rows:
            result.append(LevelSize(row[0], row[1]))
        return result

    def tiles_size_agg_min_by_z(self) -> List[LevelSize]:
        return self._get_agg_tile_size_z('MIN')

    def tiles_size_agg_max_by_z(self) -> List[LevelSize]:
        return self._get_agg_tile_size_z('MAX')

    def tiles_size_agg_avg_by_z(self) -> List[LevelSize]:
        return self._get_agg_tile_size_z('AVG')

    def tiles_size_agg_sum_by_z(self) -> List[LevelSize]:
        return self._get_agg_tile_size_z('SUM')

    def analyze(self) -> TilesetAnalysisResult:
        result = TilesetAnalysisResult()
        result.set_count_tiles_total(self.count_tiles())
        result.set_count_tiles_by_z(self.count_tiles_by_z())
        result.set_tiles_size_agg_sum_by_z(self.tiles_size_agg_sum_by_z())
        result.set_tiles_size_agg_min_by_z(self.tiles_size_agg_min_by_z())
        result.set_tiles_size_agg_max_by_z(self.tiles_size_agg_max_by_z())
        result.set_tiles_size_agg_avg_by_z(self.tiles_size_agg_avg_by_z())
        return result
