# coding=utf-8
"""
vissy@zhu
截图方法，先在用例所在目录，新建一个当天日期的文件夹，用于存放当天的截图。
所以，截图之前要先判断，当天日期的文件夹存不存在，如果已经有了，那就跳过，直接截图，没有的话，先新建再截图。
默认需要截图screenshot=True，所以调用的时候不用传
使用方法举例：
需要截图
realpath = os.path.realpath(__file__)
picname = newdir.NewDirectory().newdir(realpath)
self.wxDriver.d.screenshot(picname)
不需要截图只新建文件夹
NewDirectory.newdir(screenshot=False)
"""

import os
import time


class NewDirectory:

    def newdir(self, realpath, needscreenshot=True):
        date = time.strftime('%Y%m%d', time.localtime(time.time()))
        datetime = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        dirPath = os.getcwd()
        dirPath = dirPath.split("commonlib")[0] + "//TestResult"
        newPath = (dirPath + "//%s" % date)
        if not os.path.exists(newPath):
            os.makedirs(newPath)
        else:
            pass
        # 截图文件命名方式：当前用例名称+当前日期，所以这个方法需要传realpath，文件的真实名称。
        if needscreenshot:
            # filename = realpath.split('testcase/')[1].split('.xls')[0]
            picname = os.path.join(newPath, realpath + "_%s.png" % datetime)
            return picname
        else:
            pass
