from decimal import Decimal
import re
import os
import redis
import json
import multiprocessing
from multiprocessing import Pool
import time
from tqdm import trange


# Verilog standard terminology.
_VALUE = set(('0', '1', 'x', 'X', 'z', 'Z'))
_VECTOR_VALUE_CHANGE = set(('b', 'B', 'r', 'R'))

redis_client = redis.Redis(host='192.168.1.48', port=16380, password='knn3.14159', decode_responses=True)


# 文件大小格式化
def size_format(size):
    if size < 1000:
        return '%i' % size + 'Byte'
    elif 1000 <= size < 1000000:
        return '%.1f' % float(size/1000) + 'KB'
    elif 1000000 <= size < 1000000000:
        return '%.1f' % float(size/1000000) + 'MB'
    elif 1000000000 <= size < 1000000000000:
        return '%.1f' % float(size/1000000000) + 'GB'
    elif 1000000000000 <= size:
        return '%.1f' % float(size/1000000000000) + 'TB'


# 确定vcd文件切块信息
def cut_vcd_blocks(vcd_file, job_name):
    blocks = []
    file_size = os.path.getsize(vcd_file)
    f = open(vcd_file, 'rb')
    cur_seek_pos = 0
    block_num = 0
    while True:
        line = f.readline()
        cur_seek_pos = f.tell()
        line = str(line, 'utf-8')
        cur_seek_pos = cur_seek_pos - len(line)
        if line == '':
            break
        line0 = line[0]
        line = line.strip()
        if line == '':
            continue

        if line0 == '#':
            t = int(line[1:])
            block = {
                'id': str(block_num),
                'seek_pos': cur_seek_pos,
                'start_time': t,
                'end_time': -1
            }
            if len(blocks) > 0:
                blocks[block_num-1]['end_time'] = t
            blocks.append(block)
            block_num = block_num + 1

            # 向下跳100M
            seek_next = cur_seek_pos + 1000000 * 100
            if seek_next >= file_size:
                # 查询文件结束时间
                end_time = redis_client.hget('job:%s:wave' % job_name, 'end_time')
                if end_time is not None:
                    block['end_time'] = int(end_time)
                break
            else:
                f.seek(1000000*100, 1)
    f.close()
    # 存到redis
    for block in blocks:
        redis_client.hset('job:%s:wave:blocks:ids' % job_name, block['id'], json.dumps(block))
    redis_client.hset('job:%s:wave' % job_name, 'block_num', len(blocks))
    return blocks


# 获取vcd文件分块指定信号量的波形数据
def load_vcd_block_signal_vals(vcd_file, block, signal_name):
    signal_data = []
    signal_change = {}

    base_dir = os.path.basename(vcd_file).split('.')[0]
    # 读取信号在文件中开始与结束位置
    seek_start = redis_client.hget('wave:%s:blocks:signals' % base_dir, block['id']+'.'+signal_name+'.start')
    seek_end = redis_client.hget('wave:%s:blocks:signals' % base_dir, block['id']+'.'+signal_name+'.end')
    # 读取信号数据文件
    if seek_start and seek_end:
        seek_start = int(seek_start)
        seek_end = int(seek_end)
        signal_file = os.path.join(base_dir, 'b_%s.signal' % block['id'])
        f_signal = open(signal_file, 'rb')
        f_signal.seek(seek_start, 0)
        while True:
            line = f_signal.readline()
            cur_pos = f_signal.tell()
            line = str(line, 'utf-8')
            if cur_pos == seek_end:
                break
            if line == '':
                break
            line = line.strip()
            if line == '':
                continue
            ls = line.split()
            signal_change[ls[0]] = ls[1]
        f_signal.close()

    # 信号默认值
    value = None
    for block_id in range(int(block['id']), -1, -1):
        k = '%s.%s' % (str(block_id), signal_name)
        val = redis_client.hget('wave:%s:blocks:last_signal' % base_dir, k)
        if val is not None:
            value = val
            break

    # 读取时间文件
    block_time_file = os.path.join(base_dir, 'b_%s.time' % block['id'])
    f_block_time = open(block_time_file, 'r')

    while True:
        line = f_block_time.readline()
        if line == '':
            break
        # 判断是否存在
        line = line.strip()
        if line in signal_change:
            value = signal_change[line]
        if value is not None:
            signal_data.append([line, value])
    f_block_time.close()
    return signal_data


