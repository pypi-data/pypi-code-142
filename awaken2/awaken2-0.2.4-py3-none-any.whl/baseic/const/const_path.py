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
路径常量

"""
from pathlib import Path

from . import const_name


ACTUALLY_CWD = Path().cwd()
""" Path对象 - 实际运行时路径 """

CONSOLE_CWD = ACTUALLY_CWD
""" Path对象 - 命令行运行时路径 """


# --------------------------------------------------------------------------
class DirPath:
    """ 
    [ 目录路径对象常量 ]

    """
    Data     = ACTUALLY_CWD.joinpath(const_name.DirName.EngineeringData)
    """ 数据目录 """

    Projects = Data.joinpath(const_name.DirName.EngineeringProjects)
    """ 项目目录 """

    Logs     = Data.joinpath(const_name.DirName.EngineeringLogs)
    """ 日志目录 """

    BaseCode = Data.joinpath(const_name.DirName.EngineeringBaseCode)
    """ 底层编码目录 """


# --------------------------------------------------------------------------
class FilePath:
    """
    [ 文件路径对象常量 ]
        
    """
    EngineeringInit     = ACTUALLY_CWD.joinpath(const_name.FileName.EngineeringInit)
    """ 工程标识文件 """

    EngineeringConfig   = DirPath.Data.joinpath(const_name.FileName.EngineeringConfig)
    """ 工程配置文件 """

    EngineeringDatabase = DirPath.Data.joinpath(const_name.FileName.EngineeringDatabase)
    """ 工程数据库文件 """

    ProjectInit         = ACTUALLY_CWD.joinpath(const_name.FileName.ProjectInit)
    """ 项目标识文件 """
