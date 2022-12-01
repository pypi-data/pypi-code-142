from argparse import ArgumentParser
from typing import Dict, Union
import loguru
import sys

loguru.logger.remove()
loguru.logger.add(sys.stdout, level="WARNING")

import vkbottle
from vkbottle.bot import Message
import threading
import asyncio
from functools import partial
from dataclasses import dataclass
from random import randint


@dataclass
class MetaArgs:
    loop: asyncio.AbstractEventLoop
    user_id: int
    peer_id: int


parser = ArgumentParser("intobot", description="This converts your script to a bot.")

parser.add_argument("script")
parser.add_argument("-t", "--token", required=True)

args = parser.parse_args()

token = open(args.token).read().strip()

script = open(args.script, encoding="utf-8").read()

bot = vkbottle.Bot(token=token)

user_ids_to_states: Dict[int, Union[str, bool]] = {}


async def async_fake_print(meta, message):
    message = str(message)
    await bot.api.messages.send(
        peer_id=meta.peer_id,
        message=message,
        random_id=randint(-1_000_000, 1_000_000),
    )


def fake_print(meta, message):
    asyncio.run_coroutine_threadsafe(async_fake_print(meta, message), meta.loop)


def fake_input(meta, query=""):
    user_ids_to_states[meta.user_id] = True
    if str(query):
        fake_print(meta, query)
    while type(user_ids_to_states[meta.user_id]) is not str:
        pass
    response = user_ids_to_states[meta.user_id]
    user_ids_to_states[meta.user_id] = False
    return response


def run(meta):
    exec(
        script,
        {
            "print": partial(fake_print, meta),
            "input": partial(fake_input, meta),
        },
        {},
    )


@bot.on.message()
async def on_message(message: Message):
    user_id = message.from_id
    loop = asyncio.get_running_loop()
    try:
        state = user_ids_to_states[user_id]
    except KeyError:
        user_ids_to_states[user_id] = False
        threading.Thread(
            target=run,
            args=(MetaArgs(
                peer_id=message.peer_id,
                user_id=message.from_id,
                loop=loop
            ),),
        ).start()
    else:
        if state is True:
            user_ids_to_states[user_id] = message.text


print("Starting!")
bot.run_forever()
