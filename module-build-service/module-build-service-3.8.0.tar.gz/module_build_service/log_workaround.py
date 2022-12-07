import logging


class QpidWarningFilter(logging.Filter):
    def filter(self, record):
        return "Cannot find qpid python module" not in record.getMessage()


logging.getLogger("moksha.hub").addFilter(QpidWarningFilter())
