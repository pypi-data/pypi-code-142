"""run the command line interface if module is run"""
import sys

import logdensity.runner

if __name__ == '__main__':
    sys.exit(logdensity.runner.run())
