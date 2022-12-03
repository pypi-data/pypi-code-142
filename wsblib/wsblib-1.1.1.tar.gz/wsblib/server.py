"""
The `Server` class creates and manipulates the `socket`
of the server. The `Client` class, on the other hand, is
used to store and manipulate information from the client socket.
"""

import socket
from typing import Union


class Client:
    def __init__(self, client: socket.socket, address: tuple) -> None:
        self._client = client
        self._address = address

    def send_message(self, message: str) -> None:
        """Send message to client.

        :param message: Message to send
        :type message: str
        """

        self._client.send(message.encode())

    def get_address(self) -> tuple:
        """Get client address in a tuple (host and port).

        :return: Client address.
        :rtype: tuple
        """

        return self._address

    def get_message(self) -> Union[None, str]:
        """Get the message sent by the client socket.

        :return: Client message.
        :rtype: Union[None, str]
        """

        try:
            self._client.settimeout(1)
            message = self._client.recv(1024)
        except socket.timeout:
            return None

        self._client.settimeout(None)
        return message.decode()

    def destroy(self) -> None:
        """Destroy client connection."""

        self._client.shutdown(socket.SHUT_RDWR)
        self._client.close()


class Server(object):
    def __init__(self):
        """Create a socket in TCP protocol.

        The socket is configured to reuse the address
        that is passed in the `self.start` method
        """

        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def start(self, host: str, port: int, max_listen: int = 128) -> None:
        """Start socket in specified address.

        The `max_listen` argument is the maximum
        number of connections the socket supports,
        the default is 128.

        :param host: Host
        :type host: str
        :param port: Port
        :type port: int
        :param max_listen: maximum number of
        connections the socket, defaults to 128
        :type max_listen: int, optional
        """

        address = (host, port)

        self._socket.bind(address)
        self._socket.listen(max_listen)

    def destroy(self) -> None:
        """Destroy server socket."""

        self._socket.shutdown(socket.SHUT_RDWR)
        self._socket.close()

    def wait_client(self) -> Client:
        """Wait a client connection.

        :return: client informations
        :rtype: Client
        """

        csocket, address = self._socket.accept()
        client = Client(csocket, address)

        return client
