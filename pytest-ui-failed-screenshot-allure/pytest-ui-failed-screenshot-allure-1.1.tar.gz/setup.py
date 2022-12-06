# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   pytest_failed_screenshot_allure
# FileName:     setup.py
# Author:      Jakiro
# Datetime:    2022/12/6 13:24
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------


from setuptools import setup,find_packages

setup(
    name='pytest-ui-failed-screenshot-allure',
    author='Jakilo',
    version='1.1',
    url='https://github.com/Jakilo1996/PytestUIFailedScreenshotAllure',
    python_requires='>=3',
    description='UI自动测试失败时自动截图，并将截图加入到Allure测试报告中',
    classifiers=['Framework :: Pytest'],
    py_modules=['pytest_failed_screenshot_allure'],
    packages=find_packages(),
    install_requires=['pytest','allure-pytest==2.11.1','selenium==4.6.0'],
    entry_points={
        # pytest11为官方定义的固定入口点，用于发现插件
        'pytest11':[
            'pytest-ui-failed-screenshot-allure = pytest_failed_screenshot_allure',
        ]
    }
)