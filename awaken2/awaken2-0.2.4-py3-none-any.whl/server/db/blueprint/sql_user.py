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
[ SQL蓝图 - 用户相关 ]

"""
from typing import Any

from ..sqlite_statement_handle import G_SQLITE_STATEMENT_HANDLE
from ....baseic.keyword import G_KEYWORD


# --------------------------------------------------------------------------
class SqlUser(object):
    """
    [ SQL蓝图 - 用户相关 ]

    """


    # ----------------------------------------------------------------------
    @staticmethod
    def get_user_id_and_password(user_number: str) -> Any:
        """
        [ 通过用户号码获取用户ID与密码 ]

        ---
        参数
        - user_number : { str } - 用户账号。

        """
        selecter = G_SQLITE_STATEMENT_HANDLE.select(G_KEYWORD.DataBase.TableName.User)
        selecter.get(G_KEYWORD.DataBase.UserFieldKey.UserId)
        selecter.get(G_KEYWORD.DataBase.UserFieldKey.Password)
        selecter.filter_equal(G_KEYWORD.DataBase.UserFieldKey.UserNumber, user_number)
        return selecter


    # ----------------------------------------------------------------------
    @staticmethod
    def get_user_form_token(user_token: str) -> Any:
        """
        [ 根据登录态 token 查询用户 ]

        ---
        参数
        - user_token : { str } - 用户登录态。

        """
        selecter = G_SQLITE_STATEMENT_HANDLE.select(G_KEYWORD.DataBase.TableName.User)
        selecter.get(G_KEYWORD.DataBase.UserFieldKey.UserId)
        selecter.get(G_KEYWORD.DataBase.UserFieldKey.UserNumber)
        selecter.get(G_KEYWORD.DataBase.UserFieldKey.UserName)
        selecter.get(G_KEYWORD.DataBase.UserFieldKey.Portrait)
        selecter.filter_equal(G_KEYWORD.DataBase.UserFieldKey.UserToken, user_token)
        return selecter


    # ----------------------------------------------------------------------
    @staticmethod
    def set_user_token(
        uid: int,
        token: str
    ) -> Any:
        """
        [ 更新任务 ]

        ---
        参数
        - uid : { int } - 用户ID。
        - token : { str } - 用户TOKEN。

        """
        sql_handler = G_SQLITE_STATEMENT_HANDLE.update(G_KEYWORD.DataBase.TableName.User)
        sql_handler.push(G_KEYWORD.DataBase.UserFieldKey.UserToken, token)
        sql_handler.filter_equal(G_KEYWORD.DataBase.UserFieldKey.UserId, uid)
        return sql_handler


    # ----------------------------------------------------------------------
    @staticmethod
    def creation(
        user_number: str,
        password: str,
        user_name: str,
        user_portrait: str = 'NULL',
    ) -> Any:
        """
        [ 创建用户 ]

        ---
        参数
        - user_number   : { str } - 用户账号。
        - password      : { str } - 用户密码。
        - user_name     : { str } - 用户名称。
        - user_portrait : { str } - 用户头像。

        """
        sql_handler = G_SQLITE_STATEMENT_HANDLE.insert(G_KEYWORD.DataBase.TableName.User)
        sql_handler.push(G_KEYWORD.DataBase.UserFieldKey.UserId, 'NULL')
        sql_handler.push(G_KEYWORD.DataBase.UserFieldKey.UserNumber, user_number)
        sql_handler.push(G_KEYWORD.DataBase.UserFieldKey.Password, password)
        sql_handler.push(G_KEYWORD.DataBase.UserFieldKey.UserName, user_name)
        sql_handler.push(G_KEYWORD.DataBase.UserFieldKey.Portrait, user_portrait)
        sql_handler.push(G_KEYWORD.DataBase.UserFieldKey.RoleId, 'NULL')
        sql_handler.push(G_KEYWORD.DataBase.UserFieldKey.UserToken, 'NULL')
        return sql_handler
