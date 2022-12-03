# Import libs
import sys
from os import system, name, get_terminal_size, path
from traceback import format_exc
from time import time
try:
    from jsonc_parser.errors import ParserError
    from jsonc_parser.parser import JsoncParser
except ModuleNotFoundError:
    sys.exit('Module not found: jsonc_parser')
try:
    from colorama import init, Fore
    init(autoreset=True)
except ModuleNotFoundError:
    sys.exit('Module not found: colorama')
try:
    from requests import get, ConnectionError
except ModuleNotFoundError:
    sys.exit('Module not found: requests')

# Vars
n = 1
err = False
a = False
namespace = {}
VERSION = '1.1'

# Config
read_file = True
READER_VERSION = '1.0'
CONFIG = {'config': {'notify_updates': False, 'welcome_msg': True, 'exit_msg': True, 'crash_msg': True}, 'colors': {'update': {'text_color': Fore.LIGHTCYAN_EX, 'version_color': Fore.LIGHTGREEN_EX}, 'welcome': {'text_color': Fore.LIGHTCYAN_EX, 'padding_color': Fore.LIGHTCYAN_EX}, 'exit': {'success': {'text_color': Fore.LIGHTCYAN_EX, 'padding_color': Fore.LIGHTCYAN_EX}, 'crash': {'text_color': Fore.LIGHTYELLOW_EX, 'padding_color': Fore.LIGHTYELLOW_EX}}, 'promot': {'default': {'sq_brackets': Fore.LIGHTGREEN_EX, 'number': {'normal': Fore.LIGHTWHITE_EX, 'error': Fore.LIGHTRED_EX}, 'dash': Fore.LIGHTGREEN_EX, 'arrow': Fore.LIGHTCYAN_EX, 'indent': {'number_replace': Fore.LIGHTYELLOW_EX, 'sq_brackets': Fore.LIGHTGREEN_EX, 'dash': Fore.LIGHTGREEN_EX, 'arrow': Fore.LIGHTYELLOW_EX}}, 'timeit': {'sq_brackets': Fore.LIGHTGREEN_EX, 'text_color': Fore.LIGHTWHITE_EX, 'dash': Fore.LIGHTGREEN_EX, 'arrow': Fore.LIGHTWHITE_EX, 'time_text': {'text_color': Fore.LIGHTGREEN_EX, 'time_color': Fore.LIGHTYELLOW_EX}, 'indent': {'number_replace': Fore.LIGHTWHITE_EX, 'sq_brackets': Fore.LIGHTGREEN_EX, 'dash': Fore.LIGHTGREEN_EX, 'arrow': Fore.LIGHTWHITE_EX}}}, 'error': {'internal': Fore.LIGHTRED_EX, 'user': Fore.LIGHTRED_EX}}}
CONFIG_PATH = path.abspath(path.expanduser('~/.config/TPython/config.jsonc'))

if path.isfile(CONFIG_PATH):
    try:
        CONFIG = JsoncParser.parse_file(CONFIG_PATH)
    except ParserError:
        sys.exit(f'{Fore.LIGHTRED_EX}error loading {Fore.LIGHTYELLOW_EX}{CONFIG_PATH}')
        read_file = False

if CONFIG['version'] == READER_VERSION and read_file:
    def color_replace(string):
        if string == 'cyan':
            return Fore.LIGHTCYAN_EX
        elif string == 'green':
            return Fore.LIGHTGREEN_EX
        elif string == 'red':
            return Fore.LIGHTRED_EX
        elif string == 'yellow':
            return Fore.LIGHTYELLOW_EX
        elif string == 'white':
            return Fore.LIGHTWHITE_EX
        elif string == 'blue':
            return Fore.LIGHTBLUE_EX
        elif string == 'black':
            return Fore.LIGHTBLACK_EX
        elif string == 'magenta':
            return Fore.LIGHTMAGENTA_EX

    for key0, val0 in CONFIG.items():
        if type(val0) == dict and key0 != 'config':
            for key1, val1 in val0.items():
                if type(val1) == str:
                    CONFIG[key0][key1] = color_replace(val1)
                elif type(val1) == dict:
                    for key2, val2 in val1.items():
                        if type(val2) == str:
                            CONFIG[key0][key1][key2] = color_replace(val2)
                        elif type(val2) == dict:
                            for key3, val3 in val2.items():
                                if type(val3) == str:
                                    CONFIG[key0][key1][key2][key3] = color_replace(val3)
                                elif type(val3) == dict:
                                    for key4, val4 in val3.items():
                                        if type(val4) == str:
                                            CONFIG[key0][key1][key2][key3][key4] = color_replace(val4)

    INP_COLORS = CONFIG['colors']['promot']['default']
    INP_COLORS_INDENT = CONFIG['colors']['promot']['default']['indent']
    TNP_COLORS = CONFIG['colors']['promot']['timeit']
    TNP_COLORS_INDENT = CONFIG['colors']['promot']['timeit']['indent']

    # Update notifier
    if CONFIG['config']['notify_updates']:
        try:
            pypi_json = get('https://pypi.org/pypi/TPython/json')
            pypi_json = pypi_json.json()
            pypi_version = None
            for i in pypi_json['releases']:
                pypi_version = i
            if pypi_version != VERSION:
                print(f'{CONFIG["colors"]["update"]["text_color"]}Newer version of TPython is available: {CONFIG["colors"]["update"]["version_color"]}{pypi_version}')
        except ConnectionError:
            pass
