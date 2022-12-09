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
def send_message(bot=None,chat_id=None,text=None,parse_mode=None):
            if bot == None:
                   print(Fore.RED+f"You did not specify a keyword (bot = ...) in the 'send_message' function (line : {sys._getframe(1).f_lineno})"+Style.RESET_ALL)  
                   print(Fore.RED+f"Ви не вказали ключове слово (bot = ...) в функціі 'send_message'  (лінія :{sys._getframe(1).f_lineno})"+Style.RESET_ALL)
                   sig = getattr(signal, "SIGKILL", signal.SIGTERM)
                   os.kill(os.getpid(), sig)

            if chat_id == None:
                   print(Fore.RED+f"You did not specify a keyword (chat_id = ...) in the 'send_message' function (line : {sys._getframe(1).f_lineno})"+Style.RESET_ALL)  
                   print(Fore.RED+f"Ви не вказали ключове слово (chat_id = ...) в функціі 'send_message'  (лінія :{sys._getframe(1).f_lineno})"+Style.RESET_ALL)
                   sig = getattr(signal, "SIGKILL", signal.SIGTERM)
                   os.kill(os.getpid(), sig)
            if text == None:
                   print(Fore.RED+f"You did not specify a keyword (text = ...) in the 'send_message' function (line : {sys._getframe(1).f_lineno})"+Style.RESET_ALL)  
                   print(Fore.RED+f"Ви не вказали ключове слово (text =  ...)  в функціі 'send_message'  (лінія :{sys._getframe(1).f_lineno})"+Style.RESET_ALL)
                   sig = getattr(signal, "SIGKILL", signal.SIGTERM)
                   os.kill(os.getpid(), sig)
            if parse_mode is None:
             url = f'https://api.telegram.org/bot{bot}/sendMessage'
             payload = {
                'chat_id': chat_id,
                'text': text,
                
                }
             r = requests.post(url,json=payload)
             return r
            if parse_mode != None:
              url = f'https://api.telegram.org/bot{bot}/sendMessage'
              payload = {
                'chat_id': chat_id,
                'text': text,
                'parse_mode':parse_mode
                
                }
   
              r = requests.post(url,json=payload)
              return r
