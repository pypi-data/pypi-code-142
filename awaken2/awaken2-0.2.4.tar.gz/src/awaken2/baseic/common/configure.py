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
[ 配置器 ]

"""
import os
import yaml

from pathlib import Path

from ..const import G_CONST
from ..keyword import G_KEYWORD
from ..error.file import AwakenDependentFileIsMissing


# --------------------------------------------------------------------------
class Configure:
    """
    [ 配置器 ]
    
    """
    _config_path: Path
    """ 配置路径 """
    _config_data: dict
    """ 配置数据 """
    _default_dict: dict
    """ 缺省数据 """
    _protection_keys: list
    """ 受保护密匙列表 """


    # ----------------------------------------------------------------------
    def __init__(
        self, 
        config_path: Path, 
        default_dict: dict = None, 
        protection_keys: list = []
    ) -> ...:
        """
        [ 配置器 ]

        ---
        参数
        - config_path     : { Path } - 配置文件路径对象。
        - default_dict    : { dict } - 缺省数据字典。
        - protection_keys : { list } - 受保护密匙列表, 该列表中的 key 无法从配置器中删除。
        
        """
        self._config_path = config_path
        self._default_dict = default_dict
        self._protection_keys = protection_keys

        if not self._config_path.exists():
            raise AwakenDependentFileIsMissing(f'{ config_path }')

        self._read_config_file()


    # ----------------------------------------------------------------------
    def _read_config_file(self) -> ...:
        """
        [ 读取配置文件 ]
        
        """
        # 配置文件如果为空则创建写入缺省配置数据
        if os.path.getsize(self._config_path) == 0:
            self._write_default_data()

        with open(file=self._config_path, mode='r', encoding='UTF-8') as file:
            config_data = yaml.load(file, Loader=yaml.FullLoader)
            self._config_data = config_data if config_data else {}


    # ----------------------------------------------------------------------
    def _write_default_data(self) -> ...:
        """
        [ 写入缺省数据 ]
        
        """
        if self._default_dict:
            self._config_data = self._default_dict
            self.dump()


    # ----------------------------------------------------------------------
    def dump(self) -> ...:
        """
        [ 存储配置 ]

        """
        with open(file=self._config_path, mode='w', encoding='UTF-8') as file:
            yaml.dump(self._config_data, file, allow_unicode=True)


    # ----------------------------------------------------------------------
    def data(self) -> dict:
        return self._config_data


    # ----------------------------------------------------------------------
    def keys(self) -> list:
        return self._config_data.keys()

    
    # ----------------------------------------------------------------------
    def get(self, key: str) -> str | None:
        """
        [ 获取配置项 ]

        ---
        参数
        - key : { str } - 配置项Key。

        """
        if key in self._config_data.keys():
            return self._config_data[key]
        else:
            return None


    # ----------------------------------------------------------------------
    def set(self, key: str, value: str) -> ...:
        """
        [ 设置配置项 ]

        """
        self._config_data.update({key : value})

    
    # ----------------------------------------------------------------------
    def delete(self, key: str) -> ...:
        """
        [ 删除配置项 ]

        """
        if key in self._protection_keys:
            ...
        else:
            del self._config_data[key]


# --------------------------------------------------------------------------
_CONFIG_DEFAULT_DICT = {
    G_KEYWORD.Common.Config.Debug               : True,  # 是否开启调试
    G_KEYWORD.Common.Config.EngineQueueMaxCount : 3,     # 引擎队列最大数量
    G_KEYWORD.Common.Config.TaskQueueMaxCount   : 50,    # 任务队列最大数量
    G_KEYWORD.Common.Config.CpuPropertyTime     : 1,     # CPU资源检索时隔
    G_KEYWORD.Common.Config.CpuPropertyCeiling  : 30,    # CPU资源检索阈值
}
""" 配置器缺省字典 """

G_CONFIGURE: Configure = Configure(
    config_path=G_CONST.Path.FilePath.EngineeringConfig,
    default_dict=_CONFIG_DEFAULT_DICT,
    protection_keys=[key for key in _CONFIG_DEFAULT_DICT.keys()]
)
""" Awaken配置器全局实例 """
