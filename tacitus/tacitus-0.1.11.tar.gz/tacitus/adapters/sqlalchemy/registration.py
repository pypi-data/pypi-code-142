import collections.abc
import sqlalchemy.sql

from .generic import Link, Many2OneLink, Many2ManyLink, One2ManyLink
from ...definitions import contracts


class Registry(contracts.DataFrameRegistry):
    def __init__(self, *frames: sqlalchemy.Table):
        self._frames = {}
        self._links = collections.defaultdict(set)
        for t in frames:
            self._frames[t.name] = t
            for fk in t.foreign_keys:
                self._frames[fk.parent.name.rstrip('_id')] = fk.column.table
                self._links[t.name].update((fk.column.table.name, fk.parent.name.rstrip('_id')))

    def get_link(self, source_frame: str, target_frame: str) -> Link | None:
        source_frame = self.get_frame(source_frame)
        target_frame = self.get_frame(target_frame)
        if source_frame is None or target_frame is None:
            return
        if target_frame.name in self._links.get(source_frame.name, ()):
            return Many2OneLink(
                *self._get_link_columns(
                    source_frame,
                    target_frame
                )
            )
        if source_frame.name in self._links.get(target_frame.name, ()):
            return One2ManyLink(
                *self._get_link_columns(
                    target_frame,
                    source_frame
                )
            )
        for table_name in self._frames:
            if {source_frame.name, target_frame.name}.issubset(self._links.get(table_name, set())):
                return Many2ManyLink(
                    *self._get_link_columns(
                        source_frame,
                        target_frame,
                        intermediate_frame=self._frames.get(table_name)
                    )
                )

    def get_column(
        self,
        frame_name: str,
        field_name: str,
        prefix: str | None = None,
        alias: str | None = None
    ) -> sqlalchemy.Column | None:
        frame = self.get_frame(frame_name)
        if frame is None:
            return
        column = getattr(frame.c, field_name)
        if prefix is not None:
            column = column.label(f'{prefix}__{field_name}')
        elif alias:
            column = column.label(alias)
        return column

    def get_frame(self, frame_name: str) -> sqlalchemy.Table | None:
        return self._frames.get(frame_name)

    def get_primary_key(self, frame_name: str) -> sqlalchemy.Column | None:
        frame = self.get_frame(frame_name)
        if frame.primary_key is None:
            return
        if len(frame.primary_key) > 1:
            return
        for column in frame.primary_key.columns:
            return column

    def _get_link_columns(
        self,
        source_frame: sqlalchemy.Table,
        target_frame: sqlalchemy.Table,
        intermediate_frame: sqlalchemy.Table | None = None
    ) -> tuple[sqlalchemy.Column, ...]:
        if intermediate_frame is not None:
            intermediate_source_key, source_key = self._get_link_columns(intermediate_frame, source_frame)
            intermediate_target_key, target_key = self._get_link_columns(intermediate_frame, target_frame)
            return source_key, target_key, intermediate_source_key, intermediate_target_key

        for fk in source_frame.foreign_keys:
            if fk.column.table == target_frame:
                return fk.parent, fk.column
