from .ZoneSenderObject import ZoneSenderObject


class CanDiagMessage(ZoneSenderObject):
    def __init__(self, id: int, cmd: list, dlc=8, is_fd=False):
        super().__init__()
        self.id = id
        self.cmd = cmd
        self.dlc = dlc
        self.is_fd = is_fd
