# !/usr/bin/env python
# -*- coding: utf-8 -*-

'''
══════════════════════════════
@Time    : 2022/12/05 14:11:50
@Author  : Rey
@Contact : reyxbo@163.com
@Explain : Rey's time methods
══════════════════════════════
'''


import time
import datetime

from .rbasic import check_parm


def now(
    format: "str"="datetime"
) -> "str | int | datetime.datetime | datetime.date | datetime.time":
    """
    Get current time string or intger or object.

    Parameters
    ----------
    format : str {'datetime', 'date', 'time', 'datetime_obj', 'date_obj', 'time_obj', 'timestamp'}
        Format type.

        -'datetime' : Return string in format '%Y-%m-%d %H:%M:%S'.
        -'date' : Return string in format '%Y-%m-%d'.
        -'time' : Return string in foramt '%H:%M:%S'.
        -'datetime_obj' : Return datetime object of datetime package.
        -'date_obj' : Return date object of datetime package.
        -'time_obj' : Return time object of datetime package.
        -'timestamp' : Return time stamp of ten digit length.
    
    Returns
    -------
    str or int or datetime object or date object or time object
        Object of datetime package.
    """

    check_parm(format, "datetime", "date", "time", "datetime_obj", "date_obj", "time_obj", "timestamp")

    if format == "datetime":
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    elif format == "date":
        return datetime.datetime.now().strftime("%Y-%m-%d")
    elif format == "time":
        return datetime.datetime.now().strftime("%H:%M:%S")
    elif format == "datetime_obj":
        return datetime.datetime.now()
    elif format == "date_obj":
        return datetime.datetime.now().date()
    elif format == "time_obj":
        return datetime.datetime.now().time()
    elif format == "timestamp":
        return int(time.time())

def time_to_str(
        time_obj: "datetime.datetime | datetime.date | datetime.time | datetime.timedelta",
        format_str: "str"=None,
        throw_error: "bool"=False
    ) -> "str | object":
    """
    Format time object of datetime package as string

    Parameters
    ----------
    time_obj : datetime.datetime or datetime.date or datetime.time or datetime.timedelta
        Of datetime package.
    format_str : str or None
        Format string.

        - None : str(time_obj)
        - str : format by str.

    throw_error : bool
        Whether throw error, when parameter time_obj value error, otherwise return original value

    Returns
    -------
    str or object
        String after foramt or original value
    """

    check_parm(format_str, str, None)
    check_parm(throw_error, bool)
    if throw_error:
        check_parm(time_obj, datetime.datetime, datetime.date, datetime.time, datetime.timedelta)

    obj_type = type(time_obj)
    if obj_type == datetime.datetime:
        if format_str == None:
            string = str(time_obj)[:19]
        else:
            string = time_obj.strftime(format_str)
    elif obj_type == datetime.date:
        if format_str == None:
            string = str(time_obj)[:10]
        else:
            string = time_obj.strftime(format_str)
    elif obj_type == datetime.time:
        if format_str == None:
            string = str(time_obj)[:8]
        else:
            string = time_obj.strftime(format_str)
    elif obj_type == datetime.timedelta:
        if format_str == None:
            string = str(time_obj)
        else:
            seconds = time_obj.seconds
            time_obj = time.gmtime(seconds)
            string = time.strftime(format_str, time_obj)
    else:
        return time_obj
    return string

def str_to_time(
        string: "str",
        format_type: "str"=None,
        format_str: "str"=None,
        throw_error=False
    ) -> "datetime.datetime | datetime.date | datetime.time | datetime.timedelta | int | object":
    """
    Format string as time object of datetime package

    Parameters
    ----------
    string : str
    format_type : str {'datetime', 'date', 'time'} or None
        Format type.

        - 'datetime' : Return datetime object of datetime package.
        - 'date' : Return date object of datetime package.
        - 'time' : Return time object of datetime package.
        - 'timestamp' : Return time stamp of ten digit length.
        - None : Auto judgment

    format_str : str or None
        Format string.

        - None : Default format method.
            * When parameter format_type is 'datetime', then format string is '%Y-%m-%d %H:%M:%S'
            * When parameter format_type is 'date', then format string is '%Y-%m-%d'
            * When parameter format_type is 'time', then format string is '%H:%M:%S'
            * When parameter format_type is 'timestamp', then format string is '%Y-%m-%d %H:%M:%S'
            * When parameter format_type is None, then auto judgment
        - str : Format by str.

    throw_error : bool
        Whether throw error, when parameter time_obj value error, otherwise return original value

    Returns
    -------
    datetime.datetime or datetime.date or datetime.time or datetime.timedelta or int or object
        Time object of datetime package or time stamp or or original value.
    """

    check_parm(string, str)
    check_parm(format_type, "datetime", "date", "time", "timestamp", None)
    check_parm(format_str, str, None)
    check_parm(throw_error, bool)

    if format_type == None:
        str_len = len(string)
        if str_len == 19:
            format_str = "%Y-%m-%d %H:%M:%S"
            format_type = "datetime"
        elif str_len == 14:
            format_str = "%Y%m%d%H%M%S"
            format_type = "datetime"
        elif str_len == 10:
            format_str = "%Y-%m-%d"
            format_type = "date"
        elif str_len == 8:
            if string[2] == ":":
                format_str = "%H:%M:%S"
                format_type = "time"
            else:
                format_str = "%Y%m%d"
                format_type = "date"
        elif str_len == 6:
            format_str = "%H%M%S"
            format_type = "time"
        elif str_len == 4:
            format_str = "%Y"
            format_type = "date"
        else:
            return string
    elif format_type in ["datetime", "date", "time", "timestamp"]:
        if format_str == None:
            format_dir = {
                "datetime": "%Y-%m-%d %H:%M:%S",
                "date": "%Y-%m-%d",
                "time": "%H:%M:%S",
                "timestamp": "%Y-%m-%d %H:%M:%S"
            }
            format_str = format_dir[format_type]
    try:
        time_obj = datetime.datetime.strptime(string, format_str)
    except ValueError:
        return string
    if format_type == "date":
        time_obj = time_obj.date()
    elif format_type == "time":
        time_obj = time_obj.time()
    elif format_type == "timestamp":
        time_obj = int(time_obj.timestamp())
    return time_obj