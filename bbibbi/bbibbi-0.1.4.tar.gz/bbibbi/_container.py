from typing import Any
from ._symbol import Symbol


class Container:
    def __init__(self) -> None:
        self.instances = {}

    def register(self, key: Symbol, instance: Any) -> None:
        if self.instances.get(key) is None:
            self.instances[key] = instance

    def get(self, key: Symbol):
        return self.instances.get(key)

    def clear(self) -> None:
        self.instances = {}

    def remove(self, key: Symbol):
        self.instances.pop(key)
