from setuptools import setup, find_packages

setup(name="baskort_server_messenger",
      version="1.0.0",
      description="messenger_server",
      author="MadEngine",
      author_email="scorpio-84@mail.ru",
      packages=find_packages(),
      install_requires=['PyQt6', 'sqlalchemy']
      )