else:
    sys.exit(f"{Fore.LIGHTRED_EX}config file version '{Fore.LIGHTYELLOW_EX}{CONFIG['version']}{Fore.LIGHTRED_EX}' don't match with reader '{Fore.LIGHTYELLOW_EX}{READER_VERSION}{Fore.LIGHTRED_EX}'")

# Entry point
def main():
    global n, err, a

    # exit function
    def ext(crash=False):
        cl = get_terminal_size().columns
        crash_m = 'Crashed'
        success_m = 'Process Completed Successfully'
        if crash:
            if CONFIG['config']['crash_msg']:
                m = crash_m
                for i in range((cl-len(crash_m))//2):
                    m = f'{CONFIG["colors"]["exit"]["crash"]["padding_color"]}-{CONFIG["colors"]["exit"]["crash"]["text_color"]}{m}{CONFIG["colors"]["exit"]["crash"]["padding_color"]}-'
                sys.exit(f'{m}')
        else:
            if CONFIG['config']['exit_msg']:
                m = success_m
                for i in range((cl-len(success_m))//2):
                    m = f'{CONFIG["colors"]["exit"]["success"]["padding_color"]}-{CONFIG["colors"]["exit"]["success"]["text_color"]}{m}{CONFIG["colors"]["exit"]["success"]["padding_color"]}-'
                print(f'{m}')
            sys.exit()

    try:
        # execute function
        def execute(inp, timeit=False):
            global err, n
            run = False
            before = 0
            if timeit:
                before = time()
            try:
                e = eval(inp, namespace)
                if e != None:
                    print(repr(e))
                err = False
            except:
                run = True
            if run:
                try:
                    exec(inp, namespace)
                    err = False
                except Exception:
                    print(f'{CONFIG["colors"]["error"]["user"]}{format_exc()}')
                    err = True
            if timeit:
                print(f'{TNP_COLORS["time_text"]["text_color"]}Execution time: {TNP_COLORS["time_text"]["time_color"]}{time()-before}')
            n += 1

        # Welcome message
        if CONFIG['config']['welcome_msg']:
            cl = get_terminal_size().columns
            m = 'Welcome to TPython'
            cl -= 18
            for i in range(cl//2):
                m = f'{CONFIG["colors"]["welcome"]["padding_color"]}-{CONFIG["colors"]["welcome"]["text_color"]}{m}{CONFIG["colors"]["welcome"]["padding_color"]}-'
            print(f'{m}')

        # Input
        while True:
            try:
                inp = input(f'{INP_COLORS["sq_brackets"]}[{INP_COLORS["number"]["error" if err else "normal"]}{n}{INP_COLORS["sq_brackets"]}]{INP_COLORS["dash"]}-{INP_COLORS["arrow"]}> {Fore.LIGHTWHITE_EX}')
                if not (inp.isspace() or inp == ''):
                    inp = inp.strip()
                    # Exit command
                    if inp in ('exit', 'quit', 'close'):
                        ext()
                    elif inp in ('clear', 'cls') and not ('clear' in namespace or 'cls' in namespace):
                        system('cls' if name == 'nt' else 'clear')
                        err = False
                    # Version command
                    elif inp == 'version' and not 'version' in namespace:
                        print(f'{Fore.LIGHTCYAN_EX}{VERSION}')
                    # TimeIt command
                    elif inp == 'timeit' and not 'timeit' in namespace:
                        while True:
                            tnp = input(f'{TNP_COLORS["sq_brackets"]}[{TNP_COLORS["text_color"]}TimeIt{TNP_COLORS["sq_brackets"]}]{TNP_COLORS["dash"]}-{TNP_COLORS["arrow"]}> {Fore.LIGHTWHITE_EX}').strip()
                            if tnp.endswith(':'):
                                # Statements that require indents eg: def, if
                                while True:
                                    indent = input(f'{TNP_COLORS_INDENT["sq_brackets"]}[{TNP_COLORS_INDENT["text_replace"]}------{TNP_COLORS_INDENT["sq_brackets"]}]{TNP_COLORS_INDENT["dash"]}-{TNP_COLORS_INDENT["arrow"]}> {Fore.LIGHTWHITE_EX}')
                                    if indent.strip() == '':
                                        if not a:
                                            a = True
                                        else:
                                            break
                                    else:
                                        tnp += f'\n\t{indent}' if repr(tnp).startswith('\t') else f'\n\t{indent}'
                                execute(tnp, True)
                                a = False
                                break
                            else:
                                execute(tnp, True)
                                break
                    else:
                        # Statements that require indents eg: def, if
                        if inp.endswith(':'):
                            while True:
                                indent = input(f'{INP_COLORS_INDENT["sq_brackets"]}[{INP_COLORS_INDENT["number_replace"]}{":"*len(str(n))}{INP_COLORS_INDENT["sq_brackets"]}]{INP_COLORS_INDENT["dash"]}-{INP_COLORS_INDENT["arrow"]}> {Fore.LIGHTWHITE_EX}')
                                if indent.strip() == '':
                                    if not a:
                                        a = True
                                    else:
                                        break
                                else:
                                    inp += f'\n\t{indent}' if repr(inp).startswith('\t') else f'\n\t{indent}'
                            execute(inp)
                            a = False
                        else:
                            execute(inp)
            except KeyboardInterrupt:
                print(f'\n{Fore.LIGHTYELLOW_EX}KeyboardInterrupt')
                err = True
    except Exception:
        print(f'\n{Fore.LIGHTRED_EX}{format_exc()}')
        ext(True)