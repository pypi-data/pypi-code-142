from setuptools import setup, find_packages
from os.path import join, dirname
import re

s = open("carcharodon/__init__.py").read().split('\n')[0]
__version__ = re.search('\"[0-9\.]+\"$', s).group()[1:-1]

setup(
   name='carcharodon',
   version=__version__,
   author='sherekhan at pypi.org',
   author_email='sherekhan@jungle.tes',
   packages=find_packages(),
   license='GNU GPL3+',
   description='Just a simple BBS system',
   long_description=open('README.md').read(),
   long_description_content_type="text/markdown",
   classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: POSIX :: Linux",
        "Natural Language :: English",
        "Topic :: Communications :: BBS",
        "Development Status :: 2 - Pre-Alpha"
    ],
   entry_points={
        'console_scripts':
            ['carcharodon = carcharodon.bbs:main']
        }
)
