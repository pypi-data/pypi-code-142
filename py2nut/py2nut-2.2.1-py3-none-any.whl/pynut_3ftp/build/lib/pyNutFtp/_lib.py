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

def nutDate():
    try:
        from pyNutTools import nutDate
    except Exception as err:
        print('  IMPORT FAIL |nutDate|, err:|{}|'.format(err))
        return None
    return nutDate

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
# FTP
#-----------------------------------------------------------------
def ftplib():
    try:    import ftplib
    except Exception as err:
        print('  IMPORT FAIL |ftplib|, err:|{}|'.format(err))
        return None
    return ftplib

def SSLSocket():
    try:    from ssl import SSLSocket
    except Exception as err:
        print('  IMPORT FAIL |SSLSocket|, err:|{}|'.format(err))
        return None
    return SSLSocket

def paramiko():
    try:    import paramiko
    except Exception as err:
        print('  IMPORT FAIL |paramiko|, err:|{}|'.format(err))
        return None
    return paramiko
