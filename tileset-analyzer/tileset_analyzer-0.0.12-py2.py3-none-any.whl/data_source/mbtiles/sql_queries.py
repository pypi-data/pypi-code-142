from typing import Final

SQL_COUNT_TILES: Final[str] = 'select count(*) as count from tiles;'
SQL_COUNT_TILES_BY_Z: Final[str] = 'select zoom_level as zoom_level, count(*) as count from tiles group by zoom_level order by zoom_level ASC;'
