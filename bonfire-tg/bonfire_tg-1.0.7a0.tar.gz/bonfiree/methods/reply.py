from flask import Flask
from flask import request
from flask import Response
import requests
from inspect import currentframe, getframeinfo
app = Flask(__name__)
from colorama import init
init()
from colorama import Fore, Back, Style
import sys
import os
import signal

def reply_message(bot=None,chat_id=None,msg_id=None,text=None,parse_mode=None):
            if bot == None:
                   print(Fore.RED+f"You did not specify a keyword (bot = ...) in the 'reply_message' function (line : {sys._getframe(1).f_lineno})"+Style.RESET_ALL)  
                   print(Fore.RED+f"Ви не вказали ключове слово (bot = ...) в функціі 'reply_message'  (лінія :{sys._getframe(1).f_lineno})"+Style.RESET_ALL)
                   sig = getattr(signal, "SIGKILL", signal.SIGTERM)
                   os.kill(os.getpid(), sig)


            if msg_id == None:
                   print(Fore.YELLOW+f"You did not specify a keyword (msg_id = ...) in the 'reply_message' function (line : {sys._getframe(1).f_lineno})"+Style.RESET_ALL)  
                   print(Fore.RED+f"Ви не вказали ключове слово (msg_id = ...) в функціі 'reply_message'  (лінія :{sys._getframe(1).f_lineno})"+Style.RESET_ALL)
                   sig = getattr(signal, "SIGKILL", signal.SIGTERM)
                   os.kill(os.getpid(), sig)

            if chat_id == None:
                   print(Fore.RED+f"You did not specify a keyword (chat_id = ...) in the 'reply_message' function (line : {sys._getframe(1).f_lineno})"+Style.RESET_ALL)  
                   print(Fore.RED+f"Ви не вказали ключове слово (chat_id = ...) в функціі 'reply_message'  (лінія :{sys._getframe(1).f_lineno})"+Style.RESET_ALL)
                   sig = getattr(signal, "SIGKILL", signal.SIGTERM)
                   os.kill(os.getpid(), sig)
            if text == None:
                   print(Fore.RED+f"You did not specify a keyword (text = ...) in the 'reply_message' function (line : {sys._getframe(1).f_lineno})"+Style.RESET_ALL)  
                   print(Fore.RED+f"Ви не вказали ключове слово (text =  ...)  в функціі 'reply_message'  (лінія :{sys._getframe(1).f_lineno})"+Style.RESET_ALL)
                   sig = getattr(signal, "SIGKILL", signal.SIGTERM)
                   os.kill(os.getpid(), sig)
            if parse_mode is None:
              url = f'https://api.telegram.org/bot{bot}/sendMessage'
              payload = {
                'chat_id': chat_id,
                'text': text,
                'reply_to_message_id':msg_id
                }
   
              r = requests.post(url,json=payload)
              return r
            if parse_mode != None:
             url = f'https://api.telegram.org/bot{bot}/sendMessage'
             payload = {
                'chat_id': chat_id,
                'text': text,
                'reply_to_message_id':msg_id,
                'parse_mode':parse_mode
                }
   
             r = requests.post(url,json=payload)
             return r