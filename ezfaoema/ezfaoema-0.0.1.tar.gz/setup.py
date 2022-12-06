from setuptools import setup, find_packages
setup(
name="ezfaoema",  #项目名称
version="0.0.1", #版本号
author="ZhangHaiJun", #作者
author_email="2215664237@qq.com", #邮箱
description="This is a built-in method for python sorting",  #介绍
# 项目主页
url="https://blog.csdn.net/sdsdvsdvs?spm=1000.2115.3001.5343",
# 你要安装的包，通过 setuptools.find_packages 找到当前目录下有哪些包
    install_requires=[],  #项目依赖哪些库，这些库会在pip install的时候自动安装
    license='BSD License',
    packages=find_packages(),
    platforms=["all"],  #指定最终发布的包中要包含的packages。
    classifiers=[ #其他信息，一般包括项目支持的Python版本，License，支持的操作系统。
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Natural Language :: Chinese (Simplified)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries'
    ],
)


