import os
import sys
import shutil
import inspect
from datetime import datetime, timedelta, date

if not os.path.exists('LOG'):
	os.makedirs('LOG')
v = False
actual_process = os.getpid()

DEFAULT = '\x1b[0m'
BOLD = '\x1b[1m'  # SCRIPT step critical warning
BLACK = '\x1b[30m'  # tobechecked
RED = '\x1b[31m'  # error critical
RED_U = '\x1b[41m'
GREEN = '\x1b[32m'  # success
YELLOW = '\x1b[33m'  # warn tobechecked
YELLOW_U = '\x1b[43m'  # tobechecked
CYAN = '\x1b[36m'  # SCRIPT + STUD
BLUE = '\x1b[34m'  # step
GREY = '\x1b[37m'
GREY_U = '\x1b[47m'  # critical
PINK = '\x1b[35m'  # debug

color_type = {
	"CRITICAL": GREY_U + RED + BOLD,
	"TOBECHECKED": YELLOW,
	"ERROR": RED,
	"SUCCESS": GREEN,
	"WARNING": YELLOW + BOLD,
	"MESSAGE": CYAN + BOLD,
	"STUD": CYAN,
	"STEP": BLUE + BOLD,
	"INFO": DEFAULT,
	"DEBUG": PINK,
}

all_type = {
	"SUCCESS": False,
	"ERROR": False,
	"MESSAGE": False,
	"CRITICAL": False,
	"DEBUG": False,
	"INFO": False,
	"FULL_LOG": False,
}

@staticmethod
def get_function_history():
	stack = inspect.stack()[3]
	ret = {
		'ftc_name': stack[3]
	}
	tmp = stack[1].split('/')
	ret['file_name'] = tmp[len(tmp) - 1]
	return ret


@staticmethod
def format_time():
	return (datetime.now()).strftime("%d/%m/%Y - %X")


@staticmethod
def rotate_file(type):
	if os.path.getsize(f'./LOG/{type}/{type.lower()}.log') > 1000000:
		shutil.copy(f'./LOG/{type}/{type.lower()}.log',
					f'./LOG/{type}/{type.lower()}_{len(os.listdir(f"./LOG/{type}"))}.log')
		os.remove(f'./LOG/{type}/{type.lower()}.log')
	if os.path.getsize(f'./LOG/full_log.log') > 6000000:
		fds = os.listdir(f"./LOG/")
		nb = 0
		for fd in fds:
			if "full_log" in fd:
				nb += 1
		shutil.copy(f'./LOG/full_log.log', f'./LOG/full_log_{nb}.log')
		os.remove(f'./LOG/full_log.log')


@staticmethod
def file_stream(type, str):
	low_type = type.lower()
	ftc = get_function_history()
	if not os.path.exists(f'./LOG/{type}'):
		os.makedirs(f'./LOG/{type}')
	with open(f'./LOG/{type}/{low_type}.log', 'a') as type_file:
		if not all_type[type]:
			type_file.write("\n")
			all_type[type] = True
		type_write = f"{type} :: {actual_process} :: {format_time()} :: {str}\n"
		type_file.write(type_write)
	to_write = f"{type} :: {actual_process} :: {format_time()} :: {ftc['file_name']} :: {ftc['ftc_name']} :: {str}\n"
	with open('./LOG/full_log.log', 'a') as file:
		if not all_type['FULL_LOG']:
			file.write("\n")
			all_type['FULL_LOG'] = True
		file.write(to_write)
	rotate_file(type)
	if type_write[-1] == '\n':
		type_write = type_write[:-1]
	return type_write


@staticmethod
def standart_stream(type, print_str):
	print(color_type[type] + print_str + DEFAULT)


def success(*args):
	to_print = file_stream("SUCCESS", args[0])
	if v:
		standart_stream("SUCCESS", to_print)


def message(*args):
	to_print = file_stream("MESSAGE", args[0])
	if v:
		standart_stream("MESSAGE", to_print)
	else:
		standart_stream("MESSAGE", args[0])


def info(*args):
	to_print = file_stream("INFO", args[0])
	if v:
		standart_stream("INFO", to_print)
	else:
		standart_stream("INFO", args[0])


def error(*args):
	to_print = file_stream("ERROR", args[0])
	if v:
		standart_stream("ERROR", to_print)


def debug(*args):
	to_print = file_stream("DEBUG", args[0])
	if v:
		standart_stream("DEBUG", to_print)
	else:
		standart_stream("DEBUG", args[0])


def critical(*args):
	to_print = file_stream("CRITICAL", args[0])
	if v:
		standart_stream("CRITICAL", to_print)
	else:
		standart_stream("CRITICAL", args[0])


def step(*args):
	pass


def verbose():
	global v
	v = True


def unverbose():
	global v
	v = False


def get_verbose():
	return v


message(f"Start Log module")



