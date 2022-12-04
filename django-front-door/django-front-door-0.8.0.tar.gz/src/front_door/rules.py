import logging

from django.conf import settings

from .conf import LOG_FAIL, LOG_PASS, LOG_RULE_FAIL, LOG_RULE_PASS, config
from .exception import FrontDoorAccessDenied
from .utils import get_client_ip

logger = logging.getLogger(__name__)


def allowed_ip(request, ip, **kwargs):
    return ip in config.ALLOWED_IPS


def internal_ip(request, ip, **kwargs):
    return ip in settings.INTERNAL_IPS


def special_header(request, ip, **kwargs):
    if config.HEADER and config.TOKEN:
        return request.headers.get(config.HEADER) == config.TOKEN


def has_header(request, ip, **kwargs):
    if config.HEADER:
        return config.HEADER in request.headers


def allowed_path(request, ip, **kwargs):
    return request.path in config.ALLOWED_PATHS


def forbidden_path(request, ip, **kwargs):
    if request.path in config.FORBIDDEN_PATHS:
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
    if not config.ENABLED:
        access_allowed = True
    else:
        access_allowed = config.DEFAULT_POLICY
        ip = get_client_ip(request)
        path = request.path
        extra = {"ip": ip,
                 "path": path}
        for check in config.rules:
            try:
                if check(request, ip):
                    if config.LOG_LEVEL & LOG_RULE_PASS:
                        logger.error(f"{check.__name__}() PASS", extra=extra)
                    access_allowed = True
                    break
                else:
                    if config.LOG_LEVEL & LOG_RULE_FAIL:
                        logger.error(f"{check.__name__}() FAIL", extra=extra)
            except FrontDoorAccessDenied:
                if config.LOG_LEVEL & LOG_RULE_FAIL:
                    logger.error(f"{check.__name__}() DENY", extra=extra)
                access_allowed = False
                break
        if access_allowed and (config.LOG_LEVEL & LOG_PASS):
            logger.error("Access ALLOWED", extra=extra)
        elif config.LOG_LEVEL & LOG_FAIL:
            logger.error("Access DENIED", extra=extra)

    return access_allowed
