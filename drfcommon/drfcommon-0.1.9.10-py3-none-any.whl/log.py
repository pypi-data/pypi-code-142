#!/usr/bin/env python
import logging
from drfcommon.choices import ComCodeChoice

logger = logging.getLogger('debug')


LOG_PRINT_FUNC = {
    ComCodeChoice.OK: logger.debug,
    ComCodeChoice.BAD: logger.warning,
    ComCodeChoice.UNAUTHORIZED_ERR: logger.warning,
    ComCodeChoice.FORBIDDEN_ERR: logger.warning,
    ComCodeChoice.API_NOT_FUND: logger.warning,
    ComCodeChoice.HTTP_405_METHOD_NOT_ALLOWED: logger.warning,
    ComCodeChoice.API_ERR: logger.error,
    ComCodeChoice.DB_ERR: logger.error,
}


def logger_print_by_code(code: ComCodeChoice, exc: Exception):
    """

    :param code: ComCodeChoice
    :param exc:
    :return:
    """
    logger_print = LOG_PRINT_FUNC.get(code, logger.error)
    exc_info = False
    if logger_print == logger.error:
        exc_info = True
    logger_print("raw exc {}".format(exc), exc_info=exc_info)
    return
