##############################################################################
# Copyright by The HDF Group.                                                #
# All rights reserved.                                                       #
#                                                                            #
# This file is part of HSDS (HDF5 Scalable Data Service), Libraries and      #
# Utilities.  The full HSDS copyright notice, including                      #
# terms governing use, modification, and redistribution, is contained in     #
# the file COPYING, which can be found at the root of the source code        #
# distribution tree.  If you do not have access to this file, you may        #
# request a copy from help@hdfgroup.org.                                     #
##############################################################################
#
# Simple looger for h5pyd
#

import time
import sys

# Levels copied from python logging module
DEBUG = 10
INFO = 20
WARNING = 30
ERROR = 40

req_count = {"GET": 0, "POST": 0, "PUT": 0, "DELETE": 0, "num_tasks": 0}
log_count = {"DEBUG": 0, "INFO": 0, "WARN": 0, "ERROR": 0}
# the following defaults will be adjusted by the app
config = {"log_level": DEBUG, "prefix": "", "timestamps": False, "fout": None}


def _getLevelName(level):
    if level == DEBUG:
        name = "DEBUG"
    elif level == INFO:
        name = "INFO"
    elif level == WARNING:
        name = "WARN"
    elif level == ERROR:
        name = "ERROR"
    else:
        name = "????"
    return name


def setLogConfig(level, prefix=None, timestamps=None, filepath=None):
    if level == "DEBUG":
        config["log_level"] = DEBUG
    elif level == "INFO":
        config["log_level"] = INFO
    elif level == "WARNING":
        config["log_level"] = WARNING
    elif level == "WARN":
        config["log_level"] = WARNING
    elif level == "ERROR":
        config["log_level"] = ERROR
    else:
        raise ValueError(f"unexpected log_level: {level}")
    if prefix is not None:
        config["prefix"] = prefix
    if timestamps is not None:
        config["timestamps"] = timestamps
    if filepath is not None:
        fout = open(filepath, "w")
        config["fout"] = fout
    else:
        config["fout"] = sys.stdout



def _timestamp():

    if config["timestamps"]:
        now = time.time()
        ts = f"{now:.3f} "
    else:
        ts = ""

    return ts


def _logMsg(level, msg):
    if config["log_level"] > level:
        return  # ignore

    fout = config["fout"]

    ts = _timestamp()

    prefix = config["prefix"]

    level_name = _getLevelName(level)

    fout.write(f"{prefix}{ts}{level_name}> {msg}\n")
    fout.flush()

    log_count[level_name] += 1


def debug(msg):
    _logMsg(DEBUG, msg)


def info(msg):
    _logMsg(INFO, msg)


def warn(msg):
    _logMsg(WARNING, msg)


def warning(msg):
    _logMsg(WARNING, msg)


def error(msg):
    _logMsg(ERROR, msg)
  