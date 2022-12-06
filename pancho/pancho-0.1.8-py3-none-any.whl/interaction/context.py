import abc

from ..definitions import contracts


class MessageContext(contracts.MessageContext):
    def __init__(self):
        self._result = None

    @abc.abstractmethod
    async def __produce__(self, message: contracts.Message) -> 'MessageContext': ...

    def get(self):
        return self._result
