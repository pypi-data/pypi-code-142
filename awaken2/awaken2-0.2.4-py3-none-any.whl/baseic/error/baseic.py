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
自定义异常 - 基础

"""
import re

from ..decorator.baseic import deco_singleton
from ..common.template_rendering import TemplateRendering


_TEMPLATE_RENDERING = TemplateRendering()
_ERROR_POPUP_TITLE = '异常提示'


# --------------------------------------------------------------------------
class AwakenBaseError(Exception):
    """ 
    [ 自定义异常基类 ] 
    
    """
    err_name: str
    bas_message: str | list
    out_messages: list


    # ----------------------------------------------------------------------
    def __init__(self, error_message: str | list = []):
        # 获取自定义异常类的名称
        self.err_name = re.findall(r'\[ (.*) \]', self.__doc__)[0]
        self.out_messages = [f'[ {self.err_name} ]', '']
        self.bas_message = error_message

        if isinstance(self.bas_message, str):
            error_message = [error_message]
        self.bas_message = error_message


    # ----------------------------------------------------------------------
    def __str__(self) -> str:
        if len(self.bas_message) > 0:
            for messages in self.bas_message:
                if messages != '':
                    messages = f'- {messages}'
                self.out_messages.append(messages)

        _TEMPLATE_RENDERING.render_print(
            title=_ERROR_POPUP_TITLE,
            source=self.out_messages,
            is_show_number=False
        )
        if len(self.bas_message) >= 1:
            return self.bas_message[0]
        else:
            return self.err_name


# --------------------------------------------------------------------------
@deco_singleton
class ErrorRecorder:
    """ 错误记录器
    @ 作者 : chenjiancheng
    @ 描述 : NULL
    
    """
    _error_warehouse: list


    # ----------------------------------------------------------------------
    def __init__(self) -> None:
        self._error_warehouse = []

    
    # ----------------------------------------------------------------------
    def get_error_number(self):
        return len(self._error_warehouse)


    # ----------------------------------------------------------------------
    def record(self, error_message: str | list):
        if isinstance(error_message, str):
            self._error_warehouse.append(error_message)
        if isinstance(error_message, list):
            self._error_warehouse.extend(error_message)


    # ----------------------------------------------------------------------
    def template_out(self):
        _TEMPLATE_RENDERING.render_print(
            title='错误记录回溯',
            source=self._error_warehouse
        )
        self._error_warehouse.clear()


# --------------------------------------------------------------------------
G_ERROR_RECORDER: ErrorRecorder = ErrorRecorder()
""" 错误记录器全局实例 """
