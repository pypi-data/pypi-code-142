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
[ 用例记录相关接口 ]

"""
from flask import Response
from flask import Blueprint

from ..server_request_handler import URL_PREFIX
from ..server_request_handler import ServerRequestHandler
from ...db import DB
from ...db import SQL
from ....baseic.keyword import G_KEYWORD
from ....baseic.decorator.web_api import deco_webapi_error_capture


blueprint_record_case = Blueprint('record_case', __name__)
""" 用例记录接口蓝图 """


POST_RECORD_CASE_GET_COUNT      = '/record/case/count'
""" 接口URL - 获取用例记录数量 """
POST_RECORD_CASE_GET_LIST       = '/record/case/list'
""" 接口URL - 获取用例记录列表 """
POST_RECORD_CASE_GET_SPEND_TIME = '/record/case/spend_time'
""" 接口URL - 获取用例记录的消耗时间 """


# --------------------------------------------------------------------------
@deco_webapi_error_capture
@blueprint_record_case.route(''.join([URL_PREFIX, POST_RECORD_CASE_GET_COUNT]), methods=['POST'])
def post_count() -> Response:
    """
    [ 获取用例记录数量 ]

    ---
    可选参数
    - crid          : { str } - 用例记录编号。
    - trid          : { str } - 任务记录编号。
    - name          : { str } - 用例记录名称。
    - type          : { str } - 用例记录类型。
    - created_date  : { str } - 用例记录创建日期, 例如 2022-02-02。
    - state         : { str } - 用例记录状态。
    - start_time    : { str } - 用例记录开始时间。
    - end_time      : { str } - 用例记录结束时间。

    """
    result = {}
    
    # 解析请求
    paras = ServerRequestHandler.analysis_request_parameter(
        optional_keys=[
            G_KEYWORD.Api.CaseRecordFieldKey.CRid,
            G_KEYWORD.Api.CaseRecordFieldKey.TRid,
            G_KEYWORD.Api.CaseRecordFieldKey.Name,
            G_KEYWORD.Api.CaseRecordFieldKey.Type,
            G_KEYWORD.Api.CaseRecordFieldKey.CreatedDate,
            G_KEYWORD.Api.CaseRecordFieldKey.State,
            G_KEYWORD.Api.CaseRecordFieldKey.StartTime,
            G_KEYWORD.Api.CaseRecordFieldKey.EndTime,
        ]
    )

    # 从数据库中获取数据
    db_date = DB.execute(SQL.CaseRecord.get_count(paras), return_data_type='LIST')
    count = db_date.get(G_KEYWORD.Common.TransactionFieldKey.Items)[0][0]

    # 处理返回
    result.update({
        G_KEYWORD.Api.TransactionFieldKey.Count: count
    })
    return ServerRequestHandler.successful(result)


# --------------------------------------------------------------------------
@deco_webapi_error_capture
@blueprint_record_case.route(''.join([URL_PREFIX, POST_RECORD_CASE_GET_LIST]), methods=['POST'])
def post_list() -> Response:
    """
    [ 获取用例列表 ]

    ---
    可选参数
    - crid         : { str } - 用例记录编号。
    - trid         : { str } - 任务记录编号。
    - name         : { str } - 用例记录名称。
    - type         : { str } - 用例记录类型。
    - created_date : { str } - 用例记录创建日期, 例如 2022-02-02。
    - state        : { str } - 用例记录状态。
    - start_time   : { str } - 用例记录开始时间。
    - end_time     : { str } - 用例记录结束时间。
    - page         : { str } - 当前页数。
    - number       : { str } - 单页数据量。

    """
    result = {}

    # 解析请求
    paras = ServerRequestHandler.analysis_request_parameter(
        optional_keys=[
            G_KEYWORD.Api.CaseRecordFieldKey.CRid,
            G_KEYWORD.Api.CaseRecordFieldKey.TRid,
            G_KEYWORD.Api.CaseRecordFieldKey.Name,
            G_KEYWORD.Api.CaseRecordFieldKey.TRid,
            G_KEYWORD.Api.CaseRecordFieldKey.CreatedDate,
            G_KEYWORD.Api.CaseRecordFieldKey.State,
            G_KEYWORD.Api.CaseRecordFieldKey.StartTime,
            G_KEYWORD.Api.CaseRecordFieldKey.EndTime,
            G_KEYWORD.Common.PagingDataFieldKey.Page,
            G_KEYWORD.Common.PagingDataFieldKey.Number,
        ]
    )

    # 从数据库中获取数据
    db_data = DB.execute(SQL.CaseRecord.get_list(paras))
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
@blueprint_record_case.route(''.join([URL_PREFIX, POST_RECORD_CASE_GET_SPEND_TIME]), methods=['POST'])
def post_spend_time() -> Response:
    """
    [ 查询用例记录的消耗时间 ]

    ---
    可选参数
    - crid          : { str } - 用例记录编号。
    - trid          : { str } - 任务记录编号。
    - name          : { str } - 用例记录名称。
    - type          : { str } - 用例记录类型。
    - created_date  : { str } - 用例记录创建日期, 例如 2022-02-02。
    - result        : { str } - 用例记录结果。
    - start_time    : { str } - 用例记录开始时间。
    - end_time      : { str } - 用例记录结束时间。

    """
    result = {}

    # 解析请求
    paras = ServerRequestHandler.analysis_request_parameter(
        optional_keys=[
            G_KEYWORD.Api.CaseRecordFieldKey.CRid,
            G_KEYWORD.Api.CaseRecordFieldKey.TRid,
            G_KEYWORD.Api.CaseRecordFieldKey.Name,
            G_KEYWORD.Api.CaseRecordFieldKey.TRid,
            G_KEYWORD.Api.CaseRecordFieldKey.CreatedDate,
            G_KEYWORD.Api.CaseRecordFieldKey.Result,
            G_KEYWORD.Api.CaseRecordFieldKey.StartTime,
            G_KEYWORD.Api.CaseRecordFieldKey.EndTime,
        ]
    )

    # 从数据库中获取数据
    db_data  = DB.execute(SQL.CaseRecord.get_spend_time(paras))
    time_sum = db_data.get(G_KEYWORD.Common.TransactionFieldKey.Items)[0]['sum']

    # 处理返回
    result.update({
        G_KEYWORD.Api.TransactionFieldKey.Time: time_sum
    })
    return ServerRequestHandler.successful(result)
