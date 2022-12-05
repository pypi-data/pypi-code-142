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

def nutDataframe():
    try:
        from pyNutTools import nutDataframe
    except Exception as err:
        print('  IMPORT FAIL |nutDataframe|, err:|{}|'.format(err))
        return None
    return nutDataframe

def nutDate():
    try:
        from pyNutTools import nutDate
    except Exception as err:
        print('  IMPORT FAIL |nutDate|, err:|{}|'.format(err))
        return None
    return nutDate


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
def pandas():
    try:    import pandas
    except Exception as err:
        print('  IMPORT FAIL |pandas|, err:|{}|'.format(err))
        return None
    return pandas


#-----------------------------------------------------------------
# Files
#-----------------------------------------------------------------
def shutil():
    try:    import shutil
    except Exception as err:
        print('  IMPORT FAIL |shutil|, err:|{}|'.format(err))
        return None
    return shutil

def psutil():
    try:    import psutil
    except Exception as err:
        print('  IMPORT FAIL |psutil|, err:|{}|'.format(err))
        return None
    return psutil

def glob():
    try:    import glob
    except Exception as err:
        print('  IMPORT FAIL |glob|, err:|{}|'.format(err))
        return None
    return glob

def csv():
    try:    import csv
    except Exception as err:
        print('  IMPORT FAIL |csv|, err:|{}|'.format(err))
        return None
    return csv

def copy():
    try:    import copy
    except Exception as err:
        print('  IMPORT FAIL |copy|, err:|{}|'.format(err))
        return None
    return copy

def pythoncom():
    try:    import pythoncom
    except Exception as err:
        print('  IMPORT FAIL |pythoncom|, err:|{}|'.format(err))
        return None
    return pythoncom

def win32():
    try:    import win32com.client as win32
    except Exception as err:
        print('  IMPORT FAIL |win32|, err:|{}|'.format(err))
        return None
    return win32

def ZipFile():
    try:    from zipfile import ZipFile
    except Exception as err:
        print('  IMPORT FAIL |ZipFile|, err:|{}|'.format(err))
        return None
    return ZipFile

def xlwings():
    try:    import xlwings
    except Exception as err:
        print('  IMPORT FAIL |xlwings|, err:|{}|'.format(err))
        return None
    return xlwings

def xlsxwriter():
    try:    import xlsxwriter
    except Exception as err:
        print('  IMPORT FAIL |xlsxwriter|, err:|{}|'.format(err))
        return None
    return xlsxwriter

def xlrd():
    try:    import xlrd
    except Exception as err:
        print('  IMPORT FAIL |xlrd|, err:|{}|'.format(err))
        return None
    return xlrd

def openpyxl():
    try:    import openpyxl
    except Exception as err:
        print('  IMPORT FAIL |openpyxl|, err:|{}|'.format(err))
        return None
    return openpyxl

def openpyxl_styles():
    try:    import openpyxl.styles as openpyxl_styles
    except Exception as err:
        print('  IMPORT FAIL |openpyxl_styles|, err:|{}|'.format(err))
        return None
    return openpyxl_styles

def openpyxl_Excel():
    try:    import openpyxl.reader.excel as openpyxl_Excel
    except Exception as err:
        print('  IMPORT FAIL |openpyxl_Excel|, err:|{}|'.format(err))
        return None
    return openpyxl_Excel

def PageSetupProperties():
    try:    from openpyxl.worksheet.properties import PageSetupProperties
    except Exception as err:
        print('  IMPORT FAIL |PageSetupProperties|, err:|{}|'.format(err))
        return None
    return PageSetupProperties

def NamedStyle():
    try:    from openpyxl.styles import NamedStyle
    except Exception as err:
        print('  IMPORT FAIL |NamedStyle|, err:|{}|'.format(err))
        return None
    return NamedStyle

def Font():
    try:    from openpyxl.styles import Font
    except Exception as err:
        print('  IMPORT FAIL |Font|, err:|{}|'.format(err))
        return None
    return Font

def PatternFill():
    try:    from openpyxl.styles import PatternFill
    except Exception as err:
        print('  IMPORT FAIL |PatternFill|, err:|{}|'.format(err))
        return None
    return PatternFill

def colors():
    try:    from openpyxl.styles import colors
    except Exception as err:
        print('  IMPORT FAIL |colors|, err:|{}|'.format(err))
        return None
    return colors

def Border():
    try:    from openpyxl.styles import Border
    except Exception as err:
        print('  IMPORT FAIL |Border|, err:|{}|'.format(err))
        return None
    return Border

def Side():
    try:    from openpyxl.styles import Side    # , Alignment, Color
    except Exception as err:
        print('  IMPORT FAIL |Side|, err:|{}|'.format(err))
        return None
    return Side
