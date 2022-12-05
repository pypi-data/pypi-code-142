import collections.abc
import typing
import uuid
from dateutil.parser import parse as datetime_parser

import sqlalchemy.ext.asyncio
import sqlalchemy.sql

from .generic import One2ManyLink, Many2ManyLink
from .building import QueryBuilder
from ...definitions import contracts, exceptions


class QueryResultProxy(contracts.QueryResultProxy):
    def __init__(
        self,
        data: collections.abc.Sequence[collections.abc.Mapping],
        total: int | None = None
    ):
        self._data = data
        self._total = total

    def get_all(self) -> collections.abc.Sequence[collections.abc.Mapping] | None:
        if len(self._data) > 0:
            return self._data

    def get_one(self) -> collections.abc.Mapping | None:
        if _data := self.get_all():
            return _data[0]

    def get_total(self) -> int | None:
        return self._total


class SqlAlchemyQueryResolver:
    def __init__(
        self,
        registry: contracts.DataFrameRegistry,
        connection: sqlalchemy.ext.asyncio.AsyncConnection
    ):
        self._registry = registry
        self._connection = connection

    async def resolve_query(
        self,
        query: contracts.Query,
        index_by: str | None = None,
        remove_index_field: bool = False,
    ):
        node = query.root_node
        # Getting nested nodes to further calculations and attach key fields to node if necessary
        nested_nodes = self._get_nested_nodes(node)

        stmt = QueryBuilder(registry=self._registry)(node, query.with_total)
        result = await self._connection.execute(stmt)

        # Processing result of node query
        data = []
        total = 0
        for row in result:
            if query.with_total:
                total = row._mapping['_total_']
            for _node in nested_nodes.values():
                # collect ids of current node as parent_ids for nested node
                _node['parent_ids'].append(
                    row._mapping[_node['index_field']]
                )
            # convert query result's row to final nested structure
            _nested_row = self._flattened_to_nested(row._mapping)
            # apply node's modifier if exists
            for _f in node.fields:
                if isinstance(_f, contracts.Node) and _f.modifier and _f.qualified_name in _nested_row:
                    _nested_row[_f.qualified_name] = _f.modifier(_nested_row[_f.qualified_name])
            data.append(_nested_row)

        # Processing nested nodes
        nested_data = {}
        for _name, _node in nested_nodes.items():
            _link = _node['link']
            _parent_ids = _node['parent_ids']
            _index_field = _node['index_field']
            _node = _node['node']
            _nested_key = None
            if isinstance(_link, Many2ManyLink):
                # attach nested node key field to index by
                _nested_key = _link.intermediate_source_key
                _remove_index_field = self._add_index_field(
                    node=_node,
                    field=contracts.Field(
                        name=_nested_key.name,
                        relation=_link.intermediate_source_key.table.name
                    )
                )
            elif isinstance(_link, One2ManyLink):
                _nested_key = _link.source_key
                _remove_index_field = self._add_index_field(
                    node=_node,
                    field=contracts.Field(
                        name=_nested_key.name,
                    )
                )
            else:
                raise exceptions.LinkException(f'Cannot find link between {node.relation} and {_name}')

            # attach to nested node filter condition with parent node ids
            if _parent_ids:
                _node.filter = (_node.filter or {}) | {f'{_nested_key}:in': _parent_ids}
                nested_data[(_node.name or _node.relation, _index_field)] = await self.resolve_query(
                    query=contracts.Query(root_node=_node),
                    index_by=_nested_key.name,
                    remove_index_field=_remove_index_field
                )

        # attach nested data to parent data
        for row in data:
            for _key, _nested_data in nested_data.items():
                row[_key[0]] = _nested_data.get(row[_key[1]])

        # index nested data set by parent id
        if index_by:
            _ = collections.defaultdict(list)
            for row in data:
                _index_key = row[index_by]
                if remove_index_field:
                    row = {k: v for k, v in row.items() if k != index_by}
                if node.modifier:
                    row = node.modifier(row)
                _[_index_key].append(row)
            data = _

        return (data, total) if query.with_total else data

    def _get_nested_nodes(self, node: contracts.Node) -> dict[str, dict]:
        nested_nodes = {}
        for field in node.fields:
            if (
                isinstance(field, contracts.Node) and
                type(link := self._registry.get_link(node.relation, field.relation)) in (
                Many2ManyLink, One2ManyLink)
            ):
                index_field = link.source_key.name if isinstance(link, Many2ManyLink) else link.target_key.name
                nested_nodes[field.name or field.relation] = {
                    'link': link,
                    'parent_ids': [],
                    'node': field,
                    'index_field': index_field,
                    'remove_index_field': self._add_index_field(node, contracts.Field(name=index_field))
                }

        return nested_nodes

    @staticmethod
    def _add_index_field(node: contracts.Node, field: contracts.Field):
        for _ in node.fields:
            if isinstance(_, contracts.Field) and _ == field:
                return False
        node.fields.append(field)
        return True

    def _flattened_to_nested(self, data: collections.abc.Mapping):
        result = {}
        for key in data:
            if key.startswith('_') and key.endswith('_'):
                continue
            row = result
            for part in key.split('__')[:-1]:
                if part not in row:
                    row[part] = {}
                row = row[part]
            row[key.split('__')[-1]] = self._deserialize(data[key])
        return result

    def _deserialize(self, data: typing.Any):
        if not isinstance(data, collections.abc.Mapping):
            return data
        result = {}
        for k, v in data.items():
            if isinstance(v, collections.abc.Mapping):
                v = self._deserialize(v)
            else:
                for func in (uuid.UUID, datetime_parser):
                    try:
                        _v = func(v)
                        break
                    except:
                        _v = None
                v = _v or v
            result[k] = v
        return result
