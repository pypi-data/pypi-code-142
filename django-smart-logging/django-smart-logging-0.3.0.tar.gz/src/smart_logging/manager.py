import logging
from collections import defaultdict
from functools import lru_cache
from hashlib import md5
from typing import Any, Dict, Union

from . import conf
from .handlers import RedisLiveHandler
from .signals import logger_changed
from .utils import fqn

logger = logging.getLogger(__name__)

INFO = {"instance": None, "initial": {}}


class SmartList:
    cls: type = None

    def __init__(self):
        self.elements = {}

    @property
    def names(self):
        return sorted(self.elements.keys())

    @property
    def instances(self):
        return list(self.elements.values())

    def empty(self):
        self.elements = {}

    def get_name(self, key):
        if isinstance(key, str):
            return key
        elif isinstance(key, self.cls):
            return [k for k, v in self.elements.items() if v == key][0]
        else:
            raise ValueError(f"Key must be a str or {self.cls}, got {type(key)}")

    def get_instance(self, key):
        if isinstance(key, str):
            return self.elements[key]
        elif isinstance(key, self.cls):
            return key
        else:
            raise ValueError(f"Key must be a str or {self.cls}, got {type(key)}")

    def register(self, key: str, value: Any):
        if not isinstance(key, str):
            raise ValueError(f"Key must be a str, got {type(key)}")
        if not isinstance(value, self.cls):
            raise ValueError(f"Value must be a {self.cls}, got {type(key)}")
        self.elements[key] = value

    def __getitem__(self, key):
        if isinstance(key, str):
            return self.elements[key]
        elif isinstance(key, self.cls):
            return [k for k, v in self.elements.items() if v == key][0]
        else:
            raise ValueError(f"Key must be a str or {self.cls}, got {type(key)}")

    def __setitem__(self, key, value):
        if isinstance(key, str):
            self.register(key, value)
        else:
            self.register(value, key)

    def __contains__(self, item):
        if isinstance(item, str):
            return item in self.elements.keys()
        elif isinstance(item, self.cls):
            return item in self.elements.values()
        else:
            raise ValueError(item)

    def __repr__(self):
        return f"{repr(self.elements)}"

    def __len__(self):
        return len(self.elements)

    def items(self):
        return self.elements.items()

    def keys(self):
        return self.elements.keys()

    def values(self):
        return self.elements.values()


class HandlerList(SmartList):
    cls = (logging.Handler, logging.PlaceHolder)


class LoggerList(SmartList):
    cls = (logging.Logger, logging.PlaceHolder)


