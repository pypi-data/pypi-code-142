from typing import Optional, Iterable, Tuple

class Cache:
    def __init__(self) -> None:
        self._data = {}

    def get(self, key: bytes) -> Optional[bytes]:
        return self._data.get(key)

    def set(self, key: bytes, value: bytes) -> None:
        self._data[key] = value

    def decrement(self, key: bytes) -> bytes:
        try:
            v = int(self._data.get(key, b'0').decode()) - 1
        except:
            v = -1
        v = str(v).encode()
        self._data[key] = v
        return v
    
    def increment(self, key: bytes) -> bytes:
        try:
            v = int(self._data.get(key, b'0').decode()) + 1
        except:
            v = 1
        v = str(v).encode()
        self._data[key] = v
        return v

    def clear(self) -> None:
        self._data = {}

    def drop(self, key: bytes) -> bool:
        if key in self._data:
            self._data.pop(key)
            return True
        else:
            return False

    def exists(self, key: bytes) -> bool:
        return key in self._data

    def count(self) -> int:
        return len(self._data)

    def keys(self) -> Iterable[bytes]:
        for key, _ in self._data.items():
            yield key

    def items(self) -> Iterable[Tuple[bytes, bytes]]:
        for key, value in self._data.items():
            yield key, value
