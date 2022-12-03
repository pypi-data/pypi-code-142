# -*- coding: utf-8 -*-
"""
    :author: Dabai
    :url: samuelbaizg.github.io
    :copyright: © 2018 Dabai <zhgbai@163.com>
    :license: MIT, see LICENSE for more details.
"""

from baitoolkit.common.type_util import Singleton
from baitoolkit.database.dbclients import DbClients
from baitoolkit.exception import assert_util

"""
    Database client
"""


class DBClientManager(metaclass=Singleton):

    def __init__(self):
        self._db_clients = dict()

    def add_db_client(self, bind_key: str, client_name: str, config: dict):
        assert_util.assert_required(bind_key, 'bind_key')
        assert_util.assert_in(client_name, list(DbClients.keys()), 'client_name')
        assert_util.assert_required(config, 'config')
        db_client = DbClients.get(client_name)(config)
        self._db_clients[bind_key] = db_client

    def get_db_client(self, bind_key):
        return self._db_clients.get(bind_key)

    def get_engine(self, bind_key):
        return self.get_db_client(bind_key).engine

    def get_debug_queries(self) -> list:
        queries = list()
        for db_client in self._db_clients.values():
            queries.extend(db_client.get_debug_queries())
        return queries
