from collections import OrderedDict
from typing import Optional, List

import tornado.locks


from tornado_replay.models import RequestRecord


class InspectHttpBuffer:
    __slots__ = ['cond', 'cache', 'cache_size']

    def __init__(self, record_size: int = 10):
        self.cond = tornado.locks.Condition()
        self.cache: OrderedDict[str, RequestRecord] = OrderedDict()
        self.cache_size = record_size

    def get_record_by_request_id(self, request_id: str) -> Optional[RequestRecord]:
        return self.cache.get(request_id)

    def get_record_after_request_id(self, last_request_id: str) -> List[RequestRecord]:
        """Returns a list of record newer than the given cursor.

        ``last_request_id`` should be the ``request_id`` of the last record received.
        """
        keys = list(self.cache.keys())
        values = list(self.cache.values())
        if not last_request_id or (last_request_id not in keys):
            # First request / Wrong cursor, Return All
            return values

        index = keys.index(last_request_id)
        return values[index + 1:]

    def add_record(self, record: RequestRecord):
        self.cache[record.request_id] = record
        overflow = len(self.cache) - self.cache_size
        for _ in range(overflow):
            self.cache.popitem(last=False)
        self.cond.notify_all()

    def clear(self):
        self.cache.clear()
        self.cond.notify_all()


global_inspect_buffer = InspectHttpBuffer()
