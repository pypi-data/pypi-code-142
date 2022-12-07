import json 
from websocket import create_connection

class ArgvData:
    def __init__(self,argv):
        self.argv = argv
        
    def get(self, key):
        try: return self.argv[key]
        except: return None

class WebsocketClientMessage:
    def __init__(self):
        self.subject = None
        self.sender = None
        self.topics = []
        self.payload = None
        self.persist = False
    
    
        
    @staticmethod
    def set(topics, payload, persist=False, subject="safebox", sender="safebox"):
        try:
            obj = WebsocketClientMessage()
            obj.subject = subject
            obj.sender = sender
            obj.topics = topics
            obj.payload = payload
            obj.persist = persist
            return obj
        except Exception as e:
            print(f'[ERROR] Error in WebsocketClientMessage =>  {e}')
            return WebsocketClientMessage()
    
    @staticmethod
    def fromArgv(argv):
        try:
            argv = ArgvData(argv)
            obj = WebsocketClientMessage()
            topics = argv.get(5).split(",") or []
            obj.subject = argv.get(3)
            obj.sender = argv.get(4)
            obj.topics = topics
            obj.payload = argv.get(2)
            obj.persist = False
            return obj
        except Exception as e:
            print(f'[ERROR] Error in WebsocketClientMessage =>  fromArgv => {e}')
            return WebsocketClientMessage()
    
    @staticmethod
    def fromRecv(message_text):
        try:
            data = json.loads(message_text) 
            obj = WebsocketClientMessage()
            obj.subject = data.get('subject')
            obj.sender = data.get('sender')
            obj.topics = data.get('topics')
            obj.payload = data.get('payload')
            return obj
        except Exception as e:
            print(f'[ERROR] Error in WebsocketClientMessage =>  {e}')
            return WebsocketClientMessage()
    
    def toDict(self):
        return {
            "subject" : self.subject,
            "sender" : self.sender,
            "topics" : self.topics,
            "payload" : self.payload,
            "persist": self.persist,
        }

class WebsocketClientSender():
    def __init__(self, message:WebsocketClientMessage, server_location: str):
        self.__message__ = message
        self.__config__ = server_location
    
    def send(self):
        try:
            print(f"[INFO] Enviando mensagem de {self.__message__.sender}...")
            ws = create_connection(f"{self.__config__}?hashcode={self.__message__.sender}&topics=system")
            ws.send(json.dumps(self.__message__.toDict(), indent=4))
            ws.close()
        except Exception as e:
            print("[ERROR] Erro ao enviar notificação => %s" %str(e))
    
    

class WebsocketClientReceiver():
    def __init__(self, server_location: str, topic:str):
        self.__server_location__ = server_location
        self.__topic__ = topic
        
    @staticmethod
    def fromArgv(argv):
        try:
            argv = ArgvData(argv)
            obj = WebsocketClientReceiver(argv.get(1),argv.get(2))
            return obj
        except Exception as e:
            print(f'[ERROR] Error in WebsocketClientReceiver =>  fromArgv => {e}')
    
    def receiver(self):
        ws = create_connection(f"{self.__server_location__}?hashcode=receiver&topics={self.__topic__}")
        try:
            print(f"[INFO] Recebendo mensagem de {self.__topic__}...")
            while(1):
                res = ws.recv()
                print(f"[MESSAGE] => \n{res}")
            ws.close()
        except KeyboardInterrupt:
            ws.close()
        except Exception as e:
            print("[ERROR] Erro ao enviar notificação => %s" %str(e))