import logging
import threading

import os, os.path

log_key = "x-tt-logid"

if not os.path.exists("./logs/"):
    os.makedirs("./logs/")


class logid_filter(logging.Filter):
    def filter(self, record):
        record.logid = threading.current_thread().__dict__.get(log_key, '')
        return True


log_config = {
    "version": 1,
    "disable_existing_loggers": False,  # 不覆盖默认配置
    "formatters": {  # 日志输出样式
        "default": {
            "format": "%(asctime)s | %(levelname)s | %(logid)s | [%(threadName)s-%(thread)d] %(filename)s:%(lineno)d - %(message)s"
        }
    },
    "filters": {
        "logidfilter": {
            "()": logid_filter,
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",  # 控制台输出
            "level": "DEBUG",
            "formatter": "default",
            "filters": ["logidfilter"],
        },
        "log_file": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "INFO",
            "formatter": "default",  # 日志输出样式对应formatters
            "filename": "./logs/app.log",  # 指定log文件目录
            "maxBytes": 50 * 1024 * 1024,  # 文件最大50M
            "backupCount": 20,  # 最多20个文件
            "encoding": "utf8",  # 文件编码
            "filters": ["logidfilter"],
        },
    },
    "root": {
        "level": "DEBUG",  # # handler中的level会覆盖掉这里的level
        "handlers": ["console", "log_file"],
    },
}
