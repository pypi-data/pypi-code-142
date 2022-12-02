from fdfs_client.client import Fdfs_client
import redis
import glob
import requests
import json
import sys
import os
import vcd_utils

tracker_conf = {
    'host_tuple': ['192.168.1.47'],
    'port': 22122,
    'timeout': 60,
    'use_storage_id': False
}

fdfs_client = Fdfs_client(tracker_conf)

redis_client = redis.Redis(host='192.168.1.48', port=16380, password='knn3.14159', decode_responses=True)


def run_xxl_job(job_name):

    # 获取配置文件
    content = redis_client.hget('job:%s:info' % job_name, 'job_conf')
    if content is None:
        return False

    job_conf = json.loads(content)

    # 下载作业文件
    for item in redis_client.hscan_iter('job:%s:files' % job_name):
        try:
            fdfs_client.download_to_file(item[0], item[1].encode())
        except:
            pass

    # 执行验证文件
    if 'command' in job_conf:
        os.system(job_conf['command'])

    # 保存验证结果
    if 'result_file' in job_conf:
        result_file = job_conf['result_file']
        if os.path.exists(result_file):
            result = fdfs_client.upload_by_filename(result_file)
            if 'Status' in result and result['Status'] == 'Upload successed.':
                remote_file_id = result['Remote file_id'].decode()
                redis_client.hset('job:%s:output' % job_conf['name'], result_file, remote_file_id)

    # 保存波形文件
    if 'wave_file' in job_conf:
        wave_file = job_conf['wave_file']
        if os.path.exists(wave_file):
            result = fdfs_client.upload_by_filename(wave_file)
            if 'Status' in result and result['Status'] == 'Upload successed.':
                remote_file_id = result['Remote file_id'].decode()
                redis_client.hset('job:%s:output' % job_conf['name'], wave_file, remote_file_id)

        # 解析波形文件
        vcd_utils.get_vcd_info(wave_file, job_name)
        vcd_utils.parse_vcd_time(wave_file, job_name)
        signals, signal_ids = vcd_utils.parse_vcd_signals(wave_file, job_name)
        blocks = vcd_utils.cut_vcd_blocks(wave_file, job_name)
        vcd_utils.parse_vcd_change_vals(wave_file, blocks, signal_ids, job_name, '')

        # 保存解析后波形文件
        for item in redis_client.hscan_iter('job:%s:wave:blocks' % job_name):
            try:
                result = fdfs_client.upload_by_filename(item[1])
                if 'Status' in result and result['Status'] == 'Upload successed.':
                    remote_file_id = result['Remote file_id'].decode()
                    redis_client.hset('job:%s:wave:blocks:files' % job_name, item[1], remote_file_id)
            except:
                pass

    return True



if __name__ == "__main__":
    job_conf_file = sys.argv[1]
    run_xxl_job(job_conf_file)