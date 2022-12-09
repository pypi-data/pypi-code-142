import requests
import datetime
import sys
import os
import signal
from colorama import init
init()
from colorama import Fore, Back, Style

class message(object):
  def __init__(self, token):
    if token == None:
                   print(Fore.RED+f"You did not specify a keyword (token = ...) in the 'message' function (line : {sys._getframe(1).f_lineno})"+Style.RESET_ALL)  
                   print(Fore.RED+f"Ви не вказали ключове слово (token = ...) в функціі 'message'  (лінія :{sys._getframe(1).f_lineno})"+Style.RESET_ALL)
                   sig = getattr(signal, "SIGKILL", signal.SIGTERM)
                   os.kill(os.getpid(), sig)
    self.token = token

  @property
  def id(self):
      try:
       r = requests.get(f'https://api.telegram.org/bot{self.token}/getUpdates')
       request = r.json()
       return request["result"][0]['message']['message_id']
      except:
        return None
  @property
  def chat_remove_members(self):
      """chat event"""
      try:
       r = requests.get(f'https://api.telegram.org/bot{self.token}/getUpdates')
       request = r.json()
       return request["result"][0]['message']['left_chat_participant']
      except:
        return None

  @property
  def edit_(self):
      """edit message handler"""
      try:
       r = requests.get(f'https://api.telegram.org/bot{self.token}/getUpdates')
       request = r.json()
       return request["result"][0]['edited_message']['text']
      except:
        return None



  @property
  def chat_new_members(self):#
      """chat event"""
      try:
       r = requests.get(f'https://api.telegram.org/bot{self.token}/getUpdates')
       request = r.json()
       return request["result"][0]['message']['new_chat_members']
      except:
        return None
  @property
  def update_id(self):
      try:
       r = requests.get(f'https://api.telegram.org/bot{self.token}/getUpdates')
       request = r.json()        
       return request["result"][0]['update_id']
      except:
        return None

  @property
  def callback_data(self):
      try:
       r = requests.get(f'https://api.telegram.org/bot{self.token}/getUpdates')
       request = r.json()
       return request["result"][0]['callback_query']['data']
      except:
        return None

  @property
  def callback_message_id(self):
      try:
       r = requests.get(f'https://api.telegram.org/bot{self.token}/getUpdates')
       request = r.json()
       return request["result"][0]['callback_query']['message']['message_id']
      except:
        return None

  @property
  def callback(self):
      try:
       r = requests.get(f'https://api.telegram.org/bot{self.token}/getUpdates')
       request = r.json()
       return request["result"][0]['callback_query']
      except:
        return None

  @property
  def message(self):#
      r = requests.get(f'https://api.telegram.org/bot{self.token}/getUpdates')
      request = r.json()
      try:
       return request["result"][0]['message']
      except:
        return None
  @property
  def callback_author_username(self):
      try:
       r = requests.get(f'https://api.telegram.org/bot{self.token}/getUpdates')
       request = r.json()
       return request["result"][0]['callback_query']['from']['username']
      except:
        return None

  @property
  def callback_id(self):
      try:
       r = requests.get(f'https://api.telegram.org/bot{self.token}/getUpdates')
       request = r.json()
       return request["result"][0]['callback_query']['id']
      except:
        return None

  @property
  def callback_chat(self):
      try:
       r = requests.get(f'https://api.telegram.org/bot{self.token}/getUpdates')
       request = r.json()
       return request["result"][0]['callback_query']['message']['chat']['id']
      except:
        return None

  @property
  def author_id(self):
      try:
       r = requests.get(f'https://api.telegram.org/bot{self.token}/getUpdates')
       request = r.json()
       return request["result"][0]['message']['from']['id']
      except:
        return None
  @property
  def author_username(self):
      try:
       r = requests.get(f'https://api.telegram.org/bot{self.token}/getUpdates')
       request = r.json()
       return request["result"][0]['message']['from']['username']
      except:
        return None
  @property
  def author_first_name(self):
      try:
       r = requests.get(f'https://api.telegram.org/bot{self.token}/getUpdates')
       request = r.json()
       return request["result"][0]['message']['from']['first_name']
      except:
        return None
  @property
  def text(self):
      try:
       r = requests.get(f'https://api.telegram.org/bot{self.token}/getUpdates')
       request = r.json()
       return request["result"][0]['message']['text']
      except :
        return None

  @property
  def author_is_bot(self):
      try:
       r = requests.get(f'https://api.telegram.org/bot{self.token}/getUpdates')
       request = r.json()
       return request["result"][0]['message']['from']['is_bot']
      except:
        return None

  @property
  def chat_id(self):
      try:
       r = requests.get(f'https://api.telegram.org/bot{self.token}/getUpdates')
       request = r.json()
       return request["result"][0]['message']['chat']['id']
      except:
       return None

  @property
  def language(self):
      try:
       r = requests.get(f'https://api.telegram.org/bot{self.token}/getUpdates')
       request = r.json()
       return request["result"][0]['message']['from']['language_code']
      except:
       return None

  @property
  def reply_message(self):
      try:
       r = requests.get(f'https://api.telegram.org/bot{self.token}/getUpdates')
       request = r.json()
       return request["result"][0]['message']['reply_to_message']
      except:
        return None

  @property
  def reply_message_id(self):
      try:
       r = requests.get(f'https://api.telegram.org/bot{self.token}/getUpdates')
       request = r.json()
       return request["result"][0]['message']['reply_to_message']['message_id']
      except:
        return None

  @property
  def reply_message_author_username(self):
      try:
       r = requests.get(f'https://api.telegram.org/bot{self.token}/getUpdates')
       request = r.json()
       return request["result"][0]['message']['reply_to_message']['from']['username']
      except:
        return None

  @property
  def reply_message_author_is_bot(self):
      try:
       r = requests.get(f'https://api.telegram.org/bot{self.token}/getUpdates')
       request = r.json()
       return request["result"][0]['message']['reply_to_message']['from']['is_bot']
      except:
        return None

  @property
  def reply_message_first_name(self):
      try:
       r = requests.get(f'https://api.telegram.org/bot{self.token}/getUpdates')
       request = r.json()
       return request["result"][0]['message']['reply_to_message']['from']['first_name']
      except:
        return None



  @property
  def reply_message_text(self):
      try:
       r = requests.get(f'https://api.telegram.org/bot{self.token}/getUpdates')
       request = r.json()
       return request["result"][0]['message']['reply_to_message']['text']
      except:
        return None

  @property
  def date(self):
      try:
       r = requests.get(f'https://api.telegram.org/bot{self.token}/getUpdates')
       request = r.json()
       return request["result"][0]['message']['date']
      except:
        return None