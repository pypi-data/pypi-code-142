from multiprocessing.managers import BaseManager
from .common.protocol import DEFAULT_SIMPLE_AGENT_NAME
from .common.protocol import DEFAULT_UNIQUE_KEY_AGENT_NAME
from .clients.simple_agent_client import SimpleAgentClient
from .clients.unique_key_agent_client import UniqueKeyAgentClient
from loguru import logger


# 20221130作废，别用了
class ClientFactory:

	def __init__(self, host, port, authkey):
		logger.debug(f'client factory init host={host}, port={port}')
		BaseManager.register(DEFAULT_SIMPLE_AGENT_NAME)
		BaseManager.register(DEFAULT_UNIQUE_KEY_AGENT_NAME)
		m = BaseManager(address=(host, port), authkey=authkey)
		m.connect()
		self._unique_key_agent = getattr(m, DEFAULT_UNIQUE_KEY_AGENT_NAME)()
		self._simple_agent = getattr(m, DEFAULT_SIMPLE_AGENT_NAME)()

	def create_simple_client(self, topic_name):
		simple_client = SimpleAgentClient(self._simple_agent, topic_name)
		return simple_client

	def create_unique_key_client(self, topic_name):
		unique_key_client = UniqueKeyAgentClient(self._unique_key_agent, topic_name)
		return unique_key_client
