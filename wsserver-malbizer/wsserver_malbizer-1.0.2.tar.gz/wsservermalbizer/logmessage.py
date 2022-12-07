from datetime import datetime

class LogMessage:
    def __init__(self, message):
        self.__dt__ = datetime.now().strftime(" %d-%m-%Y %H:%M:%S -> ")
        self.__message__ = message
        print(self.getMessage())
        
    def getMessage(self):
        return f"{self.__dt__}{self.__message__}"
        
    def __str__(self) -> str:
        return self.getMessage()