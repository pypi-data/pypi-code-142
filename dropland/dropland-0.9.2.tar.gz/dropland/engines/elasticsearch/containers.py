from dependency_injector import containers, providers

from dropland.app.base import ContainerResource
from .engine import ElasticSearchBackend, EngineConfig


class ElasticSearchResource(ContainerResource):
    def get_engine(self, *args, **kwargs):
        if isinstance(self.container, SingleElasticSearchContainer) \
                or 'SingleElasticSearchContainer' == self.container.parent_name:
            return self.container.create_engine()
        return self.container.create_engine(*args, **kwargs)


class ElasticSearchContainer(containers.DeclarativeContainer):
    __self__ = providers.Self()
    engine_factory = providers.Singleton(ElasticSearchBackend)

    def _create_engine(self, *args, **kwargs):
        return self.engine_factory().create_engine(*args, **kwargs)

    create_engine = providers.Factory(_create_engine, __self__)
    instance = providers.Singleton(ElasticSearchResource, __self__)


class SingleElasticSearchContainer(ElasticSearchContainer):
    __self__ = providers.Self()
    config = providers.Configuration()

    def _create_engine(self):
        if isinstance(self.config.engine_config(), EngineConfig):
            engine_config = self.config.engine_config()
        else:
            engine_config = EngineConfig(
                url=self.config.engine_config.url(),
            )
        return ElasticSearchContainer._create_engine(self, self.config.name(), engine_config)

    create_engine = providers.Factory(_create_engine, __self__)
    instance = providers.Singleton(ElasticSearchResource, __self__)


class MultipleElasticSearchContainer(ElasticSearchContainer):
    __self__ = providers.Self()
    config = providers.Configuration()

    def _create_engine(self, name: str):
        if conf := self.config.get(name):
            if isinstance(conf['engine_config'], EngineConfig):
                engine_config = conf['engine_config']
            else:
                engine_config = EngineConfig(
                    url=conf['engine_config']['url'],
                )
            return ElasticSearchContainer._create_engine(self, name, engine_config)
        return None

    create_engine = providers.Factory(_create_engine, __self__)
    instance = providers.Singleton(ElasticSearchResource, __self__)
