from setuptools import setup, find_packages

CLASSIFIERS = [
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
]

setup(name='tileset_analyzer',
      version='0.0.1',
      url='https://github.com/geoyogesh/tileset_analyzer',
      license='GNU-GPL',
      author='Yogesh Dhanapal',
      author_email='geoyogesh@gmail.com',
      entry_points={"console_scripts": ["tileset_analyzer = tileset_analyzer.main:cli"]},
      description='Analyze vector Tileset',
      packages=find_packages(),
      long_description=open('README.md').read(),
      long_description_content_type='text/markdown',
      zip_safe=False,
      classifiers=CLASSIFIERS,
 )
