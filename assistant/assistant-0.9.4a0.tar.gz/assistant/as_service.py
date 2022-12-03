#!/usr/bin/env python
import os, sys
import json
import requests
import websockets
import asyncio
import ftfy
import yaml

from time import perf_counter, mktime
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from sanic import Sanic, response
from sanic.log import logger

from assistant.rasa.nlp import AgentRasaInterface
from assistant.rasa.conversations import Conversations
from assistant.say import TTS
from assistant.api.responses import Conversation, Response, Error
#from assistant.predictor import Predictor
from assistant.responder import Responder
from assistant import *
from domain.management import enable_service_now as dmt_now

dmt_now()

USER = USERNAME.lower()

HOST, PORT = "0.0.0.0", "5068"

def stamptime():
    return str(mktime(datetime.now().timetuple()))

class InvalidMessengerError(Exception):
    def __init__(self, messenger, user, message=None):
        self.messenger = messenger
        self.user = user
        self.message = message or f"Messenger: {messenger} is neither [agent, assistant] or [user, {user}]"
        super().__init__(self.message)

# Initialze Sanic and ThreadPoolExecutor
executor = ThreadPoolExecutor(max_workers=4)
app = Sanic("assistant_service")

app.ctx.is_q_locked = False

nlp = AgentRasaInterface(host="localhost", port="5005")

if not nlp.is_nlp_server_up():
    sys.exit(1)

conversations = Conversations()

answer = nlp.interpret_nlp_using_server("hello")
conversations.add_conversation(USER, "agent", answer, stamptime())

tts = TTS(host="localhost", port="5067", language=I18N, style_wav="/home/waser/.assistant/data/en/TTS/styles/default.wav")

#predictor = Predictor(I18N)

fallback_response = Responder(I18N)

# try:
#     asyncio.run(tts.say([answer,]))
# except (ConnectionRefusedError, OSError, Exception):
#     pass

def load_nointent():
    yf = f"{ASSISTANT_PATH}/nointent.yml"
    if os.path.exists(yf):
        with open(yf, 'r') as f:
            return yaml.load(f)
    else:
        return {}

def save_nointent(nointent):
    yf = f"{ASSISTANT_PATH}/nointent.yml"
    with open(yf, 'w') as f:
        yaml.dump(nointent, f)

def add_to_nointent(sentence):
    ni = load_nointent()
    if sentence not in ni.get('nointent', []):
        ni['nointent'].append(sentence)
        save_nointent(ni)

async def worker(name, queue):
    while True:
        job = await queue.get()
        size = queue.qsize()
        try:
            await tts.say([job,])
        except ConnectionRefusedError:
            pass
        queue.task_done()
        print(f"{name} just said {job}. {size} sentence(s) remaining")


@app.route("/", methods=["GET"])
async def healthcheck(_):
    return response.text("Welcome to assistant.sock: Assistant as a Service!")

# @app.route("/api/v1/predict", methods=["GET"])
# async def predict(request):
#     logger.debug(f"Received {request.method} request at {request.path}")
#     to_predict = request.json.get('text')
#     data = {}
#     data['prediction'] = predictor.guess(to_predict)
#     return response.json(json.dumps(data))

@app.route('/api/v1/conversation/<user:[A-z]+>', methods=["GET"])
async def conversation(request, user):
    logger.debug(f"Received {request.method} request at {request.path}")

    try:
        conv = conversations.get_conversation(user)
        return response.json(json.dumps(Conversation(conv, user).__dict__))
    except Exception as e:  # pylint: disable=broad-except
        logger.debug(f"Failed to process {request.method} request at {request.path}. The exception is: {str(e)}.")
        raise e
        return response.text(f"Someting went wrong: {str(e)}")

@app.route('/api/v1/say/<user:[A-z]+>', methods=["POST"])
async def say(request, user):
    while app.ctx.is_q_locked:
        logger.debug("Waiting for queue...")
        await asyncio.sleep(0.2)
    logger.debug("Locking queue...")
    app.ctx.is_q_locked = True
    logger.debug(f"Received {request.method} request at {request.path}")
    to_say = request.json.get('text')
    inference_start = perf_counter()
    if to_say:
        _s = stamptime()
        conversations.add_conversation(user, "agent", to_say, _s)
        await app.ctx.queue.put(to_say)
        app.add_task(worker(f"Worker-{app.ctx.queue.qsize()}-{_s}", app.ctx.queue))
    app.ctx.is_q_locked = False
    inference_end = perf_counter() - inference_start
    logger.debug(f"Completed {request.method} request at {request.path} in {inference_end} seconds")
    return response.text(to_say)


@app.websocket("/api/v1/assistant")
async def assistant(request, ws):
    logger.debug(f"Received {request.method} request at {request.path}")

    try:
        query = await ws.recv()
        query_json = json.loads(query.decode('utf-8'))

        user = query_json.get('user')
        q = query_json.get('query')

        if q:
            conversations.add_conversation(user, "user", q, stamptime())

            inference_start = perf_counter()
            answer = await app.loop.run_in_executor(executor, lambda: nlp.run(q))
            inference_end = perf_counter() - inference_start
            if answer:
                _a = ftfy.fix_text(answer)
                if "/clear" in _a: # user can ask assistant to clear the screen
                    conversations.archive_conversation(user)
                elif "/exit" in _a:
                    conversations.archive_conversation(user)
                else:
                    _s = stamptime()
                    conversations.add_conversation(user, "agent", _a, _s)
                    while app.ctx.is_q_locked:
                        await asyncio.sleep(0.2)
                    app.ctx.is_q_locked = True
                    await app.ctx.queue.put(_a)
                    app.add_task(worker(f"Worker-{app.ctx.queue.qsize()}-{_s}", app.ctx.queue))
                    app.ctx.is_q_locked = False

                await ws.send(json.dumps(Response(_a, inference_end).__dict__))
            else:
                # add to nointent list
                add_to_nointent(q)
                # fallback response
                a = fallback_response.answer(q)
                _s = stamptime()
                conversations.add_conversation(user, "agent", a, _s)
                while app.ctx.is_q_locked:
                    await asyncio.sleep(0.2)
                app.ctx.is_q_locked = True
                await app.ctx.queue.put(_a)
                app.add_task(worker(f"Worker-{app.ctx.queue.qsize()}-{_s}", app.ctx.queue))
                app.ctx.is_q_locked = False

                await ws.send(json.dumps(Response(_a, inference_end).__dict__))
            logger.debug(f"Completed {request.method} request at {request.path} in {inference_end} seconds")
        else:
            logger.debug(f"Completed {request.method} request at {request.path} without query")
    except Exception as e:  # pylint: disable=broad-except
        app.ctx.is_q_locked = False
        logger.debug(f"Failed to process {request.method} request at {request.path}. The exception is: {str(e)}.")
        await ws.send(json.dumps(Error("Something went wrong").__dict__))
        raise e

    await ws.close()

@app.listener('after_server_start')
def create_task_queue(app):
    app.ctx.queue = asyncio.Queue(3)
    app.add_task(tts.pronounce())


if __name__ == "__main__":
    app.run(
        host=HOST,
        port=PORT,
        access_log=True,
        debug=True,
    )
