import os
import re
import unittest
import sys
from pyutils.executor import Executor
from sys import executable
import pyutils.shorthand as sh


class TestExecutor(unittest.TestCase):

    def test_executor_execute_file(self):
        """测试 execute_file 的基本功能"""
        executor = Executor(True)
        test_root_dir = os.path.dirname(__file__)
        hello_path = os.path.join(test_root_dir, 'data/wrap blank/hello.py')
        hello_result = executor.execute_file(hello_path, wrap_blank_with_double_quotes=True)
        self.assertEqual(hello_result.out_str, "hello")

    def test_executor_wrap_blank_with_double_quotes(self):
        """测试 executor 自动包装双引号
        """
        executor = Executor(True)
        if sh.is_win() and re.search(r'\s', executable):
            result = executor.execute_straight(executable, ['--version'], ignore_error=True)
            self.assertEqual(result.code, 1)
            result = executor.execute_straight(executable, ['--version'], wrap_blank_with_double_quotes=True)
            self.assertEqual(result.out_str, f"Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")
        test_root_dir = os.path.dirname(__file__)
        hello_path = os.path.join(test_root_dir, 'data/wrap blank/hello.py')
        hello_result = executor.execute_straight(executable, [hello_path], wrap_blank_with_double_quotes=True, ignore_error=True)
        self.assertEqual(hello_result.out_str, "hello")
        result = executor.execute_by_git_bash('echo', 'wrap_blank_with_double_quotes', wrap_blank_with_double_quotes=True)
        self.assertEqual(result.out_str, 'wrap_blank_with_double_quotes')

    def test_execute_by_cmd(self):
        """测试 execute_by_cmd 能否正常工作
        """
        if sh.is_win():
            out_str = "You are not in admin mode!"
            test_bat_content = rf'''
            @echo off
            net session >nul 2>&1
            if %errorlevel% equ 0 (
                mklink /D pyutils_linked pyutils
            ) else (
                echo {out_str}
            )
            '''
            executor = Executor(True)
            result = executor.execute_by_cmd(test_bat_content, None)
            if sh.is_admin_win():
                self.assertTrue(os.path.exists('pyutils_linked'))
            else:
                self.assertTrue(result.out_str.endswith(out_str))

    def tearDown(self) -> None:
        if os.path.exists('pyutils_linked'):
            os.remove('pyutils_linked')
        return super().tearDown()
