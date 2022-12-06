import binascii
import os
import pytz
from datetime import datetime
from django.conf import settings


def get_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def time_now(country_code=None):
    if country_code is None:
        time_zone = settings.TIME_ZONE
    else:
        try:
            time_zone = pytz.country_timezones(country_code)[0]
        except Exception:
            time_zone = settings.TIME_ZONE
    return datetime.now(tz=pytz.timezone(time_zone))


def generate_hash(length: int) -> str:
    return binascii.hexlify(os.urandom(length)).decode()
