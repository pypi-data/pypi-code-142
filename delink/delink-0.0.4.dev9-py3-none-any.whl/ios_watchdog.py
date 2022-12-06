"""
通过监听文件变化来追加设备链接操作
"""
import json
import os

import logger
import psutil
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

from delink.ios_client import IOSDeviceManage, IOSDevice

im = IOSDeviceManage()


def connect_ios_device(udid, host, port):
    """
    写入新链接的设备信息
    """
    # 如果有主服务正在运行，则无需启动监听，只需要写入数据即可
    if not is_running():
        logger.logger.info("启动服务成功")
        # 启动链接设备的服务
        im.start()
        im.add_device(IOSDevice(udid, host, port))
        im.connect_devices()
        # 监听后续需要链接的设备
        watchdog()
        return
    pidPath = get_ios_watch_file_path()
    with open(pidPath, "w") as ios_udid:
        ios_udid.write(json.dumps({
            "udid": udid,
            "host": host,
            "port": port,
            "type": "connect"
        }))


def disconnect_ios_device(udid):
    """
    移除链接的设备
    """
    watchPath = get_ios_watch_file_path()
    with open(watchPath, "w") as ios_udid:
        ios_udid.write(json.dumps({
            "udid": udid,
            "host": None,
            "port": None,
            "type": "disconnect"
        }))


def stop():
    if is_running():
        watchPath = get_ios_watch_file_path()
        with open(watchPath, "w") as ios_udid:
            ios_udid.write(json.dumps({
                "udid": 'stop',
                "host": None,
                "port": None,
                "type": "stop"
            }))
    else:
        logger.logger.info("即将退出服务...")
        IOSDeviceManage().disconnect_devices()


def watchdog():
    """
    监听文件内容变化情况
    """
    # 生成事件处理器对象
    event_handler = DelinkEventHandler()

    # 生成监控器对象
    observer = Observer()
    # 注册事件处理器，配置监控目录
    watch_file = get_ios_watch_file_path()
    logger.logger.info("监听文件:{}".format(watch_file))
    logger.logger.info("监听文件是否存在:{}".format(os.path.exists(watch_file)))
    observer.schedule(event_handler, watch_file, recursive=True)
    # 监控器启动——创建线程
    observer.start()
    # 写入pid
    write_pid()
    # 阻塞服务
    observer.join()


def read_ios_device():
    """
    读取需要链接的设备信息
    """
    watch_file = get_ios_watch_file_path()
    if not os.path.exists(watch_file):
        return None
    with open(watch_file, "r") as ios_udid:
        return json.loads(ios_udid.read())


def get_ios_watch_file_path():
    """
    获取监听文件地址
    """
    root_path = get_root_path()
    watch_file_dir = os.path.join(root_path, "ios", "watchdog")
    watch_file_path = os.path.join(watch_file_dir, "device_list.txt")
    if os.path.exists(watch_file_dir):
        return watch_file_path
    os.makedirs(watch_file_dir)
    return watch_file_path


def get_root_path():
    """
    文件根目录，用于存储辅助运行的文件
    """
    return os.path.abspath(os.path.dirname(__file__))


class DelinkEventHandler(FileSystemEventHandler):
    """Logs all the events captured."""

    def __init__(self):
        super().__init__()

    def on_moved(self, event):
        super().on_moved(event)

    def on_created(self, event):
        super().on_created(event)

    def on_deleted(self, event):
        super().on_deleted(event)

    def on_modified(self, event):
        super().on_modified(event)
        device = read_ios_device()
        if not device:
            return
        connect_type = device["type"]
        udid = device['udid']
        logger.logger.info('准备{}设备{}'.format(connect_type, udid))
        if connect_type == "connect":
            try:
                im.add_device(IOSDevice(udid, device['host'], device['port']))
            except Exception as ex:
                logger.logger.error("链接设备异常", ex)
        elif connect_type == "disconnect":
            im.remove_device_by_udid(udid)
        elif connect_type == 'stop':
            pid = read_pid()
            if not pid:
                return
            im.disconnect_devices()
            logger.logger.info("即将退出服务...")
            psutil.Process(int(pid)).kill()
        else:
            logger.logger.warn("无法处理设备链接类型:{}".format(connect_type))
        logger.logger.info('完成{}设备{}'.format(connect_type, udid))


def get_write_pid_file():
    """
    获取存储pid的文件
    """
    root_path = get_root_path()
    pid_file_dir = os.path.join(root_path, "client")
    pid_file_path = os.path.join(pid_file_dir, "pid.txt")
    if not os.path.exists(pid_file_dir):
        os.makedirs(pid_file_dir)
    return pid_file_path


def write_pid():
    """
    将当前服务pid写入
    """
    pid = os.getpid()
    logger.logger.info("当前服务的Pid:{}".format(pid))
    with open(get_write_pid_file(), 'w') as pid_file:
        pid_file.write(str(pid))


def read_pid():
    """
    获取服务pid，以判断是否有正在运行的服务，如果有则只需要通知运行的服务链接设备即可
    """
    if not os.path.exists(get_write_pid_file()):
        return None
    with open(get_write_pid_file(), 'r') as pid_file:
        return pid_file.read()


def is_running():
    pid = read_pid()
    if not pid:
        return False
    try:
        curr_pr = psutil.Process(int(pid))
        return curr_pr.is_running()
    except:
        return False


if __name__ == "__main__":
    watchdog()
