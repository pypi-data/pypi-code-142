import asyncio
from os import environ
import websockets
import json

from .logmessage import LogMessage
from .websocketmessage import WebsocketMessage 

class ArgsWebsocket:
    def __init__(self):
        self.__values__ = {}
        self.hashcode = None
        self._topics = None    
    
    @property
    def topics(self):
        return self._topics
    
    @topics.setter
    def topics(self, value):
        self._topics = value.split(",") if value else []
    

    @staticmethod
    def fromPath(path):
        try:
            args = ArgsWebsocket()
            args.__values__ = {p.split("=")[0]:p.split("=")[1] for p in path.split("?")[-1].split("&")}
            args.hashcode = args.__values__.get("hashcode")
            args.topics = args.__values__.get("topics")
            return args
        except:
            LogMessage("[ERROR] Invalid Args => Generate: ArgsWebsocket class")
            return ArgsWebsocket()

class WebSocketServer:
    def __init__(self, uri="127.0.0.1", port=int(environ.get("PORT") or "5589")):
        self.__users__ = set()
        self.__uri__ = uri
        self.__port__ = port
        self.__last_messages__ = {}
    
    async def register(self, websocket):
        self.__users__.add(websocket)
        try:
            for t in websocket.values.topics:
                if t in self.__last_messages__: await websocket.send(self.__last_messages__.get(t))
        except Exception as e:
            LogMessage(f'[ERROR] Register Error => {e}')
        
    async def unregister(self, websocket):
        try:
            self.__users__.remove(websocket)
            LogMessage(f"[INFO] {websocket.values.hashcode} close connection!")
        except Exception as e:
            LogMessage(f"[ERROR] Error on remove user! => {self.__class__.__name__} -> {str(e)} ")
            
    async def send_broadcast_message(self, message:WebsocketMessage):
        try:
            if self.__users__:  
                data = json.dumps(message.toDict(), indent=4,)
                await asyncio.wait([user.send(data) for user in self.__users__])
        except Exception as e:
            LogMessage(f'[ERROR] Error on broadcast message => {e}')

    async def send_private_message(self, message:WebsocketMessage):
        try:
            if self.__users__:  
                LogMessage("[INFO] Message to topics: %s" %str(message.topics))
                data = json.dumps(message.toDict(), indent=4)
                
                if message.persist:
                    for t in message.topics:
                        self.__last_messages__[t] = data
                    
                    
                for user in self.__users__:
                    if len([t for t in message.topics if t in (user.values.topics or [])])>0:
                        await user.send(data)
        except Exception as e:
            LogMessage(f'[ERROR] Error on private message => {e}')
    
    async def queue(self, message:WebsocketMessage):
        try:
            if len(message.topics)>0:
                await self.send_private_message(message)
            else:
                await self.send_broadcast_message(message)
        except Exception as e:
            LogMessage(f'[ERROR] Error on send queue => {e}')

    async def serv(self, websocket, path):
        websocket.values = ArgsWebsocket.fromPath(path)
        await self.register(websocket)
        LogMessage(f"[INFO] {websocket.values.hashcode} start connection on topics: {websocket.values.topics}")
        while(1):
            try:
                await self.queue(WebsocketMessage.fromRecv(await websocket.recv()))
            except Exception as e:
                LogMessage(f"[ERROR] Error on websocket connection => {self.__class__.__name__} -> {str(e)} ")
                await self.unregister(websocket)
                break
    
    def start(self):
        LogMessage(f"[INFO] 🚀 Server Started: %s:%s" %(self.__uri__ or "0.0.0.0", str(self.__port__)))
        start_server = websockets.serve(self.serv, self.__uri__, self.__port__)
        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()
        
    
    def start_linux(self):
        LogMessage(f"[INFO] 🚀 Server Started: %s:%s" %(self.__uri__ or "127.0.0.1", str(self.__port__)))
        async def main():
            async with websockets.serve(self.serv, self.__uri__, self.__port__):
                await asyncio.Future()
        asyncio.run(main())