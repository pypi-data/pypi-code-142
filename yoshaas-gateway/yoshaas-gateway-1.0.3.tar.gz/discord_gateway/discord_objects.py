import asyncio
import threading
from types import SimpleNamespace

from requests import Response
from typing import Optional, Iterator, Union
from typing_extensions import Self

from discord_gateway.api import HttpClient
from discord_gateway.constants import ChannelType

__all__ = (
    'DiscordMessage',
    'DiscordChannel',
    'DiscordGuild',
)


class DiscordMessage:

    def __init__(self, data: Union[dict, SimpleNamespace], client: HttpClient) -> None:
        if not data:
            return
        from discord_gateway.discord_user import DiscordMember, DiscordUser  # Circular imports
        self.__token = client.get_token()
        data = dict(data.__dict__) if type(data) is not dict else data
        self.data = data
        self.id = data.get('id')
        self.content = data.get('content')
        self.api = client
        if data.get('guild_id', False):
            self.guild = DiscordGuild(guild_id=data.get('guild_id'), api=self.api)
            self.author = DiscordMember(data.get("member", {}), data.get("author", {}), self.guild.id,
                                        self.api)
        else:
            self.author = DiscordUser(data.get('author', {}), self.api)
        if data.get('channel_id', False):
            self.channel = DiscordChannel(channel_id=self.data.get('channel_id'), api=self.api)

    async def delete(self) -> Union[Response, dict]:
        """
        Deletes the message\n
        :return: :class:`Union[Response, dict]`
            The deleted message
        """
        return self.api.requests(method='DELETE', path=f'/channels/{self.channel.id}/messages/{self.id}',
                                 data={})

    async def reply(self, content: str) -> Self:
        """
        Quick way to reply to a message\n
        :param content: :class:`str`
            Message content
        :return: :class:`DiscordMessage`
            The replied message
        """
        payload = {
            'content': content,
            "message_reference":
                {
                    "channel_id": self.channel.id,
                    "message_id": self.id,
                }
        }
        return DiscordMessage(
            self.api.requests(method='POST', path=f'/channels/{self.channel.id}/messages', json=payload),
            client=self.api)

    async def edit(self, content: str) -> Union[Response, dict]:
        """
        Edit message\n
        :param content: :class:`str`
            New content
        :return: :class:`Union[Response, dict]`
            New message
        """
        headers = {
            'Authorization': self.api.get_auth(),
            'Content-Type': 'application/json'
        }
        return self.api.requests(method='PATCH', path=f'/channels/{self.channel.id}/messages/{self.id}',
                                 headers=headers, data='{"content":"' + content + '"}')


class DiscordChannel:

    def __init__(self, channel_id: str, api: HttpClient, use_data: bool = False) -> None:
        self.id: str = channel_id
        self.__token = api.get_token()
        self.api = api
        self._data: dict = {}
        self.name: Optional[str] = None
        if use_data:
            threading.Thread(target=asyncio.run, args=(self.get_data(),)).start()

    def __repr__(self) -> str:
        return f'{self.id}'

    async def get_data(self) -> None:
        self._data = self.api.requests(method='GET', path=f'/channels/{self.id}')
        self.name = self._data.get('name')

    async def send(self, content: str, threads: bool = False) -> DiscordMessage:
        """
        Send message in channel\n
        :param content: :class:`str`
            Message content
        :param threads: :class:`bool`
            Weather to use threads or not
        :return: :class:`DiscordMessage`
            The message
        """
        if content:
            r = self.api.requests(method='POST', path=f'/channels/{self.id}/messages',
                                  data={'content': content}, threads=threads)
            return DiscordMessage(r, client=self.api) if not threads else None

    async def delete(self) -> None:
        """
        Delete the channel\n
        """
        self.api.requests(method='DELETE', path=f'/channels/{self.id}', threads=True)

    async def generate_invite(self, *, max_age: int = 0, max_uses: int = 0, temporary: bool = False) -> Union[str, dict]:
        """
        Creates an invitation to the server\n
        :param max_age: :class:`int`
            Max age of the invite before it gets deleted
        :param max_uses: :class:`int`
            Max allowed uses of the invite
        :param temporary: :class:`bool`
            Grants temporary membership on join
        :return: :class:`Union[str, dict]`
            The generated invite
        """
        payload = {
            "max_age": max_age,
            "max_uses": max_uses,
            "temporary": temporary,
        }
        return self.api.requests(method='POST', path=f'/channels/{self.id}/invites', json=payload)

    def messages(self, limit: int = 50) -> Iterator[DiscordMessage]:
        """
        Fetch channel messages\n
        :param limit: :class:`int`
            Amount of messages to fetch
        :return: :class:`DiscordMessage`
            Every message which is included in the provided limit
        """
        r = self.api.requests(method='GET', path=f'/channels/{self.id}/messages', limit=limit)
        for msg in r:
            yield DiscordMessage(msg, client=self.api)


class DiscordGuild:

    def __init__(self, guild_id: str, api: HttpClient) -> None:
        self.id: str = guild_id
        self.__token = api.get_token()
        self.api = api

    async def channels(self) -> Iterator[DiscordChannel]:
        """
        Get all guild channels\n
        :return: :class:`DiscordChannel`
            The channels of the guild
        """
        for channel in self.api.requests(method='GET', path=f'/guilds/{self.id}/channels'):
            yield DiscordChannel(channel.get('id'), api=self.api, use_data=False)

    async def create_channel(self, name: str, *, channel_type: ChannelType = ChannelType.TextChannel,
                             permission_overwrites: list = (), threads: bool = False) -> DiscordChannel:
        """
        Create a channel in the guild\n
        :param name: :class:`str`
            The name of the channel
        :param channel_type: :class:`ChannelType`
            The channel type
        :param permission_overwrites: :class:`list`
            The permissions of the channel
        :param threads: :class:`bool`
            Weather to use threads or normal async
        :return: :class:`DiscordChannel`
            The created channel
        """
        payload = {
            'name': '-'.join(name.split(' ')),
            'permission_overwrites': permission_overwrites,
            'type': channel_type.value
        }
        return DiscordChannel(
            self.api.requests(method='POST', path=f'/guilds/{self.id}/channels', json=payload, threads=threads).get(
                'id'), api=self.api)

    async def leave(self) -> None:
        """
        Leaves the guild\n
        """
        self.api.requests(method='DELETE', path=f'users/@me/guilds/{self.id}')

    from discord_gateway.discord_user import DiscordMember  # Circular import

    async def kick(self, member: DiscordMember) -> None:
        """
        Kick a member from the guild\n
        :param member: :class:`DiscordMember`
            The member to kick from the guild
        """
        self.api.requests(method='DELETE', path=f'/guilds/{self.id}/members/{member.id}')

    async def ban(self, member: DiscordMember, delete_message_seconds: int = 3600) -> None:
        """
        Ban a member from the guild\n
        :param member: :class:`DiscordMember`
            The member to ban from the guild
        :param delete_message_seconds: :class:`int`
            Delete message seconds, delete all the messages from the user
            in the given time frame
        """
        payload = {
            "delete_message_seconds": delete_message_seconds
        }
        self.api.requests(method='PUT', path=f'/guilds/{self.id}/bans/{member.id}',
                          data=payload)

    async def unban(self, member_id: str) -> None:
        """
        Unbans a member from the guild\n
        :param member_id: :class:`str`
            The member id to unban
        """
        self.api.requests(method='DELETE', path=f'/guilds/{self.id}/bans/{member_id}')
