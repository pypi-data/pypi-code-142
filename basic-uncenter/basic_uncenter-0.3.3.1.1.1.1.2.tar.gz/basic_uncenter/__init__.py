__version__ = '0.3.3.1.1.1.1.2'
import time
def uncharsplit(list):
    return ''.join(list)
def charsplit(str):
    x = []
    for char in str:
        x.append(char)
    return x
def check_similarity(test, check, rating, debug = False):
    score = 0
    x = []
    for letter in test:
        x.append(letter)
    test = x
    x = []
    for letter in check:
        x.append(letter)
    check = x
    
    charcount = len(test)
    if charcount > len(check):
        charcount = len(check)
    samechar = 0
    for i in range(charcount):
        if test[i] == check[i]:
            samechar += 1
    if samechar >= (charcount/2):
        if debug == True:
            print("\033[0;32m" + "CHAR_POS ✓" + "\033[0m")
        score += 1
    else:
        if debug == True:
            print("\033[0;32m" + "CHAR_POS ✖" + "\033[0m")
    test_unique = []
    check_unique = []
    for char in test:
        if char not in test_unique:
            test_unique.append(char)
    for char in check:
        if char not in check_unique:
            check_unique.append(char)
    if test_unique == check_unique:
        if debug == True:
            print("\033[0;32m" + "UNIQUE ✓" + "\033[0m")
        score += 1
    else:
        if debug == True:
            print("\033[0;32m" + "UNIQUE ✖" + "\033[0m")
    if debug == True:
        print("\033[0;35m" + str(score) + "\033[0m")
    return score >= rating:
# NUMBERS
def isdecimal(var):
    if var.is_integer():
        decimal = False
    else:
        decimal = True
    return decimal
def factorial(num):
    if num < 0:
        factorial = "\033[0;31mInputError: Factorial does not exist for negative numbers"
    elif num == 0:
       factorial = 1
    else:
        factorial = 1
        for i in range(1, num + 1):
           factorial = factorial * i
    return factorial
# PRINTING
def println(str, count = 1):
    print("\n"*count + str)
def printsln(str):
    print(str, end='')
def printx(str, count):
    for i in range(0, count):
        print(str)
def typewriter(str, speed = 1):
    if speed == 1:
        speed = 0.18
    elif speed == 2:
        speed = 0.1
    elif speed == 3:
        speed = 0.03
    if '\033' in str:
        print
    for char in str:
        time.sleep(speed)
        print(char, end='', flush=True)
    print()
# FORMATTING
def bold(str):
    output = "\033[1m" + str + "\033[0m"
    return output
def b(str):
    output = "\033[1m" + str + "\033[0m"
    return output
def italic(str):
    output = "\033[3m" + str + "\033[0m"
    return output
def i(str):
    output = "\033[3m" + str + "\033[0m"
    return output
def underline(str):
    output = "\033[4m" + str + "\033[0m"
    return output
def underl(str):
    output = "\033[4m" + str + "\033[0m"
    return output
def ul(str):
    output = "\033[4m" + str + "\033[0m"
    return output
def format(color = ''):
    if color == 'bold' or var == 'b':
        print("\033[1m", end='')
    elif color == 'italic' or var == 'i':
        print("\033[3m", end='')
    elif color == 'underline' or var == 'underl' or var == 'ul':
        print("\033[4m", end='')
    elif color == 'black':
        print("\033[0;30m", end='')
    elif color == 'red':
        print("\033[0;31m", end='')
    elif color == 'green':
        print("\033[0;32m", end='')
    elif color == 'yellow':
        print("\033[0;33m", end='')
    elif color == 'blue':
        print("\033[0;34m", end='')
    elif color == 'magenta':
        print("\033[0;35m", end='')
    elif color == 'cyan':
        print("\033[0;36m", end='')
    elif color == 'white':
        print("\033[0;37m", end='')
    elif color == 'bright_black':
        print("\033[0;90m", end='')
    elif color == 'bright_red':
        print("\033[0;91m", end='')
    elif color == 'bright_green':
        print("\033[0;92m", end='')
    elif color == 'bright_yellow':
        print("\033[0;93m", end='')
    elif color == 'bright_blue':
        print("\033[0;94m", end='')
    elif color == 'bright_magenta':
        print("\033[0;95m", end='')
    elif color == 'bright_cyan':
        print("\033[0;96m", end='')
    elif color == 'bright_white':
        print("\033[0;97m", end='')
    elif color == 'clear':
        print("\033[0m", end='')
        
