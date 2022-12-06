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

import asyncio
import importlib
import os
import ssl


try:
    import certifi
except ImportError:
    certifi = None


class Helpers(object):
    def import_module(
        self,
        path: str,
        exclude: list = [],
        display_module: bool = True
    ):
    
        listbin = []
        listbin.clear()
    
        if not os.path.exists(path):
            return print(f"No path found: {path}")
    
        modules = []
        modules.clear()
    
        for x in os.listdir(path):
            if x.endswith(".py"):
                if x not in ["__pycache__", "__init__.py"]:
                    modules.append(x.replace(".py", ""))
    
        py_path_raw = ".".join(path.split("/"))
        py_path = py_path_raw[0:len(py_path_raw) - 1]
    
        count = 0
        for x in modules:
            if x not in exclude:
                importlib.import_module(py_path + "." + x)
                count += 1
                listbin.append(x)
    
        if display_module:
            data = sorted(listbin)
            for x in data:
                print(x + " Loaded !")
        return count


    async def get_paste(
        self,
        data: str,
        extension: str = "txt"
    ):
        ssl_context = ssl.create_default_context(cafile=certifi.where())
        json = {"content": data, "extension": extension}
        key = await self.async_searcher(
            url="https://spaceb.in/api/v1/documents/",
            json=json,
            ssl=ssl_context,
            post=True,
            re_json=True,
        )
        try:
            return True, key["payload"]["id"]
        except KeyError:
            if "the length must be between 2 and 400000." in key["error"]:
                return await self.get_paste(data[-400000:], extension=extension)
            return False, key["error"]
        except Exception as e:
            print(e)
            return None, str(e)
