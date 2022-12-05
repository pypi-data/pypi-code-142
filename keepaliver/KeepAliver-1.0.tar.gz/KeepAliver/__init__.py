import logging
from flask import Flask
from threading import Thread
from colorama import Fore, init
from datetime import datetime
init(autoreset=True)

class KeepCreate:
    def __init__(self):
        self.app = ''
        self.message = 'Running successfully!'
        self.logs = False
        
    def keep(self):
        self.app = Flask(__name__)
        
        if self.logs == False: pass
        else:
            log = logging.getLogger('werkzeug')
            log.disabled = True
            self.app.logger.disabled = True

        @self.app.route('/')
        def running():
            return str(self.message)
            
        t = Thread(target=self.app.run())
        t.start()

    def run(self, runmsg: str=None, logs: False=None):
        if runmsg is None: runmsg = self.message
        if logs is None: self.logs = False
        elif logs == True: self.logs = True
        else: self.logs = False

        print(f' * [{Fore.LIGHTGREEN_EX}{datetime.today().hour}:{datetime.today().minute}:{datetime.today().second}{Fore.RESET}] KeepAlive is Running: ' + runmsg)
        self.keep()