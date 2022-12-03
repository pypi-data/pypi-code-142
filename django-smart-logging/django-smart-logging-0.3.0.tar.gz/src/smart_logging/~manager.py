import logging
from collections import defaultdict
from typing import Dict, List, Optional, Tuple

from .utils import fqn

logger = logging.getLogger(__name__)

INFO = {"instance": None, "config": {}, "initial": {}}


class SmartList:
    cls: type = None

    def __init__(self):
        self.by_name = {}
        self.by_instance = {}

    @property
    def names(self):
        return sorted(self.by_name.keys())

    @property
    def instances(self):
        return list(self.by_instance.keys())

    def __getitem__(self, key):
        if isinstance(key, str):
            return self.by_name[key]
        elif isinstance(key, self.cls):
            return self.by_instance[key]
        else:
            raise ValueError(f"Key must be a str or {self.cls}, got {type(key)}")

    def __setitem__(self, key, value):
        if isinstance(key, str):
            self.by_name[key] = value
        elif isinstance(key, self.cls):
            self.by_instance[key] = value
        else:
            raise ValueError(f"Key must be a str or {self.cls}, got {type(key)}")

    def __contains__(self, item):
        if isinstance(item, str):
            return item in self.by_name
        elif isinstance(item, self.cls):
            return item in self.by_instance
        else:
            raise ValueError(item)

    # def items(self):
    #     return self.by_name.items()

    def __repr__(self):
        return f"{repr(self.by_name)} - {repr(self.by_instance)}"


class HandlerList(SmartList):
    cls = logging.Handler


class LoggerList(SmartList):
    cls = logging.Logger


class LoggerInfo:
    def __init__(self):
        pass

