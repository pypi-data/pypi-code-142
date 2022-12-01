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
WEB驱动引擎

"""
import time
import asyncio
from typing import Any

from pathlib import Path

from ...baseic.const import G_CONST
from ...baseic.error.engine import AwakenWebEngineError


# --------------------------------------------------------------------------
class WebEngine:
    """
    [ WEB驱动引擎 ]

    """
    _playwright: Any
    """ Playwright对象 """
    _browser_map: dict
    """ 浏览器类型映射字典 """
    _browser = None
    """ 浏览器进程对象 """
    _context = None
    """ 浏览器上下文对象 """
    _page = None
    """ 浏览器页面对象 """


    # ----------------------------------------------------------------------
    def _init_playwright(self, playwright) -> ...:
        self._playwright = playwright
        self._browser_map = {
            G_CONST.Type.Browser.Webkit : self._playwright.webkit,
            G_CONST.Type.Browser.Firefox : self._playwright.firefox,
            G_CONST.Type.Browser.Chromium : self._playwright.chromium,
        }


    # ----------------------------------------------------------------------
    async def _browser_start(
        self, 
        browser_type=G_CONST.Type.Browser.Chromium, 
        headless=False
    ) -> ...:
        """ 
        [ 启动浏览器 ]

        ---
        描述
        - 根据传入的浏览器类型启动对象浏览器进程。

        ---
        参数
        - browser_type : { str } - 浏览器类型, 默认谷歌浏览器。
        - headless : { bool } - 是否以无头模式运行。

        """
        # 如果浏览器类型不存在, 则使用默认的 Chromium 浏览器
        if browser_type not in self._browser_map.keys():
            browser_type = G_CONST.Type.Browser.Chromium

        # 创建浏览器实例不存在则创建
        if not self._browser:
            self._browser = await self._browser_map[browser_type].launch(headless=headless)
            self._context = await self._browser.new_context()


    # ----------------------------------------------------------------------
    async def _page_start(self) -> ...:
        """ 
        [ 启动页面 ]

        ---
        描述
        - 浏览器进程启动页面实例。

        """
        self._page = await self._context.new_page()


    # ----------------------------------------------------------------------
    async def _page_close(self) -> ...:
        """
        [ 关闭页面 ]

        ---
        描述
        - 浏览器进程关闭页面实例。

        """
        if self._page:
            await self._page.close()
            self._page = None


    # ----------------------------------------------------------------------
    async def _exit(self) -> ...:
        """ 
        [ 退出浏览器 ]

        ---
        描述
        - 关闭页面、上下文、浏览器对象。
        
        """
        if self._page:
            await self._page.close()
            await self._context.close()
            await self._browser.close()
        self._page = None
        self._context = None
        self._browser = None


    # ----------------------------------------------------------------------
    async def new_context(self) -> ...:
        """ 
        [ 重置上下文 ]

        ---
        描述
        - 重置浏览器的上下文, 然后重新打开一个新页面。
        
        """
        await self._page_close()
        await self._context.close()
        self._context = await self._browser.new_context()
        self._page = await self._context.new_page()


    # ----------------------------------------------------------------------
    async def get_page_name(self) -> str:
        """ 
        [ 获取页面名称 ]

        ---
        描述
        - 获取当前页面中的 Title 属性。

        ---
        返回
        - str : 当前页面的名称。

        """
        return await self._page.title()


    # ----------------------------------------------------------------------
    async def get_element_count(self, element: str) -> int:
        """
        [ 获取元素数量 ]

        ---
        描述
        - 获取当前页面中定位元素的数量。

        ---
        参数
        - element { str } : 元素选择器。

        ---
        返回
        - int : 元素数量。

        """
        count = await self._locator_element_count(element)
        return count


    # ----------------------------------------------------------------------
    async def get_element_text(self, element: str, eid: int = 1) -> str:
        """ 
        [ 获取元素文本 ]

        ---
        描述
        - 获取当前页面中定位元素的文本。

        ---
        参数
        - element { str } : 元素选择器。
        - eid { str } : 元素下标。

        ---
        返回
        - str : 元素的文本。

        """
        element = await self._locator_element(element, eid)
        element_text = await element.text_content()
        return element_text

    
    # ----------------------------------------------------------------------
    async def get_input_value(self, element: str, eid: int = 1) -> str:
        """
        [ 获取输入框的值 ]

        ---
        描述
        - 获取输入框控件中输入的值。

        ---
        参数
        - element { str } : 元素选择器。
        - eid { str } : 元素下标。

        ---
        返回
        - str : 输入框的文本。

        """
        element = await self._locator_element(element, eid)
        element_text = await element.input_value()
        return element_text


    # ----------------------------------------------------------------------
    async def get_attribute(self, name: str, element: str, eid: int = 1) -> str | int:
        """ 
        [ 获取元素属性值 ]

        ---
        描述
        - 获取元素指定属性的值。

        ---
        参数
        - name { str } : 需获取值的属性名称。
        - element { str } : 元素选择器。
        - eid { str } : 元素下标。

        ---
        返回
        - str : 元素的属性值。

        """
        element = await self._locator_element(element, eid)
        element_value = await element.get_attribute(name)
        return element_value


    # ----------------------------------------------------------------------
    async def set_window_size(self, width: int, height: int) -> ...:
        """ 
        [ 设置浏览器尺寸 ]

        ---
        描述
        - 设置当前浏览器的窗口尺寸。

        ---
        参数
        - width { int } : 浏览器宽度。
        - height { int } : 浏览器高度。

        """
        size = \
        {
            'width' : int(width),
            'height': int(height),
        }
        await self._page.set_viewport_size(size)


    # ----------------------------------------------------------------------
    async def goto(self, url: str):
        """ 
        [ 页面跳转 ]

        ---
        描述
        - 访问输入的 URL 网站。

        ---
        参数
        - url { str } : 需要访问的 URL 路径。

        """
        await self._page.goto(url)


    # ----------------------------------------------------------------------
    async def back(self):
        """ 
        [ 页面回退 ]

        ---
        描述
        - 浏览器回退到上一页。

        """
        await self._page.go_back()


    # ----------------------------------------------------------------------
    async def forward(self):
        """ 
        [ 页面前进 ]

        ---
        描述
        - 浏览器前进到下一页。

        """
        await self._page.go_forward()

    
    # ----------------------------------------------------------------------
    async def reload(self):
        """ 
        [ 页面刷新 ]

        ---
        描述
        - 浏览器刷新当前页面。
            
        """
        await self._page.reload()


    # ----------------------------------------------------------------------
    async def send(self, key: str, element: str, eid: int = 1):
        """ 
        [ 输入框输入 ]

        ---
        描述
        - 该函数期望的目标控件是 Input 类型。

        ---
        参数
        - key { str } : 输入的值。
        - element { str } : 元素选择器。
        - eid { int } : 元素下标。

        """
        element = await self._locator_element(element, eid)
        if not isinstance(key, str):
            key = str(key)
        await element.fill(key)


    # ----------------------------------------------------------------------
    async def click(self, element: str, eid: int = 1):
        """ 
        [ 鼠标单击 ]

        ---
        描述
        - 模拟鼠标进行单击元素操作。

        ---
        参数
        - element { str } : 元素选择器。
        - eid { int } : 元素下标。

        """
        element = await self._locator_element(element, eid)
        await element.click()


    # ----------------------------------------------------------------------
    async def dbl_click(self, element, eid: int = 1):
        """ 
        [ 鼠标双击 ]

        ---
        描述
        - 模拟鼠标进行双击元素操作。

        ---
        参数
        - element { str } : 元素选择器。
        - eid { int } : 元素下标。

        """
        element = await self._locator_element(element, eid)
        await element.dblclick()


    # ----------------------------------------------------------------------
    async def drag_to(self, element1: str, element2: str, eid1: int = 1, eid2: int = 1):
        """ 
        [ 鼠标拖拽 ]

        ---
        描述
        - 模拟鼠标拖拽行为, 将元素1拖拽至元素2, 然后松开鼠标。

        ---
        参数
        - element1 { str } : 元素1选择器。
        - element2 { str } : 元素2选择器。
        - eid1 { int } : 元素1下标。
        - eid2 { int } : 元素2下标。

        """
        element1 = await self._locator_element(element1, eid1)
        element2 = await self._locator_element(element2, eid2)
        await element1.drag_to(element2)


    # ----------------------------------------------------------------------
    async def hover(self, wait: int, element: str, eid: int = 1):
        """ 
        [ 鼠标悬停 ]

        ---
        描述
        - 模拟鼠标悬停在元素上。

        ---
        参数
        - wait { int } : 悬停等待时长。
        - element { str } : 元素选择器。
        - eid { int } : 元素下标。

        """
        element = await self._locator_element(element, eid)
        await element.hover()
        await asyncio.sleep(wait)


    # ----------------------------------------------------------------------
    async def popup_ok(self, element: str, eid: int = 1, text: str = ''):
        """ 
        [ 弹窗确定 ]

        ---
        描述
        - 点击一个绑定了弹窗事件的按钮元素, 然后静默确认该弹窗, 如果该弹窗存在输入框, 可通过参数 text 来填充。

        ---
        参数
        - element { str } : 元素选择器。
        - eid { int } : 元素下标。
        - text { str } : 如果该弹窗存在输入框, 可通过参数 text 来填充。

        """
        # 弹窗处理函数
        async def event(dialog):
            global temporary_text_register
            temporary_text_register = dialog.message
            await dialog.accept(text)

        # 绑定弹窗处理事件
        self._page.once('dialog', event)
        element = await self._locator_element(element, eid)
        await element.click()
        return temporary_text_register


    # ----------------------------------------------------------------------
    async def popup_no(self, element: str, eid: int = 1):
        """ 
        [ 弹窗取消 ]

        ---
        描述
        - 点击一个绑定了弹窗事件的按钮元素, 然后静默取消该弹窗。

        ---
        参数
        - element { str } : 元素选择器。
        - eid { int } : 元素下标。

        """
        # 弹窗处理函数
        async def event(dialog):
            global temporary_text_register
            temporary_text_register = dialog.message
            await dialog.dismiss()

        # 绑定弹窗处理事件
        self._page.once('dialog', event)
        element = await self._locator_element(element, eid)
        await element.click()
        return temporary_text_register


    # ----------------------------------------------------------------------
    async def upload(self, file_path: str, element: str, eid: int = 1):
        """ 
        [ 上传文件 ]

        ---
        描述
        - 点击一个绑定了文件上传事件的按钮元素, 然后静默处理该事件。

        ---
        参数
        - file_path { str } : 文件完整路径。
        - element { str } : 元素选择器。
        - eid { int } : 元素下标。

        """
        # 监听文件选择器对象
        self._page.once('filechooser', lambda _: ...)
        async with self._page.expect_file_chooser() as chooser_object:
            element = await self._locator_element(element, eid)
            await element.click()

        chooser_object = await chooser_object.value
        await chooser_object.set_files(file_path)


    # ----------------------------------------------------------------------
    async def download(self, file_path: str, element: str, eid: int = 1):
        """ 
        [ 下载文件 ]

        ---
        描述
        - 点击一个绑定了文件下载事件的按钮元素, 然后静默处理该事件。

        ---
        参数
        - file_path { str } : 文件保存完整路径。
        - element { str } : 元素选择器。
        - eid { int } : 元素下标。

        """
        # 监听下载对象
        self._page.once('download', lambda _: ...)
        async with self._page.expect_download() as download_object:
            element, _ = await self._locator_element(element, eid)
            await element.click()

        download_object = await download_object.value
        await download_object.save_as(file_path)

    
    # ----------------------------------------------------------------------
    async def save_png(self, save_path: str):
        """ 
        [ 保存图片 ]

        ---
        描述
        - 保存当前屏幕截图。

        ---
        参数
        - save_path { str } : 屏幕截图后需要保存至的本机完整路径。

        """
        png_bytes = await self._page.screenshot()
        suffix = '.png'
        if save_path[-4:] != suffix:
            save_path = ''.join([save_path, suffix])

        save_path = Path(save_path)
        save_path.touch(0o777)
        save_path.write_bytes(png_bytes)

        return save_path.resolve()


    # ----------------------------------------------------------------------
    async def _dispatch_event(self, element, event_name):
        await self._page.dispatch_event(element, event_name)


    # ----------------------------------------------------------------------
    async def _java_script(self, expression, args):
        return await self._page.evaluate(expression, args)


    # ----------------------------------------------------------------------
    async def _locator_element(self, element: str, eid: int) -> Any:
        """ 
        [ 定位元素 ]

        ---
        描述
        - 定位当前页面的所有符合预期的元素对象。

        ---
        参数
        - element { str } : 元素选择器。
        - eid { int } : 元素下标。

        ---
        返回
        - 元素对象。

        """
        element_count  = 0
        retries_number = 5  # 元素重试次数
        retries_sleep  = 1  # 元素重试间隔时间

        for _ in range(retries_number):
            result = self._page.locator(element)
            element_count = await result.count()
            if element_count < 1:
                time.sleep(retries_sleep)
                continue
            else:
                break
        
        if element_count == 0:
            raise AwakenWebEngineError(f'无法定位到元素:: { element } !')
        if element_count < eid:
            raise AwakenWebEngineError(f'元素列表数量::{ element_count }, 但是传递ID::{ eid } !')

        return result.nth(eid-1)

        # try:
        #     for _ in range(retries_number):
        #         result = self._page.locator(element)
        #         element_count = await result.count()
        #         if element_count < 1:
        #             time.sleep(retries_sleep)
        #             continue
        #         else:
        #             break
                
        #     if element_count == 0:
        #         raise BaseException

        # except BaseException:
        #     raise AwakenWebEngineError(f'无法定位到元素 :: { element } !')
                
        # try:
        #     # 如果 eid 大于元素数量则抛出异常
        #     if element_count < eid: 
        #         raise BaseException
        #     else:
        #         return result.nth(eid - 1), element_count

        # except BaseException:
        #     raise AwakenWebEngineError(f'EID 超出元素对象数量, 无法应用 !')


    # ----------------------------------------------------------------------
    async def _locator_element_count(self, element: str) -> int:
        """ 
        [ 定位元素数量 ]

        ---
        参数
        - element { str } : 元素选择器。
        
        ---
        返回
        - 元素数量。
        
        """
        result = self._page.locator(element)
        element_count = await result.count()
        return element_count
