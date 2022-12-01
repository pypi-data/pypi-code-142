from datetime import datetime, timezone
from pathlib import Path
import os
import re


def catch_exception(func):
    def wrapper(*args, **kwargs):
        try:
            out = func(*args, **kwargs)
            return out
        except Exception as e:
            f_name = func.__name__
            exc = f'{f_name} --> {str(e)}'
            raise Exception(exc)
    return wrapper


def clean_string(txt):
    out = txt.replace(r"\n", " ").replace("'", " ")
    out = re.sub(r"\s+", " ", out)
    return out.strip()


def get_time_now():
    return datetime.now(timezone.utc).astimezone().strftime("%Y-%m-%d %H:%M:%S.%f")


def str_to_datetime(tmp_str):
    tmp_str1 = tmp_str.split('.')[0]
    tmp = datetime.strptime(tmp_str1, "%Y-%m-%d %H:%M:%S")
    return tmp


def get_project_root() -> Path:
    return Path(__file__).parent.parent.parent


ROOT_DIR = get_project_root()
