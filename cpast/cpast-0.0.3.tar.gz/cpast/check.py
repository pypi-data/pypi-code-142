from datetime import datetime


def check_date(date: str) -> bool:
    try:
        datetime.strptime(date, '%Y-%m-%d')
        return True
    except ValueError:
        return False


def check_time(time: str) -> bool:
    try:
        datetime.strptime(time, '%H:%M:%S')
        return True
    except ValueError:
        return False


def run(date: str, time: str):
    if not check_date(date):
        raise ValueError('Incorrect date format, should be YYYY-MM-DD')
    if not check_time(time):
        raise ValueError('Incorrect time format, should be HH:MM:SS')
    return True
