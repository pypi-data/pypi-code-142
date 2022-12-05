import operator

import sqlalchemy
import sqlalchemy.ext.asyncio
import sqlalchemy.dialects
import sqlalchemy.sql

from .generic import Many2OneLink
from ...definitions import contracts


def _extract_vendor_and_field_names(field_name: str, default_frame: str):
    return field_name.split('.') if '.' in field_name else (default_frame, field_name)


class FilterBuilder:
    def __init__(self, default_frame: str | None = None):
        self._default_frame = default_frame

    def __call__(
        self,
        clause: contracts.FilterClause
    ):
        result = []
        for field_token, value in clause.items():
            if ':' in field_token:
                field_name, operation = field_token.split(':')
            else:
                operation = 'eq'
                field_name = field_token

            vendor_name, field_name = _extract_vendor_and_field_names(field_name, self._default_frame)

            result.append(
                contracts.FilterClauseElement(
                    vendor_name=vendor_name,
                    field_name=field_name,
                    operator=self._operation_map.get(operation),
                    value=value
                )
            )
        return result

    @property
    def _operation_map(self):
        return {
            'eq': operator.eq,
            'gt': operator.gt,
            'lt': operator.lt,
            'ge': operator.ge,
            'le': operator.le,
            'ne': operator.ne,
            'in': lambda c, v: c.in_(v),
            'is': lambda c, v: c.is_(v),
            'isnot': lambda c, v: c.is_not(v),
            'like': lambda c, v: c.like(f"%{v}%"),
            'notlike': lambda c, v: c.not_like(f"%{v}%"),
            'ilike': lambda c, v: c.ilike(f"%{v}%"),
            'notilike': lambda c, v: c.not_ilike(f"%{v}%")
        }


class QueryBuilder:
    def __init__(self, registry: contracts.DataFrameRegistry):
        self._registry = registry
        self._joins = []

    def __call__(self, node: contracts.Node, with_total: bool = False) -> sqlalchemy.sql.ClauseElement:
        fields = self._collect_fields(node)
        filters = self._collect_filters(node)

        if with_total:
            fields.append(sqlalchemy.text(f'count(*) OVER() as _total_'))

        stmt = sqlalchemy.select(fields)

        if self._joins:
            j = None
            for source, target in self._joins:
                j = (source if j is None else j).join(
                    target,
                    onclause=self._get_m2o_link_clause(source, target),
                    isouter=True
                )
            stmt = stmt.select_from(j)

        for filter_clause_element in filters or ():
            column = self._registry.get_column(
                frame_name=filter_clause_element.vendor_name,
                field_name=filter_clause_element.field_name
            )
            if column is not None:
                stmt = stmt.where(filter_clause_element.operator(column, filter_clause_element.value))

        for sort_field, sort_direction in (node.sort or {}).items():
            vendor_name, field_name = _extract_vendor_and_field_names(sort_field, node.relation)
            column = self._registry.get_column(
                frame_name=vendor_name,
                field_name=field_name
            )
            if column is not None:
                stmt = stmt.order_by(self._sort_direction_map[sort_direction](column))

        if node.limit:
            stmt = stmt.limit(node.limit)

        if node.offset:
            stmt = stmt.offset(node.offset)

        return stmt

    def _collect_fields(
        self,
        node: contracts.Node,
        parent_node: contracts.Node | None = None,
        prefix: str | None = None,
        fields: list[sqlalchemy.Column] | None = None
    ) -> list[sqlalchemy.Column] | None:
        fields = fields or []
        if parent_node:
            if not isinstance(self._registry.get_link(parent_node.relation, node.relation), Many2OneLink):
                return
            self._joins.append(
                (self._registry.get_frame(parent_node.relation), self._registry.get_frame(node.relation))
            )

        for field in node.fields:
            if isinstance(field, contracts.Field):
                if field.expression is not None:
                    _column = field.expression
                else:
                    _column = self._registry.get_column(
                        field.relation or node.relation,
                        field.name,
                        prefix
                    )
                fields.append(_column)
            elif isinstance(field, contracts.Node):
                self._collect_fields(
                    node=field,
                    parent_node=node,
                    prefix=f'{prefix}__{field.relation}' if prefix is not None else field.qualified_name,
                    fields=fields
                )
        return fields

    def _collect_filters(self, node: contracts.Node) -> list[contracts.FilterClauseElement] | None:
        if not node.filter:
            return

        for field_token, value in node.filter.items():
            vendor_name, field_name = _extract_vendor_and_field_names(field_token, node.relation)
            if (
                vendor_name != node.relation
                and
                vendor_name not in (j[0] for j in self._joins)
                and
                isinstance(
                    link := self._registry.get_link(vendor_name, node.relation),
                    Many2OneLink
                )
            ):
                self._joins.append(
                    (self._registry.get_frame(node.relation), link.source_key.table)
                )

        return FilterBuilder(node.relation)(node.filter)

    @staticmethod
    def _get_m2o_link_clause(source_table: sqlalchemy.Table, target_table: sqlalchemy.Table):
        for fk in source_table.foreign_keys:
            if fk.column.table == target_table:
                return sqlalchemy.sql.expression.BinaryExpression(fk.parent, fk.column, operator.eq)

    @property
    def _sort_direction_map(self):
        return {
            'asc': sqlalchemy.asc,
            'desc': sqlalchemy.desc
        }
