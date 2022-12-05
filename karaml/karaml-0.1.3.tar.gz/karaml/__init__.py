
#print("Running __init__.py in karaml package")
print("Welcome to the KARaML Tools package (version 0.1.3)")
import os
HOST_DIR = os.getcwd() 
if not os.path.exists('KARaML_Tools'):
  os.mkdir('KARaML_Tools')

import subprocess
subprocess.run(['pip', 'install', '--upgrade', 'gdown'])  
import gdown
gdown.download(id="1TjmLUBzDJg32A3YvI85PctAcSi4xsKVa", 
               output='KARaML_Tools/karaml_setup.py',
               quiet=True)
os.chdir('KARaML_Tools')
import karaml_setup
os.chdir(HOST_DIR)

#print("Import everything from karaml_tools.py")
#from .karaml_tools import *
