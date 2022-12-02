import typing
import sqlalchemy.ext.asyncio


class SqlalchemyConnectionPool:
    def __init__(self, dsn: str, echo: bool = True, auto_commit: bool = False):
        self._engine = sqlalchemy.ext.asyncio.create_async_engine(dsn, echo=echo)
        self._auto_commit = auto_commit

    async def get_connection(self):
        connection = sqlalchemy.ext.asyncio.AsyncConnection(self._engine)
        await connection.start()
        if self._auto_commit:
            await connection.begin()
        return connection

    async def commit(
        self,
        connection: sqlalchemy.ext.asyncio.AsyncConnection
    ):
        if self._auto_commit:
            await connection.commit()
        await connection.close()

    async def rollback(
        self,
        connection: sqlalchemy.ext.asyncio.AsyncConnection,
        exc_type: typing.Any | None = None
    ):
        if self._auto_commit:
            await connection.rollback()
        await connection.close()
