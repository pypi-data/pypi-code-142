from abc import ABC, abstractmethod
from inspect import signature


class Listenable(ABC):
    @abstractmethod
    def value(self):
        pass

    @abstractmethod
    def listen(self, listener):
        pass

    @abstractmethod
    def dispose(self):
        pass


def verify_listener(listener):
    assert(callable(listener)), \
        "A listener must be callable"
    t = signature(listener)
    assert(t.parameters), \
        "A listener must have one parameter to accept value"


class StateNotifier(Listenable):
    def __init__(self, value=None) -> None:
        self.__value = value
        self.__i = 0
        self.__listeners = dict()

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, o):
        self.__value = o
        self.notify_listeners()

    def notify_listeners(self):
        for key in self.__listeners:
            try:
                self.__listeners[key](self.value)
            except Exception as e:
                print(e)

    def listen(self, listener):
        verify_listener(listener)
        self.__listeners[self.__i] = listener
        def remove_listener_callback(): return self.__listeners.pop(self.__i)
        self.__i += 1
        return remove_listener_callback

    def dispose(self):
        self.__listeners.clear()
