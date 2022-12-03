import os
import typing
from pathlib import Path

from picsexl.icssniffer.exceptions import ICSSnifferException


class ICSSniffer:
    def __init__(self, file_path: str):
        self.__file_path: str = file_path
        self.__file_endswith: str = ".ics"
        self.__is_file: bool = os.path.isfile(file_path)
        self.__main_path: str

    def get_ics_file_string(self) -> typing.AnyStr:
        try:
            return self.__read_ics_file()
        except Exception as exc:
            raise ICSSnifferException(exc=exc)

    @property
    def is_file(self) -> bool:
        return self.__is_file

    @property
    def main_path(self) -> str:
        return self.__main_path

    def __read_ics_file(self) -> typing.AnyStr:
        if any(
            (
                not os.path.exists(self.__file_path),
                not self.__is_file,
                not self.__file_path.endswith(self.__file_endswith),
            )
        ):
            raise NotADirectoryError

        if self.__is_file:
            self.__main_path = str(Path(self.__file_path).parent.absolute())

        with open(self.__file_path, "r", encoding="utf-8") as ics_file:
            return ics_file.read()
