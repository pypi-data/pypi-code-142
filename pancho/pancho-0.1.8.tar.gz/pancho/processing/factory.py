import collections.abc
import functools
from .instance import Processor
from .generic import ProcessorSettings
from ..definitions import contracts


class ProcessorFactory(contracts.CommandProcessorFactory):
    def __init__(
        self,
        dependency_registry: contracts.DependencyRegistry,
    ):
        self._dependency_container = dependency_registry.get_container()

    def get_instance(
        self,
        settings: contracts.CommandProcessorSettings = ProcessorSettings()
    ) -> Processor:
        return Processor(
            dependency_container=self._dependency_container,
            actor_repository_map=self._actor_repository_map,
            message_actor_map=self._message_actor_map,
            settings=settings
        )

    @functools.cached_property
    def _message_actor_map(self) -> contracts.MessageActorMap:
        result = collections.defaultdict(set)
        for actor in self._actor_repository_map.keys():
            for message_type in actor.__messages_subscription__():
                result[message_type].add(actor)
        return dict(result)

    @functools.cached_property
    def _actor_repository_map(
        self
    ) -> contracts.ActorRepositoryMap:
        return self._dependency_container.get_bindings().filter(
            clause=lambda c, r: contracts.ActorRepository in c.__mro__
        ).map(
            key_clause=lambda c, r: r.instance.actor_type,
            value_clause=lambda c, r: c
        ).items()
