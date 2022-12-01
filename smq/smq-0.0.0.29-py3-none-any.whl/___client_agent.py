import time
import traceback
# from multiprocessing.managers import BaseManager
# from multiprocessing.managers import BaseProxy
# from .common.protocol import DEFAULT_SIMPLE_AGENT_NAME
# from .common.protocol import DEFAULT_UNIQUE_KEY_AGENT_NAME
# from .clients.simple_agent_client import SimpleAgentClient
# from .clients.unique_key_agent_client import UniqueKeyAgentClient
from loguru import logger


class ClientAgent:

    def __init__(self, client_manager, topic_name):
        self._client_manager = client_manager
        self._topic_name = topic_name

    def rebind(self):
        self._client_manager.rebind()


class SimpleClientAgent(ClientAgent):

    def send(self, data):
        qid = self._client_manager.create_simple_client(self._topic_name).put(self._topic_name, data)
        return qid

    def receive(self):
        data, qid = self._client_manager.create_simple_client(self._topic_name).get(self._topic_name)
        return data, qid

    def commit(self, qid):
        result = self._client_manager.create_simple_client(self._topic_name).ack(self._topic_name, qid)
        return result

    def send_batch(self, data_list: list):
        qid_list = self._client_manager.create_simple_client(self._topic_name).put_batch(self._topic_name, data_list)
        return qid_list

    def receive_batch(self, max_num):
        return self._client_manager.create_simple_client(self._topic_name).get_batch(self._topic_name, max_num)

    def commit_batch(self, qid_list):
        results = [self._client_manager.create_simple_client(self._topic_name).ack(self._topic_name, qid) for qid in qid_list]
        return results

