import dataclasses
import typing
import collections.abc

from pancho.definitions import contracts
from pancho.interaction.messages import ExceptionEvent


class MessageStream:
    def __init__(self, data: collections.abc.Sequence[contracts.Message]):
        self._data = data
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._data):
            raise StopIteration
        result = self._data[self._index]
        self._index += 1
        return result

    def has_exception_event(self) -> bool:
        return any(isinstance(message, ExceptionEvent) for message in self._data)

    def filter(self, clause: typing.Callable[[contracts.Message], bool]) -> 'MessageStream':
        self._data = list(filter(clause, self._data))
        return self


class MessageCollector:
    def __init__(self, messages: collections.abc.Iterable[contracts.Message] | None = None):
        self._data = messages or []
        self._index = 0

    def append(self, message: contracts.Message | None):
        if message:
            self._data.append(message)

    def extend(self, messages: collections.abc.Iterable[contracts.Message] | None):
        if messages:
            self._data.extend(messages)

    def pop(self) -> contracts.Message | None:
        if self._index >= len(self._data):
            return
        result = self._data[self._index]
        self._index += 1
        return result

    def get_stream(self) -> MessageStream:
        return MessageStream(self._data)


@dataclasses.dataclass
class ProcessorSettings:
    register_events: bool = True
    auto_commit: bool = True
