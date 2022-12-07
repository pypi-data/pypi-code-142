import pickle


def get_all_birds_list_():
    file = open("./files/all_birds_list", 'rb')
    all_birds_list = pickle.load(file)
    try:
        return all_birds_list
    except:
        return 0


def get_birdname_words():
    file = open("./files/birdnames_words", 'rb')
    birdnames_words = pickle.load(file)
    return birdnames_words
