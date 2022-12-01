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
命令行指令 - 初始化工程

"""
from ..baseic.const import G_CONST
from ..baseic.common.template_rendering import G_TEMPLATE_RENDERING
from ..baseic.environment.common import environment_check_dependent_files_exists


# --------------------------------------------------------------------------
def instruction_init_engineering():
    """
    [ 命令行指令 - 初始化工程 ]

    """
    environment_check_dependent_files_exists()
    G_CONST.Path.FilePath.EngineeringInit.touch(mode=0o777, exist_ok=True)
    
    G_TEMPLATE_RENDERING.render_print(
        title='Awaken - 初始化工程',
        is_show_number=False,
        source=[
            '工程初始化成功 !',
            '初始化将创建或补全项目执行依赖文件.',
            '<*.ini> 文件仅作为工程根目录标识之用;',
            '这将帮助 Awaken 在执行指令时能够识别工程根目录.'
        ],
    )
    exit(0)
