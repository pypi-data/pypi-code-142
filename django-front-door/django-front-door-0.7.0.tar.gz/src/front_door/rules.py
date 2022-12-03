import logging

from .conf import (config, front_door_is_active, get_front_door_allowed_ips,
                   get_front_door_forbidden_paths, get_front_door_internal_ips,
                   get_front_door_whitelisted_paths)
from .exception import FrontDoorAccessDenied
from .utils import get_client_ip

logger = logging.getLogger(__name__)


def allowed_ip(request, ip, **kwargs):
    return ip in get_front_door_allowed_ips()


def internal_ip(request, ip, **kwargs):
    return ip in get_front_door_internal_ips()


def special_header(request, ip, **kwargs):
    if config.HEADER and config.TOKEN:
        return request.headers.get(config.HEADER) == config.TOKEN


def has_header(request, ip, **kwargs):
    if config.HEADER:
        return config.HEADER in request.headers


def allowed_path(request, ip, **kwargs):
    return request.path in config.ALLOWED_PATHS


def forbidden_path(request, ip, **kwargs):
    if request.path in get_front_door_forbidden_paths():
        raise FrontDoorAccessDenied


def cookie_exists(request, ip, **kwargs):
    return config.COOKIE_NAME in request.COOKIES


def cookie_value(request, ip, **kwargs):
    if not config.COOKIE_PATTERN and config.COOKIE_NAME:
        return False
    try:
        value = request.COOKIES[str(config.COOKIE_NAME)]
    except KeyError:
        return False
    return bool(config.COOKIE_PATTERN.match(value))


def front_door_check_access(request):
    if not front_door_is_active():
        access_allowed = True
    else:
        access_allowed = config.DEFAULT_POLICY
        ip = get_client_ip(request)
        path = request.path
        extra = {"ip": ip,
                 "path": path}
        for check in config.allows:
            try:
                if check(request, ip):
                    logger.debug(f"{check.__name__}() PASS", extra=extra)
                    access_allowed = True
                    break
                else:
                    logger.error(f"{check.__name__}() FAIL", extra=extra)
            except FrontDoorAccessDenied:
                logger.error(f"{check.__name__}() DENY", extra=extra)
                return False
    return access_allowed
