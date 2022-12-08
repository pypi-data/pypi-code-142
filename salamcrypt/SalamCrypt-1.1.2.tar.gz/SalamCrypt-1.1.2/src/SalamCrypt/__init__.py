try:
	import requests  ,re, os , sys , random , uuid , user_agent , json,secrets,secrets
	from uuid import uuid4
	from secrets import *
	from user_agent import generate_user_agent
	import requests
	import names
	import uuid,string
	import instaloader
	import hashlib
	import urllib
	import mechanize
	import json
	import secrets
	import smtplib
	import time
    
	
except ImportError:
	os.system('pip install requests')
	
	
E = '\033[1;31m'
G = '\033[1;32m'
S = '\033[1;33m'
A = '\033[1;34m'
D = '\033[1;35m'
F = '\033[1;36m'
Y = '\033[1;37m'

	
from base64 import b64encode, b64decode
from binascii import unhexlify
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import random
import sys
import datetime,threading,time
import secrets,socket,pyfiglet
import os,marshal
from SalamHunter import *
salamhunter3=AES.MODE_CBC
salamhunter4=AES.block_size
class SalamCrypt:
    def enc(salamhunter5):
        salamhu22=pad(salamhunter5.encode(),salamhunter4)
        salamhunter=os.urandom(16)
        salamhunter1=AES.new(salamhunter,salamhunter3,salamhunter)
        salamhunter2=salamhunter1.encrypt(salamhu22)
        out = b64encode(salamhunter2).decode('utf-8')
        out1 = b64encode(salamhunter).decode('utf-8')
        return f'{out1}??{out}'
    def ex(salamhu99):
        salamhu6= salamhu99.split('??')[0]
        salamhu7= salamhu99.split('??')[1]
        salamhu8= pad(salamhu7.encode(),salamhunter4)
        salamhu10 = AES.new(b64decode(salamhu6),salamhunter3,b64decode(salamhu6))
        exec(unpad(salamhu10.decrypt(b64decode(salamhu8)),salamhunter4).decode('utf-8'))


