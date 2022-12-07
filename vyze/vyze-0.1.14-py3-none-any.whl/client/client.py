from ..service import ServiceClient
from ..system import SystemClient


class Client:

    def __init__(self, service_client: ServiceClient, system_client: SystemClient):
        self.system_client = system_client
        self.service_client = service_client

    def get_objects(self, pipe):
        pipe.load_pipe(self.universe)
        list_node = self.service_client.universe.resolve_node(pipe.list_node())
        return self.system_client.get_node(list_node)

    def get_object(self, pipe):
        pipe.load_pipe(self.universe)
        object_node = self.service_client.universe.resolve_node(pipe.object_node())
        return self.system_client.get_node(object_node)

    def put_objects(self, pipe, values, access_name='main_full'):
        pipe.load_pipe(self.universe)
        list_node = self.service_client.universe.resolve_node(pipe.list_node())
        return self.system_client.put_node(list_node, values, access_name)

    def put_object(self, pipe, value, access_name='main_full'):
        pipe.load_pipe(self.universe)
        object_node = self.service_client.universe.resolve_node(pipe.object_node())
        return self.system_client.put_node(object_node, value, access_name)

    @property
    def universe(self):
        return self.service_client.universe