def clear():
    print("\033[0m", end='')
### COLORS
def black(str = '', setColor = False):
    if str == '':
        print("\033[0;30m", end='')
        output = None
    else:
        if setColor:
            output = "\033[0;30m" + str
        else:
            output = "\033[0;30m" + str + "\033[0m"
    return output
def red(str = '', setColor = False):
    if str == '':
        print("\033[0;31m", end='')
        output = None
    else:
        if setColor:
            output = "\033[0;31m" + str
        else:
            output = "\033[0;31m" + str + "\033[0m"
    return output
def green(str = '', setColor = False):
    if str == '':
        print("\033[0;32m", end='')
        output = None
    else:
        if setColor:
            output = "\033[0;32m" + str
        else:
            output = "\033[0;32m" + str + "\033[0m"
    return output
def yellow(str = '', setColor = False):
    if str == '':
        print("\033[0;33m", end='')
        output = None
    else:
        if setColor:
            output = "\033[0;33m" + str
        else:
            output = "\033[0;33m" + str + "\033[0m"
    return output
def blue(str = '', setColor = False):
    if str == '':
        print("\033[0;34m", end='')
        output = None
    else:
        if setColor:
            output = "\033[0;34m" + str
        else:
            output = "\033[0;34m" + str + "\033[0m"
    return output
def magenta(str = '', setColor = False):
    if str == '':
        print("\033[0;35m", end='')
        output = None
    else:
        if setColor:
            output = "\033[0;35m" + str
        else:
            output = "\033[0;35m" + str + "\033[0m"
    return output
def cyan(str = '', setColor = False):
    if str == '':
        print("\033[0;36m", end='')
        output = None
    else:
        if setColor:
            output = "\033[0;36m" + str
        else:
            output = "\033[0;36m" + str + "\033[0m"
    return output
def white(str = '', setColorColor = False):
    if str == '':
        print("\033[0;37m", end='')
        output = None
    else:
        if setColor:
            output = "\033[0;37m" + str
        else:
            output = "\033[0;37m" + str + "\033[0m"
    return output
def color(color = '', str = ''):
    if str == '':
        if color == 'black':
            print("\033[0;30m", end='')
        elif color == 'red':
            print("\033[0;31m", end='')
        elif color == 'green':
            print("\033[0;32m", end='')
        elif color == 'yellow':
            print("\033[0;33m", end='')
        elif color == 'blue':
            print("\033[0;34m", end='')
        elif color == 'magenta':
            print("\033[0;35m", end='')
        elif color == 'cyan':
            print("\033[0;36m", end='')
        elif color == 'white':
            print("\033[0;37m", end='')
        elif color == 'bright_black':
            print("\033[0;90m", end='')
        elif color == 'bright_red':
            print("\033[0;91m", end='')
        elif color == 'bright_green':
            print("\033[0;92m", end='')
        elif color == 'bright_yellow':
            print("\033[0;93m", end='')
        elif color == 'bright_blue':
            print("\033[0;94m", end='')
        elif color == 'bright_magenta':
            print("\033[0;95m", end='')
        elif color == 'bright_cyan':
            print("\033[0;96m", end='')
        elif color == 'bright_white':
            print("\033[0;97m", end='')
        elif color == 'clear':
            print("\033[0m", end='')
    else:
        if color == 'black':
            output = "\033[0;30m" + str + "\033[0m"
        elif color == 'red':
            output = "\033[0;31m" + str + "\033[0m"
        elif color == 'green':
            output = "\033[0;32m" + str + "\033[0m"
        elif color == 'yellow':
            output = "\033[0;33m" + str + "\033[0m"
        elif color == 'blue':
            output = "\033[0;34m" + str + "\033[0m"
        elif color == 'magenta':
            output = "\033[0;35m" + str + "\033[0m"
        elif color == 'cyan':
            output = "\033[0;36m" + str + "\033[0m"
        elif color == 'white':
            output = "\033[0;37m" + str + "\033[0m"
        elif color == 'bright_black':
            output = "\033[0;90m" + str + "\033[0m"
        elif color == 'bright_red':
            output = "\033[0;91m" + str + "\033[0m"
        elif color == 'bright_green':
            output = "\033[0;92m" + str + "\033[0m"
        elif color == 'bright_yellow':
            output = "\033[0;93m" + str + "\033[0m"
        elif color == 'bright_blue':
            output = "\033[0;94m" + str + "\033[0m"
        elif color == 'bright_magenta':
            output = "\033[0;95m" + str + "\033[0m"
        elif color == 'bright_cyan':
            output = "\033[0;96m" + str + "\033[0m"
        elif color == 'bright_white':
            output = "\033[0;97m" + str + "\033[0m"
        else:
            output = None
        return output
