import collections.abc
import typing
import dataclasses

IdentifierType = typing.Any

DataFrame = typing.Any
DataFrameColumn = typing.Any

DataVendorName = str
FieldName = str
FieldValue = typing.Any

FilterClause = collections.abc.Mapping
FilterClauseOperation = typing.Callable

SortDirection = typing.Literal['asc', 'desc']
SortClause = collections.abc.Mapping[FieldName, SortDirection]

FilterClauseElement = tuple[FieldName, FilterClauseOperation, FieldValue]

ConnectionData = typing.Any
MutationData = collections.abc.Mapping


class DataFrameLink(typing.Protocol):
    source_key: DataFrameColumn
    target_key: DataFrameColumn


@dataclasses.dataclass
class FilterClauseElement:
    vendor_name: DataVendorName
    field_name: FieldName
    operator: FilterClauseOperation
    value: FieldValue


@dataclasses.dataclass(eq=True)
class Field:
    name: str
    alias: str | None = None
    relation: str | None = None
    expression: str | None = None


@dataclasses.dataclass
class Node:
    relation: str
    fields: collections.abc.MutableSequence[Field]
    name: str | None = None
    filter: FilterClause | None = None
    sort: SortClause | None = None
    limit: int | None = None
    offset: int | None = None
    modifier: typing.Callable = None

    @property
    def qualified_name(self):
        return self.name or self.relation


@dataclasses.dataclass
class Query:
    root_node: Node
    with_total: bool = False


class DataFrameRegistry(typing.Protocol):
    def get_link(
        self,
        source_frame: str,
        target_frame: str
    ) -> DataFrameLink: ...

    def get_column(
        self,
        frame_name: str,
        field_name: str,
        prefix: str | None = None,
        alias: str | None = None
    ) -> DataFrameColumn:
        ...

    def get_frame(self, frame_name: str) -> DataFrame:
        ...

    def get_primary_key(self, frame_name: str) -> DataFrameColumn | None:
        ...


class QueryResultProxy(typing.Protocol):
    def get_all(self): ...

    def get_one(self): ...

    def get_total(self): ...


class DataVendor(typing.Protocol):
    async def get(self, query: Query | None = None) -> QueryResultProxy | None: ...

    async def save(
        self,
        data: MutationData
    ) -> typing.NoReturn: ...

    async def insert(
        self,
        data: MutationData
    ) -> typing.NoReturn: ...

    async def update(
        self,
        data: MutationData
    ) -> typing.NoReturn: ...

    async def delete(
        self,
        filter_clause: FilterClause
    ) -> typing.NoReturn: ...


class DataVendorConnection(typing.Protocol):
    async def execute(self, data: ConnectionData): ...


class DataVendorConnectionPool(typing.Protocol):
    async def get_connection(self) -> DataVendorConnection: ...

    async def close_connection(self, connection: DataVendorConnection): ...
