import subprocess
import sys

import pkg_resources


def update_memproc():
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-U', 'memproc'])


def get_memproc_version():
    return pkg_resources.get_distribution('memproc').version
