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
[ 用户相关接口 ]

"""
import time

from flask import Response
from flask import Blueprint

from ..server_request_handler import URL_PREFIX
from ..server_request_handler import ServerRequestHandler
from ...db import DB
from ...db import SQL
from ....baseic.keyword import G_KEYWORD
from ....baseic.common.encryption import encrypt_md5
from ....baseic.decorator.web_api import deco_webapi_error_capture


blueprint_user = Blueprint('user', __name__)
""" 用户接口蓝图 """


POST_USER_GET_USER_INFO = '/user/user_info'
""" 接口URL - 获取用户信息 """
POST_USER_LOGIN         = '/user/login'
""" 接口URL - 用户登入 """
POST_USER_LOGOUT        = '/user/logout'
""" 接口URL - 用户登出 """


# --------------------------------------------------------------------------
@deco_webapi_error_capture
@blueprint_user.route(''.join([URL_PREFIX, POST_USER_GET_USER_INFO]), methods=['POST'])
def get_user_info() -> Response:
    """
    [ POST - 获取用户信息 ]
    
    """
    result = {}

    # 解析请求头
    headers = ServerRequestHandler.analysis_request_headers(
        must_keys=['Authorization']
    )
    user_token = headers['Authorization']

    # 从数据库中获取数据
    db_data = DB.execute(SQL.User.get_user_form_token(user_token=user_token))
    result = db_data.get(G_KEYWORD.Common.TransactionFieldKey.Items)[0]

    # 角色暂时先写死不实现
    result[G_KEYWORD.Api.UserFieldKey.Role] = {
        'role_name': 'Super Admin', 'value': 'super'
    }

    # 处理返回
    return ServerRequestHandler.successful(result)


# --------------------------------------------------------------------------
@deco_webapi_error_capture
@blueprint_user.route(''.join([URL_PREFIX, POST_USER_LOGIN]), methods=['POST'])
def login() -> Response:
    """
    [ POST - 用户登入 ]
    
    """
    result = {}

    # 解析请求
    paras = ServerRequestHandler.analysis_request_parameter(
        must_keys=[
            G_KEYWORD.Api.UserFieldKey.UserNumber,
            G_KEYWORD.Api.UserFieldKey.Password,
        ]
    )
    para_user_number   = paras.get(G_KEYWORD.Api.UserFieldKey.UserNumber)
    para_user_password = paras.get(G_KEYWORD.Api.UserFieldKey.Password)

    # 访问数据库
    db_data = DB.execute(SQL.User.get_user_id_and_password(para_user_number))
    db_user_info = db_data.get(G_KEYWORD.Common.TransactionFieldKey.Items)

    if len(db_user_info) == 0:
        error_type    = "登录失败"
        error_message = "用户名或密码错误, 请重试 !"
        return ServerRequestHandler.unsuccessful(error=error_type, message=error_message)

    # 将传递的密码加密后与数据库密码比对校验
    # 密码校验通过时
    # 生成用户登录态 token 并写入数据库
    db_user_id = db_user_info[0].get(G_KEYWORD.DataBase.UserFieldKey.UserId)
    db_user_encry_password = db_user_info[0].get(G_KEYWORD.DataBase.UserFieldKey.Password)
    para_user_encry_password = encrypt_md5(para_user_password)
    if para_user_encry_password == db_user_encry_password:
        material = [para_user_number, para_user_password, str(int(time.time()))]
        token = encrypt_md5(''.join(material))
        DB.execute(SQL.User.set_user_token(uid=db_user_id, token=token))
        DB.commit()

        # 处理返回
        result.update({
            G_KEYWORD.Api.UserFieldKey.UserId : db_user_id,
            G_KEYWORD.Api.UserFieldKey.Token  : token,
            G_KEYWORD.Api.UserFieldKey.Role   : {
                'role_name': 'Super Admin',
                'value'    : 'super'
            }
        })
        return ServerRequestHandler.successful(result)
    
    else:
        error_type    = "登录失败"
        error_message = "用户名或密码错误, 请重试 !"
        return ServerRequestHandler.unsuccessful(error=error_type, message=error_message)


# --------------------------------------------------------------------------
@deco_webapi_error_capture
@blueprint_user.route(''.join([URL_PREFIX, POST_USER_LOGOUT]), methods=['POST'])
def logout() -> Response:
    """
    [ 退出登录 ]

    """
    result = {}

    # 解析请求头
    headers = ServerRequestHandler.analysis_request_headers(
        must_keys=['Authorization']
    )
    user_token = headers['Authorization']

    # 访问数据库
    db_data = DB.execute(SQL.User.get_user_form_token(user_token))
    db_user_info = db_data.get(G_KEYWORD.Common.TransactionFieldKey.Items)[0]
    db_user_id   = db_user_info.get(G_KEYWORD.DataBase.UserFieldKey.UserId)
    DB.execute(SQL.User.set_user_token(db_user_id, 'NULL'))
    DB.commit()

    # 处理返回
    result.update({G_KEYWORD.Api.TransactionFieldKey.Message: '登出成功 !'})
    return ServerRequestHandler.successful(result)
