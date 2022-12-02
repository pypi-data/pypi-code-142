import grpc
from . import ZoneSenderData
from .Protos import UdsOnCanTP_pb2, UdsOnCanTP_pb2_grpc


class CanUdsNodeClient(object):
    def __init__(self):
        self._udsStub = UdsOnCanTP_pb2_grpc.UdsOnCanTPStub(
            channel=grpc.insecure_channel(
                target=f'{ZoneSenderData.CAN_UDS_NODE_IP}:{ZoneSenderData.CAN_UDS_NODE_PORT}',
                options=ZoneSenderData.GRPC_OPTIONS
            )
        )

    def generate_key(self, seed: list, algorithm_number=0x4F):
        try:
            res_ = self._udsStub.generate_key(UdsOnCanTP_pb2.request_para(
                seed_value=seed,
                algorithm_number=algorithm_number,
            ))
            print(f'seed:{seed}, algorithm_number:{algorithm_number}')
            return res_.key_value
        except Exception as e:
            print(e)
            return [0x00, 0x00, 0x00, 0x00]