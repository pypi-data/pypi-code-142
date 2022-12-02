from setuptools import setup, find_packages
from simple_proxy import __version__, __author__
import pathlib

WORK_DIR = pathlib.Path(__file__).parent

try:
    from pip.req import parse_requirements
except ImportError:  # pip >= 10.0.0
    from pip._internal.req import parse_requirements
    
with open('README.md') as readme_file:
    README = readme_file.read()
    
def install_requires():
    file = WORK_DIR / "requirements.txt"
    print(file)
    install_reqs = parse_requirements(str(file), session=False)
    try:
        requirements = [str(ir.req) for ir in install_reqs]
    except:
        requirements = [str(ir.requirement) for ir in install_reqs]
    return requirements
setup(
	name='CustomProxy',
	version=__version__,
	long_description=README,
	long_description_content_type="text/markdown",
	description='Just simple random proxy rotating package',
	author=__author__,
	packages=find_packages(),
	url="https://github.com/dyseo/custom-proxy",
	download_url="https://github.com/dyseo/custom-proxy",
	license='MIT',
	install_requires=install_requires(),
	extras_require={
		'ujson': ['ujson']
	},
	classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ]
)