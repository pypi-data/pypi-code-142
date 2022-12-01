from multiprocessing.managers import BaseManager
from .common.protocol import DEFAULT_SIMPLE_AGENT_NAME
from .common.protocol import DEFAULT_UNIQUE_KEY_AGENT_NAME
from .clients.simple_client import SimpleClient
from .clients.unique_key_client import UniqueKeyClient
from register_manager import RegisterManager
from loguru import logger


class ClientFactory:

	def __init__(self, host, port, authkey):
		logger.debug(f'client factory init host={host}, port={port}')
		self._register_manager = RegisterManager(host, port, authkey)

	def create_simple_client(self, topic_name):
		simple_client = SimpleAgentClient(self._simple_agent, topic_name)
		return simple_client

	def create_unique_key_client(self, topic_name):
		unique_key_client = UniqueKeyAgentClient(self._unique_key_agent, topic_name)
		return unique_key_client
