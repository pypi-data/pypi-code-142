import configparser
import logging.config
import os
import ast
from logging.handlers import TimedRotatingFileHandler

import traceback
import warnings


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if len(cls._instances) != 0:
            warnings.warn(
                "This instance is already created so re-use initialized parameters!")
        if cls not in cls._instances:
            cls._instances[cls] = super(
                Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Zlogger(metaclass=Singleton):
    @classmethod
    def get_logger(cls,  *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = Singleton.__call__(cls, *args, **kwargs)
        return cls._instances[cls]

    def __init__(self, project_name=None, foler_log='/data/log'):
        warnings.warn(
            "`Zlogger has been deprecated from 0.1.9.2. Please, use `ZLogger` instead`")
        try:
            env = os.environ.get('SERVICE_ENV_SETTING','DEVELOPMENT')
            assert env in ["DEVELOPMENT", "PRODUCTION", "STAGING"]
        except:
            raise ValueError(
                "The environment param `SERVICE_ENV_SETTING` need to be assigned as: DEVELOPMENT | PRODUCTION | STAGING")

        if project_name is None:
            self.project_name = os.environ.get('SERVICE_NAME', None)
            if self.project_name is None:
                self.project_name = os.environ.get('NAME', 'DEFAULT')
        else:
            self.project_name = project_name


        self.log_dir = f'{foler_log}/' + self.project_name

        if self.log_dir == "":
            raise ValueError('Error: `log_dir` is expected to be NOT EMPTY')

        self.log_dir = str(self.log_dir)  # convert it to str
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)

        # Load logger
        self.info_logger = self._get_logger('info')
        self.debug_logger = self._get_logger('debug')
        self.error_logger = self._get_logger('error')

    def _get_logger(self, logger_name):
        logger_handler = TimedRotatingFileHandler(
            filename=self.log_dir + '/{}_'.format(logger_name) + self.project_name + '.log', when='midnight', interval=1,
            backupCount=10)
        logger = logging.getLogger('MainLogger_{}'.format(logger_name))
        logger.propagate = False
        formatter = logging.Formatter(
            '%(asctime)s | %(levelname)-8s | %(filename)s-%(funcName)s-%(lineno)04d | %(message)s')
        logger_handler.setFormatter(formatter)
        logger.addHandler(logger_handler)
        return logger

    def _check_exists(self, path):
        # if not os.path.exists(path):
        #     raise FileNotFoundError("File not found: {}".format(path))
        pass

    def info(self, msg):
        self.info_logger.info(msg)

    def error(self, msg):
        self.error_logger.error(msg)

    def debug(self, msg):
        self.debug_logger.info(msg)

    def exception(self, msg):
        self.error_logger.exception(msg)


class ZLogger(Zlogger):
    def __init__(self, project_name=None, foler_log='/data/log'):
        Zlogger.__init__(self, project_name, foler_log)
