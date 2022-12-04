from setuptools import setup, find_packages

setup(name="MadEngine_server_mess",
      version="1.0.0",
      description="mess_server",
      author="MadEngine",
      author_email="scorpio-84@mail.ru",
      packages=find_packages(),
      install_requires=['PyQt6', 'sqlalchemy']
      )
