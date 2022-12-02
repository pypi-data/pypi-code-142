#!/usr/bin/env python

import colorama
import sys

# ========== LICENSE AND AUTHOR ========== #

__author__ = "Klaus Kraßnitzer"
__copyright__ = "Copyright (C) 2022 " + __author__
__version__ = "1.2"
__license__ = "Distributed under the MIT License: <https://mit-license.org/>"
__program__ = "Parallel Computing Grading Script"
__repository__ = "<https://gitlab.com/kdvkrs/parcomp_grading>"


def print_version():
    print(bright(light_blue(" ".join([__program__, __version__]))))
    print(bright(__copyright__))
    print(__license__)
    print()
    print("Written by {}, see".format(__author__))
    print(__repository__)


# ========== TERMINAL COLOR ========== #

# Color configuration
COLOR = True

def set_color(color):
	global COLOR
	COLOR = color


def red(msg):
    if COLOR:
        return colorama.Fore.RED + str(msg) + colorama.Fore.RESET
    else:
        return str(msg)


def green(msg):
    if COLOR:
        return colorama.Fore.GREEN + str(msg) + colorama.Fore.RESET
    else:
        return str(msg)


def magenta(msg):
    if COLOR:
        return colorama.Fore.MAGENTA + str(msg) + colorama.Fore.RESET
    else:
        return str(msg)


def yellow(msg):
    if COLOR:
        return colorama.Fore.YELLOW + str(msg) + colorama.Fore.RESET
    else:
        return str(msg)


def light_red(msg):
    if COLOR:
        return colorama.Fore.LIGHTRED_EX + str(msg) + colorama.Fore.RESET
    else:
        return str(msg)


def light_yellow(msg):
    if COLOR:
        return colorama.Fore.LIGHTYELLOW_EX + str(msg) + colorama.Fore.RESET
    else:
        return str(msg)


def light_green(msg):
    if COLOR:
        return colorama.Fore.LIGHTGREEN_EX + str(msg) + colorama.Fore.RESET
    else:
        return str(msg)


def light_blue(msg):
    if COLOR:
        return colorama.Fore.LIGHTBLUE_EX + str(msg) + colorama.Fore.RESET
    else:
        return str(msg)


def dim(msg):
    return colorama.Style.DIM + str(msg) + colorama.Style.RESET_ALL


def bright(msg):
    return colorama.Style.BRIGHT + str(msg) + colorama.Style.RESET_ALL


def highlight(msg):
    return colorama.Back.LIGHTBLACK_EX + bright(str(msg)) + colorama.Back.RESET




# ========== UTILITY ========== #

def suffix_string(csv_name, suffix):
    return csv_name.replace(".csv", "") + suffix + ".csv"


def print_err(msg):
    sys.stderr.write(bright(red(msg)) + "\n")


def print_info(msg):
    print(magenta("INFO: " + str(msg)))


def print_warn(msg):
    print("WARN: " + str(msg))