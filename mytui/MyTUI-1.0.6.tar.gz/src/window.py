#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import get_terminal_size

def width() -> int:
    return get_terminal_size().columns

def height() -> int:
    return get_terminal_size().lines

def hide_cursor() -> None:
    print('\033[?25l', end='')
    
def show_cursor() -> None:
    print('\033[?25h', end='')

def move(x: int, y: int) -> str:
    return f'\033[{y};{x}H'


if __name__ == '__main__':
    
    print(move(10, 2) + 'test')