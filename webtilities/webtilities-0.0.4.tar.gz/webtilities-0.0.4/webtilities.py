from datetime import datetime,time, timedelta
from urllib.request import Request, urlopen
from time import strftime, strptime, time
import os, requests, pyperclip, math
from pynput import keyboard,mouse
from selenium import webdriver
from bs4 import BeautifulSoup
from threading import Thread
from urllib import response
from timeit import timeit
import pyautogui as ptg
import imagehash as im
from time import sleep
from PIL import Image
import json

def find_file(target,local):
    pathName = lambda root,x: os.path.join(root,x)
    for root, dirs, files in os.walk("C:\\"):
        if(target in files):
            return pathName(root,target)
            
def save_json(js: dict, name: str) -> str:
    file = open(name,"w")
    json.dump(js,file)
    file.close()
    return name
read_json = lambda name: json.loads(open(name).read())

def KeyLogger():
    keys = []
    def on_release(key):
        keys.append(key)
        try:
            print(f'Key: {key.char}')
        except AttributeError:
            print(f'Key: {key}')
        if(keys[-2:] == [keyboard.Key.esc,keyboard.Key.shift]):
            return False

    with keyboard.Listener(on_release=on_release) as listener:
        listener.join()

    return keys

def MouseLogger():
    def on_move(x,y):
        print(x,y)

    def on_click(x, y, button, pressed):
        pos = x,y
        print(pos,button,pressed)

    def on_scroll(x, y, dx, dy):
        pixels = x,y
        axis = dx,dy
        print(pixels,axis)
    with mouse.Listener(on_move=on_move,on_click=on_click,on_scroll=on_scroll) as listener:
        listener.join()


def locateCenterScreen(file: str,infinity: bool = True) -> tuple[int,int]:
    while True:
        try:
            x,y = ptg.locateCenterOnScreen(file)
            if not (infinity or x != None and y != None):
                break
        except:
            print("NOT FINDED! (WTF)")
            pass
    return (x,y)

def clickImgScreen(file: str, infinity: bool = True) -> tuple[int,int]:
    x,y = locateCenterScreen(file,infinity)
    ptg.click(x,y)
    return (x,y)

def sequentialPosClickTimed(positions: list[list[int,int]],button,intervals: list) -> bool:
    for i,j in zip(positions,intervals):
        ptg.click(i,button=button)
        sleep(j)
    return True

sequentialPosClick = lambda positions, button, interval: [ptg.click(i,button=button,interval=interval) for i in positions]
listClickScreen = lambda imgs, infinity, clicks: [clickImgScreen(i,infinity) if clicks else locateCenterScreen(i,infinity) for i in imgs]

def run_threads(thd: list[Thread]):
    for t in thd:
        t.start()
    for t in thd:
        t.join()

def get_intervals(lst,cof):
    div = math.ceil(len(lst)/cof)
    intervals = [[i*div,((i+1)*div) if i < cof-1 else len(lst)] for i in range(cof)]
    intervals = [i for i in intervals if i[1] <= len(lst)]
    if(intervals[-1][0] > intervals[-2][1]):
        intervals[-1][0] = intervals[-2][1]
    if(intervals[-1][0] == intervals[-1][1]):
        intervals.pop()
    intervals = [[lst[i[0]:i[1]]] for i in intervals]
    return intervals

def get_pixel():        
    def on_click(x, y, button, pressed) -> None:
        if(button == mouse.Button.left and pressed):
            pix = ptg.pixel(x,y)
            print(f"{x}x, {y}y: {pix}")
            return pix
        elif(button == mouse.Button.right and pressed):
            return False

    with mouse.Listener(on_click=on_click) as listener:
        listener.join()

    # ...or, in a non-blocking fashion:
    listener = mouse.Listener(on_click=on_click)
    listener.start()

def time_now():
    now = datetime.now()
    return now

def time_func(func):
    start = datetime.now()
    func()
    finish = datetime.now()
    dif = finish-start
    return dif