def fprint(color, str):
    colors = ['bold', 'b', 'italic', 'i', 'underline', 'underl', 'ul', 'black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white', 'bright_black', 'bright_red', 'bright_green', 'bright_yellow', 'bright_blue', 'bright_magenta', 'bright_cyan', 'bright_white']
    if color in colors:
        if color == 'bold' or color == 'b':
            print("\033[1m" + str + '\033[0m')
        elif color == 'italic' or color == 'i':
            print("\033[3m" + str + '\033[0m')
        elif color == 'underline' or color == 'underl' or color == 'ul':
            print("\033[4m" + str + '\033[0m')
        elif color == 'black':
            print("\033[0;30m" + str + "\033[0m")
        elif color == 'red':
            print("\033[0;31m" + str + "\033[0m")
        elif color == 'green':
            print("\033[0;32m" + str + "\033[0m")
        elif color == 'yellow':
            print("\033[0;33m" + str + "\033[0m")
        elif color == 'blue':
            print("\033[0;34m" + str + "\033[0m")
        elif color == 'magenta':
            print("\033[0;35m" + str + "\033[0m")
        elif color == 'cyan':
            print("\033[0;36m" + str + "\033[0m")
        elif color == 'white':
            print("\033[0;37m" + str + "\033[0m")
        elif color == 'bright_black':
            print("\033[0;90m" + str + "\033[0m")
        elif color == 'bright_red':
            print("\033[0;91m" + str + "\033[0m")
        elif color == 'bright_green':
            print("\033[0;92m" + str + "\033[0m")
        elif color == 'bright_yellow':
            print("\033[0;93m" + str + "\033[0m")
        elif color == 'bright_blue':
            print("\033[0;94m" + str + "\033[0m")
        elif color == 'bright_magenta':
            print("\033[0;95m" + str + "\033[0m")
        elif color == 'bright_cyan':
            print("\033[0;96m" + str + "\033[0m")
        elif color == 'bright_white':
            print("\033[0;97m" + str + "\033[0m")
        else:
            print(str)
    else:
        print(color)
def cprint(color, str):
    colors = ['bold', 'b', 'italic', 'i', 'underline', 'underl', 'ul', 'black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white', 'bright_black', 'bright_red', 'bright_green', 'bright_yellow', 'bright_blue', 'bright_magenta', 'bright_cyan', 'bright_white']
    if color in colors:
        if color == 'bold' or color == 'b':
            print("\033[1m" + str + '\033[0m')
        elif color == 'italic' or color == 'i':
            print("\033[3m" + str + '\033[0m')
        elif color == 'underline' or color == 'underl' or color == 'ul':
            print("\033[4m" + str + '\033[0m')
        elif color == 'black':
            print("\033[0;30m" + str + "\033[0m")
        elif color == 'red':
            print("\033[0;31m" + str + "\033[0m")
        elif color == 'green':
            print("\033[0;32m" + str + "\033[0m")
        elif color == 'yellow':
            print("\033[0;33m" + str + "\033[0m")
        elif color == 'blue':
            print("\033[0;34m" + str + "\033[0m")
        elif color == 'magenta':
            print("\033[0;35m" + str + "\033[0m")
        elif color == 'cyan':
            print("\033[0;36m" + str + "\033[0m")
        elif color == 'white':
            print("\033[0;37m" + str + "\033[0m")
        elif color == 'bright_black':
            print("\033[0;90m" + str + "\033[0m")
        elif color == 'bright_red':
            print("\033[0;91m" + str + "\033[0m")
        elif color == 'bright_green':
            print("\033[0;92m" + str + "\033[0m")
        elif color == 'bright_yellow':
            print("\033[0;93m" + str + "\033[0m")
        elif color == 'bright_blue':
            print("\033[0;94m" + str + "\033[0m")
        elif color == 'bright_magenta':
            print("\033[0;95m" + str + "\033[0m")
        elif color == 'bright_cyan':
            print("\033[0;96m" + str + "\033[0m")
        elif color == 'bright_white':
            print("\033[0;97m" + str + "\033[0m")
        else:
            print(str)
    else:
        print(color)