'''
Data Factory Entry Point

Input data from shell


'''
import sys
from dfac.app.Help import Help
from dfac.app.Shell import Shell

if __name__ == '__main__':
    sysinput =sys.argv[1:]

    if len(sysinput) == 0:
        Help().noValue()

    if len(sysinput) > 0:
        shellcall=Shell()
        shellcall.parse(sysinput)