from aly.management.builder import Builder
from aly.management.paraser import Paraser
from settings import *
import sys,os

{project_name} = Builder("{project_name}")

def main():
    paraser = Paraser()
    paraser.parser.add_argument("newbot",help="add new bot")
    paraser.parser.add_argument("setwebhook",help="Set webhook to connect bot with telegram")
    paraser.parser.add_argument("run",help="Run the project")

    path = os.path.dirname(os.path.realpath(__file__))

    if len(sys.argv) != 1:
        if sys.argv[1] == "-h" or sys.argv[1] == "--help":
            paraser.print_help()
        elif sys.argv[1] == "newbot":
            {project_name}.new_bot(BOTS,TOKENS,path)
        elif sys.argv[1] == "setwebhook":
            {project_name}.set_webhook(BOTS)
        
        elif sys.argv[1] == "run":
            if os.getcwd() == path:
                paraser.run()
            else:
                print("\x1b[1;31m\nError: Make sure you are in the project directory to run the project\x1b[1;37m")
        
        else:
            paraser.err(f"Error: No such command "+sys.argv[1])
    else:
        paraser.print_help()
    

if __name__ == '__main__':
    main()