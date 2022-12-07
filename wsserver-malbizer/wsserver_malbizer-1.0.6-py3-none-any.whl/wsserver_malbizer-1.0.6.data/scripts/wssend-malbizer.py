from wsservermalbizer import WebsocketClientMessage, WebsocketClientSender
import sys

client = WebsocketClientMessage.fromArgv(sys.argv)
sender = WebsocketClientSender(client, sys.argv[1] or "0.0.0.0")

sender.send()