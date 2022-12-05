import pyautogui as ptg
from pynput import mouse

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

if(__name__ == "__main__"):
    get_pixel()