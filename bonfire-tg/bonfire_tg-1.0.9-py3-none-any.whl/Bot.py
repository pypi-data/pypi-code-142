import requests
import time
import inspect
import sys
from apscheduler.schedulers.background import BlockingScheduler 
import apscheduler.schedulers.background
from colorama import init
init()
from colorama import Fore, Back, Style
from .methods import message
import datetime
import sys
import os
import signal

class bot:
    def event(token):
     if token == None:
                   print(Fore.YELLOW+f"You did not specify a keyword (token = ...) in the 'event' decorator (line : {sys._getframe(1).f_lineno})"+Style.RESET_ALL)  
                   print(Fore.RED+f"Ви не вказали ключове слово (token = ...) в декораторі 'event'  (лінія :{sys._getframe(1).f_lineno})"+Style.RESET_ALL)
                   sig = getattr(signal, "SIGKILL", signal.SIGTERM)
                   os.kill(os.getpid(), sig)
     def decorator_function(func):
        def wrapper_function():
            msg = message(token)
            if func.__name__ == 'update':
             if msg.message is None:
                 print(Fore.RED+f"""{datetime.datetime.now()} : Callback
                {msg.callback}"""+Style.RESET_ALL) 
                 func() 
                
             if msg.callback is  None:
                if msg.text is None:
                    pass
                else:
                 print(Fore.RED+f"""{datetime.datetime.now()} : Message 
                {msg.message}"""+Style.RESET_ALL) 
                
                 func() 
            else:
                func()
        return wrapper_function 
     return decorator_function

    def handler(token = None,startswith = None,command = None):
     if token == None:
                   print(Fore.YELLOW+f"You did not specify a keyword (token = ...) in the 'handler' decorator (line : {sys._getframe(1).f_lineno})"+Style.RESET_ALL)  
                   print(Fore.RED+f"Ви не вказали ключове слово (token = ...) в декораторі 'handler'  (лінія :{sys._getframe(1).f_lineno})"+Style.RESET_ALL)
                   sig = getattr(signal, "SIGKILL", signal.SIGTERM)
     def decorator_function(original_function):
        def wrapper_function():
            msg = message(token)
            text = msg.text
            if startswith is not None:
                word_list = text.split()
                if word_list[0] == startswith:

                        original_function()
                else:
                    pass
            if command != None:
                if text == command:
                        original_function()
                else:
                    pass
        return wrapper_function
     return decorator_function

    def start_command(mod):
          all_functions = inspect.getmembers(mod, inspect.isfunction)
          for key, value in all_functions:
           if str(inspect.signature(value)) == "()":
            value()

    def status(token):
     
     if token == None:
                   print(Fore.YELLOW+f"You did not specify a keyword (token = ...) in the 'status' decorator (line : {sys._getframe(1).f_lineno})"+Style.RESET_ALL)  
                   print(Fore.RED+f"Ви не вказали ключове слово (token = ...) в декораторі 'stataus'  (лінія :{sys._getframe(1).f_lineno})"+Style.RESET_ALL)
                   sig = getattr(signal, "SIGKILL", signal.SIGTERM)   
     r = requests.get(f'https://api.telegram.org/bot{token}/getUpdates')
     request = r.json()
     if request == {'ok': True, 'result': []}:
        return "none"
     else:
      return "ok"

    def start(token):
     if token == None:
                   print(Fore.YELLOW+f"You did not specify a keyword (token = ...) in the 'start' decorator (line : {sys._getframe(1).f_lineno})"+Style.RESET_ALL)  
                   print(Fore.RED+f"Ви не вказали ключове слово (token = ...) в декораторі 'start'  (лінія :{sys._getframe(1).f_lineno})"+Style.RESET_ALL)
                   sig = getattr(signal, "SIGKILL", signal.SIGTERM)  
     while True:    
       sched = apscheduler.schedulers.background.BackgroundScheduler(job_defaults={'max_instances': 1})
       sched.add_job(status, 'interval', seconds=1/1000,args=[token])
    
    def end_status(token):
       if token == None:
                   print(Fore.YELLOW+f"You did not specify a keyword (token = ...) in the 'end_status' decorator (line : {sys._getframe(1).f_lineno})"+Style.RESET_ALL)  
                   print(Fore.RED+f"Ви не вказали ключове слово (token = ...) в декораторі 'end_status'  (лінія :{sys._getframe(1).f_lineno})"+Style.RESET_ALL)
                   sig = getattr(signal, "SIGKILL", signal.SIGTERM)  
       r = requests.get(f'https://api.telegram.org/bot{token}/getUpdates')
       request = r.json()
       requests.get(f'https://api.telegram.org/bot{token}/getUpdates?offset={request["result"][0]["update_id"] + 1}')


    
      

