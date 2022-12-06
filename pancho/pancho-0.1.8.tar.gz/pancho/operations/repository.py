import abc
import typing

from ..definitions import contracts, exceptions


class ActorRepository(contracts.ActorRepository, abc.ABC):
    actor_type: type[contracts.Actor] = None

    def __init__(self, data_vendor: contracts.DefaultDataVendor):
        self._data_vendor = data_vendor

    async def get(
        self,
        identifier: contracts.IdentifierType
    ) -> contracts.Actor:
        if (actor := type(self).actor_type) is None:
            raise exceptions.ActorTypeIsNotDefined(repository=self.__class__.__name__)
        state = {'id': identifier} | (await self._get_state(identifier) or {})
        return actor(**state)

    async def save(
        self,
        identifier: contracts.IdentifierType,
        data: contracts.ActorState
    ) -> typing.NoReturn:
        await self._save_state(data)

    @abc.abstractmethod
    async def _get_state(
        self,
        identifier: contracts.IdentifierType
    ) -> contracts.ActorState: ...

    @abc.abstractmethod
    async def _save_state(
        self,
        data: contracts.ActorState
    ) -> typing.NoReturn: ...
