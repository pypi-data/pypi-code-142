import sys

from os import getenv

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass


class Var(object):
    # mandatory
    API_ID = int(getenv("API_ID"))
    API_HASH = str(getenv("API_HASH"))
    # Extras
    ALIVE_PIC = getenv("ALIVE_PIC", "https://telegra.ph//file/78ec83169711f650f0188.jpg")
    ALIVE_TEXT = getenv("ALIVE_TEXT", "Hai, Saya AyiinUbot")
    # Telethon Session
    STRING_1 = getenv("STRING_1", "")
    STRING_2 = getenv("STRING_2", "")
    STRING_3 = getenv("STRING_3", "")
    STRING_4 = getenv("STRING_4", "")
    STRING_5 = getenv("STRING_5", "")
    STRING_6 = getenv("STRING_6", "")
    STRING_7 = getenv("STRING_7", "")
    STRING_8 = getenv("STRING_8", "")
    STRING_9 = getenv("STRING_9", "")
    STRING_10 = getenv("STRING_10", "")
    
    # Pyrogram Session
    SESSION_1 = getenv("SESSION_1", "")
    SESSION_2 = getenv("SESSION_2", "")
    SESSION_3 = getenv("SESSION_3", "")
    SESSION_4 = getenv("SESSION_4", "")
    SESSION_5 = getenv("SESSION_5", "")
    SESSION_6 = getenv("SESSION_6", "")
    SESSION_7 = getenv("SESSION_7", "")
    SESSION_8 = getenv("SESSION_8", "")
    SESSION_9 = getenv("SESSION_9", "")
    SESSION_10 = getenv("SESSION_10", "")
    # For Handler
    HNDLR = getenv("HNDLR", [".", "!", "*", "^", "-", "?"])
    # Database
    REDIS_URI = (
        getenv("REDIS_URI", None) or getenv("REDIS_URL", None)
    )
    REDIS_PASSWORD = getenv("REDIS_PASSWORD", None)
    # extras
    BOT_TOKEN = getenv("BOT_TOKEN")
    LOG_CHAT = int(getenv("LOG_CHAT") or 0)
    HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
    HEROKU_API = getenv("HEROKU_API", None)
    TEMP_DOWNLOAD_DIRECTORY = getenv("TEMP_DOWNLOAD_DIRECTORY", "./downloads")
    NO_LOAD = [int(x) for x in getenv("NO_LOAD", "").split()]
    TZ = getenv("TZ", "Asia/Jakarta")
    # for railway
    REDISPASSWORD = getenv("REDISPASSWORD", None)
    REDISHOST = getenv("REDISHOST", None)
    REDISPORT = getenv("REDISPORT", None)
    REDISUSER = getenv("REDISUSER", None)
    # for sql
    DATABASE_URL = getenv("DATABASE_URL", None)
    # for MONGODB users
    MONGO_URI = getenv("MONGO_URI", None)
    # for Okteto Platform
    OKTETO = bool(getenv("OKTETO", False))
