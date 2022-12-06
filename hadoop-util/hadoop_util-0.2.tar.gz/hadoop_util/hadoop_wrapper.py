# encoding: utf-8
"""
@author: huangtao13
@project : utils
@file: hadoop_wrapper.py
@time: 2019/10/24 下午11:08
@desc:
"""
from __future__ import print_function
from __future__ import unicode_literals

import os
import logging
import commands
from functools import wraps


logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] '
                    '- %(levelname)s: %(message)s', level=logging.INFO)


def eval_cmd_command(func):
    """

    :param func:
    :return:
    """

    @wraps(func)
    def wrapped_function(*arg):
        """

        :param arg:
        :return:
        """
        if not arg:
            raise Exception("Unexpected params for %s() function!" % func.__name__)
        cmd = func(*arg)
        func_name = 'HdfsHelper.' + func.__name__
        if not cmd:
            logging.error('Do %s() FAILED! cmd is Null' % func_name)
            exit(-1)
        ret_code, ret_str = commands.getstatusoutput(cmd)
        if ret_code != 0:
            logging.error('Do %s() FAILED! error code: %d , error meg:%s' % (func_name, ret_code, ret_str))
            exit(-1)
        logging.info('Do %s() OK!' % func_name)
        return ret_code

    return wrapped_function


class HdfsHelper(object):
    """ HdfsHelper """

    def __init__(self, hadoop_home):
        """
        :param hadoop_home:
        """
        self.hadoop_home = hadoop_home

    @staticmethod
    def _eval_cmd_command(cmd, func_name):
        ret_code, ret_str = commands.getstatusoutput(cmd)
        if ret_code != 0:
            logging.info('[ %s error ] error code: %d , error meg:%s' % ('HdfsHelper.' + func_name, ret_code, ret_str))
            exit(ret_code)
        return ret_code

    @eval_cmd_command
    def rmr(self, path):
        """

        :param path:
        :return:
        """
        if '*' in path or self.test(path) == 0:
            return "{hadoop_home} dfs -rmr {path}".format(hadoop_home=self.hadoop_home, path=path)
        return 'echo "Do HdfsHelper.rmr(%s) OK!"' % path

    @eval_cmd_command
    def get(self, hdfs_path, local_path):
        """

        :param hdfs_path:
        :param local_path:
        :return:
        """
        return '{hadoop_home} dfs -get {hdfs_path} {local_path} '.format(
            hadoop_home=self.hadoop_home,
            hdfs_path=hdfs_path,
            local_path=local_path
        )

    @eval_cmd_command
    def getmerge(self, hdfs_path, local_path):
        """

        :param hdfs_path:
        :param local_path:
        :return:
        """
        return '{hadoop_home} dfs -getmerge {hdfs_path} {local_path} '.format(
            hadoop_home=self.hadoop_home,
            hdfs_path=hdfs_path,
            local_path=local_path
        )

    @eval_cmd_command
    def put(self, local_file, target_hdfs_path):
        """

        :param local_file:
        :param target_hdfs_path:
        :return:
        """
        return '{hadoop_home} dfs -put {target_file} {target_hdfs_path} '.format(
            hadoop_home=self.hadoop_home,
            target_file=local_file,
            target_hdfs_path=target_hdfs_path
        )

    def cat(self, target_hdfs_path):
        """

        :param target_hdfs_path:
        :return:
        """
        cmd = '{hadoop_home} dfs -cat {target_hdfs_path} '.format(
            hadoop_home=self.hadoop_home,
            target_hdfs_path=target_hdfs_path
        )
        ret_code, ret_str = commands.getstatusoutput(cmd)
        if ret_code != 0:
            print('Do %s() FAILED! error code: %d , error meg:%s' % ('cat', ret_code, ret_str))
            exit(ret_code)
        else:
            ret_str = '\n'.join(ret_str.split('\n')[1:])
            print('\n%s\n' % ret_str)

    def cat_get_output(self, target_hdfs_path):
        """

        :param target_hdfs_path:
        :return:
        """
        cmd = '{hadoop_home} dfs -cat {target_hdfs_path} '.format(
            hadoop_home=self.hadoop_home,
            target_hdfs_path=target_hdfs_path
        )
        ret_code, ret_str = commands.getstatusoutput(cmd)
        if ret_code != 0:
            print('Do %s() FAILED! error code: %d , error meg:%s' % ('cat', ret_code, ret_str))
            exit(ret_code)
        else:
            return ret_str

    @eval_cmd_command
    def cp(self, source, target):
        """

        :param source:
        :param target:
        :return:
        """
        return '{hadoop_home} dfs -cp {source} {target} '.format(
            hadoop_home=self.hadoop_home,
            source=source,
            target=target)

    @eval_cmd_command
    def mkdir(self, dir_path):
        """

        :param dir_path:
        :return:
        """
        return '{hadoop_home} dfs -mkdir {dir_path} '.format(
            hadoop_home=self.hadoop_home,
            dir_path=dir_path
        )

    @eval_cmd_command
    def touchz(self, hdfs_done_file_path):
        """

        :param hdfs_done_file_path:
        :return:
        """
        return '{hadoop_home} dfs -touchz {hdfs_done_file_path} '.format(
            hadoop_home=self.hadoop_home,
            hdfs_done_file_path=hdfs_done_file_path
        )

    def test(self, path):
        """
        dfs -test
            -e: return 0 if <path> exists
        :param path:
        :return:
        """
        cmd = "{hadoop_home} dfs -test -e {path}".format(hadoop_home=self.hadoop_home, path=path)
        ret_code, ret_str = commands.getstatusoutput(cmd)
        if ret_code != 0:
            logging.info('Hadoop file %s does Not exist on Hadoop at all!' % path)
            logging.info(ret_str)
        return ret_code

    def get_md5sum(self, path):
        """
        :param path:
        :return:
        """
        cmd = "{hadoop_home} dfs -text {path} | md5sum | cut -d' ' -f1 ".format(hadoop_home=self.hadoop_home, path=path)
        ret_code, ret_str = commands.getstatusoutput(cmd)
        if ret_code != 0:
            logging.error('Do %s() FAILED! error code: %d , error meg:%s' % ('get_md5sum', ret_code, ret_str))
            exit(ret_code)
        md5sum = ret_str.split('\n')[-1]
        return md5sum

    def get_size(self, path):
        """
        :param path:
        :return:
        """
        cmd = "{hadoop_home} dfs -ls {path} | grep '{path}' ".format(hadoop_home=self.hadoop_home, path=path)
        ret_code, ret_str = commands.getstatusoutput(cmd)
        if ret_code != 0:
            logging.error('Do %s() FAILED! error code: %d , error meg:%s' % ('get_size', ret_code, ret_str))
            exit(ret_code)
        size = ret_str.split(' ')[-4]
        return size
