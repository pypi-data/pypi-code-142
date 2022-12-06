# coding=utf-8
"""
作者：vissy@zhu
"""
from setuptools import setup, find_packages
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
setup(
    name="lyh_ui_autotest",
    version="0.0.1",
    author="vissyzhu",
    author_email="1209354095@qq.com",
    description="lyh ui autoTest",
    url="https://github.com/vissyzhu/lyhui.git",
    license='MIT',
    packages=find_packages(),
    # zip_safe=False
)
