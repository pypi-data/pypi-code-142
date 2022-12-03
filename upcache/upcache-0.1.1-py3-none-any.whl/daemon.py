from .networking import TCPHandler
from .cache import Cache
from socketserver import ThreadingTCPServer
import json
import os
import sys

def _run_cache_server(filename: str, remove_file: bool) -> None:
    try:
        server = ThreadingTCPServer(('', 0), TCPHandler)
        server.num_connected = 0
        server.cache = Cache()
        server_port = server.socket.getsockname()[1]
        with open(filename, 'w') as fd:
            fd.write(json.dumps({"port": server_port}))
        server.serve_forever()
    finally:
        if remove_file:
            os.unlink(filename)
