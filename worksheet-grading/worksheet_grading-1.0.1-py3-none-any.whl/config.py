# external imports

import pandas as pd
import os
import json

# local imports

from worksheet_grading.util import print_err, print_info, suffix_string

# ========== CONSTANTS ========== #

EX_PATTERN = r"([0-9]+)-([0-9]+)"

# format for student header in csv files
STUDENT_PATTERN = r"student_([1-9])"
STUDENT_FORMAT = "student_{}"

NA = "NA"

FEEDBACK_PATTERN = r"@([0-9]+)@(-?[0-9]*(\.[0-9]+)?)@(.*)"

CSV_FIRSTLINE = "exercise,group,student_1,student_2,points,feedback\n"
DEDUCTIONS_FIRSTLINE = "ex_num,ans_num,reason,points,count\n"

DEFAULT_FIRSTEX = 1
DEFAULT_LASTEX = 15

GRADED = 0
PARTIALLY_GRADED = 1
UNGRADED = 2

# alignment widths
MAX_GROUP_LEN = 0
MAX_NAMES_LEN = 0

# symbols
RIGHT_ARROW = "→"
LEFT_ARROW = "←"
UP_ARROW = "↑"
DOWN_ARROW = "↓"
ENTER_ARROW = "↲"

PDF_VIEWERS = ["evince", "okular", "xdg-open", "open", "wslview"]

# ========== ADAPTABLE CONFIGURATION ========== #

CSV_BASENAME = "_{:02d}.csv"
CSV_PATTERN = r"_([0-9][0-9]).csv"
AUTOSAVE_FILENAME = ".{}_autosave.csv"
DEDUCTION_FILE = ".{}_deductions.csv"
SHEETNAME = ""

# ========== JSON CONFIGURATION ========== #

# json keys
JSON_SHEETNAME = "sheetname"
JSON_PDF_PATH = "pdf-path"
JSON_GROUPSIZE = "group-size"
JSON_EXERCISES = "exercises"

# number of students per group
GROUP_SIZE = None

# default path of submission pdfs
PDF_PATH = "pdf/"

# exercises and sheet name
EXERCISES = {}
SHEETNAME = ""


def detect_group_size(df: pd.DataFrame):
    global GROUP_SIZE
    if GROUP_SIZE is None:
        print_info("Trying to detect group size from CSV files") 
        i = 1
        while STUDENT_FORMAT.format(i) in df:
            i += 1
        i -= 1
        if i == 0:
            print_err("No valid student columns detected in CSV files, exiting")
            exit(1)
        else:
            print_info(f"Detected {i} students per group")
            GROUP_SIZE = i


