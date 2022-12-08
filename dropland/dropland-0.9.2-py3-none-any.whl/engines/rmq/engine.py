import asyncio
from contextlib import AbstractAsyncContextManager, asynccontextmanager
from dataclasses import dataclass
from typing import Callable, Dict, List, Mapping, Optional

import aio_pika
from aio_pika.pool import Pool

from dropland.engines.base import AsyncEngine, EngineBackend
from dropland.log import logger, tr

Connection = aio_pika.RobustChannel


@dataclass
class EngineConfig:
    url: str
    virtualhost: str = '/'
    timeout_seconds: int = 5
    pool_max_connections: int = 4
    pool_max_channels_per_connection: int = 100


class RmqEngineBackend(EngineBackend):
    def __init__(self):
        self._engines: Dict[str, 'RmqEngine'] = dict()

    @property
    def name(self) -> str:
        return 'rabbitmq'

    # noinspection PyMethodOverriding
    def create_engine(self, name: str, config: EngineConfig) -> 'RmqEngine':
        if engine := self._engines.get(name):
            return engine

        engine = RmqEngine(self, name, config)
        self._engines[name] = engine
        logger.info(tr('dropland.engines.rmq.engine.created').format(name=name))
        return engine

    def get_engine(self, name: str) -> Optional['RmqEngine']:
        return self._engines.get(name)

    def get_engine_names(self) -> List[str]:
        return list(self._engines.keys())

    def get_engines(self, names: Optional[List[str]] = None) -> Mapping[str, 'RmqEngine']:
        engines = dict()

        if not names:
            names = self.get_engine_names()

        for name in names:
            if engine := self.get_engine(name):
                engines[name] = engine

        return engines


class RmqEngine(AsyncEngine[Connection]):
    def __init__(self, backend: RmqEngineBackend, name: str, config: EngineConfig):
        super().__init__(backend, name)
        self._config = config
        self._lock = asyncio.Lock()
        self._conn_pool: Optional[Pool] = None
        self._chan_pool: Optional[Pool] = None
        self._counter = 0

    @asynccontextmanager
    async def session(self, *args, **kwargs) -> Callable[..., AbstractAsyncContextManager[Connection]]:
        async with self._chan_pool.acquire() as conn:
            yield conn

    async def start(self):
        async with self._lock:
            if 0 == self._counter:
                assert not self._conn_pool
                assert not self._chan_pool

                loop = asyncio.get_event_loop()
                self._conn_pool = Pool(self._get_connection, max_size=self._config.pool_max_connections, loop=loop)
                self._chan_pool = Pool(self._get_channel, max_size=self._config.pool_max_channels_per_connection, loop=loop)
                logger.info(tr('dropland.engines.rmq.engine.started').format(name=self.name))

            self._counter += 1

    async def stop(self):
        async with self._lock:
            if 1 == self._counter:
                assert self._conn_pool
                assert self._chan_pool

                await self._chan_pool.close()
                await self._conn_pool.close()

                self._conn_pool = self._chan_pool = None
                logger.info(tr('dropland.engines.rmq.engine.stopped').format(name=self.name))

            self._counter = max(self._counter - 1, 0)

    async def _get_connection(self) -> aio_pika.abc.AbstractRobustConnection:
        return await aio_pika.connect_robust(
            self._config.url, virtualhost=self._config.virtualhost,
            timeout=self._config.timeout_seconds
        )

    async def _get_channel(self) -> aio_pika.Channel:
        async with self._conn_pool.acquire() as connection:
            return await connection.channel()
