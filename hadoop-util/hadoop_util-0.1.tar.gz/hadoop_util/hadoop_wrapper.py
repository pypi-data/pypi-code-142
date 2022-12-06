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


class TLLibs(object):
    """
    TLLibs
    """
    HADOOP_BIN = "/home/work/local/turing-client/hadoop/bin/hadoop"


class KHLibs(object):
    """
    KHLibs
    """
    HADOOP_BIN = "/home/work/local/hadoop-client-nmg/hadoop-client-khan/hadoop/bin/hadoop"
    PYTHON_URI = "/app/ecom/fcr/huangtao13/share/python2.7.9.tar.gz#python27"
    PYTHON_BIN = "python27/bin/python"
    STREAMING = "/home/work/local/hadoop-client-nmg/hadoop-client-khan/hadoop/lib/streaming-3.25.0.jar"
    URL_PREFIX = "hdfs://nmg01-khan-hdfs.dmop.baidu.com:54310"


class MLLibs(object):
    """
    MLLibs
    """
    HADOOP_BIN = "/home/work/local/hadoop-client-nmg/hadoop.mulan/bin/hadoop"
    PYTHON_URI = "/app/ecom/fcr-opt/liuli/share/python2.7.9.tar.gz#python27"
    PYTHON_BIN = "python27/bin/python"
    STREAMING = "/home/work/local/hadoop-client-nmg/hadoop.mulan/contrib/streaming/hadoop-2-streaming.jar"
    URI_PREFIX = "hdfs://nmg01-mulan-hdfs.dmop.baidu.com:54310"


class THLibs(object):
    """
    THLibs
    """
    HADOOP_BIN = "/home/work/local/hadoop-client-nmg/hadoop.taihang/bin/hadoop"
    PYTHON_URI = "/app/ecom/fcr/huangtao13/share/python2.7.9.tar.gz#python27"
    PYTHON_BIN = "python27/bin/python"
    STREAMING = "/home/work/local/hadoop-client-nmg/hadoop.taihang/contrib/streaming/hadoop-2-streaming.jar"
    URI_PREFIX = "hdfs://nmg01-taihang-hdfs.dmop.baidu.com:54310"


class WDLibs(object):
    """
    WDLibs
    """
    HADOOP_BIN = "/home/work/local/hadoop-client-nmg/hadoop.wudang/hadoop/bin/hadoop"
    PYTHON_URI = "/user/cpd_dlp/huangtao13/share/python2.7.9.tar.gz#python27"
    PYTHON_BIN = "python27/bin/python"
    STREAMING = "/home/work/local/hadoop-client-nmg/hadoop.wudang/hadoop/lib/streaming-3.30.5-SNAPSHOT.jar"
    URL_PREFIX = "afs://wudang.afs.baidu.com:9902"


class ARIESLibs(object):
    """
    WDLibs
    """
    HADOOP_BIN = "/home/work/local/hadoop-client-nmg/hadoop.aries/hadoop/bin/hadoop"
    PYTHON_URI = "/user/cpd_dlp/huangtao13/share/python2.7.9.tar.gz#python27"
    PYTHON_BIN = "python27/bin/python"
    STREAMING = "/home/work/local/hadoop-client-nmg/hadoop.wudang/hadoop/lib/streaming-3.30.5-SNAPSHOT.jar"
    URL_PREFIX = "afs://aries.afs.baidu.com:9902"


class WTLibs(object):
    """
    WDLibs
    """
    HADOOP_BIN = "/home/work/local/hadoop-client-nmg/hadoop.wutai/hadoop/bin/hadoop"
    PYTHON_URI = "/app/ecom/fc-star/huangtao13/share/python2.7.9.tar.gz#python27"
    PYTHON_BIN = "python27/bin/python"
    STREAMING = "/home/work/local/hadoop-client-nmg/hadoop.wutai/hadoop/lib/streaming-3.29.2.jar"
    URL_PREFIX = "hdfs://yq01-wutai-hdfs.dmop.baidu.com:54310"


class YLLibs(object):
    """
    WDLibs
    """
    HADOOP_BIN = "/home/work/local/hadoop-client-nmg/hadoop.yinglong/hadoop/bin/hadoop"
    PYTHON_URI = "/user/cpd_dlp/huangtao13/share/python2.7.9.tar.gz#python27"
    PYTHON_BIN = "python27/bin/python"
    STREAMING = "/home/work/local/hadoop-client-nmg/hadoop.yinglong/hadoop/lib/streaming-3.30.5-SNAPSHOT.jar"
    URL_PREFIX = "afs://yinglong.afs.baidu.com:9902"


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


