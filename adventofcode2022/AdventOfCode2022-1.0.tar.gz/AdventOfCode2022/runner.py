"""
This file contains code for the runner of Advent of Code 2022 challenge codes.
Author: GlobalCreativeApkDev
"""


import os


def main():
    """
    The main function used to run Advent of Code 2022 challenge codes.
    :return: None
    """

    for i in range(1, len(os.listdir())):
        for k in ["a", "b"]:
            os.system("python3 day" + str(i) + "/day" + str(i) + str(k) + ".py")


if __name__ == '__main__':
    main()
