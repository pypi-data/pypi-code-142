import sys
from sys import exc_info

from os.path import basename


def get_frame_fallback(n):
    try:
        raise Exception
    except Exception:
        frame = exc_info()[2].tb_frame.f_back
        for _ in range(n):
            frame = frame.f_back
        return frame


def load_get_frame_function():
    if hasattr(sys, "_getframe"):
        get_frame = sys._getframe
    else:
        get_frame = get_frame_fallback
    return get_frame


get_frame = load_get_frame_function()


class Symbol:
    def __init__(self, key: str) -> None:
        self.key = key
        self.name = self._get_name()

    def __repr__(self) -> str:
        return "{}.{}".format(self.name, self.key)

    def _get_name(self) -> str:
        frame = get_frame(2)
        try:
            name = frame.f_globals["__name__"]
        except KeyError:
            name = None
        code = frame.f_code
        file_path = code.co_filename
        file_name = basename(file_path)

        return name
