from dataclasses import dataclass

@dataclass
class Connection:
    proto: str
    connectionId: str
    uid: str
    localAddr: str
    remoteAddr: str
    state: str
    pid: str
    exeName: str

    def getVals(self):
        return f'Proto {self.proto}, connection id {self.connectionId}, uid {self.uid}, local address {self.localAddr}, remote address {self.remoteAddr}, state {self.state}, pid {self.pid}, execution name {self.exeName}'

    def __str__(self):
        return f'{self.proto}, {self.connectionId}, {self.uid}, {self.localAddr}, {self.remoteAddr}, {self.state}, {self.pid}, {self.exeName}'

@dataclass
class PacketSocket:
    proto: str
    pid: str
    exeName: str

    def __str__(self):
        return f'{self.proto}, {self.pid}, {self.exeName}'

    def getVals(self):
        return f'Proto {self.proto}, pid {self.pid}, execution name{self.exeName}'
