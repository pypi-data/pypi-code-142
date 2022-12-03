import os, sys
import json
import websockets
import asyncio
import signal

from websockets.exceptions import ConnectionClosedOK

from listen import mic
#from listen.STT import enable_service_now as listen_now
from listen.STT import utils

STT_CONFIG = utils.get_config_or_default()
is_allowed_to_listen = utils.is_allowed_to_listen(STT_CONFIG)
if is_allowed_to_listen:
    #listen_now()
    pass
else:
    print("System has not user autorization to listen.")
    sys.exit(1)

signal.signal(signal.SIGINT, signal.SIG_DFL)

HOST = "0.0.0.0"
PORT = "5068"

USER = os.environ.get("USERNAME", 'user').lower()

async def nlp(query: str, user: str, host=HOST, port=PORT):
    async with websockets.connect(f"ws://{host}:{port}/api/v1/assistant") as ws:
        try:
            req = {'query': query, 'user': user}
            
            await ws.send(json.dumps(req).encode('utf-8'))

            return json.loads(await ws.recv())
        except ConnectionClosedOK:
            pass
        except (ConnectionRefusedError, OSError) as e:
            pass
        except Exception as e:
            raise e
        finally:
            await ws.close()

def main():
    try:
        source = mic.Microphone()
        while True:
            query = source.transcribe()
            if query:
                print(f"sending: {query}")
                asyncio.run(nlp(query, USER))
    except Exception as e:
        raise e