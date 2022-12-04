from TeXid import RobertaTeXid, SeqClassifierTokenizer
import torch
import spacy

class PostProcess:
    def __init__(self, ckpt):
        self.tokenizer = SeqClassifierTokenizer(ckpt)
        self.model = RobertaTeXid.from_pretrained(ckpt)
        self.nlp = spacy.load('en_core_web_sm')

    def __call__(self, sentence: str):
        batch = self.tokenizer.tokenize(sentence, padding='max_length', truncation=True, max_length=20, return_tensors='pt')
        logits = self.model(batch)
        preds = torch.argmax(logits, dim=-1).item()
        tense = self.tokenizer.convertId2Label(preds)
        if tense == "Future Continuous":
            if "will be" in sentence:
                doc = self.nlp(sentence)
                no_tokens = len(doc)
                for i, token in enumerate(doc):
                    if i < no_tokens - 1:
                        look_ahead_tok = doc[i+1]
                    else:
                        look_ahead_tok = None
                    if token.text == "will" \
                        and look_ahead_tok is not None \
                        and look_ahead_tok.text == "be":
                        if i < no_tokens - 2:
                            look_ahead_2_tok = doc[i+2]
                        else:
                            look_ahead_2_tok = None
                        if look_ahead_2_tok is None:
                            return "Future Simple"
                        else:
                            if look_ahead_2_tok.pos_ == "VERB":
                                return tense
                            else:
                                return "Future Simple"
            elif "will" in sentence:
                return "Future Simple"
            else:
                return f"ERROR: Cannot classify the tense. Not {tense}"
        else:
            return tense
