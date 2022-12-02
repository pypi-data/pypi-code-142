
import subprocess
import json
import socket
import time

print('默认启动edge浏览器')


class WebBot:
    socket.setdefaulttimeout(10)
    wait_timeout = 5  # 超时设置
    interval_timeout = 0.5  # 轮询间隔

    def __init__(self, address="127.0.0.1", port=52020, browser='edge', debug_port=0, user_data_dir="./UserData",
                 browser_path='null', argument="null"):
        """
        :param address: webDriver服务地址。
        :param port: int，服务端口
        :param browser: str，edge/chrome，其他需指定browserPath
        :param debug_port: int，调试端口。默认 0 随机端口。指定端口则接管已打开的浏览器。
        :param user_data_dir: str，用户数据目录,默认./UserData。多进程同时操作多个浏览器数据目录不能相同
        :param browser_path: str，浏览器路径
        :param argument: str，浏览器启动参数。例如：无头模式: --headless   设置代理：--proxy-server=127.0.0.1:8080
        :return: webdriver对象
        """
        '''命令行启动示例：WebDriver.exe "{\"driverPort\":26678, \"browserName\":\"chrome\", \"debugPort\":0, 
        \"userDataDir\":\"./UserData\", \"browserPath\":\"null\", \"argument\":\"null\"}" '''
        self.__debugPort = debug_port
        self.__browserPath = browser_path
        self.__address = address
        self.__browserName = browser
        self.__userDataDir = user_data_dir
        self.__port = port
        self.__sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__argument = argument
        print('当前选择的是', self.__browserName, '浏览器')
        if self.__browserName == 'edge':
            print('请注意')
            print('接管Edge浏览器必须要有用户配置文件夹设置,谷歌和360安全浏览器则不必要')
        elif self.__browserName == 'chrome':
            print('请注意')
            print('谷歌内核浏览器不能使用close_page，否则连接会断，不能往下操作, edge和360安全浏览器可以使用')

        cmd = ['WebDriver.exe', json.dumps(
            {"driverPort": self.__port, "browserName": self.__browserName, "debugPort": self.__debugPort,
             "userDataDir": self.__userDataDir, "browserPath": self.__browserPath, "argument": argument})]
        self.__cmd = cmd
        subprocess.Popen(cmd)
        address_info = socket.getaddrinfo("127.0.0.1", port, socket.AF_INET, socket.SOCK_STREAM)[0]
        family, socket_type, proto, _, socket_address = address_info
        self.__sock = socket.socket(family, socket_type, proto)
        time.sleep(2)
        while True:
            try:
                self.__sock.connect(socket_address)
                print('连接浏览器成功')
                break
            except Exception as connect_error:
                print(connect_error)
                print('重试')

    def send_data(self, *args) -> str:
        """
        发送TCP命令
        :param args: 参照开源协议 http://www.ai-bot.net/aiboteProtocol.html#4
        :return: str
        """
        args_len = ""
        args_text = ""
        for argv in args:
            if argv is None:
                argv = ""
            elif isinstance(argv, bool) and argv:
                argv = "true"
            elif isinstance(argv, bool) and not argv:
                argv = "false"
            argv = str(argv)
            args_text += argv
            args_len += str(len(argv)) + "/"
        data = (args_len.strip("/") + "\n" + args_text).encode("utf8")
        self.__sock.sendall(data)
        data_length, data = self.__sock.recv(self.__port).split(b"/", 1)
        while int(data_length) > len(data):
            data += self.__sock.recv(self.__port)
        return data.decode("utf8").strip()

    # ###############
    #   页面和导航   #
    # ###############
    def goto(self, url) -> bool:
        """
        跳转url
        :param url: 字符串型, 网址
        """
        result = self.send_data('goto', url)
        return result == "true"

    def new_page(self, url) -> bool:
        """
        新建tab页面并跳转到指定url
        :param url: 字符串型, 网址
        """
        result = self.send_data("newPage", url)
        return result == "true"

    def back(self) -> bool:
        """
        回退
        """
        result = self.send_data("back")
        return result == "true"

    def forward(self) -> bool:
        """
        前进
        """
        result = self.send_data("forward")
        return result == "true"

    def refresh(self) -> bool:
        """
        刷新
        """
        result = self.send_data("refresh")
        return result == "true"

    def get_cur_page_id(self) -> str:
        """
        获取当前页面ID
        """
        result = self.send_data("getCurPageId")
        return result

    def get_all_page_id(self) -> list[str]:
        """
        返回页面ID数组
        """
        result = self.send_data("getAllPageId").split('|')

        return result

    def switch_page(self, page_id) -> bool:
        """
        切换页面
        :param page_id: 字符串型, 要切换的页面ID
        """
        result = self.send_data("switchPage", page_id)
        return result == "true"

    def close_page(self) -> bool:
        """
        关闭当前页面
        谷歌浏览器关闭页面有bug
        """
        result = self.send_data("closePage")
        return result == "true"

    def get_current_url(self):
        """
        获取当前URL
        """
        result = self.send_data("getCurrentUrl")
        return result

    def get_title(self):
        """
        获取页面标题
        """
        result = self.send_data("getTitle")
        return result

    # #############
    #    IFrame   #
    # #############
    def switch_frame(self, xpath, timeout=None) -> bool:
        """
        切换frame
        :param xpath: 要切换frame的元素路径
        :param timeout: 超时
        :return: 成功返回true，失败返回false
        """
        result = None  # 避免提示局部变量result可能在赋值前引用的错误提示（实际并不需要，但pycharm看着碍眼）
        if timeout is None:
            timeout = self.wait_timeout
        end_time = time.time() + timeout
        while time.time() <= end_time:
            result = self.send_data("switchFrame", xpath)
            if result == "false":
                time.sleep(self.interval_timeout)
            else:
                break
        return result == "true"

    def switch_main_frame(self) -> bool:
        """
        切换主frame
        """
        result = self.send_data("switchMainFrame")
        return result == "true"

    # #############
    #    元素操作   #
    # #############
    def click_element(self, xpath, timeout=None) -> bool:
        """
        点击元素
        :param xpath: 字符串型，元素路径
        :param timeout: 超时设置
        """
        result = None  # 避免提示局部变量result可能在赋值前引用的错误提示（实际并不需要，但pycharm看着碍眼）
        if timeout is None:
            timeout = self.wait_timeout
        end_time = time.time() + timeout
        while time.time() <= end_time:
            result = self.send_data("clickElement", xpath)
            if result == "false":
                time.sleep(self.interval_timeout)
            else:
                break
        return result == "true"

    def set_element_value(self, xpath, value, timeout=None) -> bool:
        """
        设置编辑框内容
        :param xpath: 字符串型，元素路径
        :param value: 字符串型，输入的值
        :param timeout: 超时设置
        """
        result = None  # 避免提示局部变量result可能在赋值前引用的错误提示（实际并不需要，但pycharm看着碍眼）
        if timeout is None:
            timeout = self.wait_timeout
        end_time = time.time() + timeout
        while time.time() <= end_time:
            result = self.send_data("setElementValue", xpath, value)
            if result == "false":
                time.sleep(self.interval_timeout)
            else:
                break
        return result == "true"

    def get_element_text(self, xpath, timeout=None) -> str:
        """
        获取文本
        :param xpath: 字符串型，元素路径
        :param timeout: 超时设置
        """
        result = None  # 避免提示局部变量result可能在赋值前引用的错误提示（实际并不需要，但pycharm看着碍眼）
        if timeout is None:
            timeout = self.wait_timeout
        end_time = time.time() + timeout
        while time.time() <= end_time:
            result = self.send_data("getElementText", xpath)
            if result == "null":
                time.sleep(self.interval_timeout)
            else:
                break
        if result == "null":
            return ''
        else:
            return result

    def get_element_outer_html(self, xpath, timeout=None) -> str:
        """
        获取outerHTML
        :param xpath: 字符串型，元素路径
        :param timeout: 超时设置
        :return: 成功返回元素innerHTML，失败返回null
        """
        result = None  # 避免提示局部变量result可能在赋值前引用的错误提示（实际并不需要，但pycharm看着碍眼）
        if timeout is None:
            timeout = self.wait_timeout
        end_time = time.time() + timeout
        while time.time() <= end_time:
            result = self.send_data("getElementOuterHTML", xpath)
            if result == "null":
                time.sleep(self.interval_timeout)
            else:
                break
        if result == "null":
            return ''
        else:
            return result

    def get_element_inner_html(self, xpath, timeout=None) -> str:
        """
        获取innerHTML
        :param xpath: 字符串型，元素路径
        :param timeout: 超时设置
        :return: 成功返回元素innerHTML，失败返回null
        """
        result = None  # 避免提示局部变量result可能在赋值前引用的错误提示（实际并不需要，但pycharm看着碍眼）
        if timeout is None:
            timeout = self.wait_timeout
        end_time = time.time() + timeout
        while time.time() <= end_time:
            result = self.send_data("getElementOuterHTML", xpath)
            if result == "null":
                time.sleep(self.interval_timeout)
            else:
                break
        if result == "null":
            return ''
        else:
            return result

    def set_element_attribute(self, xpath, attribute_name, value, timeout=None) -> bool:
        """
        设置属性值
        :param xpath:
        :param attribute_name: 指定的属性名
        :param value: 属性值
        :param timeout: 超时设置
        """
        result = None  # 避免提示局部变量result可能在赋值前引用的错误提示（实际并不需要，但pycharm看着碍眼）
        if timeout is None:
            timeout = self.wait_timeout
        end_time = time.time() + timeout
        while time.time() <= end_time:
            result = self.send_data("setElementAttribute", xpath, attribute_name, value)
            if result == "false":
                time.sleep(self.interval_timeout)
            else:
                break
        return result == "true"

    def get_element_attribute(self, xpath, attribute_name, timeout=None) -> str:
        """
        获取属性值
        :param xpath: 字符串型，元素路径
        :param attribute_name: 指定的属性名
        :param timeout: 超时设置
        """
        result = None  # 避免提示局部变量result可能在赋值前引用的错误提示（实际并不需要，但pycharm看着碍眼）
        if timeout is None:
            timeout = self.wait_timeout
        end_time = time.time() + timeout
        while time.time() <= end_time:
            result = self.send_data("getElementAttribute", xpath, attribute_name)
            if result == "null":
                time.sleep(self.interval_timeout)
            else:
                break
        if result == "null":
            return ''
        else:
            return result

    def get_element_rect(self, xpath, timeout=None) -> dict:
        """
        获取矩形位置
        :param xpath: 字符串型，元素路径
        :param timeout: 超时设置
        :return: 失败返回{}
        """
        result = None  # 避免提示局部变量result可能在赋值前引用的错误提示（实际并不需要，但pycharm看着碍眼）
        if timeout is None:
            timeout = self.wait_timeout
        end_time = time.time() + timeout
        while time.time() <= end_time:
            result = self.send_data("getElementRect", xpath)
            if result == "null":
                time.sleep(self.interval_timeout)
            else:
                break
        if result == "null":
            return {}
        else:
            return json.loads(result)

    def is_selected(self, xpath, timeout=None) -> bool:
        """
        判断该元素是否选中
        :param xpath: 字符串型，元素路径
        :param timeout: 超时设置
        :return: 选中返回True，否则返回False
        """
        result = None  # 避免提示局部变量result可能在赋值前引用的错误提示（实际并不需要，但pycharm看着碍眼）
        if timeout is None:
            timeout = self.wait_timeout
        end_time = time.time() + timeout
        while time.time() <= end_time:
            result = self.send_data("isSelected", xpath)
            if result == "webdriver error":
                time.sleep(self.interval_timeout)
            else:
                break
        if result == "false":
            return False
        else:
            return True

    def is_displayed(self, xpath, timeout=None) -> bool:
        """
        判断该元素是否可见
        :param xpath: 字符串型，元素路径
        :param timeout: 超时设置
        :return: 选中返回true，否则返回false
        """
        result = None  # 避免提示局部变量result可能在赋值前引用的错误提示（实际并不需要，但pycharm看着碍眼）
        if timeout is None:
            timeout = self.wait_timeout
        end_time = time.time() + timeout
        while time.time() <= end_time:
            result = self.send_data("isDisplayed", xpath)
            if result == "webdriver error":
                time.sleep(self.interval_timeout)
            else:
                break
        return result == "true"

    def is_enabled(self, xpath, timeout=None) -> bool:
        """
        判断元素是否可用
        :param xpath: 字符串型，元素路径
        :param timeout: 超时设置
        :return: 选中返回true，否则返回false
        """
        result = None  # 避免提示局部变量result可能在赋值前引用的错误提示（实际并不需要，但pycharm看着碍眼）
        if timeout is None:
            timeout = self.wait_timeout
        end_time = time.time() + timeout
        while time.time() <= end_time:
            result = self.send_data("isEnabled", xpath)
            if result == "webdriver error":
                time.sleep(self.interval_timeout)
            else:
                break
        return result == "true"

    def clear_element(self, xpath, timeout=None) -> bool:
        """
        清除元素值
        :param xpath: 字符串型，元素路径
        :param timeout: 超时设置
        :return: 选中返回true，否则返回false
        """
        result = None  # 避免提示局部变量result可能在赋值前引用的错误提示（实际并不需要，但pycharm看着碍眼）
        if timeout is None:
            timeout = self.wait_timeout
        end_time = time.time() + timeout
        while time.time() <= end_time:
            result = self.send_data("clearElement", xpath)
            if result == "false":
                time.sleep(self.interval_timeout)
            else:
                break
        return result == "true"

    # #############
    #   鼠标键盘   #
    # #############

    def set_element_focus(self, xpath, timeout=None) -> bool:
        """
        设置元素焦点
        :param xpath:元素路径
        :param timeout: 超时设置
        :return:成功返回true，失败返回false
        """
        result = None  # 避免提示局部变量result可能在赋值前引用的错误提示（实际并不需要，但pycharm看着碍眼）
        if timeout is None:
            timeout = self.wait_timeout
        end_time = time.time() + timeout
        while time.time() <= end_time:
            result = self.send_data("setElementFocus", xpath)
            if result == "false":
                time.sleep(self.interval_timeout)
            else:
                break
        return result == "true"

    def upload_file(self, xpath, file_path, timeout=None):
        """
        通过元素上传文件
        :param xpath:元素路径
        :param file_path:本地文件路径
        :param timeout: 超时设置
        :return:成功返回true，失败返回false
        """
        result = None  # 避免提示局部变量result可能在赋值前引用的错误提示（实际并不需要，但pycharm看着碍眼）
        if timeout is None:
            timeout = self.wait_timeout
        end_time = time.time() + timeout
        while time.time() <= end_time:
            result = self.send_data("uploadFile", xpath, file_path)
            if result == "false":
                time.sleep(self.interval_timeout)
            else:
                break
        return result == "true"

    def send_keys(self, xpath, text, timeout=None) -> bool:
        """
        发送文本
        :param xpath: 元素路径，如果元素不能设置焦点，应ClickMouse 点击锁定焦点输入
        :param text: 要输入的文本，例如sendKeys('//*[@id="kw"]', 'aibote\r'); aibote换行
        :param timeout: 超时设置
        :return: 选中返回true，否则返回false
        """
        result = None  # 避免提示局部变量result可能在赋值前引用的错误提示（实际并不需要，但pycharm看着碍眼）
        if timeout is None:
            timeout = self.wait_timeout
        end_time = time.time() + timeout
        while time.time() <= end_time:
            result = self.send_data("sendKeys", xpath, text)
            if result == "false":
                time.sleep(self.interval_timeout)
            else:
                break
        return result == "true"

    def send_vk(self, vkCode) -> bool:
        """
        发送Vk虚拟键
        :param vkCode: 整型，VK键值，仅支持 回退键:8  回车键:13  空格键:32  方向左键:37  方向上键:38  方向右键:39  方向下键:40  删除键:46
        """
        result = self.send_data("sendVk", vkCode)
        return result == "true"

    def click_mouse(self, x, y, msg) -> bool:
        """
        点击鼠标
        :param x: 整型，横坐标，非Windows坐标，页面左上角为起始坐标
        :param y: 整型，纵坐标，非Windows坐标，页面左上角为起始坐标
        :param msg: 整型，单击左键:1  单击右键:2  按下左键:3  弹起左键:4  按下右键:5  弹起右键:6  双击左键:7
        """
        result = self.send_data("clickMouse", x, y, msg)
        return result == "true"

    def move_mouse(self, x, y) -> bool:
        """
        移动鼠标
        :param x: 整型，横坐标，非Windows坐标，页面左上角为起始坐标
        :param y: 整型，纵坐标，非Windows坐标，页面左上角为起始坐标
        """
        result = self.send_data("moveMouse", x, y)
        return result == "true"

    def wheel_mouse(self, delta_x, delta_y, x=0, y=0) -> bool:
        """
        滚动鼠标
        :param delta_x: 整型，水平滚动条移动的距离
        :param delta_y: 整型，垂直滚动条移动的距离
        :param x: 整型，可选参数，鼠标横坐标位置， 默认为0
        :param y: 整型，可选参数，鼠标纵坐标位置， 默认为0
        """
        result = self.send_data("wheelMouse", delta_x, delta_y, x, y)
        return result == "true"

    def click_mouse_by_xpath(self, xpath, msg, timeout=None) -> bool:
        """
        通过xpath点击鼠标(元素中心点)
        :param xpath: 字符串型，元素路径
        :param msg: 整型，单击左键:1  单击右键:2  按下左键:3  弹起左键:4  按下右键:5  弹起右键:6  双击左键:7
        :param timeout: 超时设置
        """
        result = None  # 避免提示局部变量result可能在赋值前引用的错误提示（实际并不需要，但pycharm看着碍眼）
        if timeout is None:
            timeout = self.wait_timeout
        end_time = timeout + time.time()
        while time.time() <= end_time:
            result = self.send_data("clickMouseByXpath", xpath, msg)
            if result == "false":
                time.sleep(self.interval_timeout)
            else:
                break
        return result == "true"

    def move_mouse_by_xpath(self, xpath, timeout=None) -> bool:
        """
        通过xpath 移动鼠标(元素中心点)
        :param xpath: 字符串型，元素路径
        :param timeout: 超时设置
        """
        result = None  # 避免提示局部变量result可能在赋值前引用的错误提示（实际并不需要，但pycharm看着碍眼）
        if timeout is None:
            timeout = self.wait_timeout
        end_time = time.time() + timeout
        while time.time() <= end_time:
            result = self.send_data("moveMouseByXpath", xpath)
            if result == "false":
                time.sleep(self.interval_timeout)
            else:
                break
        return result == "true"

    def wheel_mouse_by_xpath(self, xpath, delta_x, delta_y, timeout=None) -> bool:
        """
        通过xpath 滚动鼠标
        :param xpath: 字符串型，元素路径
        :param delta_x: 整型，水平滚动条移动的距离
        :param delta_y: 整型，垂直滚动条移动的距离
        :param timeout: 超时设置
        """
        result = None  # 避免提示局部变量result可能在赋值前引用的错误提示（实际并不需要，但pycharm看着碍眼）
        if timeout is None:
            timeout = self.wait_timeout
        end_time = time.time() + timeout
        while time.time() <= end_time:
            result = self.send_data("wheelMouseByXpath", xpath, delta_x, delta_y)
            if result == "false":
                time.sleep(self.interval_timeout)
            else:
                break
        return result == "true"

    # #############
    #     截图     #
    # #############
    def take_screenshot(self, xpath=None, timeout=None) -> str:
        """
        截图
        :param xpath: 可选参数，默认截取全屏, 如果指定元素路径，则截取元素图片。
        :param timeout: 超时设置
        :return: 成功返回PNG图片格式 base64 字符串，失败返回""
        """
        result = None  # 避免提示局部变量result可能在赋值前引用的错误提示（实际并不需要，但pycharm看着碍眼）
        if timeout is None:
            timeout = self.wait_timeout
        if xpath:
            end_time = time.time() + timeout
            while time.time() <= end_time:
                result = self.send_data("takeScreenshot", xpath)
                if result == "null":
                    time.sleep(self.interval_timeout)
                else:
                    break
        else:
            result = self.send_data("takeScreenshot")
        if result == "null":
            return ""
        return result

    # ##################
    #  alert/prompt弹窗  #
    # ##################
    def click_alert(self, accept_or_cancel, prompt_text="") -> bool:
        """
        点击警告框
        :param accept_or_cancel: 布尔型，true接受, false取消
        :param prompt_text: 字符串型，可选参数，输入prompt警告框文本
        :return:成功返回true，失败返回false
        """
        result = self.send_data("clickAlert", accept_or_cancel, prompt_text)
        return result == "true"

    def get_alert_text(self) -> str:
        """
        获取警告框内容
        """
        result = self.send_data("getAlertText")
        return result

    # ###############
    #   cookie操作   #
    # ###############
    def get_cookies(self, url) -> str:
        """
        获取指定url匹配的cookies
        :param url: 字符串型，指定的url http://或https:// 起头
        :return: 成功返回json格式的字符串，失败返回""
        """
        result = self.send_data("getCookies", url)
        if result == "null":
            return ""
        return result

    def get_all_cookies(self) -> str:
        """
        获取cookies
        :return: 成功返回json格式的字符串，失败返回""
        """
        result = self.send_data("getAllCookies")
        if result == "null":
            return ""
        return result

    def set_cookie(self, cookie_param: dict) -> bool:
        """
        设置cookie
        :param cookie_param: 字典型，{"name":string, "value":string, "url":string, "domain":string, "path":string,
            "secure":boolean, "httpOnly":boolean, "sameSite":string, "expires":number, "priority":string,
            "sameParty":boolean, "sourceScheme":string, "sourcePort":number, "partitionKey":string}
        :name、value和url必填参数，其他参数可选
        :return:成功返回true，失败返回false
        """
        # 必填
        name = cookie_param["name"]
        value = cookie_param["value"]
        url = cookie_param["url"]
        #
        # 可选
        domain = path = same_site = priority = source_scheme = partition_key = ""
        secure = http_only = same_party = False
        expires = source_port = 0
        #
        if "domain" in cookie_param:
            domain = cookie_param["domain"]
        if "path" in cookie_param:
            path = cookie_param["path"]
        if "secure" in cookie_param:
            secure = cookie_param["secure"]
        if "httpOnly" in cookie_param:
            http_only = cookie_param["httpOnly"]
        if "sameSite" in cookie_param:
            same_site = cookie_param["sameSite"]
        if "expires" in cookie_param:
            expires = cookie_param["expires"]
        if "priority" in cookie_param:
            priority = cookie_param["priority"]
        if "sameParty" in cookie_param:
            same_party = cookie_param["sameParty"]
        if "sourceScheme" in cookie_param:
            source_scheme = cookie_param["sourceScheme"]
        if "sourcePort" in cookie_param:
            source_port = cookie_param["sourcePort"]
        if "partitionKey" in cookie_param:
            partition_key = cookie_param["partitionKey"]
        str_data = (
            "setCookie", name, value, url, domain, path, secure, http_only, same_site, expires, priority, same_party,
            source_scheme, source_port, partition_key)
        result = self.send_data(str_data)
        return result == "true"

    def delete_cookies(self, name, options=None) -> bool:
        """
        删除指定cookies
        :param name: 要删除的 Cookie 的名称。
        :param options:{url:string, domain:string, path:string} options 可选参数
        :url 如果指定，则删除所有匹配 url 和 name的Cookie
        :domain 如果指定，则删除所有匹配 domain 和 name的Cookie
        :path 如果指定，则删除所有匹配 path 和 name的Cookie
        :return: 成功返回true，失败返回false
        """
        if options is None:
            options = {}
        url = ""
        if "url" in options:
            url = options["url"]
        domain = ""
        if "domain" in options:
            domain = options["domain"]
        path = ""
        if "path" in options:
            path = options["path"]
        result = self.send_data("deleteCookies", name, url, domain, path)
        return result == "false"

    def delete_all_cookies(self) -> bool:
        """
        删除所有cookies
        :return: 成功返回true，失败返回false
        """
        result = self.send_data("deleteAllCookies")
        return result == "true"

    def clear_cache(self) -> bool:
        """
        清除缓存
        """
        result = self.send_data("clearCache")
        return result == "true"

    # ################
    #  注入JavaScript  #
    # ################
    def execute_script(self, script) -> str:
        """
        执行JavaScript 代码
        :param script: 字符串型，注入的js代码
        :return: 假如注入代码为函数且有return语句，则返回 return 的值，否则返回""
        :注入示例：(function () {return "aibote rpa"})()
        """
        result = self.send_data("executeScript", script)
        if result == "null":
            return ""
        return result

    # #############
    #   浏览器窗口   #
    # #############
    def get_window_pos(self) -> dict:
        """
        获取窗口位置和状态
        :return: 成功返回矩形位置和窗口状态，失败返回{}。
        :{left:number, top:number, width:number, height:number, windowState:string}
        """
        result = self.send_data("getWindowPos")
        if result == "null":
            return {}
        return json.loads(result)

    def set_window_pos(self, window_state, rect=None) -> bool:
        """
        设置窗口位置和状态
        :param window_state: 窗口状态，正常:"normal"  最小化:"minimized"  最大化:"maximized"  全屏:"fullscreen"
        :param rect: {"left":number, "top":number, "width":number, "height":number}
        :return: 成功返回true，失败返回false
        """
        if rect is None:
            rect = {"left": 0, "top": 0, "width": 0, "height": 0}
        result = self.send_data("setWindowPos", window_state, rect["left"], rect["top"], rect["width"], rect["height"])
        return result == "true"
