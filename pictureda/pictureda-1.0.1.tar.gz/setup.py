
import setuptools
import os

# 这是一个和根目录相关的安装文件的列表，列表中setup.py更具体)

files = ["things/*"]

setuptools.setup(
      name='pictureda',
      version='1.0.1',
      keywords='picture',
      description='picture',
      long_description=open(
            os.path.join(
                  os.path.dirname(__file__),
                  'README.rst'
            )
      ).read(),
      author='Dada.cod',
      author_email='626987961@qq.com',
      packages=setuptools.find_namespace_packages(),
      license='MIT'
)
