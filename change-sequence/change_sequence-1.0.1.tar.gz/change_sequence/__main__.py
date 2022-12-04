"""default docstring"""
import argparse
import doctest
from time import sleep
import pytest
import change_seq
from change_seq import conv, conv_

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--test", dest="test_mode", action="store_true")
parser.add_argument("-d", "--doctest", dest="doctest_mode", action="store_true")
parser.add_argument("value", nargs="?", default=False)
parser.add_argument("-s", "--stretch", dest="conv_mode", action="store_true")

args = parser.parse_args()
HELP_TEXT = """
Convert string script

Usage:
    change_sequence [some_string]
    change_sequence -t [--test]
    change_sequence -d [--doctest]
    change_sequence -s [--stretch]

"""


def main():
    """
    startup function for running a change_sequence as a script
    """
    if args.test_mode:
        retcode = pytest.main(["-v"])
        print(retcode)
        exit()
    elif args.doctest_mode:
        doctest.testmod(m=change_seq, verbose=True)
        exit()
    elif args.value is False:
        print(HELP_TEXT)
    else:
        some_string = None
        try:
            some_string = str(args.value)
        except IndexError:
            print("You need to pass in a some string to conver its")
            print(HELP_TEXT)
            exit()

        print("Converting...")
        sleep(1)

        if args.conv_mode:
            print(conv_(some_string))
        else:
            print(conv(some_string))

        print("Done!")


if __name__ == "__main__":
    main()
