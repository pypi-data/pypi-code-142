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
[ 日志模块 ]

"""
import time
import logging

from ..const import G_CONST
from ..decorator.baseic import deco_singleton
from ..error.broadcast import AwakenLogRelevanError


_LOG_BASEIC_LEVEL       = 'INFO'
""" 日志默认流 Level 等级 """
_LOG_FILE_HANDLE_LEVELS = ['debug', 'info', 'warning', 'error', 'critical']
""" 日志文件流 Level 等级组 """
_LOG_OUTPUT_STRUCTURE   = logging.Formatter('[%(asctime)s] [%(levelname)7s] %(message)s')
""" 日志输出格式 """


# --------------------------------------------------------------------------
@deco_singleton
class AwakenLog:
    """
    [ 日志模块 ]
    
    """
    _logger: logging.Logger
    """ 日志记录器 """


    # ----------------------------------------------------------------------
    def __init__(self) -> ...:
        """
        [ 日志模块 ]
        
        """
        try:
            # 创建日志记录器
            self._logger = logging.getLogger()

            # 设置日志记录器 Level 等级
            self._logger.setLevel(_LOG_BASEIC_LEVEL)
            self._logger.handlers.clear()

            # 以当天日期为名称创建日志存放目录
            current_date = time.strftime('%Y-%m-%d', time.localtime())
            current_date_dir_path = G_CONST.Path.DirPath.Logs.joinpath(current_date)
            if not current_date_dir_path.exists():
                current_date_dir_path.mkdir(parents=True, exist_ok=True)

            # 构建日志默认流
            baseic_handle = logging.StreamHandler()
            baseic_handle.setLevel(_LOG_BASEIC_LEVEL)
            baseic_handle.setFormatter(_LOG_OUTPUT_STRUCTURE)
            self._logger.addHandler(baseic_handle)

            # 构建日志文件流
            for level in _LOG_FILE_HANDLE_LEVELS:
                file_path = current_date_dir_path.joinpath(f'{ level }.log')
                file_handle = logging.FileHandler(file_path)
                file_handle.setLevel(level.upper())
                file_handle.setFormatter(_LOG_OUTPUT_STRUCTURE)
                self._logger.addHandler(file_handle)

        except Exception as error:
            raise AwakenLogRelevanError(str(error))


    # ----------------------------------------------------------------------
    def out_map(self, level: str, message: str | list) -> ...:
        """
        [ 日志映射输出 ]

        ---
        描述
        - 根据传递的 level 映射对应等级日志打印。

        ---
        参数
        - level : { str } - 日志 Level 等级。
        - message : { str | list } - 输出的日志信息。

        ---
        示例
        >>> Log = AwakenLog()
        >>> Log.out_map(level='error', message='message')

        """
        try:
            type(self).__dict__[level](self, message)

        except KeyError as error:
            error_message = [f'日志 Level 等级 { str(error) } 不存在, 仅支持以下 Level 等级 !']
            error_message.extend(_LOG_FILE_HANDLE_LEVELS)
            raise AwakenLogRelevanError(error_message)


    # ----------------------------------------------------------------------
    def debug(self, message: str | list) -> ...:
        """
        [ 输出 DEBUG 日志 ]

        ---
        参数
        - message : { str | list } - 输出的日志信息。

        """
        message = [message] if isinstance(message, str) else message
        for m in message:
            self._logger.debug(m)


    # ----------------------------------------------------------------------
    def info(self, message: str | list) -> ...:
        """
        [ 输出 INFO 日志 ]

        ---
        参数
        - message : { str | list } - 输出的日志信息。

        """
        message = [message] if isinstance(message, str) else message
        for m in message:
            self._logger.info(m)


    # ----------------------------------------------------------------------
    def warning(self, message: str | list) -> ...:
        """
        [ 输出 WARNING 日志 ]

        ---
        参数
        - message : { str | list } - 输出的日志信息。

        """
        message = [message] if isinstance(message, str) else message
        for m in message:
            self._logger.warning(m)


    # ----------------------------------------------------------------------
    def error(self, message: str | list) -> ...:
        """
        [ 输出 ERROR 日志 ]

        ---
        参数
        - message : { str | list } - 输出的日志信息。

        """
        message = [message] if isinstance(message, str) else message
        for m in message:
            self._logger.error(m)
        

    # ----------------------------------------------------------------------
    def critical(self, message: str | list) -> ...:
        """
        [ 输出 CRITICAL 日志 ]

        ---
        参数
        - message : { str | list } - 输出的日志信息。

        """
        message = [message] if isinstance(message, str) else message
        for m in message:
            self._logger.critical(m)

    
# --------------------------------------------------------------------------
G_LOG: AwakenLog = AwakenLog()
""" 日志模块全局实例 """
