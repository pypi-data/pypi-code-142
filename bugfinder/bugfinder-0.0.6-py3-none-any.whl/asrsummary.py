#!/usr/bin/env python
from pydub.utils import mediainfo as mi
import ast
import codefast as cf
import pandas as pd
from typing import List, Union, Callable, Set, Dict, Tuple, Optional

from codefast.patterns.pipeline import Pipeline, Component
import redis
acc = cf.js('/data/redis_account.json')
cli = redis.Redis(host=acc['host'], port=acc['port'], password=acc['password'])


# msg = {
#         "summary": "date 日期",
#         "details": {
#             "转录总时长": "This is the model used",
#             "较昨日增长": "",
#             "转录任务次数": "This is the dataset used",
#             "extra": ""
#         }
#     }


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
                if seconds_diff > 600:
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
        self.print_log = False
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
    pipeline.process('/log/serving/serving.log')


class GetRedisRecords(Component):
    def process(self):
        records = []
        for r in cli.smembers('asr_records'):
            records.append(r.decode().strip())
        return records


class FilterProcessed(Component):
    def process(self, records: List[str]):
        res = []
        for r in records:
            md5 = cf.md5sum(r)
            if cli.exists(md5):
                cli.srem('asr_records', r)
                cf.info(f'remove processed record {r[:1000]}')
            else:
                res.append(r)
                cf.info(f'keep unprocessed record {r[:1000]}')
        return res


class GetRecordInfo(Component):
    def process(self, records: List[str]):
        res = []
        for r in records:
            try:
                str_date = r.split(']')[0].replace('[', '')
                str_js = r.split('|DATA: ')[1]
                js = ast.literal_eval(str_js)
                cid = js['conversation_id']
                link = js['file_link']
                audio = mi(link)
                cf.info(f'get audio info {js}')
                duration = audio['duration']
                industry_id = js['industry_id']
                md5 = cf.md5sum(r)
                cli.set(md5, 1, ex=3600)
                res.append({'date': str_date, 'conversation_id': cid, 'duration': duration, 'industry_id': industry_id})
            except:
                pass
        return res


class InsertToDB(Component):
    def process(self, records: List[Dict]):
        cli.sadd('asr_records_pruned', *records)
        return []


def clear_asr_records():
    pipeline = Pipeline([
        GetRedisRecords(),
        FilterProcessed(),
        GetRecordInfo(),
        InsertToDB()
    ])
    pipeline.process()
