# -*- coding: utf-8 -*-
"""
    :author: Dabai
    :url: samuelbaizg.github.io
    :copyright: © 2018 Dabai <zhgbai@163.com>
    :license: MIT, see LICENSE for more details.
"""
from baitoolkit.common.constant import ConstBase
from baitoolkit.database.dbclients.mysql_client import MySqlClient
from baitoolkit.database.dbclients.nacos_client import NacosClient
from baitoolkit.database.dbclients.pgsql_client import PgSqlClient
from baitoolkit.database.dbclients.zookeeper_client import ZkClient


class DbClients(ConstBase):
    mysql = MySqlClient
    pgsql = PgSqlClient
    nacos = NacosClient,
    zookeeper = ZkClient
