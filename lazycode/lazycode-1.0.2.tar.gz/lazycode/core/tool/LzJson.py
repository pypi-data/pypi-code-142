import json
import copy

from lazycode.core.BaseType import BaseType



class LzJson(BaseType):
    __json: dict = None

    def convert_json_str(self, json_str: str): ...

    def json_path(self, path: str) -> list: ...


class LzJsonImp(LzJson):
    __json: dict = None

    def __init__(self, base_type: dict) -> None:
        self.init(base_type)

    def __str__(self) -> str:
        return str(self.__json)

    def init(self, base_type: dict):
        self.__json = base_type

    def to_string(self) -> str:
        return super().to_string()

    def base_type(self):
        return self.__json

    def copy(self):
        return LzJsonImp(copy.deepcopy(self.__json))

    def convert_json_str(self, json_str: str):
        self.__json = json.loads(json_str)
        return self

    def json_path_data(self, path: str):
        """
        :param path: jsonpath 库语法
        :return:
        """
        return jsonpath(self.__json, path)

