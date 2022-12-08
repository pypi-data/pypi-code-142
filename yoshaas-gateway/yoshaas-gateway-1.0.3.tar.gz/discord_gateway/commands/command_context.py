from types import SimpleNamespace
from typing import Optional, Union

from discord_gateway import Embed
from discord_gateway.api import HttpClient
from discord_gateway.discord_objects import DiscordMessage

__all__ = (
    'CommandContext',
)


class CommandContext(DiscordMessage):

    def __init__(self, data: Union[dict, SimpleNamespace], client: HttpClient):
        super().__init__(data, client)
        self.api = client

    async def send(self, content: str = '', *, tts: bool = False, embed: Embed = None, threads: bool = False) -> Optional[DiscordMessage]:
        """
        Faster way to respond to a command\n
        :param content: :class:`str`
            The content to send
        :param tts: :class:`bool`
            Weather or not to use text to speach on send
        :param embed: :class:`Embed`
            An embed to send with the message
        :param threads: :class:`bool`
            Weather to use threads
        :return: :class:`Optional[DiscordMessage]`
            The final message (only works without threading)
        """
        payload = {
            'content': content or None,
            'tts': tts,
            'embeds': [embed.to_json()] if embed else [],
        }

        r = self.api.requests(method='POST', path=f'/channels/{self.channel.id}/messages',
                              json=payload, threads=threads)
        return DiscordMessage(r, client=self.api) if not threads else None
