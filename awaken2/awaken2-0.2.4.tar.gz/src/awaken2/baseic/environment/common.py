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
[ 环境相关通用函数 ]

"""
from ..const import G_CONST
from ..broadcast.awaken_log import G_LOG
from ..environment.web.browser_driver_handle import G_BROWSER_DRIVER_HANDLE


# --------------------------------------------------------------------------
def environment_check_browser_driver_exists():
    """
    [ 环境检查 - 安装浏览器驱动 ]

    ---
    描述
    - 检查本地是否下载了WEB引擎所需的浏览器驱动, 否则下载。

    """
    # 检查本地已安装的浏览器驱动
    complete   = []
    uncomplete = []
    local_driver = G_BROWSER_DRIVER_HANDLE.inspect()

    for dk, dv in local_driver.items():
        if dv:
            complete.append(dk)
        else:
            uncomplete.append(dk)

    # 安装未安装的浏览器驱动
    if len(uncomplete) > 0:
        G_BROWSER_DRIVER_HANDLE.install(uncomplete)


# --------------------------------------------------------------------------
def environment_check_dependent_files_exists():
    """
    [ 环境检查 - 创建工程依赖 ]

    """
    # 创建目录
    for path in [
        G_CONST.Path.DirPath.Data,
        G_CONST.Path.DirPath.Logs,
        G_CONST.Path.DirPath.BaseCode,
        G_CONST.Path.DirPath.Projects,
    ]:
        G_LOG.debug(f'创建工程依赖目录:: {str(path.resolve())}')
        path.mkdir(parents=True, exist_ok=True)

    # 创建文件
    for path in [
        G_CONST.Path.FilePath.EngineeringInit,
        G_CONST.Path.FilePath.EngineeringConfig,
        G_CONST.Path.FilePath.EngineeringDatabase,
    ]:
        G_LOG.debug(f'创建工程依赖文件:: {str(path.resolve())}')
        path.touch(mode=0o777, exist_ok=True)
