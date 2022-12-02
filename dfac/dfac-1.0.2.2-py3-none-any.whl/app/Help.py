import sys

class Help:
    def noValue(self):
        print("Usage: 'main.py --help' for more information")
        sys.exit()
    
    def printHelp(self):
        hfile=open("app/help.txt",'r')
        x=hfile.read()
        print(x)
        sys.exit()