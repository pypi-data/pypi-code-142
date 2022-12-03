from functools import lru_cache

from django.conf import settings

from .mega import Mega


def check_settings(alias: str) -> None:
    attr = getattr(settings, "MEGA_ACCOUNTS")

    if not isinstance(attr, dict):
        raise AttributeError(
            "setting ' MEGA_ACCOUNTS' need to be type dict but where given {}".format(
                type(attr)
            )
        )

    if attr.get(alias) is None:
        raise AttributeError(
            f"settings 'MEGA_ACCOUNTS' object has no attribute alias '{alias}' "
        )

    if not isinstance(attr[alias], dict):
        raise TypeError(
            "settings 'MEGA_ACCOUNTS' alias '{}' need to be type dict with (email,password) not type {}".format(
                alias, type(attr[alias])
            )
        )


mega: Mega = Mega()


def cached_mega_login(**credentials):
    from django.core.cache import cache

    instance = cache.get(f"mega_{credentials['email']}")
    if instance:
        return instance
    instance = mega.login(**credentials)
    cache.set(f"mega_{credentials['email']}", instance)
    return instance


def login_mega(**credentials):
    _mega = mega.login(**credentials)
    return _mega


@lru_cache()
def get_or_create_storage_instance(**credentials):
    if getattr(settings, "USE_MEGA_LOGIN_CACHE"):
        return cached_mega_login(**credentials)
    return login_mega(**credentials)
