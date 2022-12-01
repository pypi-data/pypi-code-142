import typing
import collections.abc

from .identity import IdentifierType
from .interaction import Message, MessageContext, MessageContextMap

ActorState = collections.abc.Mapping


class Actor(typing.Protocol):
    __message_context_map__: MessageContextMap

    def __receive__(
        self,
        message: Message,
        context: MessageContext | None = None
    ) -> collections.abc.Iterable[Message] | None: ...

    @classmethod
    def __messages_subscription__(cls) -> set[type[Message]]: ...

    def __identifier__(self) -> IdentifierType: ...

    def __state__(self) -> ActorState: ...

    def __serialize__(self) -> collections.abc.Mapping | None: ...


class ActorRepository(typing.Protocol):
    async def get(self, identifier: IdentifierType) -> Actor: ...

    async def save(self, identifier: IdentifierType, data: ActorState) -> typing.NoReturn: ...
