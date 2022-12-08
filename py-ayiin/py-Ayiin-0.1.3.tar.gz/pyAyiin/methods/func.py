# Ultroid - UserBot
# Copyright (C) 2021-2022 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/TeamUltroid/pyUltroid/blob/main/LICENSE>.

import os

def update_envs():
    """Update Var. attributes to adB"""
    from .. import adB

    for envs in list(os.environ):
        if envs in ["LOG_CHAT", "BOT_TOKEN"] or envs in adB.keys():
            adB.set_key(envs, os.environ[envs])
