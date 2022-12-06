# coding=utf-8
"""
作者：vissy@zhu

"""
import copy
import os
import time
import unittest
from tkinter.font import Font

from commonlib.userFunction import UserFunction
from testdata.common import common_data
from testdata.common import result_data
import xlrd
from xlutils import copy
import xlwt
import openpyxl


class CaseFunction(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(CaseFunction, self).__init__(*args)
        red_style = "font:colour_index red;"
        green_style = "font:colour_index green;"
        self.FailFont = xlwt.easyxf(red_style)
        self.PassFont = xlwt.easyxf(green_style)
        self.path = common_data['chromedriver']
        self.url = common_data['url']
        self.model = common_data['model']

    # 获取用例步骤并执行
    def executeCase(self, path):
        UserFunction.driver(self, self.path, self.url, self.model)
        tableopen = xlrd.open_workbook('./testcase/' + path)
        table = tableopen.sheet_by_name('Sheet1')
        h = table.nrows
        for i in range(1, h):
            step = table.row(i)[1].value
            method = table.row(i)[2].value
            value = table.row(i)[3].value
            index = table.row(i)[4].value
            key = table.row(i)[5].value
            if step == '' or step == ' ':
                continue
            if not index:
                index = 0
            try:
                datetime = time.strftime('%Y/%m/%d %H:%M:%S', time.localtime(time.time()))
                CaseFunction.writeResult(self, path, i, 7, value=datetime)
                if step == 'activate':
                    UserFunction.activate(self, method, value, int(index))
                elif step == 'move':
                    UserFunction.move(self, method, value, int(index))
                elif step == 'enterTextIn':
                    UserFunction.enterTextIn(self, method, value, key, int(index))
                elif step == 'sleep':
                    if not value:
                        value = 1;
                    UserFunction.sleep(self, value)
                elif step == 'close':
                    UserFunction.close(self)
                elif 'assert' in step:
                    UserFunction.verify(self, step, method, value, key, int(index))
                elif step == 'getToken':
                    UserFunction.getToken(self, value)
                elif step == 'setToken':
                    UserFunction.setToken(self, self.url)
                elif step == 'getLocalStorage':
                    UserFunction.getLocalStorage(self, value)
                elif step == 'setLocalStorage':
                    UserFunction.setLocalStorage(self, self.url, value)
                elif step == 'getCooike':
                    UserFunction.getCooike(self, value)
                elif step == 'setCooike':
                    UserFunction.setCooike(self, self.url, value)
                elif step == 'getToken':
                    UserFunction.getToken(self, value)
                elif step == "refresh":
                    UserFunction.refresh(self)
                elif step == 'quit':
                    UserFunction.quit(self)
                elif step == 'defaultFrame':
                    UserFunction.defaultFrame()
                elif step == 'switchFrame':
                    UserFunction.switchFrame(self, method, value, int(index))
                elif step == 'scorll':
                    UserFunction.scorll(self, method, value, int(index))
                elif step == 'isElementExist':
                    UserFunction.isElementExist(self, method, value, int(index))
                elif step == 'clear':
                    UserFunction.clear(self, method, value, int(index))
                elif step == 'getTitle':
                    UserFunction.getTitle(self, value)
                elif step is None:
                    continue
                CaseFunction.writeResult(self, path, i, 6, value="Pass")

            except Exception:
                CaseFunction.writeResult(self, path, i, 6, value="Fail")
                CaseFunction.writeResult(self, path, i, 8, common_data["picname"])
                CaseFunction.writeResult(self.path, i, 9, value="")
                UserFunction.quit(self)
                raise
                break

    # 通过source.xls获取执行的用例xls名
    def getCasePath(self, path):
        # realpath = os.getcwd()
        tableopen = xlrd.open_workbook(path)
        table = tableopen.sheet_by_name('Sheet1')
        h = table.nrows
        CaseFunction.clearResult(self, path.split('testcase/')[1], 1)
        CaseFunction.clearResult(self, path.split('testcase/')[1], 2)
        for i in range(1, h):
            caseName = table.row(i)[0].value
            common_data['case_name'] = caseName.split('.xls')[0]
            try:
                CaseFunction.clearResult(self, caseName, 6)
                CaseFunction.clearResult(self, caseName, 7)
                CaseFunction.clearResult(self, caseName, 8)
                datetime = time.strftime('%Y/%m/%d %H:%M:%S', time.localtime(time.time()))
                result_data["starttime"] = datetime
                CaseFunction.writeResult(self, path.split('testcase/')[1], i, 2, value=datetime)
                CaseFunction.executeCase(self, caseName)
                CaseFunction.writeResult(self, path.split('testcase/')[1], i, 1, value="Pass")
            except Exception:
                CaseFunction.writeResult(self, path.split('testcase/')[1], i, 1, value="Fail")
        datetime = time.strftime('%Y/%m/%d %H:%M:%S', time.localtime(time.time()))
        result_data["endtime"] = datetime
        CaseFunction.result(self, path)

    # source.xls和用例每一步写入执行结果
    def writeResult(self, path, i, j, value):
        tableopen = xlrd.open_workbook('./testcase/' + path)
        new_file = copy.copy(tableopen)
        sheet = new_file.get_sheet(0)
        sheet.write(i, j, value)
        new_file.save('./testcase/' + path)

    # 每次执行前，清空source.xls和每个用例里的执行结果
    def clearResult(self, path, i):
        tableopen = xlrd.open_workbook('./testcase/' + path)
        new_file = copy.copy(tableopen)
        sheet = new_file.get_sheet(0)
        for n in range(1, 1000):
            sheet.write(n, i, "")
        new_file.save('./testcase/' + path)

    # 测试报告内容
    def result(self, path):
        tableopen = xlrd.open_workbook(path)
        table = tableopen.sheet_by_name('Sheet1')
        h = table.nrows
        pass_num = fail_num = 0
        for i in range(1, h):
            if table.row(i)[1].value == "Pass":
                pass_num = pass_num + 1
            else:
                fail_num = fail_num + 1
        result_data["total_num"] = h - 1
        result_data["fail_num"] = fail_num
        result_data["pass_num"] = pass_num

    def test(self):
        CaseFunction.result(self, './testcase/source.xls')
