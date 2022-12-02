from typing import Optional, Iterable, Tuple, Callable, List
from socketserver import BaseRequestHandler, ThreadingTCPServer
from multiprocessing import Process
import json
import socket
import struct

MAGIC_WORD = 0x99DF8060
CMD_SHUTDOWN = 1
CMD_GET_KEY = 2
CMD_SET_KEY = 3
CMD_KEY_EXISTS = 4
CMD_DECR_KEY = 5
CMD_INCR_KEY = 6
CMD_CLEAR_KEYS = 7
CMD_DROP_KEY = 8
CMD_COUNT_KEYS = 9
CMD_ALL_KEYS = 10
CMD_ALL_ITEMS = 11

def _recvall(recv_func: Callable[[int], bytes], size: int) -> bytearray:
    res = bytearray()
    while len(res) != size:
        res += recv_func(size - len(res))
    return res

class Cache:
    def __init__(self) -> None:
        self._data = {}

    def get(self, key: bytes) -> Optional[bytes]:
        return self._data.get(key)

    def set(self, key: bytes, value: bytes) -> None:
        self._data[key] = value

    def decrement(self, key: bytes) -> bytes:
        try:
            v = int(self._data.get(key, b'0').decode()) - 1
        except:
            v = -1
        v = str(v).encode()
        self._data[key] = v
        return v
    
    def increment(self, key: bytes) -> bytes:
        try:
            v = int(self._data.get(key, b'0').decode()) + 1
        except:
            v = 1
        v = str(v).encode()
        self._data[key] = v
        return v

    def clear(self) -> None:
        self._data = {}

    def drop(self, key: bytes) -> bool:
        if key in self._data:
            self._data.pop(key)
            return True
        else:
            return False

    def exists(self, key: bytes) -> bool:
        return key in self._data

    def count(self) -> int:
        return len(self._data)

    def keys(self) -> Iterable[bytes]:
        for key, _ in self._data.items():
            yield key

    def items(self) -> Iterable[Tuple[bytes, bytes]]:
        for key, value in self._data.items():
            yield key, value

_envelope = struct.Struct('II')
_key_header = struct.Struct('I')
_key_response = struct.Struct('bI') # exists, length
_key_value_header = struct.Struct('II')
_value_response = struct.Struct('I')

