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


class MySqlClient(RdbClientBase):

    @classmethod
    def get_name(cls):
        return 'mysql'

    def _add_specific_parameters(self, parameter_parser: ParameterParser) -> None:
        parameter_parser.add_parameter('charset', required=True, default='utf8mb4')

    def _get_url(self) -> str:
        pwd = self._get_password()
        url = f"mysql+pymysql://{self.config.user}:{pwd}" \
              f"@{self.config.host}:{self.config.port}/{self.config.database}?charset={self.config.charset}"
        return url

    def _get_connect_args(self) -> dict:
        connect_args = {}
        return connect_args

