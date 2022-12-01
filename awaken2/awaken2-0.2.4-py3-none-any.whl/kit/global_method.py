# ╔══════════════════════════════════════════════════════════════════════════╗
# ║ Copyright 2022. quinn.7@foxmail.com All rights reserved.                 ║
# ║                                                                          ║
# ║ Licensed under the Apache License, Version 2.0 (the "License");          ║
# ║ you may not use this file except in compliance with the License.         ║
# ║ You may obtain a copy of the License at                                  ║
# ║                                                                          ║
# ║ http://www.apache.org/licenses/LICENSE-2.0                               ║
# ║                                                                          ║
# ║ Unless required by applicable law or agreed to in writing, software      ║
# ║ distributed under the License is distributed on an "AS IS" BASIS,        ║
# ║ WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. ║
# ║ See the License for the specific language governing permissions and      ║
# ║ limitations under the License.                                           ║
# ╚══════════════════════════════════════════════════════════════════════════╝
"""
[ 脚本全局方法 ]

"""
import yaml
import time
from pathlib import Path

from ..baseic.const import G_CONST
from ..baseic.broadcast.awaken_log import G_LOG
from ..baseic.decorator.baseic import deco_singleton


# --------------------------------------------------------------------------
@deco_singleton
class GlobalMethod:
    """
    [ 脚本全局方法 ]
    
    """


    def sleep(self, wait: int):
        """ 
        [ 等待 ]

        """
        time.sleep(wait)


    def logout(self, message: str, level=G_CONST.Common.LogLevel.Info) -> str:
        """ 
        [ 日志输出 ]

        ---
        描述
        - 输出日志到控制台。

        ---
        参数
        - message : { str } - 输出的日志信息。
        - level   : { str } - 日志等级。
        
        """
        G_LOG.out_map(level, message)
        return message


    def read_yaml(self, yaml_path: str) -> dict:
        """ 
        [ 读取YAML ]

        ---
        描述
        - 读取YAML文件数据。

        ---
        参数
        - yaml_path : { str } - YAML文件路径。
        
        ---
        返回
        - dict : YAML文件数据字典。

        """
        yaml_path = Path(yaml_path)
        
        with open(file=yaml_path.resolve(), mode='r', encoding='UTF-8') as file:
            data = yaml.load(file, Loader=yaml.FullLoader)
        
        return data


# --------------------------------------------------------------------------
G_GLOBAL_METHOD: GlobalMethod = GlobalMethod()
""" 脚本全局方法全局实例 """
