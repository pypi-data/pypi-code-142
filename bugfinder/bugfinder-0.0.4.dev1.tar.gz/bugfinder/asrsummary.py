#!/usr/bin/env python
import codefast as cf
import pandas as pd
from typing import List, Union, Callable, Set, Dict, Tuple, Optional

from codefast.patterns.pipeline import Pipeline, Component
import redis


class ASRRecordCollector(Component):
    def process(self, logfile: str) -> List[Dict]:
        self.print_log = False
        records = []
        with open(logfile, 'r') as f:
            for line in f:
                if 'POST /api/transcript' not in line:
                    continue
                date_str = line.split(']')[0].replace('[', '')
                date = pd.to_datetime(date_str)
                now = pd.Timestamp.now()
                seconds_diff = (now - date).total_seconds()
                if seconds_diff > 600000:
                    continue
                data = line
                records.append(data)
        return records


class PostedRecordFilter(Component):
    def process(self, records: List[Dict]) -> List[Dict]:
        acc = cf.js('/data/redis_account.json')
        cli = redis.Redis(host=acc['host'], port=acc['port'], password=acc['password'])
        pipe = cli.pipeline()
        for record in records:
            pipe.sadd('asr_records', record)
        pipe.execute()


class RecordPoster(Component):
    def process(self, records: List[Dict]) -> None:
        self.print_log=False
        acc = cf.js('/data/redis_account.json')
        cli = redis.Redis(host=acc['host'], port=acc['port'], password=acc['password'])
        pipe = cli.pipeline()
        for record in records:
            pipe.sadd('asr_records', record)
        pipe.execute()
        return records


class Summary(object):
    def __init__(self, data: pd.DataFrame):
        self.data = data

    def _date(self) -> str:
        pass

    def total_duration(self) -> str:
        pass

    def total_number(self) -> str:
        pass


def save_record() -> str:
    pipeline = Pipeline([
        ASRRecordCollector(),
        RecordPoster()
    ])
    pipeline.process('/tmp/serving.log')

# msg = {
#         "summary": "date 日期",
#         "details": {
#             "转录总时长": "This is the model used",
#             "较昨日增长": "",
#             "转录任务次数": "This is the dataset used",
#             "extra": ""
#         }
#     }


if __name__ == '__main__':
    pipeline = Pipeline([
        ASRRecordCollector(),
        RecordPoster()
    ])
    pipeline.process('/tmp/serving.log')
