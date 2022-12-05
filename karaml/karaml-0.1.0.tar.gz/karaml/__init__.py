
#print("Running __init__.py in karaml package")
print("Welcome to the KARaML Tools package (version 0.1.00)")
import os
HOST_DIR = os.getcwd() 
if not os.path.exists('KARaML_Tools'):
  os.mkdir('KARaML_Tools')
import gdown
gdown.download(url="https://colab.research.google.com/drive/14iuvYqoCWdUS_Adf3t1fBNS8tpOj-09Z", 
               output='KARaML_Tools/karaml_setup.py',
               quiet=True)
os.chdir('KARaML_Tools')
import karaml_setup
os.chdir(HOST_DIR)

#print("Import everything from karaml_tools.py")
#from .karaml_tools import *
