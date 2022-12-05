from pynput import keyboard,mouse
import pyautogui as ptg
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

if(__name__ == "__main__"):
    KeyLogger()