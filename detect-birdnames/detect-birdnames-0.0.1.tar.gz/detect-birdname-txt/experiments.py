import exim as exim_
import preprocess as p_
import spacy
import pickle

all_birds_list_ = exim_.get_all_birds_list_()
birdnames_words = exim_.get_birdname_words()
#search_term = input("search term: ")
#if search_term in all_birds_list_:
#    print(search_term, "exists.")

hashtag = "CacharWedgeBilledBabbler"
answer = p_.get_bird_name_from_hashtag_4levels(hashtag,all_birds_list_)
print(answer)