import datetime
import functools
import abc
import collections.abc
import inspect
import dataclasses

from ..definitions import contracts


@dataclasses.dataclass
class ActorMaps:
    message_handler: dict = dataclasses.field(default_factory=dict)
    message_context: dict = dataclasses.field(default_factory=dict)


class Actor(contracts.Actor, abc.ABC):
    def __init__(
        self,
        identifier: contracts.IdentifierType
    ):
        self._id = identifier
        self._deleted_at = None

    def __receive__(
        self,
        message: contracts.Message,
        context: contracts.MessageContext | None = None
    ) -> collections.abc.Iterable[contracts.Event] | None:
        handler_method_name = self._maps.message_handler.get(type(message))
        if handler_method_name:
            method = getattr(self, handler_method_name)
            events = method(message, context) if context else method(message)
            return events

    @functools.cached_property
    def __message_context_map__(self) -> contracts.MessageContextMap:
        return self._maps.message_context

    @classmethod
    def __messages_subscription__(cls) -> set[type[contracts.Message]]:
        result = set()
        for member in inspect.getmembers(cls, predicate=inspect.isfunction):
            k = inspect.getfullargspec(member[1])
            if k.annotations:
                for v in k.annotations.values():
                    if hasattr(v, '__mro__') and (
                        contracts.Event in v.__mro__ or contracts.Command in v.__mro__
                    ):
                        result.add(v)
        return result

    def __identifier__(self) -> contracts.IdentifierType:
        return self._id

    def __state__(self) -> contracts.ActorState:
        """ This is very generic calculation of actor's sate, please fill free to adjust it for specific actors"""
        result = {}
        # getting annotations of actor __init__ for purpose of further investigation
        annotations = inspect.get_annotations(self.__init__)
        for k, v in self.__dict__.items():
            k = k[1:]
            # if internal variable is not presented in params of __init__ skip it
            if k != 'deleted_at' and k not in annotations:
                continue
            # if value is None and type of variable belongs to sequence type (list, tuple, etc)
            # then assign empty list as default value
            if v is None:
                for s in ('list', 'tuple', 'collections'):
                    if s in str(annotations.get(k)):
                        v = []
            result[k] = v
        return result

    def __serialize__(self) -> collections.abc.Mapping | None:
        try:
            state = self.__state__()
            if not state:
                return None
            return state
        except Exception as e:
            raise e

    @functools.cached_property
    def _maps(self) -> ActorMaps:
        message_handler_map = {}
        message_context_map = {}
        for member in inspect.getmembers(type(self), predicate=inspect.isfunction):
            k = inspect.getfullargspec(member[1])
            message_contract = None
            if k.annotations:
                for v in k.annotations.values():
                    if hasattr(v, '__mro__') and (contracts.Event in v.__mro__ or contracts.Command in v.__mro__):
                        message_contract = v
                        message_handler_map[message_contract] = member[0]
                for v in k.annotations.values():
                    if hasattr(v, '__mro__') and (dict in v.__mro__):
                        message_context_map[message_contract] = v
        return ActorMaps(
            message_handler=message_handler_map,
            message_context=message_context_map
        )

    def _mark_as_deleted(self):
        self._deleted_at = datetime.datetime.utcnow()
