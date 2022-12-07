from wsservermalbizer import WebSocketServer
import sys

port = "7135"
try: port = sys.argv[1]
except: pass

WebSocketServer(port=port).start()