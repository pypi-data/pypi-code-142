from setuptools import setup, find_packages

setup(name='client_chat_pyct_December',
      version='0.1',
      description='Client packet',
      packages=find_packages(),
      author_email='sk-west@bk.ru',
      author='Kubanych Zholdoshov',
      install_requeres=['PyQt5', 'sqlalchemy','pycruptodome', 'pycryptodomex']
      )