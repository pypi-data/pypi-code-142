# -*- coding: utf-8 -*-
"""
    :author: Dabai
    :url: samuelbaizg.github.io
    :copyright: © 2018 Dabai <zhgbai@163.com>
    :license: MIT, see LICENSE for more details.
"""
import urllib

import requests

from baitoolkit.common import logger_factory
from baitoolkit.database.dbclients.dbclient_base import DBClientBase
from baitoolkit.param.param_parser import ParameterParser

__logger = logger_factory.get_logger(__name__)


class NacosClient(DBClientBase):

    def __init__(self, config: dict):
        super(NacosClient, self).__init__(config)

    @classmethod
    def get_name(cls):
        return 'nacos'

    def _add_extra_parameters(self, parameter_parser: ParameterParser) -> None:
        parameter_parser.add_parameter('url', required=True)

    def _create_engine(self):
        return NacosEngine(self._config.url)

    def get_debug_queries(self) -> list:
        return list()


class NacosEngine(object):

    def __init__(self, url):
        self._url = url

    def get_config_set(self, namespace, app_id, environment, config_set_id):
        """Call nacos open api /nacos/v1/cs/configs"""
        context = "/nacos/v1/cs/configs"
        params = {
            "tenant": namespace,
            "group": environment,
            "dataId": f"{app_id}-{config_set_id}"
        }
        try:
            url = self._get_absolute_url(context, params)
            response = requests.get(url)
            if response.status_code == 200:
                return response.text
        except requests.exceptions.ConnectionError:
            logger.exception("config center is not available.")
            return None

    def _get_absolute_url(self, context, params=None):
        uri = "%s%s" % (self._url, context)
        if params is not None:
            return "{}?{}".format(uri, urllib.parse.urlencode(params))
        return uri
