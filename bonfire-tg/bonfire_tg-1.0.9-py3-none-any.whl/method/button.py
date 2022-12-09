
import requests
from .send import send_message
from .edit import edit_message
from colorama import init
init()
from colorama import Fore, Back, Style
import sys
import os
import signal


def buttons(bot=None,chat_id=None,button=None,text=None):
            if bot == None:
                   print(Fore.RED+f"You did not specify a keyword (bot = ...) in the 'buttons' function (line : {sys._getframe(1).f_lineno})"+Style.RESET_ALL)  
                   print(Fore.RED+f"Ви не вказали ключове слово (bot = ...) в функціі 'buttons'  (лінія :{sys._getframe(1).f_lineno})"+Style.RESET_ALL)
                   sig = getattr(signal, "SIGKILL", signal.SIGTERM)
                   os.kill(os.getpid(), sig)
              
            if button == None:
                   print(Fore.RED+f"You did not specify a keyword (button = ...) in the 'buttons' function (line : {sys._getframe(1).f_lineno})"+Style.RESET_ALL)  
                   print(Fore.RED+f"Ви не вказали ключове слово (button = ...) в функціі 'buttons'  (лінія :{sys._getframe(1).f_lineno})"+Style.RESET_ALL)
                   sig = getattr(signal, "SIGKILL", signal.SIGTERM)
                   os.kill(os.getpid(), sig)

            if chat_id == None:
                   print(Fore.RED+f"You did not specify a keyword (chat_id = ...) in the 'button' function (line : {sys._getframe(1).f_lineno})"+Style.RESET_ALL)  
                   print(Fore.RED+f"Ви не вказали ключове слово (chat_id = ...) в функціі 'button'  (лінія :{sys._getframe(1).f_lineno})"+Style.RESET_ALL)
                   sig = getattr(signal, "SIGKILL", signal.SIGTERM)
                   os.kill(os.getpid(), sig)
            url = f'https://api.telegram.org/bot{bot}/sendMessage'
            payload = {
                'chat_id': chat_id,
                'text': text,
                "reply_markup": button
                }

            r = requests.post(url,json=payload)
            return r

def answer_callback(bot=None,msg=None,data=None,text=None,show_alters=False):
            if bot == None:
                   print(Fore.RED+f"You did not specify a keyword (bot = ...) in the 'buttons' function (line : {sys._getframe(1).f_lineno})"+Style.RESET_ALL)  
                   print(Fore.RED+f"Ви не вказали ключове слово (bot = ...) в функціі 'buttons'  (лінія :{sys._getframe(1).f_lineno})"+Style.RESET_ALL)
                   sig = getattr(signal, "SIGKILL", signal.SIGTERM)
                   os.kill(os.getpid(), sig)
              
            if msg == None:
                   print(Fore.RED+f"You did not specify a keyword (msg = ...) in the 'answer_callback' function (line : {sys._getframe(1).f_lineno})"+Style.RESET_ALL)  
                   print(Fore.RED+f"Ви не вказали ключове слово (msg = ...) в функціі 'answer_callback'  (лінія :{sys._getframe(1).f_lineno})"+Style.RESET_ALL)
                   sig = getattr(signal, "SIGKILL", signal.SIGTERM)
                   os.kill(os.getpid(), sig)

            if data == None:
                   print(Fore.RED+f"You did not specify a keyword (data = ...) in the 'answer_callback' function (line : {sys._getframe(1).f_lineno})"+Style.RESET_ALL)  
                   print(Fore.RED+f"Ви не вказали ключове слово (data = ...) в функціі 'answer_callback'  (лінія :{sys._getframe(1).f_lineno})"+Style.RESET_ALL)
                   sig = getattr(signal, "SIGKILL", signal.SIGTERM)
                   os.kill(os.getpid(), sig)
            if text == None:
                   print(Fore.RED+f"You did not specify a keyword (text = ...) in the 'answer_callback' function (line : {sys._getframe(1).f_lineno})"+Style.RESET_ALL)  
                   print(Fore.RED+f"Ви не вказали ключове слово (text = ...) в функціі 'answer_callback'  (лінія :{sys._getframe(1).f_lineno})"+Style.RESET_ALL)
                   sig = getattr(signal, "SIGKILL", signal.SIGTERM)
                   os.kill(os.getpid(), sig)

            url = f'https://api.telegram.org/bot{bot}/sendMessage'
            if data == msg.callback_data:
             print("test")
             url = f' https://api.telegram.org/bot{bot}/answercallbackquery'
             payload = {
                
                         "callback_query_id":f"{msg.callback_id}",
                         "text":text,
                         "show_alert":show_alters,
                      }

                
             r = requests.post(url,json=payload)
             return r
            if data != msg.callback_data:
             pass


