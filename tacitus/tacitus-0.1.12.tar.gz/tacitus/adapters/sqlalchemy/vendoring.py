import functools
import typing

from .obtaining import SqlAlchemyQueryResolver, QueryResultProxy
from .saving import SqlAlchemyMutationResolver
from ...definitions import contracts


class SqlAlchemyVendor(contracts.DataVendor):
    def __init__(
        self,
        registry: contracts.DataFrameRegistry,
        connection: contracts.DataVendorConnection
    ):
        self._registry = registry
        self._connection = connection

    @functools.cached_property
    def _query_resolver(self):
        return SqlAlchemyQueryResolver(
            registry=self._registry,
            connection=self._connection
        )

    @functools.cached_property
    def _mutation_resolver(self):
        return SqlAlchemyMutationResolver(
            registry=self._registry,
            connection=self._connection
        )

    async def get(self, query: contracts.Query | None = None) -> QueryResultProxy | None:
        if query is None:
            return

        data = await self._query_resolver.resolve_query(query)
        total = None

        if query.with_total:
            data, total = data

        return QueryResultProxy(
            data=data,
            total=total
        )

    async def save(self, data: contracts.MutationData) -> typing.NoReturn:
        if data:
            await self._mutation_resolver.save(data)


