import queue
import subprocess
import threading
import signal
import time
import json
import re
import os

import copy
from decimal import Decimal
from pprint import pprint, pformat
import logging
import datetime


def output_reader(proc, outq, parent):
    for line in iter(proc.stdout.readline, b""):
        outq.put(line.decode("utf-8"))
        parent.line_ready_callback()


class IOPingInstance(object):
    def __init__(self):
        self.type = None
        self.report_interval = "1"
        self.ioping_binary_path = "/usr/bin/ioping"
        self._outq = queue.Queue()
        self._proc = None
        self.server_ip = None
        self.bind_ip = None
        self.name = None
        self._running = False
        self.test_duration="3"
        self.test_path="/tmp/"
        
        self.status = "configured"
        self._results = {}
        self._on_data_callbacks = []
        self._on_error_callbacks = []
        
        self._output_reader_thread = None
        self._cleanup_timer_thread = None

        self._raw_log_filepath = None
        self._raw_log_filehandler = None

        self._creation_time = datetime.datetime.now().replace(microsecond=0).isoformat()

        self._log = logging.getLogger("")
        self._current_event_number = 0
        
        self._current_message=""

    def __del__(self):
        try:
            self._raw_log_filehandler.close()
        except:
            pass

    def set_raw_log_path(self, path):
        self._raw_log_filepath = "{0}{1}{3}_{2}_instance_raw.log".format(
            path, os.path.sep, self.name, self._creation_time
        )
        self._raw_log_filehandler = open(self._raw_log_filepath, "w")

    def message_ready_callback(self):
        
        print(json.loads(f'{{"{self.name}":{self._current_message}}}'))
        pass

    def line_ready_callback(self):
        line = self._outq.get(block=True)
        timestamp = datetime.datetime.now().isoformat()
        if self._raw_log_filehandler:
            self._raw_log_filehandler.write(line)
            self._raw_log_filehandler.flush()
        if line.strip() in ["},{"]:
            self._current_message+="}"
            self.message_ready_callback()
            self._current_message="{"
        elif line.strip() in ["[{"]:
            self._current_message="{"
        elif line.strip() in ["}]"]:
            self._current_message+="}"
            self.message_ready_callback()
        else:
            self._current_message+=line

    def get_result_events(self):
        pass

    def register_on_data_callback(self, cb, **kwargs):
        self._on_data_callbacks.append((cb, kwargs))

    def register_on_packtetloss_callback(self, cb, **kwargs):
        self._on_packetloss_callbacks.append((cb, kwargs))

    @property
    def get_name(self):
        if not self.name:
            raise ValueError("ioping instance needs a name")
        return self.name

    def output_reader(self):
        for line in iter(self._proc.stdout.readline, b""):
            self._outq.put(line.decode("utf-8"))

    def set_options(self, **kwargs):
        for option_name, option_value in kwargs.items():
            self.__setattr__(option_name, str(option_value))


    def get_options(self):
        retval = {}
        for k, v in self.__dict__.items():
            if not k.startswith("_"):
                retval[k] = v
        return retval

    def generate_cli_from_options(self):
        _cli = []
        _cli.append(self.ioping_binary_path)
        _cli.append("-J") # always use json
        
        _cli.append(self.test_path)
        
        # not yet implemented
        return _cli

    def start(self, create_thread_function=threading.Thread):
        self._results = {}
        if self._cleanup_timer_thread:
            self._cleanup_timer_thread.join()
            del self._cleanup_timer_thread
            self._cleanup_timer_thread = None
        
        self._proc = subprocess.Popen(
            self.generate_cli_from_options(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        if not self._output_reader_thread:
            self._output_reader_thread = create_thread_function(
                target=output_reader, args=(self._proc, self._outq, self)
            )

        self._output_reader_thread.start()
        self._running = True
        self.status = "running"
        time.sleep(0.2)
        if int(self.test_duration) > 0:
            self._cleanup_timer_thread = threading.Timer(
                int(self.test_duration) , self.stop
            )
            self._cleanup_timer_thread.start()
        poll_result=self._proc.poll()
        if poll_result is not None:
            msg=""
            for line in iter(self._proc.stderr.readline, b""):
                msg+=line.decode('utf-8')
            self._log.error(msg)
            self.stop()
            return poll_result

        return True

    def stop(self):
        if self._running:
            self._proc.send_signal(signal.SIGINT)
            time.sleep(0.1)
            self._proc.terminate()
            self._proc.wait()
            del self._proc
            self._proc = None
            self._output_reader_thread.join()
            del self._output_reader_thread
            self._output_reader_thread = None
            self._running = False
            self.status = "stopped"
            if self._raw_log_filehandler:
                self._raw_log_filehandler.close()
        return True

    def get_results(self):
        return self._results




test2 = IOPingInstance()
test2.set_options(name=1,test_path="/tmp",interval=0.1)
test2.start()


test = IOPingInstance()
test.set_options(name=2,test_path="/home/putzw/test/mnt",interval=0.1)
test.start()
