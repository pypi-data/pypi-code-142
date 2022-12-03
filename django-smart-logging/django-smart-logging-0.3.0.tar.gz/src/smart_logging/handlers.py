import json
import logging
import time
from functools import lru_cache

import redis

from . import conf
from .utils import get_redis_connection, get_signature


@lru_cache(maxsize=None)
class RedisLiveHandler(logging.Handler):
    def __init__(self, level=logging.DEBUG):
        self.server: redis.client.Redis = get_redis_connection()
        super().__init__(level)

    def format(self, record: logging.LogRecord) -> str:
        fmt = logging.Formatter(conf.SMART_LOG_FORMAT)
        return json.dumps(
            {
                "__sender__": get_signature(),
                "name": record.name,
                "levelname": record.levelname,
                "levelno": record.levelno,
                "msg": record.msg,
                "message": fmt.format(record),
                "pathname": record.pathname,
                "lineno": record.lineno,
                "filename": record.filename,
                "module": record.module,
                "funcName": record.funcName,
                "created": time.strftime(
                    "%Y-%m-%d %H:%M:%S", time.localtime(record.created)
                ),
                "processName": str(record.processName),
                "process": str(record.process),
                "thread": str(record.thread),
                "threadName": str(record.threadName),
                "smart_logger": id(self),
            }
        )

    def clear(self):
        self.server.ltrim(conf.LOGGER, conf.SMART_LOG_MAXSIZE, conf.SMART_LOG_MAXSIZE)

    def emit(self, record: logging.LogRecord):
        self.server.lpush(conf.LOGGER, self.format(record))
        self.server.ltrim(conf.LOGGER, 0, (conf.SMART_LOG_MAXSIZE - 1))

    def retrieve(self, reverse=False):
        entries = [json.loads(x) for x in self.server.lrange(conf.LOGGER, 0, -1)]
        if reverse:
            entries = reversed(entries)
        return list(entries)