def typeText(txt: str,frequency: int,method="type") -> str:
    runs = {
        "type":ptg.typewrite(txt,interval=frequency),
        "paste":pyperclip.paste(txt),
    }
    runs[method]
    return txt

def find_file(target,local = "C:\\", isDir = False, both = False):
    pathName = lambda root,x: os.path.join(root,x)
    for root, dirs, files in os.walk(local):
        if(isDir):
            if(target in dirs):
                return pathName(root,target)
        
        elif(both):
            if(target in dirs or target in files):
                return pathName(root,target)

        elif(target in files):
            return pathName(root,target)

header = {
    "User-Agent":"Mozilla/5.0"
}

def download_img(nome: str, url: str, path: str) -> str:
    with open(f"{path}/{nome}","wb") as f:
        im = requests.get(url)
        f.write(im.content)
    return path + nome

def setup_driver(options: list[str] = ["--start-maximized","--detach"]) -> webdriver:
    driver_opt = webdriver.ChromeOptions()
    [driver_opt.add_argument(i) for i in options]
    driver = webdriver.Chrome(options=driver_opt,executable_path=find_file("chromedriver.exe","C:\\"))
    return driver

list_in_element = lambda element,lst: any([i in element.text if(type(element) != str) else i in element for i in lst])
collect_html = lambda url,headers = header: BeautifulSoup(urlopen(Request(url=url,headers=headers)),"html.parser")
collect_hrefs = lambda bs: [i.attrs["href"] for i in bs.find_all("a") if 'href' in i.attrs]
collect_imgs = lambda bs: {i.attrs["alt"]:i.attrs["src"] for i in bs.find_all("img") if "alt" in i.attrs and "src" in i.attrs}
html_to_str = lambda bs: rf'{str(bs).encode("utf-8")}'[2:-1]
str_to_html = lambda text: BeautifulSoup(text,"html.parser")

def flatten_list(target: list, total: bool = False):
    _new = []
    for i in target:
        if(type(i) in [list,tuple]):
            for j in i:
                _new.append(j)
        else:
            _new.append(i)
    return _new

def locate_html_element_by_text(bs,string,multi):
    target = flatten_list([list(bs.find_all(i)) for i in ['p','h1','h2','h3','h4','span']])
    results = []
    for i in target:
        if(string in i.text):
            if(not multi):
                return i
            results.append(i)
    return results if(multi) else None

def image_hash(nome,url,path = 'files/imgs/',download = False) -> list:
    if(download):
        download_img(nome,url,path)
    image = Image.open(path + nome)
    hash = im.phash(image,20)
    return hash



CEND      = '\33[0m'
CBOLD     = '\33[1m'
CITALIC   = '\33[3m'
CURL      = '\33[4m'
CBLINK    = '\33[5m'
CBLINK2   = '\33[6m'
CSELECTED = '\33[7m'

CBLACK  = '\33[30m'
CRED    = '\33[31m'
CGREEN  = '\33[32m'
CYELLOW = '\33[33m'
CBLUE   = '\33[34m'
CVIOLET = '\33[35m'
CBEIGE  = '\33[36m'
CWHITE  = '\33[37m'

CBLACKBG  = '\33[40m'
CREDBG    = '\33[41m'
CGREENBG  = '\33[42m'
CYELLOWBG = '\33[43m'
CBLUEBG   = '\33[44m'
CVIOLETBG = '\33[45m'
CBEIGEBG  = '\33[46m'
CWHITEBG  = '\33[47m'

CGREY    = '\33[90m'
CRED2    = '\33[91m'
CGREEN2  = '\33[92m'
CYELLOW2 = '\33[93m'
CBLUE2   = '\33[94m'
CVIOLET2 = '\33[95m'
CBEIGE2  = '\33[96m'
CWHITE2  = '\33[97m'

CGREYBG    = '\33[100m'
CREDBG2    = '\33[101m'
CGREENBG2  = '\33[102m'
CYELLOWBG2 = '\33[103m'
CBLUEBG2   = '\33[104m'
CVIOLETBG2 = '\33[105m'
CBEIGEBG2  = '\33[106m'
CWHITEBG2  = '\33[107m'