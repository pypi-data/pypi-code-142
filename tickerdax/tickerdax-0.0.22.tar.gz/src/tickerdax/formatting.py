import calendar
from datetime import datetime, timezone


def truncate_datetime(date, timeframe):
    kwargs = {
        'year': date.year
    }
    if timeframe.endswith(('M', 'd', 'h', 'm')):
        kwargs['month'] = date.month

    if timeframe.endswith(('d', 'h', 'm')):
        kwargs['day'] = date.day

    if timeframe.endswith(('h', 'm')):
        kwargs['hour'] = date.hour

    if timeframe.endswith('m'):
        kwargs['minute'] = date.minute

    return datetime(
        tzinfo=timezone.utc,
        **kwargs
    )


def get_unix_time(date, timeframe):
    return float(calendar.timegm(truncate_datetime(date, timeframe).timetuple()))


def get_timestamp_range(start, end, timeframe):
    """
    Gets a range of timestamps between the start and end dates.

    :param datetime start: A start time.
    :param datetime end: A end time.
    :param str timeframe: The string value of the timeframe, i.e. 1m, 1h, 1d, etc.
    :rtype: list[int]
    """
    start = get_unix_time(start, timeframe)
    end = get_unix_time(end, timeframe)
    range_seconds = end - start
    timeframe_in_seconds = convert_timeframe_to_seconds(timeframe)
    time_intervals = range_seconds / timeframe_in_seconds

    timestamps = []
    for time_interval in range(int(time_intervals) + 1):
        timestamps.append(start + (time_interval * timeframe_in_seconds))

    return timestamps


def convert_timeframe_to_seconds(timeframe):
    seconds_per_unit = {"s": 1, "m": 60, "h": 3600, "d": 86400, "w": 604800}
    return int(timeframe[:-1]) * seconds_per_unit[timeframe[-1]]


def get_string_range(start, end):
    start = datetime.fromtimestamp(start).strftime('%Y-%m-%dT%H:%M:%S')
    end = datetime.fromtimestamp(end).strftime('%Y-%m-%dT%H:%M:%S')
    return f'{start} to {end}'
