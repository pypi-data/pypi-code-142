#import numpy as np
#import pandas as pd
from datetime import datetime, timedelta


def from_dates(dates, wy_month=7):
    """
    Returns water years, as a list of ints, for a given array of dates. Use this to
    add water year info into a pandas DataFrame. 

    We follow the convention used for fiscal years, and label the water years based 
    on their end dates. E.g. the 2022 water year is from 2021-07-01 to 2022-06-30 
    inclusive (assuming wy_month=7).
    """
    answer = [d.year if d.month < 7 else d.year + 1 for d in dates]
    return answer


def generate_dates(start_date, end_date=None, days=0, years=1):
    """
    Generates a list of daily datetime values from a given start date. The length 
    may be defined by an end_date, or a number of days, or a number of years. This 
    function may be useful for working with daily datasets and models.
    """
    if (days > 0):
        # great, we already have the number of days
        pass
    elif (end_date != None):
        # use end_date
        days = (end_date - start_date).days        
    else:
        # use years
        end_date = datetime(start_date.year + years, start_date.month, start_date.day,
            start_date.hour, start_date.minute, start_date.second, start_date.microsecond)
        days = (end_date - start_date).days
    date_list = [start_date + timedelta(days=x) for x in range(days)]
    return date_list