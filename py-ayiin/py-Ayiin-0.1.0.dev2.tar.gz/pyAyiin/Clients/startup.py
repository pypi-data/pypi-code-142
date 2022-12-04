# Ayiin - Userbot
# Copyright (C) 2022-2023 @AyiinXd
#
# This file is a part of < https://github.com/AyiinXd/Ayiin-Userbot >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/AyiinXd/Ayiin-Userbot/blob/main/LICENSE/>.
#
# FROM Ayiin-Userbot <https://github.com/AyiinXd/Ayiin-Userbot>
# t.me/AyiinXdSupport & t.me/AyiinSupport


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================

import logging

from fipper.errors import SessionExpired, SessionRevoked, UserDeactivated
from fipper.utils import get_peer_id

from pyAyiin.config import Var as Variable

from ..methods._database import AyiinDB
from ..methods.helpers import Helpers
from ..methods.hosting import where_hosted

from .client import *


adB = AyiinDB()
logs = logging.getLogger(__name__)
HOSTED_ON = where_hosted()
Var = Variable()
Xd = Helpers()


async def ayiin_client(client):
    try:
        await client.join_chat("AyiinXdSupport")
        await client.join_chat("AyiinSupport")
        await client.join_chat("StoryAyiin")
    except Exception:
        pass


clients = []
client_id = []


async def StartPyrogram():
    if tgbot:
        await tgbot.start()
        plugins = Xd.import_module(
            "assistant/",
            display_module=False,
            exclude=Var.NO_LOAD,
        )
        logs.info(f"{plugins} Total Plugins Bot")
        me = await tgbot.get_me()
        tgbot.id = me.id
        tgbot.mention = me.mention
        tgbot.username = me.username
        if me.last_name:
            tgbot.name = me.first_name + " " + me.last_name
        else:
            tgbot.name = me.first_name
        logs.info(
            f"TgBot in {tgbot.name} | [ {tgbot.id} ]"
        )
    if AYIIN1:
        try:
            await AYIIN1.start()
            clients.append(1)
            bot_plugins = Xd.import_module(
                "Ayiin/",
                display_module=False,
                exclude=Var.NO_LOAD,
            )
            logs.info(f"{bot_plugins} Total Plugins User")
            me = await AYIIN1.get_me()
            AYIIN1.id = me.id
            AYIIN1.mention = me.mention
            AYIIN1.username = me.username
            if me.last_name:
                AYIIN1.name = me.first_name + " " + me.last_name
            else:
                AYIIN1.name = me.first_name
            #AYIIN1.has_a_bot = True if tgbot else False
            logs.info(
                f"AYIIN1 in {AYIIN1.name} | [ {AYIIN1.id} ]\n\n"
            )
            client_id.append(AYIIN1.id)
        except Exception as ex:
            logs.info(str(ex))
    logs.info(f"Connecting Database To {adB.name}")
    if adB.ping():
        logs.info(f"Succesfully Connect On {adB.name}")
    logs.info(
        f"Connect On [ {HOSTED_ON} ]\n"
    )
