from setuptools import setup, find_packages

setup(
    name='foxhelpers',
    version='1.1.5',
    packages=find_packages(exclude=["venv", "dist"]),
    url='',
    license='',
    author='jizong',
    author_email='jizong.peng.ca@gmail.com',
    description='metrics for decoupled training',
    install_requires=["loguru", "termcolor", "pandas", "numpy", "omegaconf", "prettytable", "torch", "ipdb"],
    python_requires='>3.6.0'
)
