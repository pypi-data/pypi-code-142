import os

from qrunner.utils.exceptions import DeviceNotFoundException


def get_device_list():
    """获取当前连接的手机列表"""
    cmd = 'adb devices'
    output = os.popen(cmd).read()
    device_list = [item.split('\t')[0] for item in output.split('\n') if item.endswith('device')]
    if len(device_list) > 0:
        return device_list
    else:
        raise DeviceNotFoundException(msg=f"无已连接设备")


def get_current_device():
    """连接一个手机时，返回设备id"""
    device_list = get_device_list()
    return device_list[0]


