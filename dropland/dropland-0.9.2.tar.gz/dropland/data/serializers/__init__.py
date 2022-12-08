from typing import Any, List, Mapping, Optional, Protocol


class Serializer(Protocol):
    def serialize(self, data: Optional[Any] = None) -> bytes:
        ...


class Deserializer(Protocol):
    def deserialize(self, data: bytes) -> Optional[Any]:
        ...


class ModelSerializer(Protocol):
    serializer: Serializer

    def serialize(self, only_fields: List[str] = None) -> bytes:
        return self.serializer.serialize(self.get_serializable_values(only_fields))

    def get_serializable_values(self, only_fields: List[str] = None) -> Optional[Mapping[str, Any]]:
        ...
