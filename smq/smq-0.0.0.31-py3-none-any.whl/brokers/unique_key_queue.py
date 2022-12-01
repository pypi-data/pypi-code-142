import uuid
from queue import Queue
from queue import Empty
import threading


lock = threading.Lock()


class UniqueKeyQueue:

    def __init__(self, ack=False):
        self._queue = Queue()
        self._queue_set = set()
        self._dict = {}
        self._ack = ack

    def put(self, key, data):
        try:
            lock.acquire()
            if key not in self._queue_set:
                _qid = str(uuid.uuid1())
                self._queue.put((data, _qid, key))
                self._queue_set.add(key)
                self._dict[_qid] = data
                return _qid
            return None
        finally:
            lock.release()

    def put_batch(self, data_list):
        qid_list = [self.put(key, data) for key, data in data_list]
        return qid_list

    def get(self, block=False, timeout=None):
        try:
            lock.acquire()
            data, qid, key = self._queue.get(block=block, timeout=timeout)
            self._queue_set.remove(key)
            if not self._ack:
                del self._dict[qid]
            return data, qid
        except Empty:
            return None, None
        finally:
            lock.release()

    def get_batch(self, block=False, timeout=None, num=1000):
        data_list = []
        try:
            lock.acquire()
            while len(data_list) < num:
                data, qid, key = self._queue.get(block=block, timeout=timeout)
                self._queue_set.remove(key)
                if not self._ack:
                    del self._dict[qid]
                data_list.append((data, qid))
        except Empty:
            pass
        finally:
            lock.release()
        return data_list

    def ack(self, qid):
        if not self._ack:
            return True
        if qid is None:
            return False
        del self._dict[qid]
        return True

    def queue_size(self):
        return self._queue.qsize()

    def set_size(self):
        return len(self._queue_set)

    def dict_size(self):
        return len(self._dict)

    def clear(self):
        try:
            lock.acquire()
            self._queue.queue.clear()
            self._queue_set.clear()
            self._dict.clear()
        finally:
            lock.release()