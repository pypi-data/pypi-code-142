from setuptools import setup
import easyjapanese

description = 'Web scraping tool for NHK web news easy'
NAME = 'easyjapanese'
AUTHOR = 'Yuki Cossy'
AUTHOR_EMAIL = 'domokomod5@gmail.com'
URL = 'https://github.com/yuki-cossy/EasyJapanese'
LICENSE = 'MIT'
DOWNLOAD_URL = 'https://github.com/yuki-cossy/EasyJapanese'
VERSION = easyjapanese.__version__
PYTHON_REQUIRES = ">=3.6"
INSTALL_REQUIRES = ['tqdm', 'pandas', 'selenium', 'beautifulsoup4']
PACKAGES = ['easyjapanese']

# I don't know why but it didn't work out in the way I wanted.
with open('README4PyPI.md', 'r') as desc:
    long_description = desc.read()


setup(name=NAME,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      maintainer=AUTHOR,
      maintainer_email=AUTHOR_EMAIL,
      description=description,
      long_description=long_description,
      license=LICENSE,
      url=URL,
      version=VERSION,
      download_url=DOWNLOAD_URL,
      python_requires=PYTHON_REQUIRES,
      install_requires=INSTALL_REQUIRES,
      packages=PACKAGES,
    )