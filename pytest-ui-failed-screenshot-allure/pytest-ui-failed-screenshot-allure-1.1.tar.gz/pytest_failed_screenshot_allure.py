# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   pytest_failed_screenshot_allure
# FileName:     pytest_failed_screenshot_allure.py
# Author:      Jakiro
# Datetime:    2022/12/6 13:24
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------


import time

from selenium import webdriver
import pytest
import allure

driver = None


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    # 获取yeild的结果
    outcome = yield
    # 获取用例的执行结果
    report = outcome.get_result()
    # 获取测试步骤为测试调用和setup过程
    if report.when == 'call' or report.when == "setup":
        # 判断是否是xfail
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            # 通过attach向allure测试报告中添加截图
            with allure.step('添加失败截图'):
                allure.attach(_capture_screenshot(), '失败截图', allure.attachment_type.PNG)


def _capture_screenshot():
    return driver.get_screenshot_as_png()


@pytest.fixture(scope='session', autouse=True)
def browser(request):
    global driver
    if driver is None:
        driver = webdriver.Chrome()

    def end():
        print('浏览器退出')
        driver.quit()

    request.addfinalizer(end)
    return driver
