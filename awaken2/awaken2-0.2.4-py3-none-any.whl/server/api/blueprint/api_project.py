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
[ 项目相关接口 ]

"""
import time

from flask import Response
from flask import Blueprint

from ..server_request_handler import URL_PREFIX
from ..server_request_handler import ServerRequestHandler
from ...db import DB
from ...db import SQL
from ....baseic.const import G_CONST
from ....baseic.keyword import G_KEYWORD
from ....baseic.decorator.web_api import deco_webapi_error_capture


blueprint_project = Blueprint('project', __name__)
""" 项目接口蓝图 """


POST_PROJECT_GET_PROJECT_COUNT = '/project/count'
""" 接口URL - 获取项目数量 """
POST_PROJECT_GET_PROJECT_LIST  = '/project/list'
""" 接口URL - 获取项目列表 """
POST_PROJECT_CREATION          = '/project/creation'
""" 接口URL - 项目创建 """
POST_PROJECT_MODIFY            = '/project/modify'
""" 接口URL - 项目编辑 """
POST_PROJECT_DELETE            = '/project/delete'
""" 接口URL - 项目删除 """


# --------------------------------------------------------------------------
@deco_webapi_error_capture
@blueprint_project.route(''.join([URL_PREFIX, POST_PROJECT_GET_PROJECT_COUNT]), methods=['POST'])
def post_count() -> Response:
    """
    [ POST - 查询项目数量 ]

    ---
    可选参数
    - pid          : { str } - 项目编号。
    - type         : { str } - 项目类型。
    - state        : { str } - 项目状态。
    - created_date : { str } - 项目创建日期, 例如 2022-02-02。

    """
    result = {}

    # 解析请求
    paras = ServerRequestHandler.analysis_request_parameter(
        optional_keys=[
            G_KEYWORD.Api.ProjectFieldKey.Pid,
            G_KEYWORD.Api.ProjectFieldKey.Type,
            G_KEYWORD.Api.ProjectFieldKey.State,
            G_KEYWORD.Api.ProjectFieldKey.CreatedDate,
        ]
    )

    # 从数据库中获取数据
    db_data = DB.execute(SQL.Project.get_count(paras), return_data_type='LIST')
    count = db_data.get(G_KEYWORD.Common.TransactionFieldKey.Items)[0][0]

    # 处理返回
    result.update({
        G_KEYWORD.Api.TransactionFieldKey.Count: count
    })
    return ServerRequestHandler.successful(result)


# --------------------------------------------------------------------------
@deco_webapi_error_capture
@blueprint_project.route(''.join([URL_PREFIX, POST_PROJECT_GET_PROJECT_LIST]), methods=['POST'])
def post_list() -> Response:
    """
    [ POST - 查询项目列表 ]

    ---
    可选参数
    - pid          : { str } - 项目编号。
    - type         : { str } - 项目类型。
    - state        : { str } - 项目状态。
    - created_date : { str } - 项目创建日期, 例如 2022-02-02。
    - page         : { str } - 当前页数。
    - number       : { str } - 单页数据量。

    """
    result = {}

    # 解析请求
    paras = ServerRequestHandler.analysis_request_parameter(
        optional_keys=[
            G_KEYWORD.Api.ProjectFieldKey.Pid,
            G_KEYWORD.Api.ProjectFieldKey.Type,
            G_KEYWORD.Api.ProjectFieldKey.State,
            G_KEYWORD.Api.ProjectFieldKey.CreatedDate,
            G_KEYWORD.Common.PagingDataFieldKey.Page,
            G_KEYWORD.Common.PagingDataFieldKey.Number,
        ]
    )

    # 从数据库中获取数据
    db_data = DB.execute(SQL.Project.get_list(paras))
    items = db_data.get(G_KEYWORD.Common.TransactionFieldKey.Items)
    totai = db_data.get(G_KEYWORD.Common.TransactionFieldKey.Totai)

    # 处理返回
    result.update({
        G_KEYWORD.Api.TransactionFieldKey.Items: items,
        G_KEYWORD.Api.TransactionFieldKey.Totai: totai,
    })
    return ServerRequestHandler.successful(result)


# --------------------------------------------------------------------------
@deco_webapi_error_capture
@blueprint_project.route(''.join([URL_PREFIX, POST_PROJECT_CREATION]), methods=['POST'])
def post_creation() -> Response:
    """
    [ POST - 项目创建 ]

    ---
    必要参数
    - type : { str } - 项目类型。
    - name : { str } - 项目名称。
    - docs : { str } - 项目说明。

    """
    result = {}

    # 解析请求
    paras = ServerRequestHandler.analysis_request_parameter(
        must_keys=[
            G_KEYWORD.Api.ProjectFieldKey.Type, 
            G_KEYWORD.Api.ProjectFieldKey.Name, 
            G_KEYWORD.Api.ProjectFieldKey.Docs
        ]
    )

    # 从数据库中写入数据
    pid = DB.execute(SQL.Project.creation(
        type=paras[G_KEYWORD.Api.ProjectFieldKey.Type],
        name=paras[G_KEYWORD.Api.ProjectFieldKey.Name],
        docs=paras[G_KEYWORD.Api.ProjectFieldKey.Docs],
        state=G_CONST.State.Project.Null,
        created_date=time.strftime('%Y-%m-%d')
    ))
    DB.commit()

    # 处理返回
    result.update({
        G_KEYWORD.Api.TransactionFieldKey.Message: '项目创建成功 !',
        G_KEYWORD.Api.ProjectFieldKey.Pid: pid
    })
    return ServerRequestHandler.successful(result)


# --------------------------------------------------------------------------
@deco_webapi_error_capture
@blueprint_project.route(''.join([URL_PREFIX, POST_PROJECT_MODIFY]), methods=['POST'])
def post_modify() -> Response:
    """
    [ POST - 项目编辑 ]
 
    ---
    必要参数
    - pid  : { str } - 项目编号。
    - name : { str } - 项目名称。
    - docs : { str } - 项目说明。

    """
    result = {}

    # 解析请求
    paras = ServerRequestHandler.analysis_request_parameter(
        must_keys=[
            G_KEYWORD.Api.ProjectFieldKey.Pid,
            G_KEYWORD.Api.ProjectFieldKey.Name,
            G_KEYWORD.Api.ProjectFieldKey.Docs,
        ]
    )
    
    # 从数据库中写入数据
    DB.execute(SQL.Project.modify(
        pid=paras.get(G_KEYWORD.Api.ProjectFieldKey.Pid),
        name=paras.get(G_KEYWORD.Api.ProjectFieldKey.Name),
        docs=paras.get(G_KEYWORD.Api.ProjectFieldKey.Docs),
    ))
    DB.commit()

    # 处理返回
    result.update({
        G_KEYWORD.Api.TransactionFieldKey.Message: '项目编辑成功 !'
    })
    return ServerRequestHandler.successful(result)


# --------------------------------------------------------------------------
@deco_webapi_error_capture
@blueprint_project.route(''.join([URL_PREFIX, POST_PROJECT_DELETE]), methods=['POST'])
def post_delete() -> Response:
    """
    [ POST - 项目删除 ]

    ---
    必要参数
    - pid  : { str } - 项目编号。

    """
    result = {}

    # 解析请求
    paras = ServerRequestHandler.analysis_request_parameter(
        must_keys=[
            G_KEYWORD.Api.ProjectFieldKey.Pid,
        ]
    )
    pid = paras.get(G_KEYWORD.Api.ProjectFieldKey.Pid)

    # 从数据库中写入数据
    DB.execute(SQL.Project.delete(pid=pid))
    DB.execute(SQL.Tasks.delete_form_project(pid=pid))
    DB.commit()

    # 处理返回
    result.update({
        G_KEYWORD.Api.TransactionFieldKey.Message: '项目删除成功 !'
    })
    return ServerRequestHandler.successful(result)
