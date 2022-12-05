#-----------------------------------------------------------------
# pynut
#-----------------------------------------------------------------
def nutOther():
    try:
        from pyNutTools import nutOther
    except Exception as err:
        print('  IMPORT FAIL |nutOther|, err:|{}|'.format(err))
        return None
    return nutOther

def nutFiles():
    try:
        from pyNutFiles import nutFiles
    except Exception as err:
        print('  IMPORT FAIL |nutFiles|, err:|{}|'.format(err))
        return None
    return nutFiles


#-----------------------------------------------------------------
# Generic Lib
#-----------------------------------------------------------------
def logging():
    try:    import logging
    except Exception as err:
        print('  IMPORT FAIL |logging|, err:|{}|'.format(err))
        return None
    return logging

def logger():
    try:
        import logging
        logger = logging.getLogger()
    except Exception as err:
        print('  IMPORT FAIL |logger|, err:|{}|'.format(err))
        return None
    return logger


#-----------------------------------------------------------------
# dataframe
#-----------------------------------------------------------------
def numpy():
    try:    import numpy
    except Exception as err:
        print('  IMPORT FAIL |numpy|, err:|{}|'.format(err))
        return None
    return numpy

def pandas():
    try:    import pandas
    except Exception as err:
        print('  IMPORT FAIL |pandas|, err:|{}|'.format(err))
        return None
    return pandas


#-----------------------------------------------------------------
# DB
#-----------------------------------------------------------------
def pyodbc():
    try:    import pyodbc
    except Exception as err:
        print('  IMPORT FAIL |pyodbc|, err:|{}|'.format(err))
        return None
    return pyodbc

def sqlite3():
    try:    import sqlite3
    except Exception as err:
        print('  IMPORT FAIL |sqlite3|, err:|{}|'.format(err))
        return None
    return sqlite3

# def sqlalchemy():
#     try:    import sqlalchemy
#     except Exception as err:
#         print('  IMPORT FAIL |sqlalchemy|, err:|{}|'.format(err))
#         return None
#     return sqlalchemy

