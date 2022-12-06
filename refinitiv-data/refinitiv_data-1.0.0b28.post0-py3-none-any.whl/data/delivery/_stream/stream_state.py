from enum import Enum, unique, auto


@unique
class StreamState(Enum):
    Unopened = auto()
    Opening = auto()
    Opened = auto()
    Closing = auto()
    Closed = auto()
