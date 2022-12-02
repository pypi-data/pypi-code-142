from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import pipeline
import pandas as pd
from ..config import paths

class SentimentModel:
    def __init__(self, modelName='MarathiSentiment', gpu_enabled:bool = False):
        self.modelName = modelName
        self.modelRoute = paths['sentiment'][self.modelName]
        self.tokenizer = AutoTokenizer.from_pretrained(self.modelRoute)
        self.model = AutoModelForSequenceClassification.from_pretrained(self.modelRoute)
        self.classifier = pipeline('text-classification',
                              model=self.model, tokenizer=self.tokenizer)
    def getPolarityScore(self, text):
        result = self.classifier(text)
        df = pd.DataFrame.from_dict(result)
        return df

    def listSupportedLabels(self):
        print('Supported labels: \n -Positive\n -Negative\n -Neutral\n')

    def listModels(self):
        print(" sentiment models: ")
        for model in paths['sentiment']:
            print("\t",model, ": ", paths['sentiment'][model])
        for task in set(paths) - {'sentiment'}:
            print("\n",task,"models: ")
            for model in paths[task]:
                print("\t",model, ": ", paths[task][model])