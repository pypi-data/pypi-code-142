from datetime import timedelta

from etiket.core.config import settings


def get_access_token_expiration_time():
    return timedelta(minutes=settings.ETIKET_ACCESS_TOKEN_EXPIRE_MINUTES)


def get_refresh_token_expiration_time():
    return timedelta(minutes=settings.ETIKET_REFRESH_TOKEN_EXPIRE_MINUTES)
