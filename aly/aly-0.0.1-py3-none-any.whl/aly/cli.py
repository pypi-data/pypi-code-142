import os,sys
from aly.management.builder import *
from aly.management.paraser import *



def main():
    paraser = Paraser()
    paraser.parser.add_argument("build [project name]",help="build the project")
    paraser.parser.add_argument("run",help="run the telegram bot and flask website")

    if len(sys.argv) != 1:
        if sys.argv[1] == "-h" or sys.argv[1] == "--help":
            paraser.print_help()
        elif sys.argv[1] == "build":
            if len(sys.argv) == 3:
                project = Builder.build_project(sys.argv[2])
            elif len(sys.argv) == 2:
                paraser.err("Error: You have to specify project name 'build [project name]'")
            else:
                paraser.err("Error: You added more than one argument 'build [project name]'")

        elif sys.argv[1] == "run":
            paraser.run()
        else:
            paraser.err(f"Error: No such command '{sys.argv[1]}'")
    else:
        paraser.print_help()
    

if __name__ == '__main__':
    main()