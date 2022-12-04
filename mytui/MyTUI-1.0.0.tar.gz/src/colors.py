
BASE = '\x1b['
RESET = f'{BASE}0m'

# Foregrounds
FG_NONE = 0
FG_BLACK = 30
FG_RED = 31
FG_GREEN = 32
FG_YELLOW = 33
FG_BLUE = 34
FG_PURPLE = 35
FG_LIGHT_BLUE = 36
FG_GRAY = 37

# Backgrounds
BG_NONE = 50
BG_BLACK = 40
BG_RED = 41
BG_GREEN = 42
BG_YELLOW = 43
BG_BLUE = 44
BG_PURPLE = 45
BG_LIGHT_BLUE = 46
BG_GRAY = 47

# Effects
BLINK = 6


def color(text: str, fg: int, bg: int, style: int = 0) -> str:
    return f'{BASE}{style};{fg};{bg}m{text}{RESET}'

def red_on_gray(text: str) -> str:
    return color(text, FG_RED, BG_GRAY)

def on_blue(text: str) -> str:
    return color(text, FG_NONE, BG_BLUE)

def on_black(text: str) -> str:
    return color(text, FG_NONE, BG_BLACK)

def gray_on_red(text: str) -> str:
    return color(text, FG_GRAY, BG_RED)

def black_on_gray(text: str) -> str:
    return color(text, FG_BLACK, BG_GRAY)

def gray_on_red_blink(text: str) -> str:
    return color(text, FG_GRAY, BG_RED, BLINK)
