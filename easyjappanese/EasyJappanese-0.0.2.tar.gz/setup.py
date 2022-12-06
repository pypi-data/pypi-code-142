from setuptools import setup
import easyjapanese

DESCRIPTION = 'copy of easyjapanese, edited for cloud.'
NAME = easyjapanese.__name__
AUTHOR = easyjapanese.__author__
AUTHOR_EMAIL = easyjapanese.__author_email__
URL = easyjapanese.__url__
VERSION = easyjapanese.__version__
PYTHON_REQUIRES = ">=3.6"
INSTALL_REQUIRES = [
    'google-cloud-storage>=2.6.0',
    'beautifulsoup4>=4.11.1',
    'selenium>=4.7.2',
    'pandas>=1.5.2',
    'numpy>=1.23.5'
]
LONG_DESCRIPTION = 'copy of easyjapanese, edited for cloud'

setup(name=NAME,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      maintainer=AUTHOR,
      maintainer_email=AUTHOR_EMAIL,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      url=URL,
      version=VERSION,
      python_requires=PYTHON_REQUIRES,
      install_requires=INSTALL_REQUIRES,
    )