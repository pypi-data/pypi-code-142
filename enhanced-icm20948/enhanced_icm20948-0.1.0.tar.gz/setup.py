import sys
from glob import glob
from pybind11 import get_cmake_dir
from pybind11.setup_helpers import Pybind11Extension, build_ext
from pybind11.setup_helpers import ParallelCompile, naive_recompile
from setuptools import setup
from pathlib import Path


__version__ = '0.1.0'

ext_modules = [
    Pybind11Extension(
        "enhanced_icm20948.asm_sensors",
        sorted(glob("enhanced_icm20948/asm_sensors/*.cpp")),
        extra_compile_args = ["-O3", "-lmraa"],
        libraries = ["mraa"],
    )
]

ParallelCompile("NPY_NUM_BUILD_JOBS", needs_recompile=naive_recompile).install()
thisDirectory = Path(__file__).parent
longDescription = (thisDirectory / "README.md").read_text()

setup(
    name = "enhanced_icm20948",
    version = __version__,
    author = "Haoyuan Ma, Chenhao Zhang",
    author_email = "flyinghorse0510@zju.edu.cn, 2019021412017@std.uestc.edu.cn",
    license = "MIT",
    url = "http://gogs.infcompute.com/mhy/enhanced_icm20948.git",
    description = "An ultra-fast and powerful ICM20948 sensor reading library",
    long_description = longDescription,
    long_description_content_type='text/markdown',
    ext_modules = ext_modules,
    cmdclass = {"build_ext": build_ext},
    zip_safe = False,
    python_requires = ">=3.7",
    packages = ["enhanced_icm20948", "enhanced_icm20948.asm_sensors", "enhanced_icm20948.asm_sensors.sensors"],
    install_requires = [
        'numpy',
    ],
    include_package_data=True
)