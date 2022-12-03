from transformers import AutoModelForCausalLM, AutoTokenizer, AutoModelWithLMHead
import torch

class Responder:
    def __init__(self, lang: str):
        self.lang = lang
        self._init()
        self.chat_history_ids = None

    def _init(self):
        if self.lang == "en":
            self.tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
            self.eos = self.tokenizer.eos_token
            self.model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")
        elif self.lang == "fr":
            self.tokenizer = AutoTokenizer.from_pretrained("cedpsam/chatbot_fr")
            self.eos = self.tokenizer.eos_token
            self.model = AutoModelWithLMHead.from_pretrained("cedpsam/chatbot_fr")
        else:
            self.tokenizer = None
            self.eos = None
            self.model = None
    
    def decode_query(query):
        user_input_ids = self.tokenizer.encode(query + self.eos, return_tensors='pt')
        bot_input_ids = torch.cat([chat_history_ids, user_input_ids], dim=-1) if self.chat_history_ids else user_input_ids
        self.chat_history_ids = self.model.generate(bot_input_ids, max_length=1000, pad_token_id=self.eos)
        return self.tokenizer.decode(self.chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)

    def answer(self, query: str):
        if self.tokenizer and self.model:
            return self.decode_query(query)
        else:
            print("Your language is not supported.")