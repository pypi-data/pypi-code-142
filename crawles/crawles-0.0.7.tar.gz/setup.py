import setuptools  # 导入setuptools打包工具

with open(r"F:\please_package\README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="crawles",  # 用自己的名替换其中的YOUR_USERNAME_
    version="0.0.7",  # 包版本号，便于维护版本
    author="苯环",  # 作者，可以写自己的姓名
    author_email="1431705288@qq.com",  # 作者联系方式，可写自己的邮箱地址
    description="一个爬虫简化包",  # 包的简述
    long_description=long_description,  # 包的详细介绍，一般在README.md文件内
    long_description_content_type="text/markdown",
    url="https://github.com/kuangjianke",  # 自己项目地址，比如github的项目地址
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # 对python的最低版本要求
)
'''
[pypi]
  username = 1431705288qq.com a13641481495
  password = pypi-AgEIcHlwaS5vcmcCJDdhYWM3NDMyLThkYWEtNDY0OS1iY2M2LTNjYzI5NzJmZWU2YwACKlszLCI0NTZkZmQwMS0xZjBmLTRlOTYtYTY4OC1mNWQxMDk4MmUzMzEiXQAABiCYVSdynyMl6EabvcdWdBtqNiMkpd5I3NR8rmd78i40oA


'''
# python F:\please_package\setup.py sdist bdist_wheel
# python -m twine upload dist/*
# 1431705288qq.com
# a13641481495
