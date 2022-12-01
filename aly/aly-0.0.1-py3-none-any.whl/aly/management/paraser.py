from argparse import ArgumentParser
import os


class Paraser:

    def __init__(self):
        self.parser = ArgumentParser(description = f"\x1b[1;34mdescription: aly is a tool to build telegram bots in an easy way\x1b[1;37m\n")
       

    def err(self,error):
        print("\x1b[1;33m")
        self.parser.print_usage()
        print(f"\x1b[1;31m \n{error} \n \x1b[1;32m")
        print("for more help use [-h] or [--help]")
        print("\x1b[1;37m")

    def print_help(self):
        print("\x1b[1;33m")
        self.parser.print_help()

    def run(self):
        try:
            os.system("flask run")
        except ImportError:
            os.system("pip install flask")
            os.system("flask run")