class _TCPHandler(BaseRequestHandler):
    def setup(self) -> None:
        self._cache = self.server.cache
        self._cmds = {
            CMD_SHUTDOWN: self._shutdown,
            CMD_GET_KEY: self._get_key,
            CMD_SET_KEY: self._set_key,
            CMD_KEY_EXISTS: self._key_exists,
            CMD_DECR_KEY: self._decr_key,
            CMD_INCR_KEY: self._incr_key,
            CMD_CLEAR_KEYS: self._clear_keys,
            CMD_DROP_KEY: self._drop_key,
            CMD_COUNT_KEYS: self._count_keys,
            CMD_ALL_KEYS: self._all_keys,
            CMD_ALL_ITEMS: self._all_items,
        }

    def _shutdown(self, request_data: bytes) -> bytes:
        self.server.shutdown()
        return _envelope.pack(MAGIC_WORD, CMD_SHUTDOWN)

    def _get_key(self, request_data: bytes) -> bytes:
        key_len, = _key_header.unpack(request_data[:_key_header.size])
        key = request_data[_key_header.size:]
        if len(key) != key_len: raise IOError("length")
        value = self._cache.get(key)

        res = _envelope.pack(MAGIC_WORD, CMD_GET_KEY)
        if value is None:
            res += _key_response.pack(False, 0)
        else:
            res += _key_response.pack(True, len(value)) + value
        return res

    def _set_key(self, request_data: bytes) -> bytes:
        key_len, value_len = _key_value_header.unpack(request_data[:_key_value_header.size])
        key_value = request_data[_key_value_header.size:]
        if len(key_value) != key_len + value_len: raise IOError("length")

        self._cache.set(key_value[:key_len], key_value[key_len:])

        return _envelope.pack(MAGIC_WORD, CMD_SET_KEY)

    def _key_exists(self, request_data: bytes) -> bytes:
        key_len, = _key_header.unpack(request_data[:_key_header.size])
        key = request_data[_key_header.size:]
        if len(key) != key_len: raise IOError("length")
        exists = self._cache.exists(key)

        return _envelope.pack(MAGIC_WORD, CMD_KEY_EXISTS) + struct.pack('b', exists)

    def _decr_key(self, request_data: bytes) -> bytes:
        key_len, = _key_header.unpack(request_data[:_key_header.size])
        key = request_data[_key_header.size:]
        if len(key) != key_len: raise IOError("length")
        value = self._cache.decrement(key)

        return _envelope.pack(MAGIC_WORD, CMD_DECR_KEY) + _value_response.pack(len(value)) + value

    def _incr_key(self, request_data: bytes) -> bytes:
        key_len, = _key_header.unpack(request_data[:_key_header.size])
        key = request_data[_key_header.size:]
        if len(key) != key_len: raise IOError("length")
        value = self._cache.increment(key)

        return _envelope.pack(MAGIC_WORD, CMD_INCR_KEY) + _value_response.pack(len(value)) + value
    
    def _clear_keys(self, request_data: bytes) -> bytes:
        self._cache.clear()
        return _envelope.pack(MAGIC_WORD, CMD_CLEAR_KEYS)

    def _drop_key(self, request_data: bytes) -> bytes:
        key_len, = _key_header.unpack(request_data[:_key_header.size])
        key = request_data[_key_header.size:]
        if len(key) != key_len: raise IOError("length")
        dropped = self._cache.drop(key)

        return _envelope.pack(MAGIC_WORD, CMD_DROP_KEY) + struct.pack('b', dropped)

    def _count_keys(self, request_data: bytes) -> bytes:
        count = self._cache.count()
        return _envelope.pack(MAGIC_WORD, CMD_COUNT_KEYS) + struct.pack('I', count)

    def _all_keys(self, request_data: bytes) -> bytes:
        num_keys = 0
        key_data = bytearray()
        for k in self._cache.keys():
            key_data += _key_header.pack(len(k)) + k
            num_keys += 1
        return _envelope.pack(MAGIC_WORD, CMD_ALL_KEYS) + struct.pack('I', num_keys) + bytes(key_data)

    def _all_items(self, request_data: bytes) -> bytes:
        num_items = 0
        kv_data = bytearray()
        for k, v in self._cache.items():
            kv_data += _key_value_header.pack(len(k), len(v)) + k + v
            num_items += 1
        return _envelope.pack(MAGIC_WORD, CMD_ALL_ITEMS) + struct.pack('I', num_items) + bytes(kv_data)

    def handle(self) -> None:
        try:
            while True:
                # TODO: read until payload is done
                data = self.request.recv(1024)
                if len(data) < _envelope.size: return
                magic_word, cmd_id = _envelope.unpack(data[:_envelope.size])
                if magic_word != MAGIC_WORD: return
                cmd = self._cmds.get(cmd_id)
                if cmd is None: return

                self.request.sendall(cmd(data[_envelope.size:]))
        except:
            pass

