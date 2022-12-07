import json
from .logmessage import LogMessage 

class WebsocketMessage:
    def __init__(self):
        self.subject = None
        self.sender = None
        self.topics = []
        self.payload = None
        self.persist = False
    
    @staticmethod
    def fromRecv(message_text):
        try:
            data = json.loads(message_text) 
            obj = WebsocketMessage()
            obj.subject = data.get('subject')
            obj.sender = data.get('sender')
            obj.topics = data.get('topics')
            obj.payload = data.get('payload')
            obj.persist = data.get('persist')
            return obj
        except Exception as e:
            LogMessage(f'[ERROR] Error in WebsocketMessage =>  {e}')
            return WebsocketMessage()
    
    def toDict(self):
        return {
            "subject" : self.subject,
            "sender" : self.sender,
            "topic" : self.topics,
            "payload" : self.payload,
            "persist" : self.persist,
        }