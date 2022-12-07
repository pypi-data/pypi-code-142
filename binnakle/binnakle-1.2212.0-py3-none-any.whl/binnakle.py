#!/usr/bin/env python
# -*- coding: utf-8 -*-
# TODO: implement server connection

import logging
import json
from .utils import (
    get_timestamp_ms,
    remove_empty_keys,
)
import inspect
import traceback
from os import environ


class Binnakle:

    def __init__(
        self,
        pretty: bool = None,
        env: str = None,
        prefix: str = None,
        server_url: str = None,
        name: str = None,
        level: str = None,
    ):
        if level is None:
            level = 'INFO'
        logging.getLogger().setLevel(getattr(logging, level.upper()))
        logging.basicConfig(format='%(message)s')

        self.reload(
            pretty=pretty,
            env=env,
            prefix=prefix,
            server_url=server_url,
            name=name,
        )

    def reload(
        self,
        pretty: bool = None,
        env: str = None,
        prefix: str = None,
        server_url: str = None,
        name: str = None,
    ):
        if pretty is None:
            self._pretty = environ.get(
                'BINNAKLE_PRETTY',
                'false',
            ).lower() == 'true'
        else:
            self._pretty = pretty

        if env is None:
            self._env = environ.get(
                'BINNAKLE_ENV',
                'local',
            ).lower()
        else:
            self._env = env

        self._server_url = server_url
        self._prefix = prefix
        self._name = name

        self._logger = logging.getLogger(self._name)

    def set_level(
        self,
        level: str = None,
        name: str = None,
    ):
        if level is None:
            raise ValueError('level is required')
        logging.getLogger(name).setLevel(getattr(logging, level.upper()))

    def wrapped(method):

        def _wrapped(
            self,
            message=None,
            error: Exception = None,
            **kwargs,
        ):
            if isinstance(message, bytes):
                message = message.decode('utf-8')

            if message is not None and self._prefix is not None:
                message = self._prefix + message

            inspection = inspect.stack()[1]

            level = method.__name__.upper()
            if method.__name__ == 'exception':
                level = 'ERROR'
                error_message = traceback.format_exc()
            else:
                error_message = self._get_error_message(error)

            payload = {
                'level': level,
                'message': message,
                'error': error_message,
                'timestamp': get_timestamp_ms(),
                'env': self._env,
                'filepath': inspection.filename,
                'function': inspection.function,
                'line': inspection.lineno,
            } | kwargs
            message_dict = remove_empty_keys(payload)

            modified_message = json.dumps(
                message_dict,
                indent=4 if self._pretty else None,
                separators=None if self._pretty else (',',
                                                      ':'),
                ensure_ascii=False,
            )
            return method(self, modified_message)

        return _wrapped

    @staticmethod
    def _get_error_message(error):
        if error is None:
            return

        try:
            # Python 3.10+
            error_message_lines = traceback.format_exception(error)
        except Exception:
            error_message_lines = traceback.format_exception(
                etype=type(error),
                value=error,
                tb=error.__traceback__
            )

        error_message = ''.join(error_message_lines)
        return error_message

    @wrapped
    def debug(self, message):
        self._logger.debug(message)

    @wrapped
    def info(self, message):
        self._logger.info(message)

    @wrapped
    def warning(self, message):
        self._logger.warning(message)

    @wrapped
    def error(self, message):
        self._logger.error(message)

    @wrapped
    def critical(self, message):
        self._logger.critical(message)

    @wrapped
    def exception(self, message):
        self._logger.error(message)
