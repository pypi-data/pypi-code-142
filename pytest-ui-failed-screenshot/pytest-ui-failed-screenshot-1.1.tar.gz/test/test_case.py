# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   pytest-failed-screenshot
# FileName:     test_case.py
# Author:      Jakiro
# Datetime:    2022/11/15 16:20
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------
import time,pytest

def test_1(browser):
    '''
    断言成功
    :param browser:
    :return:
    '''
    print('in test')
    driver = browser
    driver.get('https://www.baidu.com')
    print('test_1:',type(driver))
    time.sleep(3)
    assert '百度' in driver.title


def test_2(browser):
    '''
    断言失败
    :param browser:
    :return:
    '''
    print('in test')
    driver = browser
    driver.get('https://www.baidu.com')
    print('test_1:',type(driver))
    time.sleep(3)
    assert '百度' == driver.title


def test_3(browser):
    '''
    无条件跳过
    :param browser:
    :return:
    '''
    pytest.skip(msg='no reason')
    print('in test')
    driver = browser
    driver.get('https://www.baidu.com')
    print('test_1:',type(driver))
    time.sleep(3)
    assert '百度' == driver.title
