from setuptools import setup

setup(name = "aoc_test",
      version = "0.2",
      description = "Test your Advent of Code solutions",
      author='Balan Artiom',
      license='MIT',
      packages=['src/aoc_test'],
      url='https://github.com/shunlog/aoc-test',
      scripts=['src/aoc_test/aoct'],
      zip_safe=False)
