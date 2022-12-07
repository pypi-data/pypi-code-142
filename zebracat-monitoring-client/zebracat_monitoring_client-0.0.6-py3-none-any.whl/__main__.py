import psutil
import requests
import os
import subprocess as sp

server = os.environ.get("SERVER_ADDRESS")
cpu_sens_id = os.environ.get("CPU_SENS")
memory_sens_id = os.environ.get("MEMORY_SENS")


def send(sensor_no, value):
    try:
        requests.post(url=f"{server}/log/set_data/", data={
            "value": value,
            "sens_id": sensor_no
        })
    except:
        pass


def get_gpu():
    output_to_list = lambda x: x.decode('ascii').split('\n')[:-1]
    COMMAND = "nvidia-smi --query-gpu=utilization.gpu --format=csv"
    try:
        gpu_use_info = output_to_list(sp.check_output(COMMAND.split(), stderr=sp.STDOUT))[1:]
        gpu_use_values = [int(x.split()[0]) for i, x in enumerate(gpu_use_info)]
        return gpu_use_values
    except Exception as e:
        return 0


def run():
    send(sensor_no=int(cpu_sens_id), value=psutil.cpu_percent(4))
    send(sensor_no=int(memory_sens_id), value=psutil.virtual_memory()[2])
    # print(get_gpu())


if __name__ == '__main__':
    while True:
        run()
