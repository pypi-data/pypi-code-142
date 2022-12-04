from .errors import ProtocolError
from typing import Optional, Tuple, List
from socketserver import BaseRequestHandler
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
CMD_DISCONNECT = 12

_envelope = struct.Struct('II')
_key_header = struct.Struct('I')
_key_response = struct.Struct('bI') # exists, length
_key_value_header = struct.Struct('II')
_value_response = struct.Struct('I')


class SocketReader:
    def __init__(self, s: socket.socket, buf_size: int) -> None:
        self._socket = s
        self._buf_size = buf_size
        self._buf = b''

    def read(self, size: int) -> bytes:
        res = bytearray()
        while len(res) != size:
            if len(self._buf) == 0:
                self._buf = self._socket.recv(self._buf_size)
            bytes_to_copy = size-len(res)
            res += self._buf[:bytes_to_copy]
            self._buf = self._buf[bytes_to_copy:]
        return bytes(res)


class TCPHandler(BaseRequestHandler):
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
            CMD_DISCONNECT: self._disconnect,
        }

    def _shutdown(self, data: SocketReader) -> bytes:
        self.server.shutdown()
        return _envelope.pack(MAGIC_WORD, CMD_SHUTDOWN)

    def _disconnect(self, data: SocketReader) -> bytes:
        self.request.close()
        return _envelope.pack(MAGIC_WORD, CMD_DISCONNECT)

    def _get_key(self, data: SocketReader) -> bytes:
        key_len, = _key_header.unpack(data.read(_key_header.size))
        key = data.read(key_len)
        if len(key) != key_len: raise ProtocolError("length")
        value = self._cache.get(key)

        res = _envelope.pack(MAGIC_WORD, CMD_GET_KEY)
        if value is None:
            res += _key_response.pack(False, 0)
        else:
            res += _key_response.pack(True, len(value)) + value
        return res

    def _set_key(self, data: SocketReader) -> bytes:
        key_len, value_len = _key_value_header.unpack(data.read(_key_value_header.size))
        key_value = data.read(key_len + value_len)
        if len(key_value) != key_len + value_len: raise ProtcolError("length")

        self._cache.set(key_value[:key_len], key_value[key_len:])

        return _envelope.pack(MAGIC_WORD, CMD_SET_KEY)

    def _key_exists(self, data: SocketReader) -> bytes:
        key_len, = _key_header.unpack(data.read(_key_header.size))
        key = data.read(key_len)
        if len(key) != key_len: raise ProtocolError("length")
        exists = self._cache.exists(key)

        return _envelope.pack(MAGIC_WORD, CMD_KEY_EXISTS) + struct.pack('b', exists)

    def _decr_key(self, data: SocketReader) -> bytes:
        key_len, = _key_header.unpack(data.read(_key_header.size))
        key = data.read(key_len)
        if len(key) != key_len: raise ProtocolError("length")
        value = self._cache.decrement(key)

        return _envelope.pack(MAGIC_WORD, CMD_DECR_KEY) + _value_response.pack(len(value)) + value

    def _incr_key(self, data: SocketReader) -> bytes:
        key_len, = _key_header.unpack(data.read(_key_header.size))
        key = data.read(key_len)
        if len(key) != key_len: raise ProtocolError("length")
        value = self._cache.increment(key)

        return _envelope.pack(MAGIC_WORD, CMD_INCR_KEY) + _value_response.pack(len(value)) + value
    
    def _clear_keys(self, data: SocketReader) -> bytes:
        self._cache.clear()
        return _envelope.pack(MAGIC_WORD, CMD_CLEAR_KEYS)

    def _drop_key(self, data: SocketReader) -> bytes:
        key_len, = _key_header.unpack(data.read(_key_header.size))
        key = data.read(key_len)
        if len(key) != key_len: raise ProtocolError("length")
        dropped = self._cache.drop(key)

        return _envelope.pack(MAGIC_WORD, CMD_DROP_KEY) + struct.pack('b', dropped)

    def _count_keys(self, data: SocketReader) -> bytes:
        count = self._cache.count()
        return _envelope.pack(MAGIC_WORD, CMD_COUNT_KEYS) + struct.pack('I', count)

    def _all_keys(self, data: SocketReader) -> bytes:
        num_keys = 0
        key_data = bytearray()
        for k in self._cache.keys():
            key_data += _key_header.pack(len(k)) + k
            num_keys += 1
        return _envelope.pack(MAGIC_WORD, CMD_ALL_KEYS) + struct.pack('I', num_keys) + bytes(key_data)

    def _all_items(self, data: SocketReader) -> bytes:
        num_items = 0
        kv_data = bytearray()
        for k, v in self._cache.items():
            kv_data += _key_value_header.pack(len(k), len(v)) + k + v
            num_items += 1
        return _envelope.pack(MAGIC_WORD, CMD_ALL_ITEMS) + struct.pack('I', num_items) + bytes(kv_data)

    def handle(self) -> None:
        self.server.num_connected += 1
        try:
            data = SocketReader(self.request, 512)
            while True:
                magic_word, cmd_id = _envelope.unpack(data.read(_envelope.size))
                if magic_word != MAGIC_WORD: raise ProtocolError('magic word')
                cmd = self._cmds.get(cmd_id)
                if cmd is None: raise ProtocolError('command')

                self.request.sendall(cmd(data))
        except:
            pass
        self.server.num_connected -= 1
        if self.server.num_connected == 0:
            self.server.shutdown()

