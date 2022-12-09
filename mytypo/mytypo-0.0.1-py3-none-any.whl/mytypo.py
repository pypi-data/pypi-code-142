import argparse
import os
import typing as tp
from typing import Tuple
import re
from textblob import TextBlob
from colorama import Fore

parser = argparse.ArgumentParser(
    prog="mytypo",
    description="This programs checks typos in given python file for comments",
)

parser.add_argument("path")

rgx_single_comment = r"#[^\n\r]+\w+$"


def _get_comments_for_single_file(path: str) -> tp.Dict:
    _comments = {}
    with open(path, "r") as f:
        _lines = f.readlines()

    _line_number = 1
    for _l in _lines:
        result = re.match(rgx_single_comment, _l)

        if result:
            _comments["{}:{}".format(path, _line_number)] = result.group(0)

        _line_number += 1

    return _comments


def _get_comments(path: str, is_file: bool = True) -> tp.Dict:

    if is_file:
        return _get_comments_for_single_file(path)
    else:
        dict_main = {}
        for file in os.listdir(path):
            f = os.path.join(path, file)
            if f.endswith(".py"):
                dict_temp = _get_comments_for_single_file(f)
                dict_main.update(dict_temp)
        return dict_main


def check_typo(path=None) -> tp.List[Tuple[str, str, str]]:
    suggestions = []
    if path:
        _path = path
    else:
        args = parser.parse_args()
        _path = args.path

    if os.path.isdir(_path):
        comments = _get_comments(_path, False)
    elif os.path.isfile(_path):
        comments = _get_comments(_path)
    else:
        print("The file or directory is not exist:{}".format(_path))
        return

    for k, v in comments.items():
        v = v.replace("#", "")

        _text_blob = TextBlob(v)
        _corrected = _text_blob.correct()

        if _corrected != v:
            suggest = (k, v, _corrected)
            suggestions.append(suggest)

    return suggestions


if __name__ == "__main__":
    sugggests = check_typo()
    if len(sugggests) > 0:
        for s in sugggests:
            k, v, _corrected = s
            print(
                f"{Fore.LIGHTYELLOW_EX}{k}: miss spell in {Fore.RED}{v}{Fore.RESET}, {Fore.LIGHTYELLOW_EX} suggestion is {Fore.GREEN}{_corrected}{Fore.RESET}"
            )
