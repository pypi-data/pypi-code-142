# -*- coding: utf-8 -*-
"""
    :author: Dabai
    :url: samuelbaizg.github.io
    :copyright: © 2018 Dabai <zhgbai@163.com>
    :license: MIT, see LICENSE for more details.
"""

import abc
import urllib

import sqlalchemy

from baitoolkit.common.type_util import ValueObj
from baitoolkit.param.param_parser import ParameterParser


class DBClientBase(object, metaclass=abc.ABCMeta):

    def __init__(self, config: dict):
        self._config = self._get_config_parser().parse_parameters(**config)
        self._engine = self._create_engine()

    @property
    def config(self) -> ValueObj:
        return self._config

    @property
    def engine(self):
        return self._engine

    @classmethod
    def get_name(cls):
        raise NotImplementedError("DBClientBase.name is not implemented by sub-class")

    @abc.abstractmethod
    def _create_engine(self):
        raise NotImplementedError("DBClientBase._create_engine is not implemented by sub-class.")

    def _get_config_parser(self) -> ParameterParser:
        pp = ParameterParser()
        self._add_extra_parameters(pp)
        return pp

    def _add_extra_parameters(self, parameter_parser: ParameterParser) -> None:
        raise NotImplementedError("DBClientBase._add_extra_parameters is not implemented by sub-class.")

    def get_debug_queries(self) -> list:
        raise NotImplementedError("DBClientBase.get_debug_queries is not implemented by sub-class.")


class RdbClientBase(DBClientBase, metaclass=abc.ABCMeta):

    def __init__(self, config: dict):
        super(RdbClientBase, self).__init__(config)

    def _create_engine(self):
        engine = sqlalchemy.create_engine(self._get_url(),
                                          pool_pre_ping=True, pool_size=self.config.pool_size,
                                          max_overflow=self.config.pool_timeout, pool_timeout=self.config.pool_timeout,
                                          pool_recycle=self.config.pool_recycle,
                                          connect_args=self._get_connect_args())
        return engine

    def _add_extra_parameters(self, parameter_parser: ParameterParser) -> None:
        parameter_parser.add_parameter('host', required=True)
        parameter_parser.add_parameter('port', required=True, type_=int)
        parameter_parser.add_parameter('user', required=True)
        parameter_parser.add_parameter('password', required=True)
        parameter_parser.add_parameter('database', required=True)
        parameter_parser.add_parameter('pool_max_overflow', required=True, type_=int, default=10)
        parameter_parser.add_parameter('pool_size', required=True, type_=int, default=5)
        # unit is second
        parameter_parser.add_parameter('pool_recycle', required=True, type_=int, default=5 * 60)
        # unit is second
        parameter_parser.add_parameter('pool_timeout', required=True, type_=int, default=30)
        self._add_specific_parameters(parameter_parser)

    def _get_password(self):
        pwd = urllib.parse.quote_plus(self.config.password)
        return pwd

    def _add_specific_parameters(self, parameter_parser: ParameterParser) -> None:
        raise NotImplementedError('RdbClientBase._add_specific_parameters is not implemented by sub-class.')

    def _get_url(self):
        raise NotImplementedError('RdbClientBase._get_url is not implemented by sub-class.')

    def get_debug_queries(self) -> list:
        """Todo: reference flask-sqlalchemy get debug queries"""
        return []
