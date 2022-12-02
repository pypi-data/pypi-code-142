""" Program in order to create a 'top' command implemented in Python. """

# needed imports
import time
import sys
import platform

# needed cross platform files
from ostop.mac import mactop
from ostop.windows import windowstop
from ostop.linux import linuxtop


def main():

    operatingSys = platform.system()
    if operatingSys == "Darwin":
        os = compile("mactop()", "mac", "eval")
    elif operatingSys == "Windows":
        os = compile("windowstop()", "windows", "eval")
    elif operatingSys == "Linux":
        os = compile("linuxtop()", "linux", "eval")

    try:
        if len(sys.argv) == 1:
            # if they want to run it iteratively
            while True:
                eval(os)
                time.sleep(0.90)
        else:
            iterations = int(sys.argv[1])
            # run for the amount of times entered
            for i in range(iterations):
                eval(os)
                time.sleep(1)

    except KeyboardInterrupt:
        sys.exit(0)


if __name__ == "__main__":
    main()
