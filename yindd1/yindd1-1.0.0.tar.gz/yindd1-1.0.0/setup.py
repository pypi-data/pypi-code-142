
import setuptools
import os

# 这是一个和根目录相关的安装文件的列表，列表中setup.py更具体)

files = ["waimai/*"]

setuptools.setup(
      name='yindd1',
      version='1.0.0',
      keywords='jwt_f',
      description='jwt',
      long_description=open(
            os.path.join(
                  os.path.dirname(__file__),
                  'README.md'
            )
      ).read(),
      author='Dada.cod',
      author_email='1078515202@qq.com',
      packages=setuptools.find_packages(),
      license='MIT'
)