@lru_cache(maxsize=None)
class LoggingConfManager:
    def __init__(self):
        self.django_config = None
        self.handlers: HandlerList = HandlerList()
        self.loggers: LoggerList = LoggerList()
        self.mapping: Dict[str, logging.Handler] = {}
        if conf.SMART_LOG_INSPECT:
            self.online_handler: RedisLiveHandler = RedisLiveHandler()
        else:
            self.online_handler = None

    def set_config(self, cfg):
        self.django_config = cfg

    def _find_handler_name_by_instance(self, h: logging.Handler):
        if conf.SMART_LOG_INSPECT and h == self.online_handler:
            return conf.ONLINE_LOGGER_NAME
        weights = defaultdict(int)
        for handler_name, config in self.django_config["handlers"].items():
            weights[handler_name] = -1
            if config and config["class"] == fqn(h):
                weights[handler_name] = 0
                fmt: logging.Formatter = h.formatter
                if fmt:
                    format = self.django_config["formatters"][config["formatter"]][
                        "format"
                    ]
                    if format == h.formatter._fmt:
                        weights[handler_name] += 2
                if h.level == logging._checkLevel(config.get("level", 0)):
                    weights[handler_name] += 2
        found = sorted(
            filter(lambda x: x[1] >= 0, weights.items()),
            key=lambda x: x[1],
            reverse=True,
        )
        if found:
            return found[0][0]
        return None

    def _get_handler_names_for_logger(self, lgr):
        for h in lgr.handlers:
            if n := self._find_handler_name_by_instance(h):
                yield n

    def _get_logger_active_config(self, lgr: logging.Logger):
        return {
            "level": logging._levelToName[lgr.getEffectiveLevel()],
            "handlers": list(self._get_handler_names_for_logger(lgr)),
            "propagate": lgr.propagate,
        }

    def _get_raw_config_entry(self, name):
        if name == "root":
            return self.django_config.get("root", {})
        else:
            return self.django_config.get("loggers", {}).get(name, {})

    def _get_logger_initial_config(self, name: str, logger: logging.Logger):
        raw = self._get_raw_config_entry(name)
        return {
            "level": raw.get("level", logging._levelToName[logger.getEffectiveLevel()]),
            "handlers": raw.get("handlers", []),
            "propagate": raw.get("propagate", None),
        }

    def get_signature(self):
        return md5(
            str({k: v["active"] for k, v in self.mapping.items()}).encode()
        ).hexdigest()

    def _get_logger_mapping(self, name: str, logger: logging.Logger) -> dict:
        return {
            **INFO,
            "instance": logger,
            "active": self._get_logger_active_config(logger),
            "initial": self._get_logger_initial_config(name, logger),
            "raw": self._get_raw_config_entry(name),
        }

    def create_mapping(self):
        self.mapping["root"] = self._get_logger_mapping("root", logging.getLogger())
        for nm, lgr in logging.Logger.manager.loggerDict.items():
            if not isinstance(lgr, logging.PlaceHolder):
                if (conf.SMART_LOG_LOGGERS is None) or nm in conf.SMART_LOG_LOGGERS:
                    self.mapping[nm] = self._get_logger_mapping(nm, lgr)

    def _collect_handlers(self):
        if conf.SMART_LOG_INSPECT:
            self.handlers.register(conf.ONLINE_LOGGER_NAME, self.online_handler)
        for nm, lgr in logging.Logger.manager.loggerDict.items():
            if isinstance(lgr, logging.PlaceHolder):
                handlers = []
            else:
                handlers = lgr.handlers

            for instance in handlers:
                name = self._find_handler_name_by_instance(instance)
                if name:
                    self.handlers.register(name, instance)

    def _inspect(self):
        self.loggers.register("root", logging.getLogger())
        for nm, lgr in logging.Logger.manager.loggerDict.items():
            if not isinstance(lgr, logging.PlaceHolder):
                self.loggers.register(nm, lgr)

    def refresh(self):
        self.init()

    def init(self):
        self.loggers.empty()
        self.mapping = {}
        self.handlers.empty()
        if self.online_handler:
            self.online_handler.clear()
        self._collect_handlers()
        self._inspect()
        self.create_mapping()

    def get_handler(self, name):
        return self.handlers[name]

    def configure_logger(self, lgr: Union[str, logging.Logger], **kwargs):
        if not kwargs:
            return []
        actions = []
        logger_name = self.loggers.get_name(lgr)
        lgr = self.loggers.get_instance(lgr)
        logger.debug(f"Configuring logger {logger_name} with {kwargs}")
        if "propagate" in kwargs:
            lgr.propagate = kwargs["propagate"]
            actions.append(f"{logger_name}: setting propagate {kwargs['propagate']}")
        if "level" in kwargs:
            lgr.setLevel(kwargs["level"])
            actions.append(f"{logger_name}: setting level {kwargs['level']}")
        selected_handlers = kwargs.get("handlers", [])
        if kwargs.get("inspect", False):
            selected_handlers.append(conf.ONLINE_LOGGER_NAME)
        if not selected_handlers:
            lgr.handlers.clear()
            actions.append(f"{logger_name} Empty handlers")
            logger.debug(actions[-1])
        else:
            manager._collect_handlers()
            # initial_handlers = self.mapping[logger_name]["initial"]["handlers"]
            current_handlers = self.mapping[logger_name]["active"]["handlers"]
            for handler_name in current_handlers:
                if handler_name not in selected_handlers:
                    target = manager.handlers[handler_name]
                    if target in lgr.handlers:
                        actions.append(
                            f"{logger_name}: removing handler {handler_name} {target}"
                        )
                        logger.debug(actions[-1])
                        lgr.removeHandler(target)

            for handler in selected_handlers:
                if handler not in current_handlers:
                    target = manager.handlers[handler]
                    if target not in lgr.handlers:
                        actions.append(
                            f"{logger_name}: adding handler {handler} {target}"
                        )
                        logger.debug(actions[-1])
                        lgr.addHandler(target)
        self.mapping[logger_name] = self._get_logger_mapping(logger_name, lgr)
        logger_changed.send(sender=lgr, details=self.mapping[logger_name])
        return actions

    def diff(self, lgr: Union[str, logging.Logger]):
        logger_name = self.loggers.get_name(lgr)
        pre = self.mapping[logger_name]["initial"]
        current = self.mapping[logger_name]["active"]
        return {a: pre[a] for a in pre if pre[a] != current[a]}

    def is_changed(self, lgr: Union[str, logging.Logger]):
        logger_name = self.loggers.get_name(lgr)
        pre = self.mapping[logger_name]["initial"]
        current = self.mapping[logger_name]["active"]
        return pre != current

    def reset_logger(self, lgr: Union[str, logging.Logger]):
        initials = self.mapping[lgr]["initial"]
        return self.configure_logger(lgr, **initials)

    def _get_config(self, key):
        result = {}
        for n, c in self.mapping.items():
            result[n] = {
                "logger": n or "root",
                "level": logging._nameToLevel[c[key].get("level", "NOTSET")],
                "handlers": c[key]["handlers"],
                "propagate": c[key].get("propagate", True),
            }
        return result

    def get_active_config(self):
        return self._get_config("active")

    def get_initial_config(self):
        return self._get_config("initial")


manager = LoggingConfManager()
