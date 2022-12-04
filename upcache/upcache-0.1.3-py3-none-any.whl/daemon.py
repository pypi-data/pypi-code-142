from .networking import TCPHandler
from .cache import Cache
from multiprocessing import Lock
from socketserver import ThreadingTCPServer
from typing import Tuple
import json
import os
import sys

class TCPServer(ThreadingTCPServer):
    def __init__(self, bind: Tuple[str, int]) -> None:
        super().__init__(bind, TCPHandler)
        self.cache = Cache()
        self._conn_lock = Lock()
        self._num_connected = 0

    def incr_client(self) -> None:
        with self._conn_lock:
            self._num_connected += 1

    def decr_client(self) -> None:
        with self._conn_lock:
            self._num_connected -= 1
            if self._num_connected <= 0:
                self.shutdown()

def _run_cache_server(filename: str, remove_file: bool) -> None:
    """
    Starts a TCP-based cache server which emits its ephemeral
    port to a JSON file for clients.

    :param filename JSON output file
    :param remove_file removes JSON file when server completes
    """
    try:
        server = TCPServer(('127.0.0.1', 0))
        server_port = server.socket.getsockname()[1]
        with open(filename, 'w') as fd:
            fd.write(json.dumps({"port": server_port}))
        server.serve_forever()
    finally:
        if remove_file:
            os.unlink(filename)
