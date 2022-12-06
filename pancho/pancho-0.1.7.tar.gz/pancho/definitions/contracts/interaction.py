import collections.abc
import typing
import datetime

from .identity import IdentifierType


@typing.runtime_checkable
class Command(typing.Protocol):
    def __init__(
        self,
        id: IdentifierType,
        actor_id: IdentifierType,
        created_at: datetime.datetime,
        **payload
    ): ...


@typing.runtime_checkable
class Event(typing.Protocol):
    def __init__(
        self,
        id: IdentifierType,
        actor_id: IdentifierType,
        created_at: datetime.datetime,
        **context
    ): ...


Message = Command | Event


class CommandProducer(typing.Protocol):
    def bind(
        self,
        command_contract: type[Command],
        clause: typing.Callable[[], bool] | None = None,
        fields_map: collections.abc.Mapping[str, str] | None = None
    ): ...

    def get(self) -> typing.Generator[type[Command], None, None]: ...


class EventProducer(typing.Protocol):
    def bind(
        self,
        event_contract: type[Event]
    ): ...

    def get(self) -> typing.Generator[type[Event], None, None]: ...


class InteractionFactory(typing.Protocol):
    def get_command_producer(
        self,
        actor_id: IdentifierType | None = None,
        payload: collections.abc.Mapping | None = None
    ) -> CommandProducer: ...

    def get_event_producer(
        self,
        actor_id: IdentifierType,
        context: collections.abc.Mapping | None = None
    ) -> EventProducer: ...


class MessageStream(typing.Protocol):
    def __iter__(self): ...

    def __next__(self): ...

    def has_error_event(self) -> bool: ...

    def filter(self, clause: typing.Callable[[Message], bool]) -> 'MessageStream': ...


class EventRegistrator(typing.Protocol):
    async def register(self, stream: MessageStream): ...


class MessageContext(typing.Protocol):
    async def __call__(self, message: Message): ...


MessageContextMap = collections.abc.MutableMapping[type[Message], type[MessageContext]]
