from typing import Optional

from discord_gateway.api import HttpClient
from discord_gateway.discord_objects import DiscordMessage


class CommandContext(DiscordMessage):

    def __init__(self, data: object | dict, client: HttpClient):
        super().__init__(data, client)
        self.api = client

    async def send(self, content: str, threads: bool = False) -> Optional[DiscordMessage]:
        """
        Faster way to respond to a command\n
        :param content: :class:`str`
            The content to send
        :param threads: :class:`bool`
            Weather to use threads
        :return: :class:`Optional[DiscordMessage]`
            The final message (only works without threading)
        """
        if content:
            r = self.api.requests(method='POST', path=f'/channels/{self.channel.id}/messages',
                                  data={'content': content}, threads=threads)
            return DiscordMessage(r, client=self.api) if not threads else None
