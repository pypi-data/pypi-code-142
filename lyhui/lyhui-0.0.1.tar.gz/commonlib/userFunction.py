# coding=utf-8
"""
作者：vissy@zhu

"""
from distutils.log import Log
from telnetlib import EC
from seleniumwire import webdriver

import xlutils.copy
import os
from selenium.webdriver import ActionChains

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep, time
import unittest
import requests
import xlwt
import xlrd
import logging

from commonlib import newdir
from testdata.common import common_data
from seleniumwire import webdriver


class UserFunction(unittest.TestCase):
    def __init__(self):
        self.logger = Log().getLogger()

    def driver(self, chromedriver, url, model, token_name=None, token_data=None):
        if model == 'pc':
            self.dr = webdriver.Chrome(executable_path="/Applications/Google Chrome.app/chromedriver")
            self.dr.maximize_window()
        else:
            mobile_emulation = {"deviceName": "iPhone X"}
            options = Options()
            options.add_experimental_option("mobileEmulation", mobile_emulation)
            self.dr = webdriver.Chrome(options=options, executable_path=chromedriver)
            self.dr.maximize_window()
        self.dr.implicitly_wait(10)
        self.dr.get(url)

    # 点击
    def activate(self, method, value, index=0):
        sleep(1)
        try:
            self.dr.find_elements(method, value)[index].click()
        except Exception:
            UserFunction.screenshot(self, common_data["case_name"])
            raise

    # 鼠标悬停
    def move(self, method, value, index=0):
        sleep(1)
        try:
            menu = self.dr.find_elements(method, value)[index]
            mouse = ActionChains(self.dr)
            mouse.move_to_element(menu).perform()
        except Exception:
            UserFunction.screenshot(self, common_data["case_name"])
            raise

    # 输入
    def enterTextIn(self, method, value, key, index=0):
        sleep(1)
        if type(key) is float:
            key = int(key)
        try:
            UserFunction.activate(self, method, value, index)
            self.dr.find_elements(method, value)[index].send_keys(key)
        except Exception:
            UserFunction.screenshot(self, common_data["case_name"])
            raise

    # 获取参数值
    def getTextFrom(self, method, value, index=0):
        sleep(1)
        try:
            text = self.dr.find_elements(method, value)[index].text
            return text
        except Exception:
            UserFunction.screenshot(self, common_data["case_name"])
            raise

    # 判断返回值和预期结果
    def verify(self, step, method, value, key, index=0):
        sleep(1)
        try:
            text = UserFunction.getTextFrom(self, method, value, index)
            if step == 'assertIn':
                self.assertIn(key, text)
            elif step == 'assertEqual':
                self.assertEquals(key, text)
            elif step == 'assertLessEqual':
                self.assertLessEqual(int(key), int(text))
            elif step == 'assertNotEqual':
                self.assertNotEqual(key, text)
            elif step == 'assertNotIn':
                self.assertNotIn(key, text)
        except Exception:
            UserFunction.screenshot(self, common_data["case_name"])
            raise

    # 刷新页面
    def refresh(self):
        self.dr.refresh()

    # 判断元素存在
    def isElementExist(self, method, value, index=0):
        sleep(1)
        try:
            self.dr.find_elements(method, value)[index]
        except Exception:
            UserFunction.screenshot(self, common_data["case_name"])
            raise

    # 判断元素不存在，比如loading属性是否存在，如果不存在，则加载完成，可以执行下一步
    def isElementNotExist(self, method, value, index=0):
        sleep(1)
        try:
            self.dr.find_elements(method, value)[index]
        except Exception:
            UserFunction.screenshot(self, common_data["case_name"])
            raise

    def clear(self, method, value, index=0):
        sleep(1)
        try:
            self.dr.find_elements(method, value)[index].clear()
        except Exception:
            raise

    # 滚动页面，注意需要选择大于当前屏幕尺寸的元素属性（现在使用的iphone X(500*812px)），否则无效，用浏览器模拟手机尺寸来确定页面可显示的全部元素。
    # 比如屏幕长812px，选择一个元素大于812px位置的元素，如果想翻页，则直接选择移动到1600px位置的元素，因为移动是页面底部移动到目标元素位置
    def scorll(self, method, value, index=0):
        # size = self.dr.get_window_size()
        set_ele = self.dr.find_elements(method, value)[index]
        action = ActionChains(self.dr)
        action.move_to_element(set_ele)
        action.perform()
        sleep(1)

    # 强制等待
    def sleep(self, sec):
        sleep(sec)

    # 关闭标签页
    def close(self):
        self.dr.close()

    # 退出浏览器
    def quit(self):
        self.dr.quit()

    def screenshot(self, value):
        picname = newdir.NewDirectory().newdir(value)
        common_data['picname'] = picname.split("TestResult/")[1]
        self.dr.save_screenshot(picname)

    # 获取localStorage里的用户信息，用法：UserFunction.getLocalStorage(self,"DMP,TIM_1400495465_mdou52_profile")
    def getLocalStorage(self, value):
        sleep(1)
        localStorage_name = value.split(',')
        for i in range(0, len(localStorage_name)):
            localStorage_data = self.dr.execute_script('return localStorage.getItem("%s");' % localStorage_name[i])
            realpath = os.getcwd().split("testcase")[0]
            tableopen = xlrd.open_workbook(realpath + '/testdata/get_cookie_token_localStorage.xls')
            new_file = xlutils.copy.copy(tableopen)
            sheet = new_file.get_sheet(0)
            sheet.write(i + 1, 0, "%s" % localStorage_name[i])
            sheet.write(i + 1, 1, "%s" % localStorage_data)
            new_file.save('./testdata/get_cookie_token_localStorage.xls')

    # 设置localStorage，先打开浏览器，然后设置，最后重新打开连接
    def setLocalStorage(self, url, value):
        sleep(1)
        localStorage_name = value.split(',')
        for i in range(0, len(localStorage_name)):
            tableopen = xlrd.open_workbook('./testdata/get_cookie_token_localStorage.xls')
            table = tableopen.sheet_by_name('Sheet1')
            localStorage_name = table.row(i)[0].value
            localStorage_data = table.row(i)[1].value
            if localStorage_name and localStorage_data:
                js = '''window.localStorage.setItem("%s",'%s')''' % (localStorage_name, localStorage_data)
                self.dr.execute_script(js)
        self.dr.get(url)

    # 获取请求头里的token值，target_url代表目标url，通过目标url，获取其请求头中token_name的token值，
    # 用法：UserFunction.getToken(self, "https://edu.liangyihui.net/learn_rank/user?type=month&sourceFrom=home","X-CSRF-Token")
    def getToken(self, value):
        self.dr.refresh()
        data = value.split(',')
        for i in range(0, len(data)):
            if 'http' in data[i]:
                target_url = data[i]
            else:
                token_name = data[i]
        for j in range(0, len(self.dr.requests)):
            if self.dr.requests[j].url == target_url:
                token_data = dict(self.dr.requests[j].headers)[token_name]
                break
        realpath = os.getcwd().split("testcase")[0]
        tableopen = xlrd.open_workbook(realpath + '/testdata/get_cookie_token_localStorage.xls')
        new_file = xlutils.copy.copy(tableopen)
        sheet = new_file.get_sheet(0)
        sheet.write(1, 2, "%s" % token_name)
        sheet.write(1, 3, "%s" % token_data)
        new_file.save('./testdata/get_cookie_token_localStorage.xls')

    # 设置token，暂未找到使用token系统，无法调试
    def setToken(self, url, *args):
        tableopen = xlrd.open_workbook('./testdata/get_cookie_token_localStorage.xls')
        table = tableopen.sheet_by_name('Sheet1')
        cookie_name = table.row(0)[2].value
        cookie_data = table.row(0)[3].value
        self.dr.get(url)

    # 获取cookie值，用法：UserFunction.getCooike(self, "REMEMBERME", "PHPSESSID", "online-uuid")
    def getCooike(self, value):
        cookie_name = value.split(',')
        for i in range(0, len(cookie_name)):
            cooike_data = self.dr.get_cookie(cookie_name[i])['value']
            realpath = os.getcwd().split("testcase")[0]
            tableopen = xlrd.open_workbook(realpath + '/testdata/get_cookie_token_localStorage.xls')
            new_file = xlutils.copy.copy(tableopen)
            sheet = new_file.get_sheet(0)
            sheet.write(i + 1, 4, "%s" % cookie_name[i])
            sheet.write(i + 1, 5, "%s" % cooike_data)
            new_file.save('./testdata/get_cookie_token_localStorage.xls')

    # 设置cookie，用法：UserFunction.setCooike(self, self.url, "REMEMBERME", "PHPSESSID", "online-uuid")，最后重新打开目标页面
    def setCooike(self, url, value):
        cookie_name = value.split(',')
        for i in range(0, len(cookie_name)):
            tableopen = xlrd.open_workbook('./testdata/get_cookie_token_localStorage.xls')
            table = tableopen.sheet_by_name('Sheet1')
            cookie_name = table.row(i)[4].value
            cookie_data = table.row(i)[5].value
            self.dr.add_cookie({'name': '%s' % cookie_name, 'value': '%s' % cookie_data})
        self.dr.get(url)


# 默认frame窗口
def defaultFrame(self):
    sleep(1)
    self.dr.switch_to().defaultContent()


# 切到某个frame
def switchFrame(self, method, value, index=0):
    sleep(1)
    if (index == 99):
        self.dr.switch_to().frame(self.dr.find_elements(method, value)[index])
    else:
        self.dr.switch_to().frame(index)


# 获取页面title，并判断和预期结果是否一致
def getTitle(self, value):
    sleep(1)
    title = self.dr.title
    try:
        if title == value:
            pass
    except Exception:
        UserFunction.screenshot(self, common_data["case_name"])
        raise


if __name__ == '__main__':
    UserFunction().driver(common_data['chromedriver'], common_data['url'])
