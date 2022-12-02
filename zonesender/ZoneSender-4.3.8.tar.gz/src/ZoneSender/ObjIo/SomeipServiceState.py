from copy import copy
import typing
import copy
from .ZoneSenderObject import ZoneSenderObject


class SomeipServiceState(ZoneSenderObject):
    '''
    SomeipServiceState 对象，用来描述一个 SomeipServiceState
    service_name: 服务名
    service_id: 服务 ID
    instance_id: 服务的 instance_id
    service_state: 该服务的状态
    service_side: 'consumer'|'provider'
    '''
    def __init__(
        self,
        service_name: str = '',
        service_id: int = -1,
        instance_id: int = -1,
        service_state: bool = False,
        service_side: str = ''
        ) -> None:
        # #####################################
        super().__init__()
        self.serviceName = service_name
        self.serviceId = service_id
        self.instanceId = instance_id
        self.serviceState = service_state
        self.serviceSide = service_side

    def __str__(self) -> str:
        # return super().__str__()
        return 'service_name: {0} service_id: {1} instance_id: {2} service_state: {3} service_side: {4}'.format(
            self.serviceName,
            self.serviceId,
            self.instanceId,
            self.serviceState,
            self.serviceSide,
        )