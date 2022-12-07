"""
给setuptools提供的信息(名称, 脚本)
打包: python -m pip install --upgrade setuptools wheel
"""

import setuptools

with open("README.md", mode="r", encoding="utf8") as f:
    long_description = f.read()


setuptools.setup(
    name="xfpip",
    version="1.0",
    author="LunFengChen",
    author_email="1622246366@qq.com",
    description="一个用于学习制作开源pip的包",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LunFengChen/xfpip",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "pillow"
    ],
    python_requires=">=3",
)
