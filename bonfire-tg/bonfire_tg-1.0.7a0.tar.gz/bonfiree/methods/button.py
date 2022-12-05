from flask import Flask
from flask import request
from flask import Response
import requests
from .send import send_message
app = Flask(__name__)
from colorama import init
init()
from colorama import Fore, Back, Style
import sys
import os
import signal

def url_buttons(bot=None,chat_id=None,text=None,button_text=None,url=None):
            ur = f'https://api.telegram.org/bot{bot}/sendMessage'
            payload = {
                'chat_id': chat_id,
                'text': text,
                "reply_markup": {"inline_keyboard": [
                  [{"text":f"{button_text}","url":url}],
                  [{"text":f"{button_text}","url":url}],
                  [{"text":f"{button_text}","callback_data":f"/button"}]
                  ]
                  }  ,

                

                }

            r = requests.post(ur,json=payload)
            return r

def buttons(bot=None,chat_id=None,button=None,text=None):
            url = f'https://api.telegram.org/bot{bot}/sendMessage'
            payload = {
                'chat_id': chat_id,
                'text': text,
                "reply_markup": button
                }

            r = requests.post(url,json=payload)
            return r

def answer_callback(bot=None,msg=None,data=None,text=None,show_alters=False):

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



def callback(bot,data=None,data_json=None,text=None):
    if data == data_json.callback_data:
            url = f' https://api.telegram.org/bot{bot}/answercallbackquery'
            payload = {
                
  "callback_query_id":data_json.callback_id,
              }

                
            r = requests.post(url,json=payload)
            send_message(bot,chat_id=data_json.callback_chat,text=f"{text}",parse_mode='HTML')#send message\{}
  

            
