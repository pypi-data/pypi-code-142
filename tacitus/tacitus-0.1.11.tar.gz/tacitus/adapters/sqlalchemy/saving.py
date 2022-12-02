import collections.abc
import datetime
import operator
import asyncio

import sqlalchemy.ext.asyncio
import sqlalchemy.dialects.postgresql
from .building import FilterBuilder
from .registration import Many2ManyLink, One2ManyLink
from ...definitions import contracts, exceptions

StoringDataType = collections.abc.Mapping | collections.abc.Sequence[collections.abc.Mapping]


class SqlAlchemyMutationResolver:
    def __init__(
        self,
        registry: contracts.DataFrameRegistry,
        connection: sqlalchemy.ext.asyncio.AsyncConnection
    ):
        self._registry = registry
        self._connection = connection

    async def save(
        self,
        data: contracts.MutationData
    ):
        return await self._resolve(data)

    async def insert(
        self,
        data: contracts.MutationData
    ):
        if len(data) != 1:
            raise exceptions.ConstraintException(f'Data must be single key dict with dict as value')

        table, values = self._get_table_and_values(data)
        await self._connection.execute(
            sqlalchemy.insert(table).values(values)
        )

    async def update(
        self,
        data: contracts.MutationData
    ):
        if len(data) != 1:
            raise exceptions.ConstraintException(f'Data must be single key dict with dict as value')

        table, values = self._get_table_and_values(data)
        pk = self._get_pk(table.name, values)
        await self._connection.execute(
            sqlalchemy.update(table).values(values).where(pk=data.get(pk.name))
        )

    async def delete(self, clause: contracts.FilterClause):
        _map = collections.defaultdict(dict)
        for field_token, value in clause.items():
            if '.' not in field_token:
                continue
            table, field = field_token.split('.')
            _map[table][field] = value

        for table, clause in _map.items():
            await self._delete(table, FilterBuilder(table)(clause))

    async def _resolve(
        self,
        data: contracts.MutationData,
        parent_key: str | None = None
    ):
        _data = {}
        _tasks = []
        for field_name, field_value in data.items():
            if isinstance(field_value, collections.abc.MutableSequence):
                link = self._registry.get_link(source_frame=parent_key, target_frame=field_name)
                if isinstance(link, Many2ManyLink):
                    _tasks.append(self._save_collection(
                        table=link.target_key.table,
                        data=field_value
                    ))
                    _tasks.append(self._save_collection(
                        table=link.intermediate_target_key.table,
                        data=[
                            {
                                link.intermediate_source_key.name: data.get(link.source_key.name),
                                link.intermediate_target_key.name: row.get(link.target_key.name)
                            }
                            for row in field_value
                        ],
                        purge_filter=[
                            contracts.FilterClauseElement(
                                vendor_name=link.intermediate_target_key.table.name,
                                field_name=link.intermediate_source_key.name,
                                value=data.get(link.source_key.name),
                                operator=operator.eq
                            )
                        ]
                    ))
                elif isinstance(link, One2ManyLink):
                    _pk = self._registry.get_primary_key(link.source_key.table.name)
                    _purge_filter = None
                    for row in field_value:
                        if link.source_key.name not in row:
                            row[link.source_key.name] = data.get(link.target_key.name)
                        if _purge_filter is None and (_pk is None or row.get(_pk) is None):
                            _purge_filter = [
                                contracts.FilterClauseElement(
                                    vendor_name=link.source_key.table.name,
                                    field_name=link.source_key.name,
                                    value=data.get(link.target_key.name),
                                    operator=operator.eq
                                )
                            ]

                    _tasks.append(self._save_collection(
                        table=link.source_key.table,
                        data=field_value,
                        purge_filter=_purge_filter
                    ))
                continue
            elif isinstance(field_value, collections.abc.MutableMapping):
                await self._resolve(field_value, parent_key=field_name)
                continue
            else:
                _data[field_name] = field_value

        if (table := self._registry.get_frame(parent_key)) is not None:
            await self._save_object(table, _data)
        if _tasks:
            await asyncio.gather(*_tasks)

    async def _save_collection(
        self,
        table: sqlalchemy.Table,
        data: collections.abc.Sequence[collections.abc.Mapping],
        purge_filter: collections.abc.Sequence[contracts.FilterClauseElement] | None = None
    ):
        await self._delete(table, purge_filter)
        if not data:
            return

        _pk = self._registry.get_primary_key(table.name)
        if _pk is None or data[0].get(_pk.name) is None:
            await self._connection.execute(
                sqlalchemy.insert(table).values(data)
            )
        else:
            data = {row.get(_pk.name): row for row in data}
            _given = set(data.keys())
            _exists = set()

            if data:
                result = await self._connection.execute(
                    sqlalchemy.select([_pk]).where(_pk.in_(list(data.keys())))
                )
                _exists = set(r[_pk.name] for r in result)

            _to_insert = _given - _exists
            _to_update = _given & _exists
            _to_delete = _exists - _given

            if _to_insert:
                await self._connection.execute(
                    sqlalchemy.insert(table).values([
                        data[_id] for _id in _to_insert
                    ])
                )

            if _to_update:
                for _id in _to_update:
                    await self._connection.execute(
                        sqlalchemy.update(table).values(data[_id]).where(_pk == _id)
                    )

            if _to_delete:
                await self._delete(
                    table=table,
                    filter_clause=[
                        contracts.FilterClauseElement(
                            vendor_name=table.name,
                            field_name=_pk,
                            value=list(_to_delete),
                            operator=lambda c, v: c.in_(v)
                        )
                    ]
                )

    async def _save_object(self, table: sqlalchemy.Table, data: collections.abc.MutableMapping):
        insert_stmt = sqlalchemy.dialects.postgresql.insert(table)
        if data.get('created_at', ...) is None:
            del data['created_at']
        await self._connection.execute(insert_stmt.on_conflict_do_update(
            index_elements=[self._get_pk(table.name, data)],
            set_=dict(insert_stmt.excluded)
        ), data)

    async def _delete(
        self,
        table: sqlalchemy.Table,
        filter_clause: collections.abc.Sequence[contracts.FilterClauseElement]
    ):
        if not filter_clause:
            return
        if hasattr(table.c, 'deleted_at'):
            stmt = sqlalchemy.update(table).values(deleted_at=datetime.datetime.utcnow())
        else:
            stmt = sqlalchemy.delete(table)
        for _element in filter_clause:
            stmt = stmt.where(_element.operator(getattr(table.c, _element.field_name), _element.value))
        await self._connection.execute(stmt)

    def _get_table_and_values(self, data: contracts.MutationData):
        table_name, values = next(iter(data.items()))
        if not isinstance(values, collections.abc.MutableMapping):
            raise exceptions.ConstraintException(f'Data must be single key dict with dict as value: {table_name}')

        table = self._registry.get_frame(table_name)
        if table is None:
            raise exceptions.NotFoundException(f'Table not found: {table_name}')

        return table, values

    def _get_pk(self, table_name: str, data: collections.abc.Mapping) -> sqlalchemy.Column | None:
        pk = self._registry.get_primary_key(table_name)
        if pk is None:
            raise exceptions.ConstraintException(
                f"Cannot save object to table without or compound primary key: {table_name}"
            )
        if not data.get(pk.name):
            raise exceptions.ConstraintException(
                f"Data must contains primary key to be automatically saved: {table_name}"
            )
        return pk
