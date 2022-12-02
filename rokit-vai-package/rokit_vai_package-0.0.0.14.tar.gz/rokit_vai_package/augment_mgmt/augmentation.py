from abc import *


class Augmentation(metaclass=ABCMeta):
    def __init__(self, global_variable, log):
        self.gv = global_variable
        self.log = log
    
    @abstractmethod
    def execute():
        pass