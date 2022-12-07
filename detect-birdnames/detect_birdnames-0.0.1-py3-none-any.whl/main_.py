import preprocess as pp_
import exim as exim_
import bird_detection as bd_
import tweepy

# Load predefined files
all_birds_list = []
all_birds_list_ = exim_.get_all_birds_list_()
for bird in all_birds_list_:
    all_birds_list.append(" " + bird + " ")

birdnames_words = exim_.get_birdname_words()


def merge_lists(list1, final_list):
    for i in list1:
        if type(i) != str:
            i = str(i)
        if i not in final_list:
            final_list.append(i)
    return final_list


def consolidate_bird_list(list1, list2):
    total_list = []
    total_list = merge_lists(list1, total_list)
    total_list = merge_lists(list2, total_list)

    i = 0
    while i < len(total_list):
        for elem in total_list:
            if elem.find(total_list[i]) >- 1 and elem != total_list[i]:
                total_list.remove(total_list[i])
                continue
        i += 1

    return total_list


def create_twitter_app_obj():
    consumer_key = "iPaIdR8GRI59yTJMs0Es0dIBN"
    consumer_secret = "pLadg3UaLeK3yKDujRMChRN3p8hUDBOjBsuOBy8j8ERr4zz1vs"
    access_token = "39085479-AabHt6bmFSbClDfUZuHjModYPAxVlOxHeMA79UyVt"
    access_token_secret = "3IqXDISfqg14wzMNNn2AX4KYG9Wfkltt21QxKasE4YNnG"
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    return api


twitter = create_twitter_app_obj()


def get_bird_names_from_tweet_id(tweet_id_):
    sentence = get_tweet(tweet_id_)
    bird_names = return_bird_name(sentence)
    return bird_names


def get_tweet(tweet__id):
    try:
        tweet = twitter.get_status(tweet__id, tweet_mode="extended").full_text
        return tweet
    except Exception as e:
        print(str(e))


def return_bird_name(sentence):
    # PreProcess the sentence
    # step 1: Remove emojis
    sentence = pp_.remove_emojis(sentence)

    # step 2: Replace underscores
    sentence = pp_.replace_underscores(sentence)

    # step 3: Find bird names in hashtags.
    sentence = pp_.try_replacing_hashtags_mit_birdname(sentence, all_birds_list_)

    # step 4: Do basic preprocessing, including removing numbers, additional spaces.
    sentence = pp_.basic_preprocess(sentence)

    # step 5: Convert plural nouns to singular nouns.
    sentence = pp_.plural_nn_to_singular(sentence, birdnames_words)

    # Check if the bird can be found in any list.
    return_bird_list = bd_.find_bird_from_list(sentence, all_birds_list)

    # Run the model.
    bird_list_ner = bd_.run_model(sentence)

    return_bird_list = consolidate_bird_list(return_bird_list, bird_list_ner)

    return return_bird_list


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    birdnames = return_bird_name("This is a shikra")
    print(birdnames)
