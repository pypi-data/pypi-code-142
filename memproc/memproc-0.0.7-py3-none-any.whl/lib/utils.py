import subprocess
import sys

import pkg_resources


def update_memproc():
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-U', 'memproc'])


def get_memproc_version():
    return pkg_resources.get_distribution('memproc').version


def convert_mem(mem_in_bytes: int, to_unit: str):
    MEM_FACTOR = {'B': 1, 'KB': 2**10, 'MB': 2**20, 'GB': 2**30}

    mem_factor = MEM_FACTOR[to_unit]
    return mem_in_bytes / mem_factor
