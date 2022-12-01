from loguru import logger
from .simple_queue import SimpleQueue


class SimpleTopicAgent:

    _topics = {}

    _instance = None

    def __new__(cls, *args, **kwargs):
        # If no instance of class already exits
        if cls._instance is None:
            cls._instance = object.__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, *args, **kwargs):
        if self._initialized:
            return
        # set the attribute to `True` to not initialize again
        self._initialized = True

    def bind(self, topic_name):
        if topic_name in self._topics:
            logger.debug(f'topic name {topic_name} already exist')
            return False
        self._topics[topic_name] = SimpleQueue()
        return True

    def put(self, topic_name, data):
        q = self._topics[topic_name]
        qid = q.put(data)
        logger.debug(f'topic: {topic_name}, put data: {data}, qid: {qid}')
        return qid

    def put_batch(self, topic_name, data_list):
        q = self._topics[topic_name]
        qid_list = q.put_batch(data_list)
        logger.debug(f'topic: {topic_name}, put data_list: {data_list}, qid_list: {qid_list}')
        return qid_list

    def get(self, topic_name):
        q = self._topics[topic_name]
        data, qid = q.get()
        if data is None:
            logger.debug(f'topic: {topic_name}, get data: {data}, qid: {qid}')
        else:
            logger.debug(f'topic: {topic_name}, get data: {data}, qid: {qid}')
        return data, qid

    def get_batch(self, topic_name, num=1000):
        q = self._topics[topic_name]
        data_list = q.get_batch(num=num)
        logger.debug(f'topic: {topic_name}, return data len{len(data_list)}')
        return data_list  # [(data1, qid1), (data2, qid2)]

    def ack(self, topic_name, qid):
        q = self._topics[topic_name]
        result = q.ack(qid)
        logger.debug(f'topic: {topic_name}, ack qid: {qid}')
        return result

    def info(self, ):
        desp = {name: f'queue size = {q.queue_size()}, dict size = {q.dict_size()}' for name, q in self._topics.items()}
        return desp

    def clear(self,):
        for _name, _queue in self._topics.items():
            _queue.clear()
        # self._topics.clear()
        return True
