import os
import time

import allure
import uiautomator2 as u2

from qrunner.core.android.common import get_device_list, get_current_device
from qrunner.core.android.element import AndroidElement
from qrunner.utils.config import config
from qrunner.utils.exceptions import ScreenFailException, DeviceNotFoundException
from qrunner.utils.log import logger


class AndroidDriver(object):
    # _instance = {}
    #
    # def __new__(cls, serial_no=None):
    #     if serial_no not in cls._instance:
    #         cls._instance[serial_no] = super().__new__(cls)
    #     return cls._instance[serial_no]

    def __init__(self, serial_no=None, pkg_name=None):
        if serial_no is None:
            self.serial_no = get_current_device()
        else:
            if serial_no in get_device_list():
                self.serial_no = serial_no
            else:
                raise DeviceNotFoundException(msg=f"设备 {serial_no} 未连接")
        self.pkg_name = pkg_name

        logger.info(f"启动 android driver for {self.serial_no}")
        self.d = u2.connect(self.serial_no)

    # @classmethod
    # def get_instance(cls, serial_no=None):
    #     """Create singleton"""
    #     if serial_no not in cls._instance:
    #         logger.info(f"[{serial_no}] Create android driver singleton")
    #         return AndroidDriver(serial_no)
    #     return AndroidDriver._instance[serial_no]

    @staticmethod
    def get_elem(**kwargs):
        """获取控件对象"""
        return AndroidElement(**kwargs)

    def uninstall_app(self, pkg_name=None):
        """卸载应用"""
        if not pkg_name:
            pkg_name = self.pkg_name
        logger.info(f"卸载应用: {pkg_name}")
        self.d.app_uninstall(pkg_name)

    def install_app(self, apk_path, auth=True, new=True, pkg_name=None):
        """安装应用
        @param pkg_name: 应用包名
        @param apk_path: 安装包链接，支持本地路径以及http路径
        @param auth: 是否进行授权
        @param new: 是否先卸载再安装
        """
        logger.info(f"安装应用: {apk_path}")
        if new is True:
            if pkg_name is None:
                pkg_name = self.pkg_name
            self.uninstall_app(pkg_name)
        if auth is True:
            target = "/data/local/tmp/_tmp.apk"
            self.d.push(apk_path, target, show_progress=True)
            logger.debug("pm install -r -t -g %s", target)
            ret = self.d.shell(['pm', 'install', "-r", "-t", "-g", target], timeout=300)
            if ret.exit_code != 0:
                raise RuntimeError(ret.output, ret.exit_code)
            return
        self.d.app_install(apk_path)

    def start_app(self, pkg_name=None, stop=True):
        """启动应用
        @param pkg_name: 应用包名
        @param stop: 是否先关闭应用再启动
        """
        if not pkg_name:
            pkg_name = self.pkg_name
        logger.info(f"启动应用: {pkg_name}")
        self.d.app_start(pkg_name, stop=stop, use_monkey=True)

    def stop_app(self, pkg_name=None):
        """停止指定应用"""
        if not pkg_name:
            pkg_name = self.pkg_name
        logger.info(f"退出应用: {pkg_name}")
        self.d.app_stop(pkg_name)

    def stop_all_app(self):
        """停止所有应用"""
        logger.info(f"退出所有应用")
        self.d.app_stop_all()

    def stop_app_list(self, app_list: list):
        """退出指定多个应用"""
        logger.info(f"退出多个应用: {app_list}")
        self.d.app_stop_all(excludes=app_list)

    def clear_app(self, pkg_name=None):
        """清除应用缓存"""
        if not pkg_name:
            pkg_name = self.pkg_name
        logger.info(f"清除应用缓存: {pkg_name}")
        self.d.app_clear(pkg_name)

    def get_driver_info(self):
        """设备连接信息"""
        logger.info(f"获取连接信息")
        return self.d.info

    def get_app_info(self, pkg_name=None):
        """获取指定应用信息"""
        if not pkg_name:
            pkg_name = self.pkg_name
        logger.info(f"获取指定应用信息: {pkg_name}")
        info = self.d.app_info(pkg_name)
        logger.info(info)
        return info

    def get_current_app(self):
        """获取当前应用信息"""
        logger.info(f"获取当前应用信息")
        return self.d.app_current()

    def save_app_icon(self, pkg_name=None):
        """保存应用icon"""
        if not pkg_name:
            pkg_name = self.pkg_name
        logger.info(f"获取应用icon并保存到当前目录")
        img = self.d.app_icon(pkg_name)
        img.save(f"{pkg_name}-icon.png")

    def get_running_apps(self):
        """获取正在运行的应用"""
        logger.info(f"获取所有正在运行的应用")
        app_list = self.d.app_list_running()
        logger.info(app_list)
        return app_list

    def get_app_list(self):
        """获取所有已安装的应用"""
        logger.info(f"获取所有已安装的应用")
        app_list = self.d.app_list()
        logger.info(app_list)
        return app_list

    def wait_app_running(self, pkg_name=None, front=True, timeout=20):
        """
        等待应用运行
        @param pkg_name: 应用包名
        @param front: 是否前台运行
        @param timeout: 等待时间
        @return: 应用pid
        """
        if not pkg_name:
            pkg_name = self.pkg_name
        pid = self.d.app_wait(pkg_name, front=front, timeout=timeout)
        if not pid:
            logger.info(f"{pkg_name} is not running")
        else:
            logger.info(f"{pkg_name} pid is {pid}")
        return pid

    def wait_activity(self, activity_name, timeout=10):
        """
        等待activity运行
        @param activity_name: activity名称，.ApiDemos
        @param timeout: 超时时间
        @return: True or False
        """
        logger.info(f"等待activity {activity_name}")
        flag = self.d.wait_activity(activity_name, timeout=timeout)
        logger.info(flag)
        return flag

    def push(self, src_path, target_path, mode=None):
        """
        把电脑本地文件上传到手机上
        @param src_path: 电脑本地文件，foo.txt
        @param target_path: 手机目录，/sdcard/
        @param mode: 需要修改的权限，0o755
        @return:
        """
        logger.info(f"把{src_path} push到手机 {target_path}目录")
        if mode is not None:
            self.d.push(src_path, target_path)
        else:
            self.d.push(src_path, target_path, mode=mode)

    def pull(self, src_path, target_path):
        """
        把手机上的文件下载到电脑
        @param src_path: 手机文件，/sdcard/tmp.txt
        @param target_path: 电脑目录，tmp.txt
        @return:
        """
        logger.info(f"{src_path} pull到电脑 {target_path}目录")
        self.d.pull(src_path, target_path)

    def check(self):
        """检查设备连接状态"""
        logger.info("检查并维持设备端守护进程处于运行状态")
        self.d.healthcheck()

    def open_url(self, url):
        """
        通过url打开web页面或者app schema
        @param url: 页面url，https://www.baidu.com，taobao://taobao.com
        @return:
        """
        logger.info(f"打开链接: {url}")
        self.d.open_url(url)

    def shell(self, cmd, timeout=60):
        """
        执行短周期shell脚本
        @param cmd: shell字符串或list，pwd，["ls", "-l"]
        @param timeout: 超时时间
        @return:
        """
        logger.info(f"执行shell命令: {cmd}")
        output, exit_code = self.d.shell(cmd, timeout=timeout)
        return output, exit_code

    def start_session(self, pkg_name=None):
        """
        启动应用并生成session
        @param pkg_name: 应用包名
        @return:
        """
        logger.info(f"启动{pkg_name}session")
        if not pkg_name:
            pkg_name = self.pkg_name
        self.session = self.d.session(pkg_name)

    def stop_session(self):
        """关闭session并停止应用"""
        logger.info(f"关闭session并停止应用")
        self.session.close()

    def check_session(self):
        """检查session是否可用"""
        logger.info(f"检查session是否可用")
        is_running = self.session.running()
        logger.info(is_running)
        return is_running

    def screenshot(self, file_name):
        """
        截图并保存到预定路径
        @param file_name: foo.png or fool
        @return:
        """
        # 把文件名处理成test.png的样式
        try:
            if "." in file_name:
                file_name = file_name.split(r".")[0]
            # 截图并保存到当前目录的images文件夹中
            img_dir = os.path.join(os.getcwd(), "images")
            if os.path.exists(img_dir) is False:
                os.mkdir(img_dir)
            time_str = time.strftime("%Y年%m月%d日 %H时%M分%S秒")
            file_path = os.path.join(img_dir, f"{time_str}-{file_name}.png")
            self.d.screenshot(file_path)
            logger.info(f"截图并保存至: {file_path}")
            # 上传allure报告
            allure.attach.file(
                file_path,
                attachment_type=allure.attachment_type.PNG,
                name=f"{file_name}.png",
            )
            return file_path
        except Exception as e:
            raise ScreenFailException(f"{file_name} 截图失败\n{str(e)}")

    def upload_pic(self, file_name):
        """截图并上传allure"""
        # 截图并保存
        file_path = self.screenshot(file_name)
        # 上传allure报告
        allure.attach.file(
            file_path,
            attachment_type=allure.attachment_type.PNG,
            name=f"{file_name}.png",
        )
        logger.debug(f"[截图并上传报告] {file_path}")

    def get_page_content(self):
        """获取页面xml内容"""
        return self.d.dump_hierarchy()

    def get_window_size(self):
        """获取页面宽高"""
        return self.d.window_size()

    def get_serial(self):
        """获取设备id"""
        logger.info("获取设备id")
        serial = self.d.serial
        logger.info(serial)
        return serial

    def get_device_info(self):
        """获取设备信息"""
        logger.info(f"获取设备信息")
        info = self.d.device_info
        logger.info(info)
        return info

    def screen_on(self):
        """点亮屏幕"""
        logger.info("点亮屏幕")
        self.d.screen_on()

    def screen_off(self):
        """关闭屏幕"""
        logger.info("关闭屏幕")
        self.d.screen_off()

    def get_screen_status(self):
        """获取屏幕点亮状态"""
        logger.info("获取屏幕点亮状态")
        status = self.d.info.get("screenOn")
        logger.info(status)
        return status

    def unlock(self):
        """解锁手机"""
        logger.info("解锁手机")
        self.d.unlock()

    def press(self, key):
        """
        点击原生自带按键
        @param key: 按键名，支持：home、back、left、right、up、down、center、menu、search、enter、delete、recent、volume_up、
                    volume_down、volume_mute、camera、power
        @return:
        """
        logger.info(f"点击key: {key}")
        self.d.press(key)

    def click_xy(self, x, y):
        """点击坐标"""
        logger.info(f"单击坐标: {x},{y}")
        self.d.click(x, y)

    def click_alerts(self, alert_list: list):
        """点击弹窗"""
        logger.info(f"批量点击弹窗: {alert_list}")
        with self.d.watch_context() as ctx:
            for alert in alert_list:
                if "id/" in alert:
                    alert = f"{config.get_pkg()}:{alert}"
                ctx.when(alert).click()
            ctx.wait_stable()

    def double_click_xy(self, x, y):
        """双击坐标"""
        logger.info(f"双击坐标: {x},{y}")
        self.d.double_click(x, y)

    def long_click_xy(self, x, y):
        """长按坐标"""
        logger.info(f"长按坐标: {x},{y}")
        self.d.long_click(x, y)

    def swipe_xy(self, sx, sy, ex, ey):
        """滑动"""
        logger.info(f"从坐标{sx},{sy} 滑到 {ex},{ey}")
        self.d.swipe(sx, sy, ex, ey)

    def swipe_left(self, scale=0.9):
        """往左滑动"""
        logger.info("往左滑动")
        self.d.swipe_ext("left", scale=scale)

    def swipe_right(self, scale=0.9):
        """往右滑动"""
        logger.info("往右滑动")
        self.d.swipe_ext("right", scale=scale)

    def swipe_up(self, scale=0.8):
        """往上滑动"""
        logger.info("往上滑动")
        self.d.swipe_ext("up", scale=scale)

    def swipe_down(self, scale=0.8):
        """往下滑动"""
        logger.info("往下滑动")
        self.d.swipe_ext("down", scale=scale)

    def scroll_down_fast(self):
        """快速往下滑动"""
        logger.info("快速往下滑动")
        self.d(scrollable=True).fling()

    def scroll_down_slow(self, step=50):
        """
        通过step控制滑动速度
        @param step:
        @return:
        """
        logger.info("慢速往下滑动")
        self.d(scrollable=True).scroll(steps=step)

    def scroll_up_fast(self):
        """快速往上滑动"""
        logger.info("快速往上滑动")
        self.d(scrollable=True).fling.vert.backward()

    def scroll_up_slow(self, step=50):
        """
        通过step控制滑动速度
        @param step:
        @return:
        """
        logger.info("慢速往下滑动")
        self.d(scrollable=True).scroll.vert.backward(steps=step)

    def scroll_bottom_fast(self):
        """快速滑到底部"""
        logger.info("快速滑到底部")
        self.d(scrollable=True).fling.toEnd()

    def scroll_bottom_slow(self, step=50):
        """
        通过step控制滑动速度
        @param step:
        @return:
        """
        logger.info("慢速滑到底部")
        self.d(scrollable=True).scroll.toEnd(steps=step)

    def scroll_top_fast(self):
        """快速滑动到顶部"""
        logger.info("快速滑到顶部")
        self.d(scrollable=True).fling.toBeginning()

    def scroll_top_slow(self, step=50):
        """
        通过step控制滑动速度
        @param step:
        @return:
        """
        logger.info("慢速滑到顶部")
        self.d(scrollable=True).scroll.toBeginning(steps=step)

    def scroll_to_element(self, *args, **kwargs):
        """滑动到元素"""
        logger.info(f"滑动到元素: {kwargs}")
        self.d(scrollable=True).scroll.to(*args, **kwargs)

    def drag_xy(self, sx, sy, ex, ey):
        """拖动"""
        logger.info(f"从坐标{sx},{sy} 拖动到坐标{ex},{ey}")
        self.d.drag(sx, sy, ex, ey)

    def set_password(self, text, clear=True):
        """输入密码"""
        logger.info(f"输入: {text}")
        self.d.set_fastinput_ime(True)
        if clear:
            self.d.clear_text()
        self.d(focused=True).set_text(text)
        self.d.set_fastinput_ime(False)

    def set_ori_left(self):
        """屏幕向右边转动"""
        logger.info("屏幕向右边转动")
        self.d.set_orientation("l")

    def set_ori_right(self):
        """屏幕向左边转动"""
        logger.info("屏幕向左边转动")
        self.d.set_orientation("r")

    def set_ori_natural(self):
        """屏幕恢复原始转向"""
        logger.info("屏幕恢复原始转向")
        self.d.set_orientation("n")

    def start_record(self, file_name="output"):
        """开始录制"""
        logger.info("开始录制")
        img_dir = os.path.join(os.getcwd(), "images")
        if os.path.exists(img_dir) is False:
            os.mkdir(img_dir)
        time_str = time.strftime("%m%d%H%M%S")
        file_path = os.path.join(img_dir, f"{file_name}-{time_str}.mp4")
        self.d.screenrecord(file_path)

    def stop_record(self):
        """停止录制"""
        logger.info("停止录屏")
        self.d.screenrecord.stop()
