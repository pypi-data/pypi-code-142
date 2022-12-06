# coding: utf-8

import re
import os
import sys
import platform
import subprocess
import multiprocessing
from os.path import exists
from math import floor
from setuptools import setup, Extension, find_packages
from setuptools.command.build_ext import build_ext
from distutils.version import LooseVersion


def num_available_cpu_cores(ram_per_build_process_in_gb):
    if 'TRAVIS' in os.environ and os.environ['TRAVIS'] == 'true':
        # When building on travis-ci, just use 2 cores since travis-ci limits
        # you to that regardless of what the hardware might suggest.
        return 2
    try:
        mem_bytes = os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES')
        mem_gib = mem_bytes/(1024.**3)
        num_cores = multiprocessing.cpu_count()
        # make sure we have enough ram for each build process.
        mem_cores = int(floor(mem_gib/float(ram_per_build_process_in_gb)+0.5))
        # We are limited either by RAM or CPU cores.  So pick the limiting amount
        # and return that.
        return max(min(num_cores, mem_cores), 1)
    except ValueError:
        # just assume 2 if we can't get the os to tell us the right answer.
        return 2


class CMakeExtension(Extension):
    def __init__(self, name, sourcedir=''):
        Extension.__init__(self, name, sources=[])
        self.sourcedir = os.path.abspath(sourcedir)


class CMakeBuild(build_ext):

    def get_cmake_version(self):
        try:
            out = subprocess.check_output(['cmake', '--version'])
        except:
            sys.stderr.write(
                "\nERROR: CMake must be installed to build vame\n\n")
            sys.exit(1)
        return re.search(r'version\s*([\d.]+)', out.decode()).group(1)

    def run(self):
        cmake_version = self.get_cmake_version()
        if platform.system() == "Windows":
            if LooseVersion(cmake_version) < '3.1.0':
                sys.stderr.write(
                    "\nERROR: CMake >= 3.1.0 is required on Windows\n\n")
                sys.exit(1)

        for ext in self.extensions:
            self.build_extension(ext)

    def build_extension(self, ext):
        extdir = os.path.abspath(os.path.dirname(
            self.get_ext_fullpath(ext.name)))

        cmake_args = ['-DCMAKE_LIBRARY_OUTPUT_DIRECTORY=' + extdir,
                      '-DPYTHON_EXECUTABLE=' + sys.executable]

        cfg = 'Debug' if self.debug else 'Release'
        build_args = ['--config', cfg]

        if platform.system() == "Windows":
            cmake_args += [
                '-DCMAKE_LIBRARY_OUTPUT_DIRECTORY_{}={}'.format(cfg.upper(), extdir)]
            if sys.maxsize > 2**32:
                cmake_args += ['-A', 'x64']
            # Do a parallel build
            build_args += ['--', '/m']
        else:
            cmake_args += ['-DCMAKE_BUILD_TYPE=' + cfg]
            # Do a parallel build
            build_args += ['--', '-j'+str(num_available_cpu_cores(2))]

        build_folder = os.path.abspath(self.build_temp)

        if not os.path.exists(build_folder):
            os.makedirs(build_folder)

        cmake_setup = ['cmake', ext.sourcedir] + cmake_args
        cmake_build = ['cmake', '--build', '.'] + build_args

        print("Building extension for Python {}".format(
            sys.version.split('\n', 1)[0]))
        print("Invoking CMake setup: '{}'".format(' '.join(cmake_setup)))
        sys.stdout.flush()
        subprocess.check_call(cmake_setup, cwd=build_folder)
        print("Invoking CMake build: '{}'".format(' '.join(cmake_build)))
        sys.stdout.flush()
        subprocess.check_call(cmake_build, cwd=build_folder)

from setuptools.command.test import test as TestCommand
class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to pytest")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = 'vame/python/test vacm/python/test vacl/python/test vace/python/test vaml/python/test'

    def run_tests(self):
        import shlex
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(shlex.split(self.pytest_args))
        sys.exit(errno)

def set_name():
    if os.getenv('VAST_AI_VIDEO'):
        return 'vaststream-all'
    
    elif os.getenv('VAST_AI'):
        return 'vaststream-ai'
    
    elif os.getenv('VAST_VIDEO'):
        return 'vaststream-video'
    else:
        raise("error ")

def set_packages():
    packages = ["vaststream", "vaststream.vacm", "vaststream.vace", "vaststream.vaml"]
    if os.getenv('VAST_AI_VIDEO'):
        packages.append("vaststream.vame")
        packages.append("vaststream.vacl")
        return packages
    
    elif os.getenv('VAST_AI'):
        packages.append("vaststream.vacl")
        return packages
    
    elif os.getenv('VAST_VIDEO'):
        packages.append("vaststream.vame")
        return packages    
    else:
        raise("error ")

def set_package_dir():
    package_dir={
        "vaststream": "python/vaststream",
        "vaststream.vacm": "vacm/python/vacm",
        "vaststream.vace": "vace/python/vace",
        "vaststream.vaml": "vaml/python/vaml"
    }    

    if os.getenv('VAST_AI_VIDEO'):
        package_dir["vaststream.vame"] = "vame/python/vame"
        package_dir["vaststream.vacl"] = "vacl/python/vacl"
        return package_dir
    
    elif os.getenv('VAST_AI'):
        package_dir["vaststream.vacl"] = "vacl/python/vacl"
        return package_dir
    
    elif os.getenv('VAST_VIDEO'):
        package_dir["vaststream.vame"] = "vame/python/vame"
        return package_dir    
    else:
        raise("error ")

def gen_packages_items(require_fpath: str):
    if not exists(require_fpath):
        print("warning:requirement not install.")
    items = []
    with open(require_fpath) as f:
        for line in f.readlines():
            line = line.strip()
            if line and not line.startswith('#'):
                items.append(line)
    return items
install_requires = gen_packages_items('./requirements.txt')
setup(
    # 包名
    # name="vaststream",
    name=set_name(),
    # TODO: 版本号，从CMakeLists中解析
    version="1.0.0",
    description="The Vastai SDK",
    long_description="",
    author="Vastai Team",
    # author_email="",
    # license="",
    # 自定义构建模块
    ext_modules=[CMakeExtension('_vaststream_pybind11', 'python')],
    cmdclass=dict(build_ext=CMakeBuild, test=PyTest),
    zip_safe=False,
    tests_require=['pytest'],
    # 指定python包以及路径
    # packages=find_packages(where="python"),
    # packages=["vaststream", "vaststream.vacm", "vaststream.vame", "vaststream.vacl", "vaststream.vace", "vaststream.vaml"],
    packages=set_packages(),
    install_requires=install_requires,
    
    # package_dir={
    #     "vaststream": "python/vaststream",
    #     "vaststream.vacm": "vacm/python/vacm",
    #     "vaststream.vame": "vame/python/vame",
    #     "vaststream.vacl": "vacl/python/vacl",
    #     "vaststream.vace": "vace/python/vace",
    #     "vaststream.vaml": "vaml/python/vaml"
    # },
    package_dir=set_package_dir(),
    # classifiers=[]
    python_requires=">=3",
)
