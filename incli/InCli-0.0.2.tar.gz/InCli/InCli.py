if __name__ == '__main__' and __package__ == '':
    import os, sys, importlib
    parent_dir = os.path.abspath(os.path.dirname(__file__))
    sys.path.append(os.path.dirname(parent_dir))
    __package__ = os.path.basename(parent_dir)
    importlib.import_module(__package__)

from SFAPI import restClient
import sys  

def main():
    print('We are in main')
    restClient.init()

if __name__ == '__main__':
    main()