# 解析vcd信号变化量
def parse_vcd_change_vals(vcd_file, blocks, signal_ids, job_name, output=''):
    pool = Pool(multiprocessing.cpu_count())
    p = trange(len(blocks))
    for block in blocks:
        pool.apply_async(parse_vcd_signal_change_vals, (vcd_file, block, signal_ids, job_name, output), callback=lambda _: p.update(1), error_callback=lambda _: p.update(1))
    pool.close()
    pool.join()


# 解析vcd文件信号变化值
def parse_vcd_signal_change_vals(vcd_file, block, signal_ids, job_name, output=''):
    base_dir = os.path.basename(vcd_file).split('.')[0]
    # 分块信号数据
    signals_data = {}
    # 分块时间数据
    time_data = []
    # 初始化信号数据
    for signal_id in signal_ids:
        signal_name = signal_ids[signal_id]
        signals_data[signal_name] = []
    # 对于分块0加信号初始值与时间初始值
    # 对于block['id'] == '0'
    if block['id'] == '0':
        # 获取信号初始值
        init_vals = parse_vcd_signal_init_vals(vcd_file)
        # 增加信号初始值
        for signal_id in signal_ids:
            signal_name = signal_ids[signal_id]
            init_value = '0 %s \n' % init_vals[signal_id]
            signals_data[signal_name].append(init_value)
        # 增加时间初始值
        time_data.append('0\n')

    # 打开vcd文件
    f = open(vcd_file, 'rb')
    f.seek(block['seek_pos'])
    cur_time = None
    while True:
        line = f.readline()
        line = str(line, 'utf-8')
        if line == '':
            break
        line0 = line[0]
        line = line.strip()
        if line == '':
            continue
        if line0 == '#':
            cur_time = int(line[1:])
            if cur_time == block['end_time']:
                break
            # time 0在前面已加
            if cur_time != 0:
                time_data.append(line[1:] + '\n')
            else:
                cur_time = None
        elif cur_time is not None and line0 in _VECTOR_VALUE_CHANGE:
            value, identifier_code = line[1:].split()
            signal_name = signal_ids[identifier_code]
            change_val = '%s %s' % (str(cur_time), value) + '\n'
            signals_data[signal_name].append(change_val)
        elif cur_time is not None and line0 in _VALUE:
            value = line0
            identifier_code = line[1:]
            signal_name = signal_ids[identifier_code]
            change_val = '%s %s' % (str(cur_time), value) + '\n'
            signals_data[signal_name].append(change_val)
    f.close()

    # 保存时间数据
    file_time = os.path.join(output, base_dir, 'b_%s.time' % block['id'])
    save_dir = os.path.dirname(file_time)
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    f_time = open(file_time, 'w')
    f_time.writelines(time_data)
    f_time.close()
    redis_client.hset('job:%s:wave:blocks' % job_name, 'b_%s.time' % block['id'], file_time)


    # 保存信号数据
    file_signal = os.path.join(output, base_dir, 'b_%s.signal' % block['id'])
    f_signal = open(file_signal, 'w')
    seek_start = 0
    seek_end = 0
    for signal_id in signal_ids:
        signal_name = signal_ids[signal_id]
        signal_data = signals_data[signal_name]
        if len(signal_data) > 0:
            f_signal.writelines(signal_data)
            seek_end = f_signal.tell()

            # 保存信息的起始位置
            signal_start_name = block['id']+'.'+signal_name+'.start'
            signal_end_name = block['id']+'.'+signal_name+'.end'
            redis_client.hset('job:%s:wave:blocks:signals' % job_name, signal_start_name, seek_start)
            redis_client.hset('job:%s:wave:blocks:signals' % job_name, signal_end_name, seek_end)
            # 设置信号最后变化值
            last_val = signal_data[-1].split()[1]
            signal_last_name = block['id']+'.'+signal_name
            redis_client.hset('job:%s:wave:blocks:last_signal' % job_name, signal_last_name, last_val)

            seek_start = seek_end

    f_signal.close()
    redis_client.hset('job:%s:wave:blocks' % job_name, 'b_%s.signal' % block['id'], file_signal)


# 解析vcd文件信号量初始值
def parse_vcd_signal_init_vals(vcd_file):
    cur_sig_vals = {}
    f = open(vcd_file, 'rb')
    while True:
        line = f.readline()
        line = str(line, 'utf-8')
        if line == '':
            break
        line0 = line[0]
        line = line.strip()
        if line == '':
            continue
        if line0 == '#':
            # 部分vcd文件初始化存在 #0
            t = int(line[1:])
            if t != 0:
                break
        elif line0 in _VECTOR_VALUE_CHANGE:
            value, identifier_code = line[1:].split()
            cur_sig_vals[identifier_code] = value
        elif line0 in _VALUE:
            value = line0
            identifier_code = line[1:]
            cur_sig_vals[identifier_code] = value
    f.close()
    return cur_sig_vals


