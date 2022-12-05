# py - Ayiin
# Copyright (C) 2022-2023 @AyiinXd
#
# This file is a part of < https://github.com/AyiinXd/pyAyiin >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/AyiinXd/pyAyiin/blob/main/LICENSE/>.
#
# FROM py-Ayiin <https://github.com/AyiinXd/pyAyiin>
# t.me/AyiinChat & t.me/AyiinSupport


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================

import logging
import os
import sys
import time

from pyAyiin.Clients import *
from pyAyiin.methods import *
from pyAyiin.pyrogram import AyiinMethods
from pyAyiin.pyrogram import eod, eor
from pyAyiin.xd import GenSession
from pyAyiin.telethon.ayiin import *


# Bot Logs setup:
logging.basicConfig(
    format="[%(name)s] - [%(levelname)s] - %(message)s",
    level=logging.INFO,
)
logging.getLogger("pyAyiin").setLevel(logging.INFO)
logging.getLogger("fipper").setLevel(logging.ERROR)
logging.getLogger("fipper.client").setLevel(logging.ERROR)
logging.getLogger("fipper.session.auth").setLevel(logging.ERROR)
logging.getLogger("fipper.session.session").setLevel(logging.ERROR)


logs = logging.getLogger(__name__)


__copyright__ = "Copyright (C) 2022-present AyiinXd <https://github.com/AyiinXd>"
__license__ = "GNU General Public License v3.0 (GPL-3.0)"
__version__ = "0.1.0"
ayiin_ver = "0.0.1"


adB = AyiinDB()

DEVS = [997461844, 1905050903, 1965424892]


class PyrogramXd(AyiinMethods, GenSession, Methods):
    pass


class TelethonXd(AyiinMethod, GenSession, Methods):
    pass


suc_msg = (f"""
========================×========================
           Credit Py-Ayiin {__version__}
========================×========================
"""
)

fail_msg = (f"""
========================×========================
      Commit Yang Bener Bego Biar Gak Error
           Credit Py-Ayiin {__version__}
========================×========================
"""
)

run_as_module = False

if sys.argv[0] == "-m":
    run_as_module = True
    
    import asyncio
    
    from aiohttp import ClientSession

    from .decorator import *
    from .methods import AyiinDB, where_hosted
    from .pyrogram import *
    from .Clients import AYIIN1, tgbot

    print("\n\n" + __copyright__ + "\n" + __license__)
    print(suc_msg)

    CMD_HELP = {}
    adB = AyiinDB()
    aiosession = ClientSession()
    loop = asyncio.get_event_loop()
    HOSTED_ON = where_hosted()
else:
    logs.info("\n\n" + __copyright__ + "\n" + __license__)

    app = None
    AYIIN1 = None
