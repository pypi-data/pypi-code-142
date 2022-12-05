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

def win32():
    try:    import win32com.client as win32
    except Exception as err:
        print('  IMPORT FAIL |win32|, err:|{}|'.format(err))
        return None
    return win32

def pythoncom():
    try:    import pythoncom
    except Exception as err:
        print('  IMPORT FAIL |pythoncom|, err:|{}|'.format(err))
        return None
    return pythoncom


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
# EMAIL
#-----------------------------------------------------------------
def Credentials():
    try:    from exchangelib import Credentials
    except Exception as err:
        print('  IMPORT FAIL |Credentials|, err:|{}|'.format(err))
        return None
    return Credentials

def Account():
    try:    from exchangelib import Account
    except Exception as err:
        print('  IMPORT FAIL |Account|, err:|{}|'.format(err))
        return None
    return Account

def Configuration():
    try:    from exchangelib import Configuration
    except Exception as err:
        print('  IMPORT FAIL |Configuration|, err:|{}|'.format(err))
        return None
    return Configuration

def DELEGATE():
    try:    from exchangelib import DELEGATE
    except Exception as err:
        print('  IMPORT FAIL |DELEGATE|, err:|{}|'.format(err))
        return None
    return DELEGATE

def FileAttachment():
    try:    from exchangelib import FileAttachment
    except Exception as err:
        print('  IMPORT FAIL |FileAttachment|, err:|{}|'.format(err))
        return None
    return FileAttachment

def EWSTimeZone():
    try:    from exchangelib import EWSTimeZone
    except Exception as err:
        print('  IMPORT FAIL |EWSTimeZone|, err:|{}|'.format(err))
        return None
    return EWSTimeZone

def EWSDateTime():
    try:    from exchangelib import EWSDateTime
    except Exception as err:
        print('  IMPORT FAIL |EWSDateTime|, err:|{}|'.format(err))
        return None
    return EWSDateTime
