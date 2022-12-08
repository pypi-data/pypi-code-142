from typing import Union

from discord_gateway import constants

__all__ = (
    'Embed',
)


class Embed:

    __slots__ = 'title', 'description', 'url', 'color'

    def __init__(self, title: str, description: str = '', *, url: str = '',
                 color: Union[constants.Color, int] = constants.Color.Default) -> None:
        self.title = title
        self.description = description
        self.url = url
        self.color = color.value

    def to_json(self):
        return {
            key: getattr(self, key)
            for key in self.__slots__
            if hasattr(self, key)
        }

