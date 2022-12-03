
import _config

class A:
    
    def __init__(self) -> None:
        print("initial class A")
        
    def fun(self):
        print("called function!")
        print(_config._SHOULD_LOG_SCOPE)