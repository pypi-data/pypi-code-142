from setuptools import setup, find_packages

setup(name='server_chat_pyct_December',
      version='0.2',
      description='Server packet',
      packages=find_packages(),
      author_email='sk-west@bk.ru',
      author='Kubanych Zholdoshov',
      install_requeres=['PyQt5', 'sqlalchemy','pycruptodome', 'pycryptodomex']
      )