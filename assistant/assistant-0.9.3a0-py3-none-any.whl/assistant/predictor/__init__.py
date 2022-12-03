from transformers import pipeline

class Predictor:
    def __init__(self, lang: str):
        self.lang = lang
        self._init()

    def _init(self):
        if self.lang == "en":
            self.mask = "<mask>"
            self.unmasker = pipeline('fill-mask', model='xlm-roberta-base')
            self.ts_key = "token_str"
        elif self.lang == "fr":
            self.mask = "[MASK]"
            self.unmasker = pipeline('fill-mask', model='qwant/fralbert-base')
            self.ts_key = "token_str"
        else:
            self.mask = "[MASK]"
            self.unmasker = pipeline('fill-mask', model='bert-base-multilingual-cased')
            self.ts_key = "token_str"
    
    def guess(self, words: str):
        w = words + self.mask
        n = self.unmasker(w)
        _n = []
        for m in n:
            s = m.get(self.ts_key)
            if s:
                _n.append(s)
        return _n