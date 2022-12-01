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
浏览器驱动管理器

"""
import os
import shutil

from pathlib import Path

from ...broadcast.awaken_log import G_LOG
from ...common.template_rendering import G_TEMPLATE_RENDERING
from ...decorator.baseic import deco_singleton
from ...error.file import AwakenUserConfigPathNotExist
from ...error.type_error import AwakenBrowserDriverNotSupportError


_REGISTERED_BROWSERS = [
    'chromium', 'firefox', 'webkit',
]
""" 支持的浏览器清单 """

_ENVIRONMENT_VARIABLE = 'USERPROFILE'
""" 用户配置文件系统环境变量KEY """

_PLAYWRIGHT_CACHE_PATH = Path(os.environ[_ENVIRONMENT_VARIABLE]).joinpath('AppData\Local\ms-playwright')
""" Playwright缓存目录路径对象 """


# --------------------------------------------------------------------------
@deco_singleton
class BrowserDriverHandle:
    """
    [ 浏览器驱动管理器 ]

    """
    local_driver_path_map = {}


    # ----------------------------------------------------------------------
    def __init__(self) -> None:
        self._search_local_downloaded_browser_drivers()


    # ----------------------------------------------------------------------
    def get_registered_browsers(self):
        """ 
        [ 获取支持的浏览器清单 ] 
        
        """
        return _REGISTERED_BROWSERS


    # ----------------------------------------------------------------------
    def inspect(self, browser_drivers: str | list = []):
        """
        [ 检查已安装的浏览器 ]

        ---
        描述
        - 检查本地是否安装浏览器驱动。

        ---
        参数
        - browser_drivers : { str | list } - 需要查询的浏览器驱动名称或列表, 为空表示全部。

        ---
        返回
        - dict : 查询的浏览器驱动是否安装结果字典。

        """
        # 检查本地 playwright 环境是否安装浏览器驱动
        self._search_local_downloaded_browser_drivers()
        browser_drivers = self._unified_processing_browser_driver_list(browser_drivers)

        drive_installation_results = {}
        for driver_item in browser_drivers:
            result = False
            if driver_item in self.local_driver_path_map.keys():
                result = True
            drive_installation_results.update({driver_item : result})
        return drive_installation_results


    # ----------------------------------------------------------------------
    def install(self, browser_drivers: str | list = []):
        """
        [ 安装浏览器驱动 ]

        ---
        描述
        - 安装指定的浏览器驱动。

        ---
        参数
        - browser_drivers : { str | list } - 需要安装的浏览器驱动名称或列表, 为空表示全部。

        ---
        返回
        - dict : 浏览器驱动的安装结果字典。

        """
        drive_install_results = {}
        drive_installation_results = self.inspect()
        browser_drivers = self._unified_processing_browser_driver_list(browser_drivers)

        for driver_item in browser_drivers:
            install_result = True
            if drive_installation_results[driver_item] == True:
                drive_install_results.update({driver_item : install_result})
                continue
            try:
                G_LOG.debug(f'正在连接网络下载 [{driver_item}] 浏览器驱动.')
                G_TEMPLATE_RENDERING.render_print(
                    title='浏览器驱动管理器',
                    source=[f'正在连接网络下载 [{driver_item}] 浏览器驱动.'],
                    is_show_number=False
                )
                os.system(f'playwright install { driver_item }')
            except BaseException:
                install_result = False
                continue
            drive_install_results.update({driver_item : install_result})

        return drive_install_results


    # ----------------------------------------------------------------------
    def uninstall(self, browser_drivers: str | list = []):
        """
        [ 卸载浏览器驱动 ]

        ---
        描述
        - 卸载指定的浏览器驱动。

        ---
        参数
        - browser_drivers : { str | list } - 需要卸载的浏览器驱动名称或列表, 为空表示全部。

        ---
        返回
        - dict : 浏览器驱动的卸载结果字典。

        """
        drive_uninstall_results = {}
        drive_installation_results = self.inspect()
        browser_drivers = self._unified_processing_browser_driver_list(browser_drivers)

        for driver_item in browser_drivers:
            uninstall_result = True
            if drive_installation_results[driver_item] == False:
                drive_uninstall_results.update({driver_item : uninstall_result})
                continue
            try:
                G_LOG.debug(f'正在连接网络下载 [{driver_item}] 浏览器驱动.')
                G_TEMPLATE_RENDERING.render_print(
                    title='浏览器驱动管理器',
                    source=[f'正在从本地删除 [{driver_item}] 浏览器驱动.'],
                    is_show_number=False
                )
                shutil.rmtree(self.local_driver_path_map[driver_item])
                del self.local_driver_path_map[driver_item]
            except BaseException:
                uninstall_result = False
                continue
            drive_uninstall_results.update({driver_item : uninstall_result})
    
        return drive_uninstall_results


    # ----------------------------------------------------------------------
    def _search_local_downloaded_browser_drivers(self):
        """
        [ 搜索本地下载的浏览器驱动 ]

        ---
        描述
        - 从本地的Playwright缓存目录中搜索下载的浏览器驱动。

        """
        if _ENVIRONMENT_VARIABLE in os.environ:
            for dir_path in _PLAYWRIGHT_CACHE_PATH.glob('*'):
                driver_name = dir_path.stem.split('-')[0]
                if driver_name in _REGISTERED_BROWSERS:
                    self.local_driver_path_map.update({driver_name : dir_path})
        else:
            error_message = '未能在系统环境变量中获取到用户配置文件路径 !'
            raise AwakenUserConfigPathNotExist(error_message)


    # ----------------------------------------------------------------------
    def _unified_processing_browser_driver_list(self, browser_drivers: str | list):
        """
        [ 统一处理浏览器驱动列表 ]

        ---
        参数
        - browser_drivers : { str | list } - 浏览器驱动名称或列表。

        """
        browser_drivers = [browser_drivers] if isinstance(browser_drivers, str) else browser_drivers
        
        if len(browser_drivers) < 1:
            browser_drivers = _REGISTERED_BROWSERS

        for driver_item in browser_drivers:
            if driver_item not in _REGISTERED_BROWSERS:
                error_message = f'{driver_item} 不是支持的浏览器类型 !'
                raise AwakenBrowserDriverNotSupportError(error_message)

        return browser_drivers


# --------------------------------------------------------------------------
G_BROWSER_DRIVER_HANDLE: BrowserDriverHandle = BrowserDriverHandle()
""" 浏览器驱动管理器全局实例 """
