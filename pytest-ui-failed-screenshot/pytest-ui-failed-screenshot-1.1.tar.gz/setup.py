# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   pytest-failed-screenshot
# FileName:     setup.py
# Author:      Jakiro
# Datetime:    2022/11/15 16:11
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------

from setuptools import setup, find_packages

setup(
    name='pytest-ui-failed-screenshot',
    author='Jakilo',
    version='1.1',
    url='https://github.com/Jakilo1996/PytestUIFailedScreenshot',
    python_requires='>=3',
    description='UI自动测试失败时自动截图，并将截图加入到测试报告中',
    classifiers=['Framework :: Pytest'],
    py_modules=['pytest_failed_screenshot'],  # 需要包含插件函数所在的文件内容
    packages=find_packages(),
    install_requires=['pytest'],
    entry_points={
        # pytest11为官方定义的固定入口点，用于发现插件
        'pytest11': [
            'pytest-ui-failed-screenshot = pytest_failed_screenshot',
        ],
    },
)

