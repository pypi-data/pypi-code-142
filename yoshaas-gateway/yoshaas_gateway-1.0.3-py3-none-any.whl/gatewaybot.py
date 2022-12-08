from typing import Optional, Callable, Any, Union

from requests import Response

from discord_gateway.discord_objects import DiscordChannel, DiscordGuild
from discord_gateway.discord_user import DiscordUser
from discord_gateway.gateway_handler import Gateway
from gateway import GatewayMessage
from discord_gateway.api import HttpClient
from types import SimpleNamespace
from discord_gateway.constants import Intents


__all__ = (
    'GatewayBot',
)


class GatewayBot(Gateway):

    def __init__(self, *, intents: int = Intents.All):
        super().__init__(intents=intents.value)
        self.api = None
        self.user: Optional[SimpleNamespace] = None
        self.add_listener(self.default_ready, event='ready', type='default')

    async def default_ready(self, msg: GatewayMessage) -> None:
        """
        Default ready,\n
        Stores user data, api and user tag.\n
        :param msg: :class:`GatewayMessage`
            The data received from the identify response
        """
        self.api = HttpClient(self._token, bot=self.is_bot)
        self.user = SimpleNamespace(**msg.data.user)
        self.user.guilds = msg.data.__dict__.get('guilds')  # Guilds IDs only
        self.user.tag = f'{self.user.username}#{self.user.discriminator}'

    def event(self, func: Callable) -> Callable[..., Any]:
        """
        **Decorator**\n
        Used to assign a function with an event\n
        :param func: The function to assign
        :return: :class:`Callable`
            Returns the function itself
        """
        self.add_listener(func, event=func.__name__.replace('on_', '', 1) if func.__name__.startswith(
            'on_') else func.__name__)
        return func

    async def get_channel(self, channel_id: str) -> DiscordChannel:
        """
        Get channel by his id\n
        :param channel_id: :class:`str`
            The channel id
        :return: :class:`DiscordChannel`
            Returns the channel
        """
        return DiscordChannel(channel_id, api=self.api)

    async def get_guild(self, guild_id: str) -> DiscordGuild:
        """
        Get guild by id\n
        :param guild_id: :class:`str`
            The guild id
        :return: :class:`DiscordGuild`
            Returns the guild
        """
        return DiscordGuild(guild_id, api=self.api)

    async def dms(self) -> Union[Response, dict]:
        """
        Get open dms of bot\n
        :return: :class:`Union[Response, dict]`
            Returns the open dms
        """
        return self.api.requests(method='GET', path='/users/@me/channels')

    async def get_user(self, user_id: str) -> DiscordUser:
        """
        Get user by his id\n
        :param user_id: :class:`str`
            The user id
        :return: :class:`DiscordUser`
            Returns the user
        """
        headers = {
            'authorization': self.api.get_auth(),
            'content-type': 'application/json'
        }
        return DiscordUser(self.api.requests(method='POST', path=f'/users/@me/channels', json={"recipients": [user_id]},
                                             headers=headers), self.api)

    async def join(self, server_invite: str) -> Union[Response, dict]:
        """
        Join a guild by invite {SelfBot only}\n
        :param server_invite: :class:`str`
            The server invite link
        :return: :class:`Union[Response, dict]`
            The obtained server
        """
        return self.api.requests(method='POST', path=f'/invites/{server_invite}')

    async def leave(self, guild_id: str) -> None:
        """
        Leaves a guild\n
        :param guild_id: :class:`str`
            The guild id to leave
        """
        self.api.requests(method='DELETE', path=f'/users/@me/guilds/{guild_id}')

    async def create_group_chat(self, ids: list[str]) -> Union[Response, dict]:
        """
        Creates a group chat with members {SelfBot only}\n
        :param ids: :class:`list[str]`
            The list of the member ids
        :return: :class:`Union[Response, dict]`
            The opened group chat
        """
        headers = {
            'authorization': self.api.get_auth(),
            'content-type': 'application/json'
        }
        return self.api.requests(method='POST', path=f'/users/@me/channels', json={'recipients': ids}, headers=headers)
