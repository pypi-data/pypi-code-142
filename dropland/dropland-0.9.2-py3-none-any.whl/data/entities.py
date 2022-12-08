class Entity:
    class Meta:
        pass

    def __init__(self, **kwargs):
        super().__init__()
        self.__dict__.update(kwargs)


class ModelEntity(Entity):
    async def save(self) -> bool:
        return True
