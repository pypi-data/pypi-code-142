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

import dotenv
import heroku3
import logging
import os
import sys

from ..config import Var as Variable
from ..methods import where_hosted

logs = logging.getLogger(__name__)
HOSTED = where_hosted()
Var = Variable()


class Ubot(object):
    async def set_var_value(self, client, vars, value, env):
        if HOSTED == "Heroku":
            if Var.HEROKU_API is None or Var.HEROKU_APP_NAME is None:
                logs.info(
                    "Pastikan HEROKU_API dan HEROKU_APP_NAME anda dikonfigurasi dengan benar di config vars heroku"
                )
            Heroku = heroku3.from_key(Var.HEROKU_API)
            happ = Heroku.app(Var.HEROKU_APP_NAME)
            heroku_config = happ.config()
            if vars not in heroku_config:
                heroku_config[vars] = value
                logs.info(f"Berhasil Menambahkan Vars {vars}")
                return True
            else:
                pass
        else:
            path = dotenv.find_dotenv(env)
            if not path:
                logs.info(".env file not found.")
            if not dotenv.get_key(path, vars):
                dotenv.set_key(path, vars, value)
                logs.info(f"Berhasil Menambahkan var {vars}")
                os.execvp(sys.executable, [sys.executable, "-m", "pyAyiin"])
            else:
                pass


    async def create_ubot(self, client, string_session, env):
        if Var.SESSION_1 != "None":
            pass
        try:
            done = await self.set_var_value(client, "SESSION_1", string_session, env)
            if done:
                return True
            else:
                pass
        except BaseException as e:
            logs.info(e)

        if Var.SESSION_2 != "None":
            pass
        try:
            done = await self.set_var_value(client, "SESSION_2", string_session, env)
            if done:
                return True
            else:
                pass
        except BaseException as e:
            logs.info(e)

        if Var.SESSION_3 != "None":
            pass
        try:
            done = await self.set_var_value(client, "SESSION_3", string_session, env)
            if done:
                return True
            else:
                pass
        except BaseException as e:
            logs.info(e)

        if Var.SESSION_4 != "None":
            pass
        try:
            done = await self.set_var_value(client, "SESSION_4", string_session, env)
            if done:
                return True
            else:
                pass
        except BaseException as e:
            logs.info(e)

        if Var.SESSION_5 != "None":
            pass
        try:
            done = await self.set_var_value(client, "SESSION_5", string_session, env)
            if done:
                return True
            else:
                pass
        except BaseException as e:
            logs.info(e)

        if Var.SESSION_6 != "None":
            pass
        try:
            done = await self.set_var_value(client, "SESSION_6", string_session, env)
            if done:
                return True
            else:
                pass
        except BaseException as e:
            logs.info(e)

        if Var.SESSION_7 != "None":
            pass
        try:
            done = await self.set_var_value(client, "SESSION_7", string_session, env)
            if done:
                return True
            else:
                pass
        except BaseException as e:
            logs.info(e)

        if Var.SESSION_8 != "None":
            pass
        try:
            done = await self.set_var_value(client, "SESSION_8", string_session, env)
            if done:
                return True
            else:
                pass
        except BaseException as e:
            logs.info(e)

        if Var.SESSION_9 != "None":
            pass
        try:
            done = await self.set_var_value(client, "SESSION_9", string_session, env)
            if done:
                return True
            else:
                pass
        except BaseException as e:
            logs.info(e)

        if Var.SESSION_10 != "None":
            pass
        try:
            done = await self.set_var_value(client, "SESSION_10", string_session, env)
            if done:
                return True
            else:
                pass
        except BaseException as e:
            logs.info(e)
        
        logs.info("Userbot Anda sudah Penuh...")

