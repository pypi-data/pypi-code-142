import datetime
import dataclasses
import typing

from ..definitions import contracts

UNSET = typing.cast(None, object())


def dump_payload(obj: contracts.Message, exclude_unset=True):
    return {
        k: v
        for k, v in obj.__dict__.items()
        if k not in ('id', 'actor_id', 'created_at') and not (exclude_unset and v is UNSET)
    }


def dump_message(obj: contracts.Message):
    return dataclasses.asdict(obj)


@dataclasses.dataclass
class Command(contracts.Command):
    id: contracts.IdentifierType
    actor_id: contracts.IdentifierType
    created_at: datetime.datetime = dataclasses.field(default_factory=datetime.datetime.utcnow)


@dataclasses.dataclass
class Event(contracts.Event):
    id: contracts.IdentifierType
    actor_id: contracts.IdentifierType
    created_at: datetime.datetime = dataclasses.field(default_factory=datetime.datetime.utcnow)


@dataclasses.dataclass(kw_only=True)
class ExceptionEvent(Event):
    code: int
    message: str


@dataclasses.dataclass(kw_only=True)
class UnexpectedError(ExceptionEvent):
    code: int = 500
    message: str
