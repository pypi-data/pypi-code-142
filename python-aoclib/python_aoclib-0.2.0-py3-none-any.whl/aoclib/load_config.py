import os
from dotenv import load_dotenv

load_dotenv()

def getSessionID() -> str:
    sessionID = os.getenv('AOC_SESSION')
    if not sessionID:
        sessionID = input('Input your session ID: ')
    return sessionID
