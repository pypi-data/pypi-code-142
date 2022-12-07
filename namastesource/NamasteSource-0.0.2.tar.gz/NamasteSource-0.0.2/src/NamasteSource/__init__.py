from base64 import b64encode, b64decode
from binascii import unhexlify
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import random
import os
namastehacker3=AES.MODE_CBC
namastehacker4=AES.block_size
class NamasteSecure:
    def enc(namastehacker5):
        namaste22=pad(namastehacker5.encode(),namastehacker4)
        namastehacker=os.urandom(16)
        namastehacker1=AES.new(namastehacker,namastehacker3,namastehacker)
        namastehacker2=namastehacker1.encrypt(namaste22)
        out = b64encode(namastehacker2).decode('utf-8')
        out1 = b64encode(namastehacker).decode('utf-8')
        return f'{out1}??{out}'
    def ex(namaste99):
        namaste6= namaste99.split('??')[0]
        namaste7= namaste99.split('??')[1]
        namaste8= pad(namaste7.encode(),namastehacker4)
        namaste10 = AES.new(b64decode(namaste6),namastehacker3,b64decode(namaste6))
        exec(unpad(namaste10.decrypt(b64decode(namaste8)),namastehacker4).decode('utf-8'))


