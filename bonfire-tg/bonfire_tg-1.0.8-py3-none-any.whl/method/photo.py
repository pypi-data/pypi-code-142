
import requests
from colorama import init
init()
from colorama import Fore, Back, Style
from os import path
from PIL import Image,ImageFilter 
import subprocess
import sys
import fileinput



def send_photo(bot=None,chat_id=None,photo=None):
            url = f'https://api.telegram.org/bot{bot}/sendPhoto'
            payload = {
                'chat_id': chat_id,
                'photo' : fileinput.input(files=open('D:/Desktop/bonfire-discord-libraly/obama.png', 'rb'))
                }


            r = requests.post(url,json=payload,)
            return r