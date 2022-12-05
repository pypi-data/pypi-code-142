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
def delete_message(bot=None,chat_id=None,msg_id=None):
            if bot == None:
                   print(Fore.RED+f"You did not specify a keyword (bot = ...) in the 'delete_message' function (line : {sys._getframe(1).f_lineno})"+Style.RESET_ALL)  
                   print(Fore.RED+f"Ви не вказали ключове слово (bot = ...) в функціі 'delete_message'  (лінія :{sys._getframe(1).f_lineno})"+Style.RESET_ALL)
                   sig = getattr(signal, "SIGKILL", signal.SIGTERM)
                   os.kill(os.getpid(), sig)

            if chat_id == None:
                   print(Fore.RED+f"You did not specify a keyword (chat_id = ...) in the 'delete_message' function (line : {sys._getframe(1).f_lineno})"+Style.RESET_ALL)  
                   print(Fore.RED+f"Ви не вказали ключове слово (chat_id = ...) в функціі 'delete_message'  (лінія :{sys._getframe(1).f_lineno})"+Style.RESET_ALL)
                   sig = getattr(signal, "SIGKILL", signal.SIGTERM)
                   os.kill(os.getpid(), sig)
            if msg_id == None:
                   print(Fore.YELLOW+f"You did not specify a keyword (msg_id = ...) in the 'delete_message' function (line : {sys._getframe(1).f_lineno})"+Style.RESET_ALL)  
                   print(Fore.RED+f"Ви не вказали ключове слово (msg_id = ...) в функціі 'delete_message'  (лінія :{sys._getframe(1).f_lineno})"+Style.RESET_ALL)
                   sig = getattr(signal, "SIGKILL", signal.SIGTERM)
                   os.kill(os.getpid(), sig)


            url = f'https://api.telegram.org/bot{bot}/deleteMessage'
            payload = {
                'chat_id': chat_id,
                'message_id' : msg_id
                }
   
            r = requests.post(url,json=payload)
            return r