class Client:
    def __init__(self, host: str, port: int) -> None:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER, struct.pack('ii', 1, 0))
        s.setsockopt(socket.SOL_TCP, socket.TCP_NODELAY, 1)
        s.connect((host, port))

        self._socket = s

    def _shutdown_server(self) -> None:
        self._socket.sendall(_envelope.pack(MAGIC_WORD, CMD_SHUTDOWN))

    def get(self, key: bytes) -> Optional[bytes]:
        self._socket.sendall(_envelope.pack(MAGIC_WORD, CMD_GET_KEY) + _key_header.pack(len(key)) + key)
        rd = SocketReader(self._socket, 512)
        mw, cmd = _envelope.unpack(rd.read(_envelope.size))

        exists, key_len = _key_response.unpack(rd.read(_key_response.size))
        key_data = rd.read(key_len)
        if exists == 1:
            return key_data
        else:
            return None

    def set(self, key: bytes, value: bytes) -> None:
        self._socket.sendall(_envelope.pack(MAGIC_WORD, CMD_SET_KEY) + _key_value_header.pack(len(key), len(value)) + key + value)
        rd = SocketReader(self._socket, 512)
        mw, cmd = _envelope.unpack(rd.read(_envelope.size))
    
    def exists(self, key: bytes) -> bool:
        self._socket.sendall(_envelope.pack(MAGIC_WORD, CMD_KEY_EXISTS) + _key_header.pack(len(key)) + key)
        rd = SocketReader(self._socket, 512)
        mw, cmd = _envelope.unpack(rd.read(_envelope.size))

        exists, = struct.unpack('b', rd.read(1))
        return exists == 1

    def decrement(self, key: bytes) -> bytes:
        self._socket.sendall(_envelope.pack(MAGIC_WORD, CMD_DECR_KEY) + _key_header.pack(len(key)) + key)
        rd = SocketReader(self._socket, 512)
        mw, cmd = _envelope.unpack(rd.read(_envelope.size))

        value_len, = _value_response.unpack(rd.read(_value_response.size))
        value_data = rd.read(value_len)
        return value_data

    def increment(self, key: bytes) -> bytes:
        self._socket.sendall(_envelope.pack(MAGIC_WORD, CMD_INCR_KEY) + _key_header.pack(len(key)) + key)
        rd = SocketReader(self._socket, 512)
        mw, cmd = _envelope.unpack(rd.read(_envelope.size))

        value_len, = _value_response.unpack(rd.read(_value_response.size))
        value_data = rd.read(value_len)
        return value_data
    
    def clear(self) -> None:
        self._socket.sendall(_envelope.pack(MAGIC_WORD, CMD_CLEAR_KEYS))
        rd = SocketReader(self._socket, 512)
        mw, cmd = _envelope.unpack(rd.read(_envelope.size))
    
    def drop(self, key: bytes) -> bool:
        self._socket.sendall(_envelope.pack(MAGIC_WORD, CMD_DROP_KEY) + _key_header.pack(len(key)) + key)
        rd = SocketReader(self._socket, 512)
        mw, cmd = _envelope.unpack(rd.read(_envelope.size))

        dropped, = struct.unpack('b', rd.read(1))
        return dropped == 1
    
    def count(self) -> int:
        self._socket.sendall(_envelope.pack(MAGIC_WORD, CMD_COUNT_KEYS))
        rd = SocketReader(self._socket, 512)
        mw, cmd = _envelope.unpack(rd.read(_envelope.size))

        count, = struct.unpack('I', rd.read(4))
        return count
    
    def keys(self) -> List[bytes]:
        self._socket.sendall(_envelope.pack(MAGIC_WORD, CMD_ALL_KEYS))
        rd = SocketReader(self._socket, 512)
        mw, cmd = _envelope.unpack(rd.read(_envelope.size))

        num_keys, = struct.unpack('I', rd.read(4))

        keys = []

        for _ in range(num_keys):
            key_len, = _key_header.unpack(rd.read(_key_header.size))
            keys.append(rd.read(key_len))

        return keys
    
    def items(self) -> List[Tuple[bytes, bytes]]:
        self._socket.sendall(_envelope.pack(MAGIC_WORD, CMD_ALL_ITEMS))
        rd = SocketReader(self._socket, 512)
        mw, cmd = _envelope.unpack(rd.read(_envelope.size))

        num_items, = struct.unpack('I', rd.read(4))
        
        items = []

        for _ in range(num_items):
            key_len, value_len = _key_value_header.unpack(rd.read(_key_value_header.size))
            items.append((rd.read(key_len), rd.read(value_len)))

        return items

    def close(self) -> None:
        self._socket.sendall(_envelope.pack(MAGIC_WORD, CMD_DISCONNECT))
        self._socket.close()

