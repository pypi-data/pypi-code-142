import sys
import os
PYTHON_PATH = sys.executable
file_path = os.getcwd() + '\server.py'
os.system(f'{PYTHON_PATH} {file_path}')