class LoggingConfManager:
    def __init__(self, django_config: dict):
        self.django_config = django_config
        self.live_config = django_config
        self.handlers: HandlerList = HandlerList()
        self.loggers: LoggerList = LoggerList()
        self.mapping: Dict[str, logging.Handler] = {}
        # self.config: Dict = {}
        # self.nameToHandler["inspect"] = InspectRedisHandler()

    def set_config(self, cfg):
        self.django_config = cfg

    def _find_handler_name_by_instance(self, h: logging.Handler):
        weights = defaultdict(int)
        for handler_name, conf in self.django_config["handlers"].items():
            weights[handler_name] = 0
            if conf and conf["class"] == fqn(h):
                fmt: logging.Formatter = h.formatter
                if fmt:
                    format = self.django_config["formatters"][conf["formatter"]][
                        "format"
                    ]
                    if format == h.formatter._fmt:
                        weights[handler_name] += 2
                if h.level == logging._checkLevel(conf.get("level", 0)):
                    weights[handler_name] += 2
                #
                # if fmt and level:
                # elif fmt:
                #     format = self.django_config["formatters"][conf["formatter"]]["format"]
                #     if format == h.formatter._fmt:
                #         return handler_name
                # elif level:
                # else:
                #     return handler_name
            # if fmt:
            #     format = self.django_config["formatters"][conf["formatter"]]["format"]
            #     if format == h.formatter._fmt:
            #         result = handler_name
            #     else:
            #         result = None
            # if lvl := conf.get("level", None) and level:
            #     if logging._checkLevel(lvl) == h.level:
            #         result = handler_name
            #
            # else:
            #     result = handler_name
        return sorted(weights.items(), key=lambda x: x[1], reverse=True)[0][0]

    def _get_suitable_handlers(self, logger: logging.Logger) -> List[str]:
        return [h for h in logger.handlers if h in self.handlers]

    def _get_logger_config(self, logger: logging.Logger):
        hs = self._get_suitable_handlers(logger)
        return {
            "level": logging._levelToName[logger.getEffectiveLevel()],
            "handlers": hs,
            "propagate": logger.propagate,
        }

    def _get_raw_config(self, name):
        if name == "root":
            return self.django_config.get("root", {})
        else:
            return self.django_config.get("loggers", {}).get(name, {})

    def _get_initial_config(self, name: str, logger: logging.Logger):
        raw = self._get_raw_config(name)
        return {
            "level": raw.get("level", logging._levelToName[logger.getEffectiveLevel()]),
            "handlers": raw.get("handlers", []),
            "propagate": raw.get("propagate", None),
        }

    def _get_logger_mapping(self, name: str, logger: logging.Logger) -> dict:
        return {
            **INFO,
            "instance": logger,
            "active": self._get_logger_config(logger),
            "initial": self._get_initial_config(name, logger),
            "raw": self._get_raw_config(name),
        }

    def create_mapping(self):
        self.mapping["root"] = self._get_logger_mapping("root", logging.getLogger())
        for nm, lgr in logging.Logger.manager.loggerDict.items():
            if isinstance(lgr, logging.PlaceHolder):
                self.mapping[nm] = lgr.loggerMap
            else:
                self.mapping[nm] = self._get_logger_mapping(nm, lgr)

    def _inspect(self):
        for nm, lgr in logging.Logger.manager.loggerDict.items():
            if not isinstance(lgr, logging.PlaceHolder):
                self.loggers[nm] = lgr
                self.loggers[lgr] = nm
                for instance in lgr.handlers:
                    name = self._find_handler_name_by_instance(instance)
                    if name not in self.handlers:
                        self.handlers[name] = instance
                        self.handlers[instance] = name

    def refresh(self):
        self.init()

    def init(self):
        self._inspect()
        self.create_mapping()

    def get_handler(self, name):
        return self.handlers[name]

    def _get_config(self, key, limit: Optional[Tuple] = None):
        result = {}
        for n, c in self.mapping.items():
            if limit and n not in limit:
                continue
            if "initial" in c:
                result[n] = {
                    "logger": n or "root",
                    "level": logging._nameToLevel[c["active"].get(key, "NOTSET")],
                    "handlers": c[key]["handlers"],
                    "propagate": c[key].get("propagate", True),
                }
            else:
                result[n] = {
                    "logger": n,
                    "level": "NOTSET",
                    "handlers": [],
                    "propagate": False,
                }
        return result

    def get_active_config(self, limit=None):
        return self._get_config("active", limit)

    def get_initial_config(self, limit=None):
        return self._get_config("initial", limit)

    # def inspect(self):
    #     config = {}
    #     rootlogger = logging.getLogger()
    #     hs = self.get_suitable_handlers(rootlogger)
    #     config["root"] = {
    #         "level": logging._levelToName[rootlogger.getEffectiveLevel()],
    #         "handlers": hs,
    #         "propagate": rootlogger.propagate
    #     }
    #
    #     for nm, lgr in logging.Logger.manager.loggerDict.items():
    #         if not isinstance(lgr, logging.PlaceHolder):
    #             hs = self.get_suitable_handlers(lgr)
    #             config[nm] = {
    #                 "level": logging._levelToName[lgr.getEffectiveLevel()],
    #                 "handlers": hs,
    #                 "propagate": lgr.propagate
    #             }
    #             handler_names.extend(hs)
    #
    #     self.handlers = set(sorted(handler_names))
    #     self.config = {k: v for k, v in sorted(config.items())}
    #
    # def inspect2(self):
    #     """Inspect exiting logging 'in-memory' configuration"""
    #     config = {}
    #     rootlogger = logging.getLogger()
    #     hs = self.get_suitable_handlers(rootlogger)
    #     config["root"] = {
    #         "level": logging._levelToName[rootlogger.getEffectiveLevel()],
    #         "handlers": hs,
    #         "propagate": rootlogger.propagate
    #     }
    #     handler_names.extend(hs)
    #
    #     for nm, lgr in logging.Logger.manager.loggerDict.items():
    #         if not isinstance(lgr, logging.PlaceHolder):
    #             hs = self.get_suitable_handlers(lgr)
    #             config[nm] = {
    #                 "level": logging._levelToName[lgr.getEffectiveLevel()],
    #                 "handlers": hs,
    #                 "propagate": lgr.propagate
    #             }
    #             handler_names.extend(hs)
    #
    #     self.handlers = set(sorted(handler_names))
    #     self.config = {k: v for k, v in sorted(config.items())}
    #


manager = LoggingConfManager(None)
