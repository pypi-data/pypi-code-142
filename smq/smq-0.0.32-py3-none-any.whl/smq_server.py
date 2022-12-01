import sys
import time
from multiprocessing.managers import BaseManager
from .brokers.simple_topic import SimpleTopic
from .brokers.unique_key_topic import UniqueKeyTopic
from flask import Flask
from flask import jsonify
from flask import redirect
from .common.protocol import DEFAULT_SIMPLE_AGENT_NAME
from .common.protocol import DEFAULT_UNIQUE_KEY_AGENT_NAME
from loguru import logger
import threading
import psutil

logger.remove()
# logger.add(sys.stderr, level='DEBUG')
logger.add('./_info.log', level='INFO')

global_info = {}

def net_io_total_bytes():
    total_sent = 0
    total_received = 0
    net = psutil.net_io_counters(pernic=True)
    for k in net.keys():
        if k != 'lo0':
            total_sent += net[k].bytes_sent
            total_received += net[k].bytes_recv
    return total_sent, total_received

def monitor_info():
    while True:
        try:
            last_total_sent, last_total_received = net_io_total_bytes()
            time.sleep(1)
            now_total_sent, now_total_received = net_io_total_bytes()
            sent_bytes = now_total_sent - last_total_sent
            received_bytes = now_total_received - last_total_received
            # 查看cpu物理个数的信息
            cpu_count = psutil.cpu_count(logical=False)
            # CPU的使用率
            cpu_percent = psutil.cpu_percent(1)
            # 查看cpu逻辑个数的信息
            cpu_count_logical = psutil.cpu_count(logical=True)
            # 内存
            mem = psutil.virtual_memory()
            # 系统总计内存
            mem_total = float(mem.total) / 1024 / 1024 / 1024
            # 系统已经使用内存
            mem_used = float(mem.used) / 1024 / 1024 / 1024
            # 系统空闲内存
            mem_free = float(mem.free) / 1024 / 1024 / 1024
            mem_used_percent = mem[2]
            # 磁盘使用率
            disk_used_percent = psutil.disk_usage('/').percent
            dist_io = psutil.disk_io_counters()
            global_info['物理CPU个数'] = f'{cpu_count}'
            global_info['逻辑CPU个数'] = f'{cpu_count_logical}'
            global_info['CPU使用率'] = f'{cpu_percent:.2f}%'
            global_info['系统总计内存'] = f'{mem_total:.2f}GB'
            global_info['系统已经使用内存'] = f'{mem_used:.2f}GB'
            global_info['系统空闲内存'] = f'{mem_free:.2f}GB'
            global_info['内存使用占比'] = f'{mem_used_percent:.2f}%'
            global_info['磁盘使用占比'] = f'{disk_used_percent:.2f}%'
            global_info['流量出'] = f'{(sent_bytes / 1024 * 8):.2f}Kbps'
            global_info['流量入'] = f'{(received_bytes / 1024 * 8):.2f}Kbps'
        except Exception as e:
            logger.error(f'monitor_info error, {e}')
        finally:
            time.sleep(1)

t = threading.Timer(1, monitor_info)
t.start()

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_MIMETYPE'] = 'application/json;charset=utf-8'

unique_key_agent = UniqueKeyTopic()
simple_agent = SimpleTopic()

@app.route('/')
def index():
    resp = {
        'Info': global_info,
        'Topics': {
            'UniqueKeyAgent': unique_key_agent.info(),
            'SimpleAgent': simple_agent.info(),
        }
    }
    return jsonify(resp)

@app.route('/clear')
def clear():
    unique_key_agent.clear()
    simple_agent.clear()
    return redirect('/')


class QueueManager(BaseManager):
    pass


QueueManager.register(DEFAULT_SIMPLE_AGENT_NAME, SimpleTopic)
QueueManager.register(DEFAULT_UNIQUE_KEY_AGENT_NAME, UniqueKeyTopic)


class SmqServer():


    def __init__(self, api_port, queue_port, auth_key, log_level='INFO'):
        self._api_port = api_port
        self._queue_port = queue_port
        self._auth_key = auth_key
        logger.add(sys.stderr, level=log_level)

    def run(self):
        threading.Thread(target=lambda: app.run(host='0.0.0.0', port=self._api_port, debug=True, use_reloader=False), daemon=True).start()
        m = QueueManager(address=('0.0.0.0', self._queue_port), authkey=self._auth_key)
        s = m.get_server()
        s.serve_forever()


if __name__ == '__main__':
    smq_server = SmqServer(55555, 44444, b'abr')
    smq_server.run()
