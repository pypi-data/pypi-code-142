#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Provides Terminal User Interface for Python Projects

Easy way to create TUI in Python
"""

# Built-in/Generic Imports
from atexit import register
from os import name, system 
from signal import signal, SIGWINCH
from typing import Union
from window import width, height, move, hide_cursor, show_cursor
from colors import red_on_gray, on_blue, on_black, gray_on_red, black_on_gray, gray_on_red_blink
hide_cursor()

# 3rd Party Libs
# from blessed import Terminal
from getkey import getkey, keys


__author__ = "Paulin-Dev"
__copyright__ = "Copyright 2022, MyTUI"
__credits__ = []
__license__ = "MIT"
__version__ = "1.0.9"
__maintainer__ = "Paulin-Dev"
__email__ = ""
__status__ = "Development"


# Constants
HORIZONTAL_BAR = b'\xe2\x94\x80'.decode()
VERTICAL_BAR = b'\xe2\x94\x82'.decode()
           

class MyTUI:
    
    __current = None
    __options = []
    __selected = 0
    __selector = (0, 0)
    __input = ''
    __margin = 0
    
    # Config
    __text_ml = 0.05
    __text_mr = 0.05
    __text_center = False
    __quit_key = 'q'
    __can_quit = True
    __input_size = 0.75
    __max_length = 200
    __min_length = 0
    __default_text_length = 0
    __include_spaces = True
    __only_numeric = False
    __only_alpha = False
    
    def __init__(self) -> None:
        ''' raise an exeption if an instance is created '''
        raise Exception('You cannot create an instance of this class, use the class itself')
    
    @classmethod
    def config(cls, text_margin_left: float = 0.05, text_margin_right: float = 0.05, text_center: bool = False, quit_key: str = 'q', 
        can_quit: bool = True) -> None:
        '''Edit TUI configuration 
        Parameters
        ----------
        text_margin_left : `int`
            Percentage of margin left, from `2` to `45`.

        text_margin_right : `int`
            Percentage of margin right, from `2` to `45`.

        text_center : `bool`
            `True` to center text else `False`

        quit_key : `str`
            Key to press to quit

        can_quit : `bool`
            `True` if user can use the `quit_key` to quit else `False`
        '''
        if text_margin_left != cls.__text_ml and 2 <= text_margin_left <= 45:
            cls.__text_ml = text_margin_left/100
        if text_margin_right != cls.__text_mr and 2 <= text_margin_right <= 45:
            cls.__text_mr = text_margin_right/100
        if text_center != cls.__text_center:
            cls.__text_center = text_center
        if quit_key != cls.__quit_key:
            cls.__quit_key = quit_key
        if can_quit != cls.__can_quit:
            cls.__can_quit = can_quit
            
    @classmethod
    def refresh(cls) -> None:
        cls.__current() # type: ignore
                       
    @classmethod
    def __title(cls, title: str) -> str:
        title = title.replace('\n', '')
        if len(title) > width()-13:
            title = title[:width()-13]
        return title
    
    @classmethod
    def __text(cls, text: str) -> list:
        output = []
        max_width = width()-int((cls.__text_ml+cls.__text_mr-0.01)*(width()-5))-5
        while text != "":
            l = cls.__line_width(text, max_width=max_width)
            if '\n' in l:
                l = l.split('\n')
                if '' in l:
                    l.remove('')
                l = l[0]
                text = text[len(l)+1:]
            else:
                text = text[len(l):]
            
            if len(l) != max_width:
                if cls.__text_center:
                    l = ' '*int(max_width/2-len(l)/2) + l
                
            output.append(l)            
        return output
        
    @classmethod
    def menu(cls, title: str = "", text: str = "", options: list = [], no_return: bool = False) -> Union[str, None]:
        ''' create a menu and return the selected option '''
        cls.__current = lambda: cls.menu(title=title, text=text, options=options, no_return=True)
        edited_title = cls.__title(title)
        edited_text = cls.__text(text)
        cls.__margin = len(edited_text)
        height = len(options)+2+len(edited_text) if edited_text else len(options)+1
        cls.__options = options
        cls.__display(title=edited_title, text=edited_text, options=options, content_height=height)
        if not no_return:
            return cls.__loop()  # type: ignore
        
    @classmethod
    def textbox(cls, title: str = "", text: str = "", no_return: bool = False) -> None:
        cls.__current = lambda: cls.textbox(title=title, text=text, no_return=True)
        edited_title = cls.__title(title)
        edited_text = cls.__text(text)
        height = len(edited_text)
        cls.__margin = len(edited_text)
        cls.__display(title=edited_title, text=edited_text, content_height=height, extra_line=False)
        if not no_return:
            return cls.__loop() # type: ignore
    
    @classmethod
    def __line_width(cls, line: str, margin: float = 0.0, max_width: int = 0) -> str:
        line = str(line)
        if margin != 0.0:
            max_width = width()-int(margin*(width()-5))-5
        if len(line) > max_width:
            line = line[:max_width]
        return line
    
    @classmethod
    def __print_selector(cls) -> None:
        if cls.__current.__repr__().find('menu') != -1 and cls.__options:  # type: ignore
            y = ((height() - ((len(cls.__options)+2+cls.__margin if cls.__margin != 0 else len(cls.__options)+1)+5)) // 2) + 4 + cls.__margin + cls.__selected           
            x = int(0.2*width())+2
            print(move(x, y) + gray_on_red(cls.__line_width(cls.__options[cls.__selected], margin=0.2)))
            cls.__selector = (x, y)

        elif cls.__current.__repr__().find('yesno') != -1: # type: ignore
            x = int(0.35*(width()-5))
            y = ((height() - (7+cls.__margin)) // 2) + 4 + cls.__margin + (1 if height() % 2 != 0 and cls.__margin % 2 != 0 or height() % 2 == 0 and cls.__margin % 2 == 0 else 0)
            if height() < 10 + cls.__margin:
                y -= (3+cls.__margin)-(height()+(1 if cls.__margin % 2 != 0 else 0))//2
            if height() > 4:
                if cls.__selected == 0:
                    x += 3
                    print(move(x, y) + gray_on_red('Yes'))
                else:
                    x += (width()-5)-(2*x) +1
                    print(move(x, y) + gray_on_red('No'))
                cls.__selector = (x, y)
            
    @classmethod
    def __print_input_text(cls) -> None:
        
        input_size = int((cls.__input_size)*(width()-5))
        input_size += 1 if input_size % 2 == 0 and width() % 2 == 0 or input_size % 2 != 0 and width() % 2 != 0 else 0

        if cls.__selected < len(cls.__input):
            cls.__selected = input_size
        if cls.__selected >= input_size and len(cls.__input) >= input_size:
            cls.__selected = input_size-1
        elif cls.__selected > len(cls.__input) and len(cls.__input) < input_size:
            cls.__selected = len(cls.__input)

        x = ((width()-5) - input_size) // 2 + 3
        y = ((height() - (8 + cls.__margin)) // 2) + 5 + cls.__margin #+ (1 if height() % 2 == 0 and cls.__margin % 2 != 0 or height() % 2 != 0 and cls.__margin % 2 == 0 else 0)
        
        if height() <= 9+cls.__margin:
            y = 0

        text = cls.__input[(len(cls.__input)-(input_size-1)):] if len(cls.__input) >= input_size-1 else cls.__input

        print(move(x, y) + gray_on_red(text))
        print(move(x+cls.__selected, y) + gray_on_red_blink('_'))

    @classmethod
    def __erase_selector(cls) -> None:
        if cls.__current.__repr__().find('menu') != -1 and cls.__options: # type: ignore
            print(move(cls.__selector[0], cls.__selector[1]) + black_on_gray(cls.__line_width(cls.__options[cls.__selected], margin=0.2)))
        elif cls.__current.__repr__().find('yesno') != -1: # type: ignore
            if cls.__selected == 0:
                print(move(cls.__selector[0], cls.__selector[1]) + black_on_gray('Yes'))
            else:
                print(move(cls.__selector[0], cls.__selector[1]) + black_on_gray('No'))
    
    @classmethod
    def yesno(cls, title: str = "", text: str = "", no_return: bool = False) -> Union[bool, None]:
        ''' create a yes no choice, return False for 'no' and True for 'yes' '''
        cls.__current = lambda: cls.yesno(title=title, text=text, no_return=True)
        edited_title = cls.__title(title)
        edited_text = cls.__text(text)
        cls.__margin = len(edited_text)
        height = len(edited_text)+2 if edited_text else 1
        cls.__display(title=edited_title, text=edited_text, yesno=True, content_height=height)
        if not no_return:
            return cls.__loop() # type: ignore
    
    @classmethod
    def input(cls, title: str = "", text: str = "", max_length: int = 1000, min_length: int = 0, default_text: str = "", can_delete_default_text: bool = False, 
              input_size: int = 75, no_return: bool = False, allow_spaces: bool = True, only_numeric: bool = False,
              only_alpha: bool = False) -> Union[str, None]:
        ''' create an input field and return the input string '''
        cls.__current = lambda: cls.input(title=title, text=text, no_return=True)
        edited_title = cls.__title(title)
        edited_text = cls.__text(text)
        height = len(edited_text)+2 if edited_text else 1
        cls.__margin = len(edited_text)
        if not no_return:
            if 10 < input_size < 90:
                cls.__input_size = input_size/100
            cls.__include_spaces = allow_spaces
            cls.__default_text_length = len(default_text) if not can_delete_default_text else 0
            cls.__min_length = min_length + len(default_text)
            cls.__max_length = max_length + len(default_text)
            cls.__input = default_text
            cls.__selected = len(default_text)
            cls.__only_numeric = only_numeric
            cls.__only_alpha = only_alpha
        cls.__display(title=edited_title, text=edited_text, input=True, content_height=height)
        if not no_return:
            return cls.__loop() # type: ignore
        
    @classmethod
    def __display_top(cls, title: str, spaces: int) -> None:
        print(move(0, 0) + on_blue(''), end='')
        for i in range(spaces):
            print(on_blue(' '*width()))
        if title:
            bar_length = width() - len(title) - 10
            bonus = 1 if len(title) % 2 != 0 and width() % 2 == 0 or len(title) % 2 == 0 and width() % 2 != 0 else 0
            print(on_blue(" ") + black_on_gray(b"\xe2\x94\x8c".decode() + HORIZONTAL_BAR*((bar_length//2)) + b"\xe2\x94\xa4".decode() + '  ') + red_on_gray(title) + black_on_gray("  " + b"\xe2\x94\x9c".decode() + HORIZONTAL_BAR*((bar_length//2)-1+bonus) + b"\xe2\x94\x90".decode()) + on_blue("  "))
        else:
            print(on_blue(" ") + black_on_gray(b"\xe2\x94\x8c".decode() + HORIZONTAL_BAR*(width()-5) + b"\xe2\x94\x90".decode()) + on_blue("  "))
        print(f'{on_blue(" ") + black_on_gray(VERTICAL_BAR + " "*(width()-5) + VERTICAL_BAR) + on_black(" ") + on_blue(" ")}')

    @classmethod
    def __display_bottom(cls, spaces: int, extra_line: bool = True, yesno: bool = False, menu: bool = False, input: bool = False) -> None:
        if extra_line:
            print(f'{on_blue(" ") + black_on_gray(VERTICAL_BAR + " "*(width()-5) + VERTICAL_BAR) + on_black(" ") + on_blue(" ")}')
        print(on_blue(" ") + black_on_gray(b"\xe2\x94\x94".decode() + HORIZONTAL_BAR*(width()-5) + b"\xe2\x94\x98".decode()) + on_black(" ") + on_blue(" "))
        print(on_blue("  ") + on_black(" "*(width()-3) + on_blue(" ")))

        for i in range(spaces):
            if i == spaces - 1:
                print(on_blue(' '*width()), end='')
            else:
                print(on_blue(' '*width()))
        
    @classmethod
    def __display_text(cls, text: list) -> None:
        gap = int(cls.__text_ml*(width()-5))
        for line in text:
            print(f'{on_blue(" ") + black_on_gray(VERTICAL_BAR + " "*gap + line + " "*(width()-5-len(line)-gap) + VERTICAL_BAR) + on_black(" ") + on_blue(" ")}')
        print(f'{on_blue(" ") + black_on_gray(VERTICAL_BAR + " "*(width()-5) + VERTICAL_BAR) + on_black(" ") + on_blue(" ")}')
    
    @classmethod
    def __display_options(cls, options: list) -> None:
         for line in options:
            gap = int(0.2*(width()-5))
            line = cls.__line_width(line, margin=0.2)
            print(f'{on_blue(" ") + black_on_gray(VERTICAL_BAR + " "*gap + line + " "*(width()-5-len(line)-gap) + VERTICAL_BAR) + on_black(" ") + on_blue(" ")}')

    @classmethod
    def __display_yesno(cls) -> None:
        lr_gap = int(0.35*(width()-5))
        middle_gap = (width()-5-(2*lr_gap))-5
        print(f'{on_blue(" ") + black_on_gray(VERTICAL_BAR + " "*(width()-5) + VERTICAL_BAR) + on_black(" ") + on_blue(" ")}')
        print(f'{on_blue(" ") + black_on_gray(VERTICAL_BAR + " "*lr_gap + "Yes" + " "*middle_gap + "No" + " "*lr_gap + VERTICAL_BAR) + on_black(" ") + on_blue(" ")}')
    
    @classmethod
    def __display_input(cls) -> None:
        input_size = int((cls.__input_size)*(width()-5))
        gap = ((width()-5) - input_size) // 2
        input_size += 1 if input_size % 2 == 0 and width() % 2 == 0 or input_size % 2 != 0 and width() % 2 != 0 else 0
        print(f'{on_blue(" ") + black_on_gray(VERTICAL_BAR + " "*(width()-5) + VERTICAL_BAR) + on_black(" ") + on_blue(" ")}')
        print(f'{on_blue(" ") + black_on_gray(VERTICAL_BAR + " "*gap) + gray_on_red(" "*input_size) + black_on_gray(" "*gap + VERTICAL_BAR) + on_black(" ") + on_blue(" ")}')
    
    @classmethod
    def __add_input_text(cls, key):
        if len(cls.__input) < cls.__max_length:
            cls.__input += str(key)
            input_size = int((cls.__input_size)*(width()-5))
            input_size += 1 if input_size % 2 == 0 and width() % 2 == 0 or input_size % 2 != 0 and width() % 2 != 0 else 0

            if cls.__selected < input_size-1:
                cls.__selected += 1
            
            cls.__print_input_text()

    @classmethod
    def __remove_input_text(cls) -> None:
        if cls.__selected > 0 and cls.__selected > cls.__default_text_length:
            input_size = int((cls.__input_size)*(width()-5))
            input_size += 1 if input_size % 2 == 0 and width() % 2 == 0 or input_size % 2 != 0 and width() % 2 != 0 else 0
            x = ((width()-5) - input_size) // 2 + 2 + cls.__selected
            y = ((height() - (8 + cls.__margin)) // 2) + 6 + cls.__margin - (1 if height() % 2 != 0 else 0)
            print(move(x+1, y) + gray_on_red(' '))
            cls.__input = cls.__input[:-1]
            if cls.__selected > len(cls.__input):
                cls.__selected -= 1
                print(move(x, y) + gray_on_red(' '))
            cls.__print_input_text()

    @classmethod
    def __display(cls, title: str = "", text: list = [], options: list = [], yesno: bool = False, input: bool = False,
                  content_height: int = 0, extra_line: bool = True) -> None:
        ''' '''
        spaces = (height() - (content_height+5)) // 2
        cls.__display_top(title, spaces)
        
        if text:
            cls.__display_text(text)
        if options:
            cls.__display_options(options)
        if yesno:
            cls.__display_yesno()
        if input:
            cls.__display_input()
               
        cls.__display_bottom(spaces, extra_line, yesno, menu=True if options else False, input=input)
        if input:
            cls.__print_input_text()
        else:
            cls.__print_selector()
            
        print(move(0, 0))
    
    @classmethod
    def clear(cls) -> None:
        ''' clear the terminal '''
        if name == 'nt':
            system('cls')
        else:
            system('clear')
            
    @classmethod
    def __on_keydown(cls, key) -> Union[str, None, bool]:
        if key.isalnum() or key == keys.SPACE and cls.__include_spaces or key in ['!', '"', "'", '?', '.', ',', '@', '%', ':', ';', '/', '&', '~', '#', '{', '}', '(', ')', '[', ']', '-', '|', '_', '\\', '/', '*', '<', '>', '§', '^', '+', '=']:
            if cls.__current.__repr__().find('input') != -1: # type: ignore
                if cls.__only_numeric:
                    if key.isnumeric():
                        cls.__add_input_text(key)
                elif cls.__only_alpha:
                    if key.isalpha():
                        cls.__add_input_text(key)
                else:
                    cls.__add_input_text(key)
        else:
            if key in [keys.UP, keys.DOWN] and cls.__current.__repr__().find('menu') != -1: # type: ignore
                cls.__erase_selector()
                if key == keys.UP:
                    if cls.__selected == 0:
                        cls.__selected = len(cls.__options) - 1
                    else:
                        cls.__selected -= 1
                elif key == keys.DOWN:
                    if cls.__selected == len(cls.__options)-1:
                        cls.__selected = 0
                    else:
                        cls.__selected += 1
                cls.__print_selector()

            elif key in [keys.RIGHT, keys.LEFT, keys.TAB] and cls.__current.__repr__().find('yesno') != -1: # type: ignore
                cls.__erase_selector()
                if key == keys.RIGHT:
                    cls.__selected = 1
                elif key == keys.LEFT:
                    cls.__selected = 0
                elif key == keys.TAB:
                    if cls.__selected == 0:
                        cls.__selected = 1
                    else:
                        cls.__selected = 0
                cls.__print_selector()
                
            elif key == keys.ENTER:
                if cls.__current.__repr__().find('menu') != -1: # type: ignore
                    return cls.__options[cls.__selected] if cls.__options else 'error'
                elif cls.__current.__repr__().find('yesno') != -1: # type: ignore
                    if cls.__selected == 0:
                        return True
                    return False
                elif cls.__current.__repr__().find('input') != -1: # type: ignore
                    if len(cls.__input) >= cls.__min_length:
                        return cls.__input
                elif cls.__current.__repr__().find('text') != -1: # type: ignore
                    return ' '
            
            elif key == keys.ESC:
                return "back"
            
            elif key == keys.BACKSPACE and cls.__current.__repr__().find('input') != -1: # type: ignore
                cls.__remove_input_text()
        

    @classmethod
    def __loop(cls) -> Union[str, bool, None]:
        try:
            while True:
                key = getkey()
                output = cls.__on_keydown(key)
                if output is not None:
                    return output
                if key.lower() == cls.__quit_key and cls.__can_quit and cls.__current.__repr__().find('input') == -1: # type: ignore
                    exit()
        except KeyboardInterrupt:
            cls.__loop()
        finally:
            MyTUI.clear()


def on_resize(sig, action) -> None:
    MyTUI.clear()
    MyTUI.refresh()

signal(SIGWINCH, on_resize)
register(show_cursor)
MyTUI.clear()

if __name__ == '__main__':
    pass