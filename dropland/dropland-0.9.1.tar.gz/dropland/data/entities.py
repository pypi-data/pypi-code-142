from typing import Protocol, runtime_checkable


@runtime_checkable
class EntityBase(Protocol):
    pass


class Entity(EntityBase):
    class Meta:
        pass

    def __init__(self, **kwargs):
        super().__init__()
        self.__dict__.update(kwargs)


class ModelEntity(Entity):
    async def save(self) -> bool:
        return True
