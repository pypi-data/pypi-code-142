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
命令行指令 - 更新版本

"""
import re
import subprocess

from .. import AwakenDetails
from ..baseic.common.template_rendering import G_TEMPLATE_RENDERING


# --------------------------------------------------------------------------
def instruction_update():
    """
    [ 命令行指令 - 更新版本 ]

    ---
    参数
    - argv : { list } - 参数列表。

    """
    G_TEMPLATE_RENDERING.render_print(
        title='Awaken - 更新版本',
        is_show_number=False,
        source=[
            '正在查询 PYPI 服务器 ...',
        ],
    )

    dos_result = subprocess.Popen(['pip', 'install', f'{ AwakenDetails.Name }=='], stderr=subprocess.PIPE)
    _, err = dos_result.communicate()
    newest_version: str = re.findall(r'from versions: (.*)\)', str(err))[0].split(',')[-1].strip()

    if newest_version > AwakenDetails.Version:
        G_TEMPLATE_RENDERING.render_print(
            title='Awaken - 更新版本',
            is_show_number=False,
            source=[
                f'从 PYPI 中发现最新版本号: {newest_version} !',
                '正在执行更新程序 ...',
                f'{AwakenDetails.Version} >> {newest_version}',
            ],
        )

        dos_result = subprocess.Popen(['pip', 'install', '--upgrade', AwakenDetails.Name], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        dos_result.communicate()

        G_TEMPLATE_RENDERING.render_print(
            title='Awaken - 更新版本',
            is_show_number=False,
            source=[
                f'当前为最新版本号:: {newest_version}',
                '已完成更新 ...',
            ],
        )

    else:
        G_TEMPLATE_RENDERING.render_print(
            title='Awaken - 更新版本',
            is_show_number=False,
            source=[
                f'当前为最新版本号:: {newest_version}',
                '暂无更新 ...',
            ],
        )
        exit(0)
