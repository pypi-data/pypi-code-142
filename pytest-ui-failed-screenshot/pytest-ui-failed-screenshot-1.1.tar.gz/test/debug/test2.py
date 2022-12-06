# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   pytest-failed-screenshot
# FileName:     test2.py
# Author:      Jakiro
# Datetime:    2022/11/15 16:36
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------

import time
from selenium import webdriver

driver = None
def _capture_screenshot():
    '''
    :return:
    '''
    print('cap:',type(driver))
    return driver.get_screenshot_as_base64()

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
print('test_1:', type(driver))
time.sleep(3)
assert '百度' in driver.title
