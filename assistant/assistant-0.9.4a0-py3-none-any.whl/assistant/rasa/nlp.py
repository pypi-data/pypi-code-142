import attr
import asyncio
import builtins
import requests
import random

from xonsh.built_ins import XSH

@attr.s(auto_attribs=True, frozen=True)
class PredictReturn:
    success: bool
    unparse: str = None
    error_message: str = None

class AgentRasaInterface():
    host="localhost"
    port="5005"
    interface = None
    #models_path = None


    def __init__(self, host="localhost", port="5005", **kwargs):
        self.host = host
        self.port = port
        if self.is_nlp_server_up():
            self.interface = self.interpret_nlp_using_server
        else:
            #self.interface = self.interpret_nlp_using_agent # this would require RASA and Py3.8
            self.interface = self.interpret_nlp_using_fallback
            #self.models_path = model_path
            #self.agent = load_agent(model_path=self.models_path)

    def is_nlp_server_up(self):
        try:
            r = requests.get(f"http://{self.host}:{self.port}")
            if r.status_code == 200:
                return True
            else:
                raise Exception()
        except Exception as e:
            return False

    def interpret_nlp_using_fallback(self, question: str):
        return f"Assistant: Sorry, I can\'t reach the NLP services.\nEnable them by typing the folowing command:\n`systemctl enable --now dmt assistant`"

    #async def interpret_nlp_using_agent(self, question: str):
    #    return await self.agent.handle_message(question)

    def interpret_nlp_using_server(self, question: str):
        response = None
        if question:
            headers = {'content-type': 'application/json'}
            payload = { 'message': question, 'sender': "user" }
            r = requests.post(f"http://{self.host}:{self.port}/webhooks/rest/webhook", json=payload, headers=headers)
            if r.status_code == 200:
                rj = r.json()
                if rj:
                    response = "\n".join(x.get('text', "") for x in rj)

        return response
    
    def run(self, query):
        return self.interface(query)