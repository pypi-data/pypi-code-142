from distutils.core import setup
from setuptools import find_packages

with open("C:/Users/admin/Desktop/IdnsBotCh/README.rst", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(name='IdnsBotCh',  # 包名
      version='1.1.4',  # 版本号
      description='一套基于selenium谷歌驱动的idns机器人框架',
      long_description=long_description,
      author='mikezhou_talk',
      author_email='1678594309@qq.com',
      install_requires=[],
      license='BSD License',
      packages=find_packages(),
      platforms=["all"],
      classifiers=[
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
