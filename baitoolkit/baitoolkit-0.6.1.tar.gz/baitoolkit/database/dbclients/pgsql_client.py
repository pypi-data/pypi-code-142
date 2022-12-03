# -*- coding: utf-8 -*-
"""
    :author: Dabai
    :url: samuelbaizg.github.io
    :copyright: © 2018 Dabai <zhgbai@163.com>
    :license: MIT, see LICENSE for more details.
"""

import urllib

from baitoolkit.database.dbclients.dbclient_base import RdbClientBase
from baitoolkit.param.param_parser import ParameterParser


class PgSqlClient(RdbClientBase):

    @classmethod
    def get_name(cls):
        return 'pgsql'

    def _add_specific_parameters(self, parameter_parser: ParameterParser) -> None:
        parameter_parser.add_parameter('schema', required=True)
        # unit is second
        parameter_parser.add_parameter('connect_timeout', required=True, type_=int, default=5)
        # unit is second
        parameter_parser.add_parameter('statement_timeout', required=True, type_=int, default=6 * 60 * 60)

    def _get_url(self) -> str:
        pwd = self._get_password()
        url = f"postgresql+psycopg2://{self.config.user}:{pwd}" \
              f"@{self.config.host}:{self.config.port}/{self.config.database}"
        return url

    def _get_connect_args(self) -> dict:
        connect_args = {
            'connect_timeout': self.config.connect_timeout,
            'options': f'-c statement_timeout={self.config.statement_timeout} '
                       f'-c search_path={self.config.schema}'
        }
        return connect_args
