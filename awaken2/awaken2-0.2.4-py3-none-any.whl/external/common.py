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
命令行指令 - 通用模块

"""
from ..baseic.const import G_CONST
from ..baseic.common.template_rendering import G_TEMPLATE_RENDERING


_NUMBER_NESTING_LAYERS = 3
""" 工程目录嵌套最大层数 """


# --------------------------------------------------------------------------
def confirm_root_directory_runtime_project():
    """
    [ 确认运行时工程的根目录 ]

    """
    cwd = G_CONST.Path.ACTUALLY_CWD

    for _ in range(_NUMBER_NESTING_LAYERS):
        engineering_init = cwd.joinpath(G_CONST.Name.FileName.EngineeringInit)
        if engineering_init.exists():
            G_CONST.Path.ACTUALLY_CWD      = cwd
            G_CONST.Path.DirPath.Data      = cwd.joinpath(G_CONST.Name.DirName.EngineeringData)
            G_CONST.Path.DirPath.Logs      = G_CONST.Path.DirPath.Data.joinpath(G_CONST.Name.DirName.EngineeringLogs)
            G_CONST.Path.DirPath.BaseCode  = G_CONST.Path.DirPath.Data.joinpath(G_CONST.Name.DirName.EngineeringBaseCode)
            G_CONST.Path.FilePath.EngineeringInit     = cwd.joinpath(G_CONST.Name.FileName.EngineeringInit)
            G_CONST.Path.FilePath.EngineeringConfig   = G_CONST.Path.DirPath.Data.joinpath(G_CONST.Name.FileName.EngineeringConfig)
            G_CONST.Path.FilePath.EngineeringDatabase = G_CONST.Path.DirPath.Data.joinpath(G_CONST.Name.FileName.EngineeringDatabase)
            return True
        else:
            cwd = cwd.resolve().parent
            continue
    
    G_TEMPLATE_RENDERING.render_print(
        title='检查环境',
        is_show_number=False,
        source=[
            '当前运行路径不是Awaken工程结构路径;',
            '请在工程根目录中执行工程初始化命令:',
            'awaken -init'
        ]
    ) 
    exit(0)
