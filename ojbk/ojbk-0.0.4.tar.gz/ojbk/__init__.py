#!/usr/bin/env python
import datetime
import json
from typing import Dict, List, Optional, Set, Tuple

import codefast as cf
from authc import get_redis


class Base(object):
    pass


class Messager(object):
    def post(self, msg: Dict):
        pass


class MessageQueue(Messager):
    def __init__(self) -> None:
        super().__init__()
        self.queue = get_redis()
        self.name = '__MessageQUEUE__'

    def post(self, msg: Dict):
        self.queue.lpush(self.name, json.dumps(msg))

    def popall(self) -> List[Dict]:
        """ Get all messages from queue. 
        """
        results = []
        while True:
            msg = self.queue.lpop(self.name)
            if msg:
                results.append(json.loads(msg))
            if self.queue.llen(self.name) == 0:
                break
        return results

    def getall(self) -> List[Dict]:
        """ Get all messages from queue. 
        """
        return self.queue.lrange(self.name, 0, -1)


class EventReporter(object):
    def __init__(self, messager: Messager) -> None:
        self.messager = messager

    def report(self, msg: Dict) -> bool:
        self.messager.post(msg)


class TaskReporter(EventReporter):
    def __init__(self, task_name: str,
                 messager: Messager = MessageQueue()) -> None:
        super().__init__(messager)
        self.task_name = task_name

    def collect_info(self) -> dict:
        hostname = cf.shell('hostname')
        date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return {
            'task_name': self.task_name,
            'hostname': hostname,
            'date': date
        }


def report_self(name: str) -> bool:
    """
    Args: 
        name, the name of the task.
    """
    tr = TaskReporter(name)
    tr.report(tr.collect_info())


def report_self_cli() -> bool:
    """
    """
    import sys
    name = sys.argv[1]
    cf.info('report self: {}'.format(name))
    report_self(name)
    cf.info('report self done.')


if __name__ == '__main__':
    pass
