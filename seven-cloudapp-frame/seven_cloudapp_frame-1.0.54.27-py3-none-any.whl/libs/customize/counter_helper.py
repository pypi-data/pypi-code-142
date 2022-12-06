# -*- coding: utf-8 -*-
"""
@Author: HuangJianYi
@Date: 2021-10-25 18:00:46
@LastEditTime: 2022-12-06 17:37:10
@LastEditors: HuangJianYi
@Description: 
"""

from seven_framework import *
from seven_cloudapp_frame.libs.customize.redis_helper import *


class CounterHelper:
    """
    :description: 计数帮助类
    """
    logger_error = Logger.get_logger_by_name("log_error")

    @classmethod
    def amount(self, key_name, object_id, value):
        """
        :description: 计数
        :param key_name: 计数key
        :param object_id: 对象标识
        :param value: 值
        :return: 
        :last_editors: HuangJianYi 
        """
        try:
            object_id = str(object_id)
            counter_config = config.get_value("counter_config", {})
            key_name_config = counter_config.get(key_name,{})
            db_connect_key = key_name_config.get("db_connect_key", "")
            table_name = key_name_config.get("table_name", "")
            id_field_name = key_name_config.get("id_field_name", "")
            value_field_name = key_name_config.get("value_field_name", "")
            if db_connect_key and table_name and id_field_name and value_field_name:
                db = MySQLHelper(config.get_value(db_connect_key))
                sql = f'update {table_name} set {value_field_name}={value_field_name}+{value} where {id_field_name}={object_id}'
                db.update(sql)
            init = RedisExHelper.init()
            count = init.hincrby(key_name, object_id, value)
            if count == value:
                db_value = self.get_db_amount(key_name, object_id)
                init.hincrby(key_name, object_id, db_value)
            init.expire(key_name, 365 * 24 * 3600)
            return count
        except Exception as ex:
            self.logger_error.error("【计数】" + traceback.format_exc())
            return 0

    @classmethod
    def increment(self, key_name, object_id, value):
        """
        :description: 增加计数
        :param key_name: 计数key
        :param object_id: 对象标识
        :param value: 增加的值
        :return: 
        :last_editors: HuangJianYi 
        """
        return self.amount(key_name, object_id, abs(int(value)))

    @classmethod
    def decrement(self, key_name, object_id, value):
        """
        :description: 减少计数
        :param key_name: 计数key
        :param object_id: 对象标识
        :param value: 减少的值
        :return: 
        :last_editors: HuangJianYi 
        """
        return self.amount(key_name, object_id, -int(value))

    @classmethod
    def get_values(self, key_name, object_ids):
        """
        :description: 获取计数值
        :param key_name: 计数key
        :param object_id: 对象标识数组
        :return: 
        :last_editors: HuangJianYi 
        """
        values = []
        init = RedisExHelper.init()
        if isinstance(object_ids,str):
            object_ids = object_ids.split(',')
        hash_values = init.hmget(key_name, object_ids)
        if len(hash_values) <= 0:
            hash_values = []
        try:
            for object_id in object_ids:
                object_id = str(object_id)
                cur_value = list(filter(lambda item: item["key"] == object_id, hash_values))
                if len(cur_value) > 0:
                    values.append(cur_value[0])
                else:
                    db_value = self.get_db_amount(key_name, object_id)
                    init.hincrby(key_name, object_id, db_value)
                    init.expire(key_name, 365 * 24 * 3600)
                    values.append({"key": object_id, "value": db_value})
        except Exception as ex:
            self.logger_error.error("【获取计数值】" + traceback.format_exc())
        return values

    @classmethod
    def get_db_amount(self, key_name, object_id):
        """
        :description: 获取数据库计数值
        :param key_name: 计数key
        :param object_id: 对象标识
        :return: 
        :last_editors: HuangJianYi 
        """
        db_value = 0
        try:
            counter_config = config.get_value("counter_config", {})
            key_name_config = counter_config.get(key_name,{})
            db_connect_key = key_name_config.get("db_connect_key", "")
            table_name = key_name_config.get("table_name", "")
            id_field_name = key_name_config.get("id_field_name", "")
            value_field_name = key_name_config.get("value_field_name", "")
            if db_connect_key and table_name and id_field_name and value_field_name:
                db = MySQLHelper(config.get_value(db_connect_key))
                db_value = db.query(f'select {value_field_name} from {table_name} where {id_field_name}={object_id}')
                if not db_value:
                    db_value = 0
        except Exception as ex:
            self.logger_error.error("【获取数据库计数值】" + traceback.format_exc())
        return db_value
