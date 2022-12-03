import collections
import logging
import types
from copy import deepcopy
from dataclasses import dataclass
from functools import lru_cache
from inspect import isclass
from logging.config import DictConfigurator
from typing import Dict, List, Set

from django.conf import settings

#
# def get_handlers():
#     return [(k, k) for k in settings.LOGGING["handlers"]]
from .handlers import InspectRedisHandler


@lru_cache(100)
def fqn(o, silent=False, from_module=None):
    """Returns the fully qualified class name of an object or a class

    :param o: object or class
    :return: class name
    """
    parts = []
    if isinstance(o, (str, bytes)):
        return o
    if not hasattr(o, "__module__"):
        if silent:
            return
        raise ValueError("Invalid argument `%s` %s" % (type(o), o))
    parts.append(o.__module__)
    if isclass(o):
        parts.append(o.__name__)
    elif isinstance(o, types.FunctionType):
        parts.append(o.__name__)
    else:
        parts.append(o.__class__.__name__)
    return ".".join(parts)


@lru_cache(10)
def find_handler_name_by_class(c):
    for h, conf in settings.LOGGING["handlers"].items():
        if conf["class"] == fqn(c):
            return h
    return "unknown"


@lru_cache(10)
def find_handler_name_by_instance(h: logging.Handler):
    for handler_name, conf in settings.LOGGING["handlers"].items():
        if conf and conf["class"] == fqn(h):
            fmt: logging.Formatter = h.formatter
            if fmt:
                format = settings.LOGGING["formatters"][conf["formatter"]]["format"]
                if format == h.formatter._fmt:
                    return handler_name
            else:
                return handler_name
    return None
    # return f"{h.__class__.__name__}({id(h)})"


class CurrentConfig:
    def __init__(self):
        self.dict_config = settings.LOGGING
        self.nameToHandler: Dict[str, object] = {}
        self.handlers: Set = set()
        self.config: Dict = {}
        self.nameToHandler["inspect"] = InspectRedisHandler()

    def get_inspect_handler(self):
        return InspectRedisHandler()

    def get_handlers(self):
        return [(k, k) for k in settings.LOGGING["handlers"] if k in self.nameToHandler]

    def get_suitable_handlers(self, logger: logging.Logger) -> List[str]:
        ret = []
        for instance in logger.handlers:
            if name := find_handler_name_by_instance(instance):
                ret.append(name)
                self.nameToHandler[name] = instance
        return ret

    def get_handler_by_name(self, name):
        try:
            return self.nameToHandler[name]
        except KeyError:
            raise
            # cfg = DictConfigurator({"formatters": self.dict_config["formatters"]})
            # config = self.dict_config["handlers"][name]
            # result = cfg.configure_handler(config)
            # self.nameToHandler[name] = result
            # return result

    def inspect(self):
        config = {}
        handler_names = []
        rootlogger = logging.getLogger()
        hs = self.get_suitable_handlers(rootlogger)
        config["root"] = {
            "level": logging._levelToName[rootlogger.getEffectiveLevel()],
            "handlers": hs,
            "propagate": rootlogger.propagate,
        }
        handler_names.extend(hs)

        for nm, lgr in logging.Logger.manager.loggerDict.items():
            if not isinstance(lgr, logging.PlaceHolder):
                hs = self.get_suitable_handlers(lgr)
                config[nm] = {
                    "level": logging._levelToName[lgr.getEffectiveLevel()],
                    "handlers": hs,
                    "propagate": lgr.propagate,
                }
                handler_names.extend(hs)

        self.handlers = set(sorted(handler_names))
        self.config = {k: v for k, v in sorted(config.items())}


currentConfig = CurrentConfig()


def patch(dict1: dict, dict2: dict) -> dict:
    """
    Returns new dict using dict1 as `base` and updating -only existing- keys with dict2 values
    """

    result = deepcopy(dict1)

    for key, value in dict2.items():
        if isinstance(value, collections.Mapping):
            result[key] = patch(result.get(key, {}), value)
        elif key in dict1:
            result[key] = deepcopy(dict2[key])

    return result


def merge(dict1: dict, dict2: dict) -> dict:
    """
    Returns new dict using dict1 as `base` and updating/adding keys with dict2 values
    """
    merged = dict(dict1)
    for key, val in dict1.items():
        if type(val) == dict:
            if key in dict2 and type(dict2[key] == dict):
                merge(dict1[key], dict2[key])
        else:
            if isinstance(dict2, collections.Mapping) and key in dict2:
                dict1[key] = dict2[key]

    if isinstance(dict2, collections.Mapping):
        for key, val in dict2.items():
            if key not in dict1:
                dict1[key] = val
    return merged
