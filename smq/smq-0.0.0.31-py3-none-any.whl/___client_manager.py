import time
import traceback
from multiprocessing.managers import BaseManager
from multiprocessing.managers import BaseProxy
from .common.protocol import DEFAULT_SIMPLE_AGENT_NAME
from .common.protocol import DEFAULT_UNIQUE_KEY_AGENT_NAME
from .clients.simple_topic_agent import SimpleTopicAgent
from .clients.unique_key_topic_agent import UniqueKeyTopicAgent
from loguru import logger


class ClientManager:

    def __init__(self, register_manager):
        self._register_manager = register_manager
        # self._simple_topics = {}
        # self._unique_key_topics = {}

    def simple_topic(self):
        return self._register_manager.get_simple_topic()

    def unique_key_topic(self):
        return self._register_manager.get_unique_key_topic()

    def rebind(self):
        self._register_manager.reconnect()
        # for _topic, _client in self._simple_topics.items():
        #     self._simple_topics[_topic] = SimpleTopicAgent(self._register_manager.get_simple_agent(), _topic)
        # for _topic, _client in self._unique_key_topics.items():
        #     self._unique_key_topics[_topic] = UniqueKeyTopicAgent(self._register_manager.get_unique_key_agent(), _topic)

    # def create_simple_topic(self, topic_name):
    #   if topic_name not in self._simple_topics:
    #       simple_topic = SimpleTopicAgent(self._register_manager.get_simple_agent(), topic_name)
    #       self._simple_topics[topic_name] = simple_topic
    #   return self._simple_topics[topic_name]

    # def create_unique_key_topic(self, topic_name):
    #   if topic_name not in self._unique_key_topics:
    #       unique_key_topic = UniqueKeyTopicAgent(self._register_manager.get_unique_key_agent(), topic_name)
    #       self._unique_key_topics[topic_name] = unique_key_topic
    #   return self._unique_key_topics[topic_name]


class SimpleClientManager(ClientManager):

    def __init__(self, register_manager, topic_name):
        super().__init__(register_manager)
        self._topic_name = topic_name
        self.simple_topic().bind(self._topic_name)

    def send(self, data):
        qid = self.simple_topic().put(self._topic_name, data)
        return qid

    def receive(self):
        data, qid = self.simple_topic().get(self._topic_name)
        return data, qid

    def commit(self, qid):
        result = self.simple_topic().ack(self._topic_name, qid)
        return result

    def send_batch(self, data_list: list):
        qid_list = self.simple_topic().put_batch(self._topic_name, data_list)
        return qid_list

    def receive_batch(self, max_num):
        return self.simple_topic().get_batch(self._topic_name, max_num)

    def commit_batch(self, qid_list):
        results = [self.simple_topic().ack(self._topic_name, qid) for qid in qid_list]
        return results

    def rebind(self):
        self._register_manager.reconnect()
        self.simple_topic().bind(self._topic_name)
