# -*- coding: utf-8 -*-
#  日期 : 2022/11/30 11:33
#  作者 : Christmas
#  邮箱 : 273519355@qq.com
#  项目 : Project
#  版本 : python 3
#  摘要 :
"""

"""
import datetime
import numpy as np
import sys
import socket
import getpass


def convertToTime(strDate):
    """
    将 %Y%m%d 格式的8位字符串，转换为日期
    :param strDate: %Y%m%d 格式的8位日期字符串
    :return: datetime 类型的日期
    """
    date = datetime.datetime.now()  # 默认取当天日期

    try:
        if len(strDate) == 8:
            date = datetime.datetime.strptime(strDate, "%Y%m%d")
        elif len(strDate) == 10:
            date = datetime.datetime.strptime(strDate, "%Y%m%d%H")
        elif len(strDate) == 12:
            date = datetime.datetime.strptime(strDate, "%Y%m%d%H%M")
        elif len(strDate) == 14:
            date = datetime.datetime.strptime(strDate, "%Y%m%d%H%M%S")
        elif len(strDate) == 19:
            date = datetime.datetime.strptime(strDate, "%Y-%m-%d_%H:%M:%S")  # 2022-11-09_01:00:00
    except:  # 转换错误时，取默认值
        pass

    return date


def new_filename(_pre, _lon, _lat, _date, _res):
    """
    根据前缀、经纬度、日期、分辨率生成输出文件名
    :param _pre: 输出文件前缀
    :param _lon: 经度
    :param _lat: 纬度
    :param _date: 日期
    :param _res: 分辨率
    :return: 输出文件名
    """
    if np.min(_lon) < 0:
        lon_1 = str(format(abs(np.min(_lon)), '.2f')).zfill(6) + 'W'
    else:
        lon_1 = str(format(abs(np.min(_lon)), '.2f')).zfill(6) + 'E'
    if np.max(_lon) < 0:
        lon_2 = str(format(abs(np.max(_lon)), '.2f')).zfill(6) + 'W'
    else:
        lon_2 = str(format(abs(np.max(_lon)), '.2f')).zfill(6) + 'E'
    if np.min(_lat) < 0:
        lat_1 = str(format(abs(np.min(_lat)), '.2f')).zfill(5) + 'S'
    else:
        lat_1 = str(format(abs(np.min(_lat)), '.2f')).zfill(5) + 'N'
    if np.max(_lat) < 0:
        lat_2 = str(format(abs(np.max(_lat)), '.2f')).zfill(5) + 'S'
    else:
        lat_2 = str(format(abs(np.max(_lat)), '.2f')).zfill(5) + 'N'
    filename = _pre + '_' + lon_1 + '_' + lon_2 + '_' + lat_1 + '_' + lat_2 + '_' + str(_date) + '_' + str(_res) + '.nc'
    del lon_1, lon_2, lat_1, lat_2
    return filename


def get_date():
    """
    获取日期
    :return:
    """
    if len(sys.argv) == 1:
        date = datetime.datetime.now().strftime("%Y%m%d")
    elif len(sys.argv) >= 2 and len(sys.argv[1]) == 8:
        date = sys.argv[1]
    return date


def make_dir(path):
    """
    创建文件夹
    :param path: 文件夹路径
    :return:
    """
    import os
    if not os.path.exists(path):
        os.makedirs(path)


class FtpUploadTracker:
    sizeWritten = 0
    totalSize = 0
    lastShownPercent = 0

    def __init__(self, totalSize, sizeWritten):
        self.totalSize = totalSize

    def handle(self, block):
        self.sizeWritten += len(block)
        percentComplete = round((self.sizeWritten / self.totalSize) * 100)

        if self.lastShownPercent != percentComplete:
            self.lastShownPercent = percentComplete
            if percentComplete % 10 == 0:
                print(str(percentComplete) + '% complete')
            # print(str(percentComplete) +"% complete")


def get_serve_info():
    """
    获取服务器信息
    :return: 服务器信息
    """
    user = getpass.getuser()
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    return user, hostname, ip
