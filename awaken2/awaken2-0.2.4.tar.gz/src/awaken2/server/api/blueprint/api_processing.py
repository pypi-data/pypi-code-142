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
[ 数据处理相关接口 ]

"""
import requests
from flask import Response
from flask import Blueprint

from ..server_request_handler import URL_PREFIX
from ..server_request_handler import ServerRequestHandler
from ....baseic.keyword import G_KEYWORD
from ....baseic.decorator.web_api import deco_webapi_error_capture


blueprint_processing = Blueprint('processing', __name__)
""" 数据处理接口蓝图 """


POST_PROCESSING_GET_URL_DOM = '/processing/get_url_dom'
""" 接口URL - 获取目标URL的DOM文档 """


# --------------------------------------------------------------------------
@deco_webapi_error_capture
@blueprint_processing.route(''.join([URL_PREFIX, POST_PROCESSING_GET_URL_DOM]), methods=['POST'])
def post_get_url_dom() -> Response:
    """
    [ POST - 获取目标URL的DOM文档 ]

    ---
    必要参数
    - url : { str } - 目标URL。

    """
    try:
        result = {}

        # 解析请求
        paras = ServerRequestHandler.analysis_request_parameter(
            must_keys=[
                G_KEYWORD.Api.ProcessingFieldKey.Url
            ]
        )
        url = paras.get(G_KEYWORD.Api.ProcessingFieldKey.Url)

        r = requests.get(url)
        r.encoding = 'UTF-8'
        document = r.text

        # 处理返回
        result.update({
            G_KEYWORD.Api.TransactionFieldKey.Data: document
        })
        return ServerRequestHandler.successful(result)

    except BaseException as error:
        return ServerRequestHandler.unsuccessful(str(error))
