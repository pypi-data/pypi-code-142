from graceful_exit.custom_logger.custom_logging import get_logger

logger = get_logger("SignalExceptions")


class SigTerm(SystemExit):
    logger.debug("registering SigTerm")


class SigInt(SystemExit):
    logger.debug("registering SigInt")
