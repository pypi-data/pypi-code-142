# Copyright 2022 quinn.7@foxmail.com All rights reserved.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
[ 数据库模块 ]

"""
from .awaken_db import AwakenDb
from .awaken_sql import AwakenSql
from ...baseic.common.encryption import encrypt_md5


DB: AwakenDb = AwakenDb()
""" 数据库实例 """

SQL: AwakenSql = AwakenSql()
""" SQL语句实例 """


# 创建 admin 用户
if DB.execute(SQL.User.get_user_id_and_password(user_number='admin')).get('total') == 0:
    DB.execute(SQL.User.creation(
        user_number='admin',
        password=encrypt_md5('admin'),
        user_name='Admin',
        user_portrait='https://q1.qlogo.cn/g?b=qq&nk=190848757&s=640',
    ))

# 创建 test 用户
if DB.execute(SQL.User.get_user_id_and_password(user_number='test')).get('total') == 0:
    DB.execute(SQL.User.creation(
        user_number='test',
        password=encrypt_md5('123456'),
        user_name='Test',
        user_portrait='https://q1.qlogo.cn/g?b=qq&nk=190848757&s=640',
    ))

DB.commit()
