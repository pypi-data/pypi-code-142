from contextlib import AbstractAsyncContextManager, asynccontextmanager
from dataclasses import dataclass
from typing import Callable, Dict, List, Mapping, Optional

from elasticsearch import AsyncElasticsearch

from dropland.engines.base import AsyncEngine, EngineBackend
from dropland.log import logger, tr

Connection = AsyncElasticsearch


@dataclass
class EngineConfig:
    url: str


class ElasticSearchBackend(EngineBackend):
    def __init__(self):
        self._engines: Dict[str, 'ElasticSearchEngine'] = dict()

    @property
    def name(self) -> str:
        return 'elasticsearch'

    # noinspection PyMethodOverriding
    def create_engine(self, name: str, config: EngineConfig) -> 'ElasticSearchEngine':
        if engine := self._engines.get(name):
            return engine

        engine = ElasticSearchEngine(self, name, config)
        self._engines[name] = engine
        logger.info(tr('dropland.engines.es.engine.created').format(name=name))
        return engine

    def get_engine(self, name: str) -> Optional['ElasticSearchEngine']:
        return self._engines.get(name)

    def get_engine_names(self) -> List[str]:
        return list(self._engines.keys())

    def get_engines(self, names: Optional[List[str]] = None) -> Mapping[str, 'ElasticSearchEngine']:
        engines = dict()

        if not names:
            names = self.get_engine_names()

        for name in names:
            if engine := self.get_engine(name):
                engines[name] = engine

        return engines


class ElasticSearchEngine(AsyncEngine[Connection]):
    def __init__(self, backend: ElasticSearchBackend, name: str, config: EngineConfig):
        super().__init__(backend, name)
        self._config = config
        self._es = AsyncElasticsearch(config.url)

    @asynccontextmanager
    async def session(self, *args, **kwargs) -> Callable[..., AbstractAsyncContextManager[Connection]]:
        async with self._es as conn:
            yield conn

    async def start(self):
        pass

    async def stop(self):
        pass
