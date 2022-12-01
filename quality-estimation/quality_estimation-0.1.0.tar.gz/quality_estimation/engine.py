from typing import List
import fasttext
import torch
from transquest.algo.sentence_level.monotransquest.run_model import MonoTransQuestModel

def quality_estimation(srcs: List[str], tgts: List[str]):  #, src_hint='N.A.'
    
    # model = MonoTransQuestModel("xlmroberta", "TransQuest/monotransquest-hter-de_en-pharmaceutical", num_labels=1, use_cuda=torch.cuda.is_available())
    model = MonoTransQuestModel("xlmroberta", "TransQuest/monotransquest-da-any_en", num_labels=1, use_cuda=False) # use_cuda=torch.cuda.is_available() 
    sentence_pairs = list(map(list, zip(srcs, tgts)))

    predictions, raw_outputs = model.predict(sentence_pairs)
    print(predictions)
    return predictions
    
    
    
    
    
    
    # fasttext_model = fasttext.load_model("lid.176.bin")
    # eu_langs = ['de','bg','cs','hr','da','sk','sl','es','et','fi','fr','el','hu','ga','it','lv','lt','mt','nl','pl','pt','ro','sv']
    
    # if mode == "EUROPEANA":
        
    #     res_labels, res_scores = [], []
    #     labels, scores = fasttext_model.predict(srcs, k = 10)

    #     for k_labels,k_scores in zip(labels,scores):
    #         label = 'N.A.'
    #         score = 0
    #         for l,s in zip(k_labels, k_scores):
    #             if l.split('__')[-1] in eu_langs:
    #                 label = l.split('__')[-1]
    #                 score = s
    #                 break
    #         if label != src_hint and src_hint in eu_langs and (label=="N.A." or score < 0.5):
    #             label = src_hint
    #         res_labels.append(label)
    #         res_scores.append(round(float(score),4))
    #     return res_labels, res_scores
    
    # else:
    #     labels, scores = fasttext_model.predict(' '.join(srcs), k = 1)
    #     label = labels[0].split('__')[-1]
        # score = round(scores[0],4)
        # return label, score
 
 
