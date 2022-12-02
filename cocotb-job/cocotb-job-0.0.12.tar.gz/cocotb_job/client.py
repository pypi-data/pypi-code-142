from fdfs_client.client import Fdfs_client
import redis
import glob
import requests
import json
import sys
import os
import datetime

tracker_conf = {
    'host_tuple': ['192.168.1.47'],
    'port': 22122,
    'timeout': 60,
    'use_storage_id': False
}

fdfs_client = Fdfs_client(tracker_conf)

redis_client = redis.Redis(host='192.168.1.48', port=16380, password='knn3.14159', decode_responses=True)

xxl_job_admin_url = 'http://192.168.1.48:8666/xxl-job-admin'


# 执行作业
def run_job(job_conf_file='./job.conf'):
    # 检查作业配置文件是否存在
    if not os.path.exists(job_conf_file):
        print('%s配置文件不存在' % job_conf_file)
        return False

    # 读取作业配置内容
    with open(job_conf_file, encoding='utf-8') as file:
        content = file.read()
    if content is None:
        print('配置文件内容为空')
        return False
    job_conf = json.loads(content)

    if 'name' not in job_conf:
        print('配置文件没有找到name属性')
        return False

    print('读取配置文件...ok')

    # 清空远程作业文件
    for item in redis_client.hscan_iter('job:%s:files' % job_conf['name']):
        try:
            result = fdfs_client.delete_file(item[1].encode())
            if result[0] == 'Delete file successed.':
                redis_client.hdel('job:%s:files' % job_conf['name'], item[0])
        except:
            pass
    print('清空远程作业文件...ok')

    # 清空远程验证输出文件
    for item in redis_client.hscan_iter('job:%s:output' % job_conf['name']):
        try:
            result = fdfs_client.delete_file(item[1].encode())
            if result[0] == 'Delete file successed.':
                redis_client.hdel('job:%s:output' % job_conf['name'], item[0])
        except:
            pass
    print('清空远程作业输出文件...ok')

    # 清空远程解析波形文件
    for item in redis_client.hscan_iter('job:%s:wave:blocks:files' % job_conf['name']):
        try:
            result = fdfs_client.delete_file(item[1].encode())
            if result[0] == 'Delete file successed.':
                redis_client.hdel('job:%s:wave:blocks:files' % job_conf['name'], item[0])
        except:
            pass
    print('清空远程作业波形文件...ok')

    # 获取本地作业文件
    if 'files' in job_conf:
        job_files = []
        for f in job_conf['files']:
            job_files.extend(glob.glob(f))

        # 上传作业文件到fdfs
        for f_name in job_files:
            try:
                result = fdfs_client.upload_by_filename(f_name)
                if 'Status' in result and result['Status'] == 'Upload successed.':
                    remote_file_id = result['Remote file_id'].decode()
                    redis_client.hset('job:%s:files' % job_conf['name'], f_name, remote_file_id)
            except:
                pass
    print('上传本地作业文件到远程...ok')

    # 保存配置文件
    redis_client.hset('job:%s:info' % job_conf['name'], 'job_conf', content)
    print('保存作业配置文件到远程...ok')

    # 调用xxl-job-admin
    try:
        # 获取xxl-job的token
        cookie = {}
        body = {
            'userName': 'admin',
            'password': '123456'
        }

        resp = requests.post('%s/login' % xxl_job_admin_url, data=body)
        cookies = resp.cookies
        cookie = requests.utils.dict_from_cookiejar(cookies)
        print('获取xxl-job的cookie...ok')

        xxl_job_id = create_xxl_job(job_conf, cookie)
        print('创建xxl-job任务...ok')
        print('xxl-job任务标识%s' % xxl_job_id)
        if xxl_job_id:
            # 触发xxl-job任务
            body = {
                'id': xxl_job_id,
                'executorParam': job_conf['name'],
                'addressList': ''
            }
            requests.post('%s/jobinfo/trigger' % xxl_job_admin_url, data=body, cookies=cookie)
            print('触发xxl-job任务标识%s执行一次...ok' % xxl_job_id)

    except:
        pass

    return True


# 创建xxl_job
def create_xxl_job(job_conf, cookie):
    job_id = None
    glueSource = """
#!/bin/bash
echo "xxl-job: hello shell"

echo "脚本位置：$0"
echo "任务参数：$1"
echo "分片序号 = $2"
echo "分片总数 = $3"
cd /data
rm -rf $1
mkdir $1
cd $1
python /root/anaconda3/lib/python3.9/site-packages/cocotb_job/executor.py $1
echo "Good bye!"
exit 0
    """
    body = {
        'jobGroup': '1',
        'jobDesc': job_conf['name'],
        'author': 'QXX',
        'alarmEmail': '909263817@qq.com',
        'scheduleType': 'NONE',
        'scheduleConf': '',
        'cronGen_display': '',
        'schedule_conf_CRON': '',
        'schedule_conf_FIX_RATE': '',
        'schedule_conf_FIX_DELAY': '',
        'glueType': 'GLUE_SHELL',
        'executorHandler': '',
        'executorParam': job_conf['name'],
        'executorRouteStrategy': 'RANDOM',
        'childJobId': '',
        'misfireStrategy': 'DO_NOTHING',
        'executorBlockStrategy': 'SERIAL_EXECUTION',
        'executorTimeout': '0',
        'executorFailRetryCount': '0',
        'glueRemark': 'GLUE代码初始化',
        'glueSource': glueSource
    }

    resp = requests.post('%s/jobinfo/add' % xxl_job_admin_url, data=body, cookies=cookie)
    json1 = json.loads(resp.text)
    if json1['code'] == 200:
        job_id = json1['content']
        redis_client.hset('job:%s:info' % job_conf['name'], 'xxl_job_id', job_id)
        redis_client.hset('job:%s:history' % job_conf['name'], job_id, str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

    return job_id


if __name__ == "__main__":
    job_conf_file = sys.argv[1]
    run_job(job_conf_file)