# 解析vcd文件的信号量
def parse_vcd_signals(vcd_file, job_name):
    signals = {}
    signal_ids = {}
    hier = []
    f = open(vcd_file, 'rb')
    while True:
        line = f.readline()
        line = str(line, 'utf-8')
        if line == '':
            break
        line0 = line[0]
        line = line.strip()
        if line == '':
            continue
        elif '$scope' in line:
            scope_name = line.split()[2]
            hier.append(scope_name)
        elif '$upscope' in line:
            hier.pop()
        elif '$var' in line:
            ls = line.split()
            dentifier_code = ls[3]
            name = ''.join(ls[4:-1])
            path = '.'.join(hier)
            if path:
                reference = path + '.' + name
            else:
                reference = name
            signals[reference] = dentifier_code
            signal_ids[dentifier_code] = reference
        elif '$enddefinitions' in line:
            break
    f.close()
    for signal in signals:
        redis_client.hset('job:%s:wave:signals:info' % job_name, signal, signals[signal])
    for signal_id in signal_ids:
        redis_client.hset('job:%s:wave:signals:ids' % job_name, signal_id, signal_ids[signal_id])
    redis_client.hset('job:%s:wave' % job_name, 'signal_num', len(signals))
    return signals, signal_ids


# 获取vcd文件基本信息
def get_vcd_info(vcd_file, job_name):
    file_size = os.path.getsize(vcd_file)
    file_size = size_format(file_size)

    # 保存到redis
    redis_client.hset('job:%s:wave' % job_name, 'file_size', file_size)
    redis_client.hset('job:%s:wave' % job_name, 'file_path', vcd_file)

    return file_size


# 解析vcd文件时间信息
def parse_vcd_time(vcd_file, job_name):
    begin_time = None
    end_time = None
    time_scale = {}

    first_time = True
    f = open(vcd_file, 'rb')
    while True:
        line = f.readline()
        line = str(line, 'utf-8')
        if line == '':
            break
        line0 = line[0]
        line = line.strip()
        if line == '':
            continue
        if line0 == '#':
            t = int(line[1:])
            if first_time:
                begin_time = t
                first_time = False
                # 定位到文件尾部
                file_size = os.path.getsize(vcd_file)
                if file_size > 1024:
                    seek_pos = -1024*1
                    f.seek(seek_pos, 2)
            end_time = t
        elif '$timescale' in line:
            if not '$end' in line:
                while True:
                    line += " " + str(f.readline(), 'utf-8').strip().rstrip()
                    if '$end' in line:
                        break
            timescale = ' '.join(line.split()[1:-1])
            magnitude = Decimal(re.findall(r"\d+|$", timescale)[0])
            if magnitude not in [1, 10, 100]:
                print("Error: Magnitude of timescale must be one of 1, 10, or 100. "\
                        + "Current magnitude is: {}".format(magnitude))
                exit(-1)
            unit = re.findall(r"s|ms|us|ns|ps|fs|$", timescale)[0]
            factor = {
                "s": '1e0',
                "ms": '1e-3',
                "us": '1e-6',
                "ns": '1e-9',
                "ps": '1e-12',
                "fs": '1e-15',
            }[unit]
            time_scale["timescale"] = magnitude * Decimal(factor)
            time_scale["magnitude"] = magnitude
            time_scale["unit"] = unit
            time_scale["factor"] = Decimal(factor)
    f.close()

    # 保存到redis
    redis_client.hset('job:%s:wave' % job_name, 'begin_time', begin_time)
    redis_client.hset('job:%s:wave' % job_name, 'end_time', end_time)
    redis_client.hset('job:%s:wave' % job_name, 'time_unit', time_scale['unit'])
    redis_client.hset('job:%s:wave' % job_name, 'time_scale', str(time_scale['timescale']))

    return begin_time, end_time, time_scale


if __name__ == '__main__':
    t1 = time.time()
    vcd_file = '/data14/data/ftp/fudan/waveform/test_large.vcd'
    get_vcd_info(vcd_file)
    parse_vcd_time(vcd_file)
    signals, signal_ids = parse_vcd_signals(vcd_file)
    blocks = cut_vcd_blocks(vcd_file)
    parse_vcd_change_vals(vcd_file, blocks, signal_ids, '')
    t2 = time.time() - t1
    print('total time(s)->', t2)