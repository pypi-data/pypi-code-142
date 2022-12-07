import spacy


def find_bird_from_list(sentence, all_birds_list):
    bird_list = []
    sentence = " " + sentence + " "  # padding
    for bird in all_birds_list:
        if sentence.find(bird) > -1:
            bird_list.append(bird.strip())
    return bird_list


def run_model(sentence):
    result_ = []
    nlp_ner = spacy.load("./model-best")
    doc = nlp_ner(sentence)
    for ent in doc.ents:
        result_.append(ent)
    return result_
