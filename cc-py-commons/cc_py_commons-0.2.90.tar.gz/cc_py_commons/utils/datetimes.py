import pytz
from dateutil.parser import parse

##
# Date, Time, and DateTime handling functions.
# The dateutil library is used to have robust string parsing.
##


def parse_date_str_to_datetime(date_str):
  return parse(date_str)


def to_utc(input_datetime):
  """
  Take a datetime of any timezone and returns a datetime in UTC
  """
  return input_datetime.astimezone(pytz.UTC)