def callback_edit(bot,data=None,data_json=None,text=None,button={}):
            if bot == None:
                   print(Fore.RED+f"You did not specify a keyword (bot = ...) in the 'callback_edit' function (line : {sys._getframe(1).f_lineno})"+Style.RESET_ALL)  
                   print(Fore.RED+f"Ви не вказали ключове слово (bot = ...) в функціі 'callback_edit'  (лінія :{sys._getframe(1).f_lineno})"+Style.RESET_ALL)
                   sig = getattr(signal, "SIGKILL", signal.SIGTERM)
                   os.kill(os.getpid(), sig)
              
            if data_json == None:
                   print(Fore.RED+f"You did not specify a keyword (data_json = ...) in the 'callback_edit' function (line : {sys._getframe(1).f_lineno})"+Style.RESET_ALL)  
                   print(Fore.RED+f"Ви не вказали ключове слово (data_json = ...) в функціі 'callback_edit'  (лінія :{sys._getframe(1).f_lineno})"+Style.RESET_ALL)
                   sig = getattr(signal, "SIGKILL", signal.SIGTERM)
                   os.kill(os.getpid(), sig)

            if data == None:
                   print(Fore.RED+f"You did not specify a keyword (data = ...) in the 'callback_edit' function (line : {sys._getframe(1).f_lineno})"+Style.RESET_ALL)  
                   print(Fore.RED+f"Ви не вказали ключове слово (data = ...) в функціі 'callback_edit'  (лінія :{sys._getframe(1).f_lineno})"+Style.RESET_ALL)
                   sig = getattr(signal, "SIGKILL", signal.SIGTERM)
                   os.kill(os.getpid(), sig)
            if text == None:
                   print(Fore.RED+f"You did not specify a keyword (text = ...) in the 'callback_edit' function (line : {sys._getframe(1).f_lineno})"+Style.RESET_ALL)  
                   print(Fore.RED+f"Ви не вказали ключове слово (text = ...) в функціі 'callback_edit'  (лінія :{sys._getframe(1).f_lineno})"+Style.RESET_ALL)
                   sig = getattr(signal, "SIGKILL", signal.SIGTERM)
                   os.kill(os.getpid(), sig)
            if data == data_json.callback_data:
             url = f' https://api.telegram.org/bot{bot}/answercallbackquery'
             payload = {
                
  "callback_query_id":data_json.callback_id,
               }

                
             r = requests.post(url,json=payload)
             edit_message(bot,chat_id=data_json.callback_chat,msg_id=data_json.callback_message_id,text=f"{text}",button=button)#send message\{}
def callback(bot,data=None,data_json=None,text=None):
            if bot == None:
                   print(Fore.RED+f"You did not specify a keyword (bot = ...) in the 'callback' function (line : {sys._getframe(1).f_lineno})"+Style.RESET_ALL)  
                   print(Fore.RED+f"Ви не вказали ключове слово (bot = ...) в функціі 'callback'  (лінія :{sys._getframe(1).f_lineno})"+Style.RESET_ALL)
                   sig = getattr(signal, "SIGKILL", signal.SIGTERM)
                   os.kill(os.getpid(), sig)
              
            if data_json == None:
                   print(Fore.RED+f"You did not specify a keyword (data_json = ...) in the 'callback' function (line : {sys._getframe(1).f_lineno})"+Style.RESET_ALL)  
                   print(Fore.RED+f"Ви не вказали ключове слово (data_json = ...) в функціі 'callback'  (лінія :{sys._getframe(1).f_lineno})"+Style.RESET_ALL)
                   sig = getattr(signal, "SIGKILL", signal.SIGTERM)
                   os.kill(os.getpid(), sig)

            if data == None:
                   print(Fore.RED+f"You did not specify a keyword (data = ...) in the 'callback' function (line : {sys._getframe(1).f_lineno})"+Style.RESET_ALL)  
                   print(Fore.RED+f"Ви не вказали ключове слово (data = ...) в функціі 'callback'  (лінія :{sys._getframe(1).f_lineno})"+Style.RESET_ALL)
                   sig = getattr(signal, "SIGKILL", signal.SIGTERM)
                   os.kill(os.getpid(), sig)
            if text == None:
                   print(Fore.RED+f"You did not specify a keyword (text = ...) in the 'callback' function (line : {sys._getframe(1).f_lineno})"+Style.RESET_ALL)  
                   print(Fore.RED+f"Ви не вказали ключове слово (text = ...) в функціі 'callback'  (лінія :{sys._getframe(1).f_lineno})"+Style.RESET_ALL)
                   sig = getattr(signal, "SIGKILL", signal.SIGTERM)
                   os.kill(os.getpid(), sig)
            if data == data_json.callback_data:
             url = f' https://api.telegram.org/bot{bot}/answercallbackquery'
             payload = {
                
  "callback_query_id":data_json.callback_id,
              }

                
             r = requests.post(url,json=payload)
             send_message(bot,chat_id=data_json.callback_chat,text=f"{text}",parse_mode='HTML')#send message\{}
  

            
