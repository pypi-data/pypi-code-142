from transformers import AutoTokenizer, AutoModelForCausalLM
from transformers import pipeline
import pandas as pd
from ..config import paths

class GPTModel:
    def __init__(self, modelName='marathi-gpt', gpu_enabled:bool = False):
        self.modelName = modelName
        self.modelRoute = paths['autocomplete'][self.modelName]
        self.tokenizer = AutoTokenizer.from_pretrained(self.modelRoute)
        self.model = AutoModelForCausalLM.from_pretrained(self.modelRoute)
        self.classifier = pipeline('text-generation',
                              model=self.model, tokenizer=self.tokenizer)
        pd.options.display.max_colwidth = None 

    def nextWord(self, text, numOfPredictions = 1):
        result = self.classifier(text, max_new_tokens = 1, num_return_sequences = numOfPredictions)
        df = pd.DataFrame.from_dict(result)
        return df


    def completeSentence(self, text, numOfWords = 25, numOfPredictions = 1):
        result = self.classifier(text, max_new_tokens = numOfWords, num_return_sequences = numOfPredictions)
        df = pd.DataFrame.from_dict(result)
        return df

    def listModels(self):
        print(" autocomplete models: ")
        for model in paths['autocomplete']:
            print("\t",model, ": ", paths['autocomplete'][model])
        for task in set(paths) - {'autocomplete'}:
            print("\n",task,"models: ")
            for model in paths[task]:
                print("\t",model, ": ", paths[task][model])