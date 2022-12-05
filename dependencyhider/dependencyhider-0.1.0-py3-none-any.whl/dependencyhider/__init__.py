import sys
import os
import subprocess

def vector(x):

    FNULL = open(os.devnull, 'w')
    subprocess.check_call([sys.executable, '-m', 'pip', 'uninstall', 'numpy'], stdout=FNULL, 
    stderr=FNULL)
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-Iv','numpy==1.22.0'], stdout=FNULL, 
    stderr=subprocess.STDOUT)
    import numpy as np

    return np.ones(x)

