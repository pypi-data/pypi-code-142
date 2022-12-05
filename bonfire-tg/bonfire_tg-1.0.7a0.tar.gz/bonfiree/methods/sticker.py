from flask import Flask
from flask import request
from flask import Response
import requests

app = Flask(__name__)
from colorama import init
init()
from colorama import Fore, Back, Style
import sys
import os
import signal
def send_sticker(bot=None,chat_id=None,sticker=None):
            if bot == None:
                   print(Fore.RED+f"You did not specify a keyword (bot = ...) in the 'send_sticker' function (line : {sys._getframe(1).f_lineno})"+Style.RESET_ALL)  
                   print(Fore.RED+f"Ви не вказали ключове слово (bot = ...) в функціі send_sticker'  (лінія :{sys._getframe(1).f_lineno})"+Style.RESET_ALL)
                   sig = getattr(signal, "SIGKILL", signal.SIGTERM)
                   os.kill(os.getpid(), sig)

            if chat_id == None:
                   print(Fore.RED+f"You did not specify a keyword (chat_id = ...) in the 'send_sticker' function (line : {sys._getframe(1).f_lineno})"+Style.RESET_ALL)  
                   print(Fore.RED+f"Ви не вказали ключове слово (chat_id = ...) в функціі 'send_sticker'  (лінія :{sys._getframe(1).f_lineno})"+Style.RESET_ALL)
                   sig = getattr(signal, "SIGKILL", signal.SIGTERM)
                   os.kill(os.getpid(), sig)
            if sticker == None:
                   print(Fore.RED+f"You did not specify a keyword (sticker = ...) in the 'send_sticker' function (line : {sys._getframe(1).f_lineno})"+Style.RESET_ALL)  
                   print(Fore.RED+f"Ви не вказали ключове слово (sticker =  ...)  в функціі 'send_stickere'  (лінія :{sys._getframe(1).f_lineno})"+Style.RESET_ALL)
                   sig = getattr(signal, "SIGKILL", signal.SIGTERM)
                   os.kill(os.getpid(), sig)

            url = f'https://api.telegram.org/bot{bot}/sendSticker'
            payload = {
                'chat_id': chat_id,
                'sticker': sticker,
                }
   
            r = requests.post(url,json=payload)
            return r