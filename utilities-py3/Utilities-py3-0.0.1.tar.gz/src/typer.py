import pyautogui as ptg
import pyperclip

def typeText(txt: str,frequency: int,method="type") -> str:
    runs = {
        "type":ptg.typewrite(txt,interval=frequency),
        "paste":pyperclip.paste(txt),
    }
    runs[method]
    return txt