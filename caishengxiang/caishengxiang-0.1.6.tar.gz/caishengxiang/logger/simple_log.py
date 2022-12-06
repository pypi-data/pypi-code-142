#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/7/19 上午12:32
# @Author  : caishengxiang
# @File    : simple_log.py
"""
简易日志
"""
import os
import time
import datetime
import threading
from functools import reduce
import pathlib


class SimpleLog:

    def __init__(self, log_dir, logger_level='debug', backup_days=90, suffix='.log'):
        if not os.path.exists(log_dir):
            pathlib.Path(log_dir).mkdir(parents=True, exist_ok=True)  # 创建目录
        self.level_relations = {
            'debug': 10,
            'info': 20,
            'warning': 30,
            'error': 40,
            'crit': 50
        }
        self.logger_level = logger_level.lower()
        self.logger_level_num = self.level_relations[logger_level]
        self.log_dir = log_dir
        self.backup_days = backup_days
        self.suffix = suffix
        self.hostname = os.getenv('HOSTNAME') or os.getenv('hostname')
        try:
            self.pid = os.getpid()
        except:
            self.pid = 'None'

    def _clean_logs(self):
        """清理过期日志"""
        try:
            file_names = os.listdir(self.log_dir)
            filter_file_names = filter(lambda file_name: file_name.endswith(self.suffix), file_names)
            for file_name in filter_file_names:
                date_str = file_name[:-len(self.suffix)]
                file_time = datetime.datetime.strptime(date_str, '%Y-%m-%d')
                clean_time = datetime.datetime.now() - datetime.timedelta(days=self.backup_days)
                if file_time < clean_time:
                    try:
                        os.remove(os.path.join(self.log_dir, file_name))
                    except Exception as e:
                        print(e)
                        continue
        except Exception as e:
            print(e)

    def _write_log(self, *contents, logger_level=None):
        if logger_level is None:
            logger_level = self.logger_level
        try:
            if not os.path.exists(self.log_dir):
                pathlib.Path(self.log_dir).mkdir(parents=True, exist_ok=True)
            date = time.strftime('%Y-%m-%d')
            filename = '{}{}'.format(str(date), self.suffix)
            file = os.path.join(self.log_dir, filename)
            if not os.path.exists(file):
                self._clean_logs()

            content = str(reduce(lambda x, y: str(x) + '  ' + str(y), contents))
            fp = open(file, 'a', encoding='utf-8')
            now_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            hostname_str = ''
            if self.hostname:
                hostname_str = '[hostname:{hostname}]'.format(hostname=self.hostname)
            log_header = "[{now}]{hostname_str}[pid:{pid}][{logger_level}]".format(now=now_str,
                                                                                   hostname_str=hostname_str,
                                                                                   pid=self.pid,
                                                                                   logger_level=logger_level)
            strlog = log_header + content + '\n'
            print(strlog)
            fp.write(strlog)
            fp.close()
        except Exception as e:
            print(e)

    def write_log(self, *contents, **kwargs):
        try:
            t = threading.Thread(target=self._write_log, args=contents, kwargs=kwargs)
            t.start()
        except Exception as e:
            print(e)

    def debug(self, *contents):
        if self.logger_level_num <= self.level_relations['debug']:
            self.write_log(*contents, logger_level='debug')

    def info(self, *contents):
        if self.logger_level_num <= self.level_relations['info']:
            self.write_log(*contents, logger_level='info')

    def warning(self, *contents):
        if self.logger_level_num <= self.level_relations['warning']:
            self.write_log(*contents, logger_level='warning')

    def error(self, *contents):
        if self.logger_level_num <= self.level_relations['error']:
            self.write_log(*contents, logger_level='error')

    def crit(self, *contents):
        if self.logger_level_num <= self.level_relations['crit']:
            self.write_log(*contents, logger_level='crit')


if __name__ == '__main__':
    test_logger = SimpleLog(log_dir='/tmp/simple_log', logger_level='debug', backup_days=90, suffix='.test_log')
    test_logger.debug('debug', 'xx')
    test_logger.info('info', 9, 'zzzz')
    test_logger.warning('warning', 10, 'xxx')
