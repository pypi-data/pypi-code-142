#  为打包做准备的设置文件

from setuptools import setup # 导入setuptools打包工具

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="XiYun",  # 用自己的名替换其中的YOUR_USERNAME_
    version="0.0.1",  # 包版本号，便于维护版本
    author="凉笙",  # 作者，可以写自己的姓名
    author_email="author@example.com",  # 作者联系方式，可写自己的邮箱地址
    description="GUI项目",  # 包的简述
    long_description=long_description,  # 包的详细介绍，一般在README.md文件内
    long_description_content_type="text/markdown",
    url="https://github.com/BigDataFounder/XiYun",  # 自己项目地址，比如github的项目地址
    packages=['XiYun'],
    python_requires='>=3.9',  # 对python的最低版本要求
)