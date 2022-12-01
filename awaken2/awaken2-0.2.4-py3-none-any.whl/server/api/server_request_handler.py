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
服务端请求处理程序

"""
import json

from flask import jsonify
from flask import request
from flask import Response

from ...baseic.const import G_CONST
from ...baseic.broadcast.awaken_log import G_LOG
from ...baseic.error.server import AwakenWebApiServerError
from ...baseic.common.convert import try_converting_string_format


URL_PREFIX: str = '/api'
""" URL前缀 """


# --------------------------------------------------------------------------
class ServerRequestHandler:
    """
    [ 服务端请求处理程序 ]

    ---
    描述
    - 处理 WebApi 请求的相关事务, 如解析前端请求参数与返回响应对象。

    """


    # ----------------------------------------------------------------------
    @staticmethod
    def analysis_request_parameter(must_keys: list = [], optional_keys: list = []) -> dict:
        """ 
        [ 解析请求参数 ]

        ---
        描述
        - 解析请求中指定 Key, 如果该值为空, 则舍弃该 Key, 而不是返回 None;
        - 如果需要确保解析结果中必须携带指定 Key, 请通过 must_keys 定义。

        ---
        参数
        - must_keys : { list } - 必要的待解析 Keys, 不存在时抛出异常。
        - optional_keys : { list } - 可选的待解析 Keys, 不存在时会忽略。 

        ---
        返回
        - dict : 返回解析完成的参数字典。

        """
        request_handle = request.args
        if request.method == 'POST':
            try:
                request_handle = json.loads(request.data.decode('UTF-8'))
            except json.decoder.JSONDecodeError:
                request_handle = request.form

        return ServerRequestHandler._common_analysis_request_keys(request_handle, must_keys, optional_keys)


    # ----------------------------------------------------------------------
    @staticmethod
    def analysis_request_headers(must_keys: list = [], optional_keys: list = []) -> dict:
        """
        [ 解析请求头 ]

        ---
        参数
        - must_keys : { list } - 必要的待解析 Keys, 不存在时抛出异常。
        - optional_keys : { list } - 可选的待解析 Keys, 不存在时会忽略。 

        ---
        返回
        - dict : 返回解析完成的参数字典。
        
        """
        headers_handle = request.headers
        return ServerRequestHandler._common_analysis_request_keys(headers_handle, must_keys, optional_keys)


    # ----------------------------------------------------------------------
    @staticmethod
    def successful(result: dict, message=G_CONST.Api.StateMessage.Success) -> Response:
        """
        [ 请求成功 ]

        ---
        描述
        - 将数据序列化为 Json 并包装成 Flask.Response 响应体返回。

        ---
        参数
        - result : { dict } - 需要返回的数据。

        ---
        返回
        - Response : 响应体对象。
         
        """
        return jsonify({
            'code': G_CONST.Api.StateCode.Success, 
            'message': message,
            'result': result
        })


    # ----------------------------------------------------------------------
    @staticmethod
    def unsuccessful(error: str, message=G_CONST.Api.StateMessage.Error) -> Response:
        """
        [ 请求失败 ]

        ---
        描述
        - 将数据序列化为 Json 并包装成 Flask.Response 响应体返回。

        ---
        参数
        - error : { str } - 需要返回的错误信息。

        ---
        返回
        - Response : 响应体对象。
         
        """
        return jsonify({
            'code': G_CONST.Api.StateCode.Error, 
            'message': message,
            'error': error
        })


    # ----------------------------------------------------------------------
    @staticmethod
    def _common_analysis_request_keys(data: dict, must_keys: list, optional_keys: list) -> dict:
        """
        [ 通用的解析参数 ]

        ---
        描述
        - 解析请求参数与解析请求头的通用函数。

        ---
        参数
        - data : { dict } - 待解析的数据。
        - must_keys : { list } - 必要的待解析 Keys, 不存在时抛出异常。
        - optional_keys : { list } - 可选的待解析 Keys, 不存在时会忽略。 

        """
        decryption_parameter: dict = {}

        # 解析必要的 Keys
        for key in must_keys:
            value = data.get(key)
            if value == None:
                raise AwakenWebApiServerError(f'请求数据不存在必要参数 "{key}" !')
            else:
                if value != '':
                    value = try_converting_string_format(value)
                decryption_parameter.update({key: value})
        
        # 解析可选的 Keys
        for key in optional_keys:
            value = data.get(key)
            if value == None:
                ...
            else:
                if value != '':
                    value = try_converting_string_format(value)
                decryption_parameter.update({key: value})

        return decryption_parameter
