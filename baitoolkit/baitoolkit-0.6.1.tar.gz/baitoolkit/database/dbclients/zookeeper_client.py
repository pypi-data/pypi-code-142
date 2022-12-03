# -*- coding: utf-8 -*-
"""
    :author: Dabai
    :url: samuelbaizg.github.io
    :copyright: © 2018 Dabai <zhgbai@163.com>
    :license: MIT, see LICENSE for more details.
"""

from kazoo.client import KazooClient

from baitoolkit.common import logger_factory
from baitoolkit.common.type_util import Singleton
from baitoolkit.database.dbclients.dbclient_base import DBClientBase
from baitoolkit.param.param_parser import ParameterParser

__logger = logger_factory.get_logger(__name__)


class ZkClient(DBClientBase):

    def __init__(self, config: dict):
        super(ZkClient, self).__init__(config)

    @classmethod
    def get_name(cls):
        return 'zookeeper'

    def _add_extra_parameters(self, parameter_parser: ParameterParser) -> None:
        parameter_parser.add_parameter('hosts', required=True)
        # unit is second
        parameter_parser.add_parameter('timeout', required=True, type_=float, default=10.0)
        parameter_parser.add_parameter('client_id')
        parameter_parser.add_parameter('handler')
        parameter_parser.add_parameter('default_acl')
        parameter_parser.add_parameter('auth_data')
        parameter_parser.add_parameter('read_only')
        parameter_parser.add_parameter('randomize_hosts')
        parameter_parser.add_parameter('connection_retry')
        parameter_parser.add_parameter('command_retry')
        parameter_parser.add_parameter('keyfile')
        parameter_parser.add_parameter('keyfile_password')
        parameter_parser.add_parameter('certfile')
        parameter_parser.add_parameter('ca')
        parameter_parser.add_parameter('use_ssl', type_=bool, default=False)
        parameter_parser.add_parameter('verify_certs', type_=bool, default=False)

    def _create_engine(self):
        return ZookeeperEngine(**self._config)

    def get_debug_queries(self) -> list:
        return list()


class ZookeeperEngine(object, metaclass=Singleton):

    def __init__(self, **kwargs):
        self._kazoo_kwargs = kwargs

    def get_connection(self):
        return KazooClient(**self._kazoo_kwargs)
