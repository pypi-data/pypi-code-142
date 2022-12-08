import setuptools

with open("README.md", "r",encoding='UTF-8') as fh:
  long_description = fh.read()

setuptools.setup(
  name="WZCMCCAPPLOGGER",
  version="0.0.6",
  author="YHQ",
  author_email="228899059@qq.com",
  description="LOG",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/pypa/sampleproject",
  packages=setuptools.find_packages(),
  classifiers=[
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: MIT License",
  "Operating System :: OS Independent",
  ],
)
#python setup.py sdist bdist_wheel
#https://zhuanlan.zhihu.com/p/60836179
#python setup.py sdist upload
#https://www.cnblogs.com/danhuai/p/14915042.html
# 4.1、可以先升级打包工具
#pip install --upgrade setuptools wheel twine

# 4.2、打包
#python setup.py sdist bdist_wheel

# 4.3、可以先检查一下包
#twine check dist/*

# 4.4、上传包到pypi（需输入用户名、密码）
#twine upload dist/*
#twine upload dist/* --verbose