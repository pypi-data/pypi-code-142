class KsubscribeSingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Ksubscribe(metaclass=KsubscribeSingletonMeta):
    def __init__(self):
        self.__eventList={}  

    def _subscribeForAnEvent(self,subscriber,eventName:str):
        try:
            if(self.__eventList.get(eventName) != None):
                self.__eventList[eventName].append(subscriber)
            else:
                print("EventBasedFramework : Cannot subscribe an event. Because the event is not exist in event collections")
        except Exception as e:
            print("EventBasedFramework :",e)

    def _createAnEvent(self, eventName:str):
        try:
            if(self.__eventList.get(eventName) == None):
                self.__eventList[eventName] = []
            else:
                print("EventBasedFramework : Cannot create an event. Because the event is exist in event collections")
        except Exception as e:
            print("EventBasedFramework :",e)



    def _fireAnEvent(self,eventName:str):
        try:
            if(self.__eventList.get(eventName) != None):
                for x in self.__eventList[eventName]:
                    x._inform(eventName)
            else:
                print("EventBasedFramework : Cannot subscribe an event. Because the event is not exist in event collections")
        except Exception as e:
            print("EventBasedFramework :",e)