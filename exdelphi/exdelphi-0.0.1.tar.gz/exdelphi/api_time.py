from datetime import datetime


def datetime_to_int(datetime_object: datetime) -> int:
    """Returns Unix timestamp (in seconds) for given datetime"""
    return int(datetime_object.timestamp())


def datetime_string_to_int(datetime_string: str, format_string: str) -> int:
    """Returns Unix timestamp (in seconds) for given datetime string with specified formatting"""
    dto = datetime.strptime(datetime_string, format_string)
    return datetime_to_int(dto)


def int_to_datetime(unix_timestamp: int) -> datetime:
    """Returns datetime object created from given unix timestamp"""
    return datetime.fromtimestamp(unix_timestamp)
