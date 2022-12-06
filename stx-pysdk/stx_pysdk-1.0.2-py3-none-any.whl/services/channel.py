import json

import websockets

from stxsdk.typings import ChannelMessage


class Channel:
    def __init__(self, socket_url: str, channel_command: str):
        """
        It takes two arguments: a socket url and a channel command
        :param socket_url: The URL of the socket server
        :param channel_command: The command that will be sent to the server to request a channel
        """
        self.socket_url = socket_url
        self.channel_command = channel_command

    async def channel_handler(self, consumer):
        """
        It connects to a websocket, sends a command, and then waits for a response
        :param consumer: a function that takes a single parameter,
                        which is the message received from the websocket
        """
        async with websockets.connect(self.socket_url) as websocket:
            await websocket.send(self.channel_command)
            await self.__message_handler(websocket, consumer)

    async def __load_message(self, message):
        return json.loads(message)

    async def __message_handler(self, websocket, consumer):
        """
        It takes a websocket and a consumer function as arguments, and then it asynchronously loops
        through the messages received from the websocket, and passes the data to consumer function
        :param websocket: The websocket object that is returned from the websocket.connect() method
        :param consumer: This is the function that will be called when a message is received
        """
        try:
            async for message in websocket:
                data_object = await self.__load_message(message)
                await consumer(
                    ChannelMessage(
                        closed=False,
                        message_received=True,
                        message="Message received",
                        data=data_object,
                    )
                )
        except websockets.ConnectionClosed:
            await consumer(
                ChannelMessage(
                    closed=True,
                    message_received=False,
                    message="Connection Terminated",
                    data=None,
                )
            )
        except Exception as exc:
            await consumer(
                ChannelMessage(
                    closed=True,
                    message_received=False,
                    message=str(exc),
                    data=None,
                )
            )
