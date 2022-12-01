import io
import os
import pathlib
import shelve
import time
import traceback
import typing
import weakref
from dataclasses import dataclass
from datetime import date, datetime, timedelta
from threading import Thread
from types import FunctionType

from .utils import logger

HERE = os.path.dirname(os.path.abspath(__file__))


@dataclass
class Task:
    function: FunctionType
    start_at: datetime
    interval: timedelta

    def __post_init__(self):
        self.task_id = self.function.__name__


class Stream:
    def __init__(self):
        self.lines = []

    def print_(self, *a, **kw):
        stream = io.StringIO()
        kw["file"] = stream
        print(*a, **kw)
        self.lines.extend(stream.getvalue().split("\n"))

    def next_line(self):
        if not self.lines:
            return None
        line = self.lines[0]
        self.lines = self.lines[1:]
        return line


class LogWriter(Thread):
    def __init__(self, prefix, stream):
        super().__init__()
        self.prefix = prefix
        self.stream = stream
        self.daemon = True

    def run(self):
        while True:
            line = self.stream.next_line()
            if line is None:
                time.sleep(0.001)
                continue
            if line.strip() == "_DONE_":
                break
            logger.info(f"{self.prefix}{line.rstrip()}")


def run_task(task):
    logger.info(f"{task.task_id:15s} - start task")
    out_stream = Stream()

    lout = LogWriter(f"{task.task_id:15s} - ", out_stream)
    lout.start()
    try:
        task.function(print=out_stream.print_)
    except Exception:
        for line in traceback.format_exc().split("\n"):
            print(line.rstrip())
    finally:
        out_stream.print_("_DONE_")
        lout.join()
    logger.info(f"{task.task_id:15s} - finished task")


class Scheduler:
    def __init__(self, store: typing.Union[str, pathlib.Path]):
        self.tasks = []
        self.next_execution = shelve.open(store, writeback=True)
        weakref.finalize(self, self.next_execution.close)

    def schedule(self, task):
        self.tasks.append(task)
        if task.task_id not in self.next_execution:
            self.next_execution[task.task_id] = task.start_at

    def run(self, until: typing.Optional[datetime] = None):
        while until is None or datetime.now() < until:
            for task in self.tasks:
                if datetime.now() >= self.next_execution[task.task_id]:
                    self.start_task(task)
                    self.next_execution[task.task_id] += task.interval
                    self.next_execution.sync()
            time.sleep(0.1)

    def start_task(self, task):
        t = Thread(target=run_task, args=(task,))
        t.daemon = True
        t.start()


def next_date(week_day):
    d = date.today()

    while d.strftime("%a") != week_day:
        d += datetime.timedelta(1)

    return d
