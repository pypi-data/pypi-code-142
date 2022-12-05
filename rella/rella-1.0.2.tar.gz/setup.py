from setuptools import setup

setup(
  name="rella",
  version="1.0.2",
  description="A simple Python package for tracking events with Rella",
  url="https://github.com/rella/python-sdk",
  author="Harry Lucas",
  author_email="harry@rella.so",
  license="MIT",
  packages=["."],
  install_requires=["requests"],
  zip_safe=False,
)
