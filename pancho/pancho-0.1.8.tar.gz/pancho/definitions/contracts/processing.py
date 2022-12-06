import collections.abc
import typing

from .interaction import Message, MessageStream
from .operations import Actor, ActorRepository
from .integrity import UnitOfWork

MessageActorMap = collections.abc.MutableMapping[type[Message], set[Actor]]
ActorRepositoryMap = collections.abc.Mapping[type[Actor], type[ActorRepository]]


class CommandProcessor(typing.Protocol):
    async def __aenter__(self) -> 'CommandProcessor': ...

    async def __aexit__(self, exc_type, exc_val, exc_tb): ...

    async def receive(self, *message: Message): ...

    def get_message_stream(self) -> MessageStream: ...

    async def commit(self): ...

    async def shutdown(self): ...


class CommandProcessorSettings(typing.Protocol):
    register_events: bool = True
    auto_commit: bool = True


class CommandProcessorFactory(typing.Protocol):
    def get_instance(
        self,
        settings: CommandProcessorSettings
    ) -> CommandProcessor: ...
