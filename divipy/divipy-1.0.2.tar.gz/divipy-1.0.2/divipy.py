
import webbrowser,json,datetime,time,random,colorama,requests,sys,subprocess,os,pyperclip, fake_useragent
from colorama import init;from colorama import Fore;from fake_useragent import UserAgent;init() # All modules has imported

class color: 
    dBlack = Fore.BLACK # All colors
    dBlue = Fore.BLUE # All colors
    dCyan = Fore.CYAN # All colors
    dGreen = Fore.GREEN # All colors
    lBlack = Fore.LIGHTBLACK_EX # All colors
    lBlue = Fore.LIGHTBLUE_EX # All colors
    lCyan = Fore.LIGHTCYAN_EX # All colors
    lGreen = Fore.LIGHTGREEN_EX # All colors
    lMagenta  = Fore.LIGHTMAGENTA_EX # All colors
    lRed = Fore.LIGHTRED_EX # All colors
    lWhite  = Fore.LIGHTWHITE_EX # All colors
    lYellow = Fore.LIGHTYELLOW_EX # All colors
    dMagenta = Fore.MAGENTA # All colors
    dRed = Fore.RED # All colors
    reset = Fore.RESET # All colors
    dWhite = Fore.WHITE # All colors
    dYellow = Fore.YELLOW # All colors


def divipy_help():
    help_panel = """
    Colors: black, blue, cyan, green, yellow, white
    Clear: clear_cli / clear_cli()
    UserAgents: random, safari, firefox, chrome, opera
    Maths: sum, average, multi, divi, sub, per
    Animals: bird, cat, dog, fox, kangaroo, koala, panda, raccoon, red panda
    YouTube Comment: avatar, comment, username (all required) / (avatar, comment, username)
    Dictionary: word / (word)
    Welcome: name / (name)
    """
    print(help_panel)


def clear_cli():
    try:
        os.system("cls") # Windows or other OS
    except:
        os.system("clear") # Linux or MacOS


def random_useragent():
    ua = UserAgent()
    print(f'{color.dGreen}[User Agent/Random >] {color.lBlue}{ua.opera}{color.reset}') # Random UserAgent


def safari_useragent():
    ua = UserAgent()
    print(f'{color.dGreen}[User Agent/Safari >] {color.lBlue}{ua.safari}{color.reset}') # Safari UserAgent


def firefox_useragent():
    ua = UserAgent()
    print(f'{color.dGreen}[User Agent/Firefox >] {color.lBlue}{ua.firefox}{color.reset}') # Firefox UserAgent


def chrome_useragent():
    ua = UserAgent()
    print(f'{color.dGreen}[User Agent/Chrome >] {color.lBlue}{ua.chrome}{color.reset}') # Chrome UserAgent


def opera_useragent():
    ua = UserAgent()
    print(f'{color.dGreen}[User Agent/Opera >] {color.lBlue}{ua.opera}{color.reset}') # Opera UserAgent


def sum(x,y):
    print(x+y)  # Result of x + y


def average(x,y):
    print((x+y)/2)  # Result of x + y / 2


def multi(x,y):
    print(x*y)  # Result of x * y
  

def divi(x,y):
    print(x/y)  # Result of x / y
  

def sub(x,y):
    print(x-y)  # Result of x - y
 

def per(x,y):
    print((x*y)/100)  # Result of x * y / 100


def raccoon():
    r = requests.get('https://some-random-api.ml/animal/raccoon') # api
    content_json = r.json()
    content_section = content_json['image']
    print(f'{color.lGreen} Open raccoon image, please wait...')
    time.sleep(0.5)
    webbrowser.open(content_section)


def bird():
    r = requests.get('https://some-random-api.ml/animal/bird') # api
    content_json = r.json()
    content_section = content_json['image']
    print(f'{color.lGreen} Open bird image, please wait...')
    time.sleep(0.5)
    webbrowser.open(content_section)


def kangaroo():
    r = requests.get('https://some-random-api.ml/animal/kangaroo') # api
    content_json = r.json()
    content_section = content_json['image']
    print(f'{color.lGreen} Open kangaroo image, please wait...')
    time.sleep(0.5)
    webbrowser.open(content_section)


def cat():
    r = requests.get('https://some-random-api.ml/animal/cat') # api
    content_json = r.json()
    content_section = content_json['image']
    print(f'{color.lGreen} Open cat image, please wait...')
    time.sleep(0.5)
    webbrowser.open(content_section)


def dog():
    r = requests.get('https://some-random-api.ml/animal/dog') # api
    content_json = r.json()
    content_section = content_json['image']
    print(f'{color.lGreen} Open dog image, please wait...')
    time.sleep(0.5)
    webbrowser.open(content_section)


def koala():
    r = requests.get('https://some-random-api.ml/animal/koala') # api
    content_json = r.json()
    content_section = content_json['image']
    print(f'{color.lGreen} Open koala image, please wait...')
    time.sleep(0.5)
    webbrowser.open(content_section)

    
def fox():
    r = requests.get('https://some-random-api.ml/animal/fox') # api
    content_json = r.json()
    content_section = content_json['image']
    print(f'{color.lGreen} Open fox image, please wait...')
    time.sleep(0.5)
    webbrowser.open(content_section)

   
def red_panda():
    r = requests.get('https://some-random-api.ml/animal/red_panda') # api
    content_json = r.json()
    content_section = content_json['image']
    print(f'{color.lGreen} Open fox image, please wait...')
    time.sleep(0.5)
    webbrowser.open(content_section)


def dictionary_word(x):
    try:
        r = requests.get(f'https://some-random-api.ml/dictionary?word={x}') # api
        content_json = r.json()
        content_definition = content_json['definition']
        print(f'{color.dYellow}[{color.dGreen}Word:{color.reset} {x}{color.dYellow}] [{color.dGreen}Definition:{color.reset} {content_definition}{color.dYellow}]{color.reset}')
    except:
        print('The word does not exist and an error has occurred, please try again.')
        time.sleep(2)
        clear_cli()

def color_viewer(x):
    try:  
        print(f'{color.lGreen} Open color viewer image, please wait...')
        time.sleep(0.5)
        webbrowser.open(f'https://some-random-api.ml/canvas/colorviewer?hex={x}') # api
    except:
        print('The color does not exist and an error has occurred, please try again.')
        time.sleep(2)
        clear_cli()
def youtube_comment(x,y,z):
    print(f'{color.lGreen} Open YouTube image, please wait...')
    time.sleep(0.5)
    webbrowser.open(f'https://some-random-api.ml/canvas/misc/youtube-comment?avatar={x}&comment={y}&username={z}') # api

def welcome(x):
    print(f'Welcome, {x}!')