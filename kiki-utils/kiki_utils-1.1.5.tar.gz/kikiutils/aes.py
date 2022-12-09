from binascii import a2b_hex, b2a_hex
from Cryptodome.Cipher import AES
from typing import Union

from .check import isdict, islist
from .string import b2s, s2b
from .hash import md5
from .json import odumps, oloads


class AesCrypt:
    def __init__(
        self,
        key: Union[bytes, str],
        iv: Union[bytes, str] = None,
        mode=AES.MODE_CBC
    ):
        self.init_args = (md5(key, True), mode,)

        if mode != AES.MODE_ECB:
            self.init_args += (s2b(iv),)

    def decrypt(self, ciphertext: str) -> Union[dict, list, str]:
        ciphertext = a2b_hex(s2b(ciphertext))
        text = AES.new(*self.init_args).decrypt(ciphertext).rstrip()

        try:
            return oloads(text)
        except:
            return b2s(text)

    def encrypt(self, text: Union[dict, list, str]):
        text = self.pad(text)
        ciphertext = AES.new(*self.init_args).encrypt(text)
        return b2s(b2a_hex(ciphertext))

    @staticmethod
    def pad(data: Union[bytes, dict, list, str]) -> bytes:
        if isdict(data) or islist(data):
            data = odumps(data)

        data = s2b(data)

        if len(data) % 16:
            data += b' ' * (16 - (len(data) % 16))

        return data
