"""
Created on Tue Oct 12 14:33:49 2021
@usage:create a log file. 
@author: Pankaj Kalal
"""
import logging
from logging import Formatter
from logging.handlers import TimedRotatingFileHandler


class python_custom_logging:
    def __init__(self, logpath, loggername, logformat, log_level, logfilehandlertime, interval,backupcount):
        self.log_path = logpath
        self.loggername = loggername
        self.LOG_FORMAT = logformat
        self.LOG_LEVEL = log_level
        self.when = logfilehandlertime
        self.interval = interval
        self.backupcount = backupcount
        
    def create_log(self):
        logging.basicConfig(level = self.LOG_LEVEL)
        custom_logger = logging.getLogger(self.loggername)
        custom_logger.setLevel(self.LOG_LEVEL)
        custom_logger_file_handler = TimedRotatingFileHandler(self.log_path, when = self.when, interval = self.interval, backupCount = self.backupcount)
        custom_logger_file_handler.setLevel(self.LOG_LEVEL)
        custom_logger_file_handler.setFormatter(Formatter(self.LOG_FORMAT))
        custom_logger.addHandler(custom_logger_file_handler)

        return custom_logger