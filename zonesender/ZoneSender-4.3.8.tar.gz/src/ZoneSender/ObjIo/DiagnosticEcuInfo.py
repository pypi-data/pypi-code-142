from .ZoneSenderObject import ZoneSenderObject


class DiagnosticEcuInfo(ZoneSenderObject):
    def __init__(self, ecu_name: str, channel: int, request_id: int, response_id: int, function_id: int):
        super().__init__()
        self.ecu_name = ecu_name
        self.channel = channel
        self.request_id = request_id
        self.response_id = response_id
        self.function_id = function_id

    def __str__(self):
        return f'{self.ecu_name} channel: {self.channel}, request_id: {self.request_id}, response_id: {self.response_id}, function_id: {self.function_id}'
