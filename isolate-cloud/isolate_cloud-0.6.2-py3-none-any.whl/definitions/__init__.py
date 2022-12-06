from google.protobuf.json_format import MessageToDict as struct_to_dict
from google.protobuf.struct_pb2 import Struct

# Imitates how includes in our protobuf files are handled.
from isolate.connections.grpc.definitions import *
from isolate.server.definitions import *

from isolate_cloud.definitions.controller_pb2 import *
from isolate_cloud.definitions.controller_pb2_grpc import (
    IsolateControllerServicer,
    IsolateControllerStub,
)
from isolate_cloud.definitions.controller_pb2_grpc import (
    add_IsolateControllerServicer_to_server as register_controller,
)
