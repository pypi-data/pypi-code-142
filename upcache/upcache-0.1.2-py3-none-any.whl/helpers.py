from .errors import InvalidNameLengthError, InvalidNameError, CacheServerConnectionError
from .networking import Client
from .daemon import _run_cache_server

from multiprocessing import Process
from typing import Optional
import os
import json
import tempfile
import string
import sys
import time

def _validate_name(name: str) -> None:
    """
    Validates a cache name for use within a filename.
    Raises InvalidNameLengthError or InvalidNameError
    upon failure.

    :param name cache name to validate
    """
    if len(name) < 1 or len(name) > 128:
        raise InvalidNameLengthError()

    valid_chars = string.ascii_letters + string.digits + '-_'
    for ch in name:
        if ch not in valid_chars:
            raise InvalidNameError(ch)

def _open_client(filename: str) -> Client:
    """
    Opens a JSON file for cache server connection
    info and returns a cache client object.

    :param filename JSON file containing cache server port
    :returns cache client object
    """
    with open(filename, 'r') as fd:
        data = json.loads(fd.read())
        return Client('', data['port'])

def create_cache_client(filename: str, wait_for_file: bool = True) -> Client:
    """
    Creates a cache client and optionally waits for
    the JSON file to be populated with connection info.

    :param filename JSON file containing cache server port
    :param wait_for_file when True, polls the file 250ms intervals
                         for a total of 2.5 seconds (10 polls) until
                         raising a CacheServerConnectionError
    :returns cache client object upon successful connection
    """
    num_retries = 10
    if wait_for_file:
        while True:
            try:
                return _open_client(filename)
            except json.JSONDecodeError:
                if num_retries == 0:
                    try:
                        st = os.stat(filename)
                        if st.st_size == 0:
                            os.unlink(filename)
                    except:
                        pass
                    raise CacheServerConnectionError()
                time.sleep(0.25)
                num_retries -= 1
    else:
        return _open_client(filename)

def create_cache_server(filename: str) -> None:
    # Create file as a barrier for multiple servers
    fd = os.open(filename, os.O_CREAT | os.O_EXCL | os.O_TRUNC | os.O_WRONLY, mode=0o644)
    os.close(fd)

    proc = Process(target=_run_cache_server, args=(filename, True))
    proc.start()

def open_cache(name: str, path: Optional[str] = None) -> Client:
    _validate_name(name)
    filename = os.path.join(path or tempfile.gettempdir(), f'upcache-{name}.json')
    try:
        create_cache_server(filename)
    except:
        pass
    return create_cache_client(filename, wait_for_file=True)

# Convenience alias
UpCache = open_cache
