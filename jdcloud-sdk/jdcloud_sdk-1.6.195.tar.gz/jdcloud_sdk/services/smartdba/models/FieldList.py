# coding=utf8

# Copyright 2018 JDCLOUD.COM
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# NOTE: This class is auto generated by the jdcloud code generator program.


class FieldList(object):

    def __init__(self, dbName=None, tableName=None, engine=None, keyType=None, rowName=None, rowType=None, tableRows=None, tableSize=None, indexName=None, indexRow=None, number=None, sql=None, autoIncrement=None, maxNum=None):
        """
        :param dbName: (Optional) 数据库名
        :param tableName: (Optional) 表名
        :param engine: (Optional) 表引擎
        :param keyType: (Optional) 主键类型
        :param rowName: (Optional) 列名
        :param rowType: (Optional) 列类型
        :param tableRows: (Optional) 表行数
        :param tableSize: (Optional) 表存储大小
        :param indexName: (Optional) 索引名
        :param indexRow: (Optional) 索引的列
        :param number: (Optional) 个数
        :param sql: (Optional) 操作sql
        :param autoIncrement: (Optional) 当前自增序列值
        :param maxNum: (Optional) 最大序列值
        """

        self.dbName = dbName
        self.tableName = tableName
        self.engine = engine
        self.keyType = keyType
        self.rowName = rowName
        self.rowType = rowType
        self.tableRows = tableRows
        self.tableSize = tableSize
        self.indexName = indexName
        self.indexRow = indexRow
        self.number = number
        self.sql = sql
        self.autoIncrement = autoIncrement
        self.maxNum = maxNum
