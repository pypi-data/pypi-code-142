# Name: PyQwidgets
# Version: 5.0

from tkinter import *
from tkinter import messagebox

import webbrowser
import pyautogui
import qrcode
import wget

# from PyQwidgets import PyQwidgets

class PyQwidgets:

    def Error(name, text):
        messagebox.showerror(name, text)

    def Warning(name, text):
        messagebox.showwarning(name, text)

    def Info(name, text):
        messagebox.showinfo(name, text)

    def Screenshot(namefile):
        pyautogui.screenshot(name)

    def Download(url, namefile):
        wget.download(url, name)

    def Open(url):
        webbrowser.open(url)

    def QRCode(namefile, link):
        img = qrcode.make(link)
        img.save(namefile)