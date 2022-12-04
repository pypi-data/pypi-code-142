from setuptools import setup, find_packages

setup(name="mess_server_redkin",
      version="0.0.1",
      description="Messenger Server",
      author="Ivan Redkin",
      author_email="stazhor@bk.ru",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex'],
      )
