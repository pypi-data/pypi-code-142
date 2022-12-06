# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   pytest-failed-screenshot
# FileName:     pytest_failed_screenshot.py
# Author:      Jakiro
# Datetime:    2022/11/15 16:11
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------

import time

from selenium import webdriver
import pytest
from py._xmlgen import html

driver = None


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    :param item:
    """
    #
    pytest_html = item.config.pluginmanager.getplugin('html')
    # 获取yeild的结果，后续文章会讲解整个过程
    outcome = yield
    # 获取用例的执行结果
    report = outcome.get_result()

    # 获取用例报告的扩展信息
    extra = getattr(report, 'extra', [])

    # 当步骤为测试调用和setup过程
    if report.when == 'call' or report.when == "setup":
        # 获得当前是否跳过
        xfail = hasattr(report, 'wasxfail')
        # 判断当前的状态是失败 还是跳过，由于xfail的用例是失败状态，
        if (report.skipped and xfail) or (report.failed and not xfail):
            # 将截图文件命名为用例节点id
            file_name = report.nodeid.replace("::", "_") + ".png"
            # 调用截图方法
            screen_img = _capture_screenshot()
            if file_name:
                html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:600px;height:300px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % screen_img
                # 在用例描述部分新增截图
                extra.append(pytest_html.extras.html(html))
        # 新增一个字段附加的测试报告内容
        report.extra = extra
    # 为报告新增一个字段,将测试函数描述的第一行写入报告
    if item.function.__doc__:
        report.description = str(item.function.__doc__.split('\n')[1])


@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    # 加入一个表头
    cells.insert(1, html.th('description'))


@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    # 加入数据
    cells.insert(1, html.td(report.description))


def _capture_screenshot():
    '''
    :return:
    '''
    # 调用截图操作
    return driver.get_screenshot_as_base64()


@pytest.fixture(scope='session', autouse=True)
def browser(request):
    '''
    返回一个webdriver对象，此方法，实例过浏览器对象后，后续所有的测试调用，都会使用同一个浏览器对象
    :param request:
    :return:
    '''
    global driver
    # 需要处理新实例化浏览器 还是用旧的浏览器
    if driver is None:
        driver = webdriver.Chrome()

    def end():
        print('浏览器退出')
        driver.quit()
        time.sleep(1)
        print('driver quit')

    request.addfinalizer(end)
    return driver
