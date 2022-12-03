
import asyncio
#import xonsh
#import six
from builtins import input, __xonsh__
from typing import Text

#from rasa_core.channels import HttpInputChannel
from rasa.core import utils
from rasa.core.agent import Agent
#from rasa.core.interpreter import RasaNLUInterpreter
#from rasa.core.channels.channel import UserMessage, CollectingOutputChannel
#from rasa_core.channels.rest import HttpInputComponent
#from rasa.core.channels.console import ConsoleInputChannel, ConsoleOutputChannel
#from flask import Blueprint, request, jsonify

#from rasa_sdk.__main__ import main as sdk_main
#logger = logging.getLogger(__name__)

#xonsh.main.setup()

#__xonsh__.run_subproc(["cd", "/home/waser/.assistant"], ["&&"], ["python3.8", "-m", "rasa_sdk", "--actions", "actions.fr"] )

async def run(serve_forever=True):
    #path to your NLU model
    #interpreter = RasaNLUInterpreter("/home/waser/.assistant/models/")
    # path to your dialogues models
    agent = Agent.load("/home/waser/.assistant/models/fr/NLU/")
    #http api endpoint for responses
    #input_channel = SimpleWebBot()
    #if serve_forever:
        #agent.handle_channel(HttpInputChannel(5004, "/chat", input_channel))
        #agent.handle_channel(AssistantInputConsoleChannel(sender_id="waser"))
        #agent.handle_channel(AssistantConsoleOutputChannel())
    while True:
        try:
            q = input("? ")
            print()
            r = await agent.handle_message(q)
            print(r)
        except KeyboardInterrupt:
            exit(1)
    
    return agent

asyncio.run(run())