class StreamingJob(object):
    """
    StreamingJob class
    """
    GENERAL_OPTIONS = ['stream_num_map_output_key_fields',
                       'num_key_fields_for_partition',
                       'mapred_output_key_comparator_class',
                       'mapred_job_name',
                       'mapred_job_map_capacity',
                       'mapred_job_reduce_capacity',
                       'mapred_map_tasks',
                       'mapred_reduce_tasks',
                       'mapred_job_priority']
    OPTIONS_MAYBE_LIST_VALUE = ['input', 'file', 'cacheArchive']

    def __init__(self,
                 input,
                 output,
                 file=None,
                 mapper=None,
                 reducer=None,
                 cacheArchive=None,
                 stream_num_map_output_key_fields=1,
                 num_key_fields_for_partition=1,
                 partitioner="org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner",
                 mapred_output_key_comparator_class="org.apache.hadoop.mapred.lib.KeyFieldBasedComparator",
                 mapred_job_name="huangtao13_wrapper_instance",
                 mapred_job_map_capacity=1000,
                 mapred_job_reduce_capacity=1000,
                 mapred_map_tasks=1000,
                 mapred_reduce_tasks=1000,
                 mapred_job_priority='NORMAL',
                 **kwargs):
        # conf param
        self.D_mapred_job_name = mapred_job_name
        self.D_mapred_job_priority = mapred_job_priority

        self.D_mapred_output_key_comparator_class = mapred_output_key_comparator_class

        self.D_stream_num_map_output_key_fields = stream_num_map_output_key_fields
        self.D_num_key_fields_for_partition = num_key_fields_for_partition

        self.D_mapred_job_map_capacity = mapred_job_map_capacity
        self.D_mapred_job_reduce_capacity = mapred_job_reduce_capacity
        self.D_mapred_map_tasks = mapred_map_tasks
        self.D_mapred_reduce_tasks = mapred_reduce_tasks

        # job param
        self.cacheArchive = cacheArchive  # maybe list
        self.file = file  # maybe list
        self.partitioner = partitioner
        # self.outputformat = outputformat

        self.input = input
        self.output = output
        self.mapper = mapper
        self.reducer = reducer
        for conf_name, conf_value in kwargs.keys():
            self.conf_name = conf_value

    def _gen_cmd(self, hadoop_home, streaming):
        config_dict = self.__dict__
        general_options = []
        command_options = []
        for conf in config_dict.keys():
            # todo: cacheArchive\input\file - maybe list
            if conf.startswith('D'):
                conf_name = conf.split('_', 1)[1].replace('_', '.')
                conf_value = config_dict[conf]
                general_options.append(
                    '-D {conf_name}={conf_value}'.format(conf_name=conf_name,
                                                         conf_value=conf_value))
            else:
                # conf_name = conf
                if not config_dict[conf]:
                    continue
                if conf in StreamingJob.OPTIONS_MAYBE_LIST_VALUE and isinstance(config_dict[conf], list):
                    value_list = config_dict[conf]
                    for conf_value in value_list:
                        command_options.append(
                            '-{conf_name} {conf_value}'.format(conf_name=conf, conf_value=conf_value))
                else:
                    # Todo: conf_name = conf.replace('_', '.')  # ?是否必要
                    conf_value = config_dict[conf]
                    command_options.append('-{conf_name} {conf_value}'.format(conf_name=conf, conf_value=conf_value))
        cmd_config = ' '.join(general_options + command_options)
        cmd = "{hadoop_home} jar {streaming} {config} ".format(hadoop_home=hadoop_home, streaming=streaming,
                                                               config=cmd_config)
        return cmd

    def run(self, hadoop_bin, streaming_jar, log_console=True, send_mail=False):
        """

        :param hadoop_bin:
        :param streaming_jar:
        :param log_console:
        :param send_mail:
        :return:
        """
        cmd = self._gen_cmd(hadoop_home=hadoop_bin, streaming=streaming_jar) + ' > mr.log'

        ret_code, ret_str = commands.getstatusoutput(cmd)
        print('ret_code:', ret_code)
        print('ret_str:', ret_str)
        print('-' * 20)
        if ret_code != 0:
            print('hadoop job failed!')
            exit(1)
        # todo: send mail
        if send_mail:
            pass
        return ret_code


if __name__ == '__main__':
    pass
