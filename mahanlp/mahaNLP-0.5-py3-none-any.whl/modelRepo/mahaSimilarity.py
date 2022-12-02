from sentence_transformers import SentenceTransformer, util
import numpy
from ..config import paths

class SimilarityModel:
    def __init__(self, modelName = 'marathi-sentence-similarity-sbert', gpu_enabled:bool = False):
        self.modelName = modelName
        self.modelRoute = paths['similarity'][self.modelName]
        self.model = SentenceTransformer(self.modelRoute)

    def embedSentences(self,sentences):
        sentenceEmbeddings = self.model.encode(sentences)
        return sentenceEmbeddings

    def getSimilarityScore(self, sourceSentence, sentences, as_dict: bool = False):
        embeddings1 = self.embedSentences(sourceSentence)
        embeddings2 = self.embedSentences(sentences)
        cosine_scores = util.cos_sim(embeddings1, embeddings2)
        resultNpArray = cosine_scores.numpy()[0]

        if as_dict:
          dict = {}
          if type(sentences) == str:
            sentences = [sentences]
          for i in range(len(sentences)):
            dict[sentences[i]] =  resultNpArray[i]
          return dict
        return resultNpArray

    def listModels(self):
        print(" similarity models: ")
        for model in paths['similarity']:
            print("\t",model, ": ", paths['similarity'][model])
        for task in set(paths) - {'similarity'}:
            print("\n",task,"models: ")
            for model in paths[task]:
                print("\t",model, ": ", paths[task][model])


    
