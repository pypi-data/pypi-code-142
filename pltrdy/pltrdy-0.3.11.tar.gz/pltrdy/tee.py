# tee.py
# Purpose: A Python class with a write() method which, when
# used instead of print() or sys.stdout.write(), for writing
# output, will cause output to go to both sys.stdout and
# the filename passed to the class's constructor. The output
# file is called the teefile in the below comments and code.

# The idea is to do something roughly like the Unix tee command,
# but from within Python code, using this class in your program.

# The teefile will be overwritten if it exists.

# The class also has a writeln() method which is a convenience
# method that adds a newline at the end of each string it writes,
# so that the user does not have to.

# Python's string formatting language is supported (without any
# effort needed in this class), since Python's strings support it,
# not the print method.

# Author: Vasudev Ram
# Web site: https://vasudevram.github.io
# Blog: https://jugad2.blogspot.com
# Product store: https://gumroad.com/vasudevram

from __future__ import print_function
import sys


class Tee(object):
    RAISE = "raise"
    EXIT = "exit"

    def __init__(
        self,
        tee_fil=None,
        tee_filename=None,
        stdout=None,
        behavior=RAISE,
        auto_flush=True,
    ):
        if stdout is not None:
            self.stdout = stdout
        else:
            self.stdout = sys.stdout
        self.auto_flush = auto_flush

        self.behavior = behavior.lower()
        assert self.behavior in [
            Tee.RAISE,
            Tee.EXIT,
        ]
        if tee_fil is not None:
            self.tee_fil = tee_fil
        else:
            try:
                self.tee_fil = open(tee_filename, "w")
            except IOError as ioe:
                if self.behavior == Tee.RAISE:
                    raise
                else:
                    exit("Caught IOError: {}".format(repr(ioe)))
            except Exception as e:
                if self.behavior == Tee.RAISE:
                    raise
                else:
                    exit("Caught Exception: {}".format(repr(e)))

    def write(self, s):
        self.stdout.write(s)
        self.tee_fil.write(s)
        if self.auto_flush:
            self.flush()

    def flush(self):
        self.stdout.flush()
        self.tee_fil.flush()

    def __getattr__(self, k):
        if hasattr(self.stdout, k):
            return getattr(self.stdout, k)

    @property
    def isatty(self):
        return self.stdout.isatty

    def writeln(self, s):
        self.write(s + "\n")

    def close(self):
        try:
            self.tee_fil.close()
        except IOError as ioe:
            if self.behavior == Tee.RAISE:
                raise
            else:
                exit("Caught IOError: {}".format(repr(ioe)))
        except Exception as e:
            if self.behavior == Tee.RAISE:
                raise
            else:
                exit("Caught Exception: {}".format(repr(e)))

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()


class TeeFiles:
    def __init__(self, *files):
        self.files = files

    def write(self, *args, **kwargs):
        for f in self.files:
            f.write(*args, **kwargs)