class Client:
    def __init__(self, host: str, port: int) -> None:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER, struct.pack('ii', 1, 0))
        s.setsockopt(socket.SOL_TCP, socket.TCP_NODELAY, 1)
        s.connect((host, port))

        self._socket = s

    def shutdown_server(self) -> None:
        self._socket.sendall(_envelope.pack(MAGIC_WORD, CMD_SHUTDOWN))
        _ = self._socket.recv(32)
        self._socket.close()

    def get(self, key: bytes) -> Optional[bytes]:
        self._socket.sendall(_envelope.pack(MAGIC_WORD, CMD_GET_KEY) + _key_header.pack(len(key)) + key)
        res = self._socket.recv(1024)
        mw, cmd = _envelope.unpack(res[:_envelope.size])

        res = res[_envelope.size:]

        exists, key_len = _key_response.unpack(res[:_key_response.size])
        key_data = res[_key_response.size:]
        if exists:
            return key_data
        else:
            return None

    def set(self, key: bytes, value: bytes) -> None:
        self._socket.sendall(_envelope.pack(MAGIC_WORD, CMD_SET_KEY) + _key_value_header.pack(len(key), len(value)) + key + value)
        _ = self._socket.recv(32)
    
    def exists(self, key: bytes) -> bool:
        self._socket.sendall(_envelope.pack(MAGIC_WORD, CMD_KEY_EXISTS) + _key_header.pack(len(key)) + key)
        res = self._socket.recv(1024)
        mw, cmd = _envelope.unpack(res[:_envelope.size])

        res = res[_envelope.size:]
        exists, = struct.unpack('b', res)
        return exists

    def decrement(self, key: bytes) -> bytes:
        self._socket.sendall(_envelope.pack(MAGIC_WORD, CMD_DECR_KEY) + _key_header.pack(len(key)) + key)
        res = self._socket.recv(1024)
        mw, cmd = _envelope.unpack(res[:_envelope.size])

        res = res[_envelope.size:]

        value_len, = _value_response.unpack(res[:_value_response.size])
        value_data = res[_value_response.size:]
        return value_data

    def increment(self, key: bytes) -> bytes:
        self._socket.sendall(_envelope.pack(MAGIC_WORD, CMD_INCR_KEY) + _key_header.pack(len(key)) + key)
        res = self._socket.recv(1024)
        mw, cmd = _envelope.unpack(res[:_envelope.size])

        res = res[_envelope.size:]

        value_len, = _value_response.unpack(res[:_value_response.size])
        value_data = res[_value_response.size:]
        return value_data
    
    def clear(self) -> None:
        self._socket.sendall(_envelope.pack(MAGIC_WORD, CMD_CLEAR_KEYS))
        _ = self._socket.recv(32)
    
    def drop(self, key: bytes) -> bool:
        self._socket.sendall(_envelope.pack(MAGIC_WORD, CMD_DROP_KEY) + _key_header.pack(len(key)) + key)
        res = self._socket.recv(32)
        mw, cmd = _envelope.unpack(res[:_envelope.size])

        res = res[_envelope.size:]
        dropped, = struct.unpack('b', res)
        return dropped
    
    def count(self) -> int:
        self._socket.sendall(_envelope.pack(MAGIC_WORD, CMD_COUNT_KEYS))
        res = self._socket.recv(32)
        mw, cmd = _envelope.unpack(res[:_envelope.size])

        res = res[_envelope.size:]
        count, = struct.unpack('I', res)
        return count
    
    def keys(self) -> List[bytes]:
        self._socket.sendall(_envelope.pack(MAGIC_WORD, CMD_ALL_KEYS))
        res = self._socket.recv(1024)
        mw, cmd = _envelope.unpack(res[:_envelope.size])

        res = res[_envelope.size:]
        num_keys, = struct.unpack('I', res[:4])
        res = res[4:]

        keys = []

        for _ in range(num_keys):
            key_len, = _key_header.unpack(res[:_key_header.size])
            res = res[_key_header.size:]
            keys.append(res[:key_len])
            res = res[key_len:]

        return keys
    
    def items(self) -> List[Tuple[bytes, bytes]]:
        self._socket.sendall(_envelope.pack(MAGIC_WORD, CMD_ALL_ITEMS))
        res = self._socket.recv(1024)
        mw, cmd = _envelope.unpack(res[:_envelope.size])

        res = res[_envelope.size:]
        num_items, = struct.unpack('I', res[:4])
        res = res[4:]
        
        items = []

        for _ in range(num_items):
            key_len, value_len = _key_value_header.unpack(res[:_key_value_header.size])
            res = res[_key_value_header.size:]
            items.append((res[:key_len], res[key_len:key_len+value_len]))
            res = res[key_len+value_len:]

        return items

    def close(self) -> None:
        self._socket.close()

def _run_cache_server(filename: str) -> None:
    server = ThreadingTCPServer(('127.0.0.1', 0), _TCPHandler)
    server.cache = Cache()
    server_port = server.socket.getsockname()[1]
    with open(filename, 'w') as fd:
        fd.write(json.dumps({"port": server_port}))
    server.serve_forever()

def create_cache_client(filename: str) -> Client:
    with open(filename, 'r') as fd:
        data = json.loads(fd.read())
        return Client('127.0.0.1', data['port'])

def create_cache_server(filename: str) -> Process:
    proc = Process(target=_run_cache_server, args=(filename,))
    proc.start()
    return proc
