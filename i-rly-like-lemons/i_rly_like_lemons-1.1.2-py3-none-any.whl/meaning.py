#  __                                      __  __                  __  __  __                        __                                                       
# |  \                                    |  \|  \                |  \|  \|  \                      |  \                                                      
#  \$$        ______    ______    ______  | $$| $$ __    __       | $$ \$$| $$   __   ______        | $$  ______   ______ ____    ______   _______    _______ 
# |  \       /      \  /      \  |      \ | $$| $$|  \  |  \      | $$|  \| $$  /  \ /      \       | $$ /      \ |      \    \  /      \ |       \  /       \
# | $$      |  $$$$$$\|  $$$$$$\  \$$$$$$\| $$| $$| $$  | $$      | $$| $$| $$_/  $$|  $$$$$$\      | $$|  $$$$$$\| $$$$$$\$$$$\|  $$$$$$\| $$$$$$$\|  $$$$$$$
# | $$      | $$   \$$| $$    $$ /      $$| $$| $$| $$  | $$      | $$| $$| $$   $$ | $$    $$      | $$| $$    $$| $$ | $$ | $$| $$  | $$| $$  | $$ \$$    \ 
# | $$      | $$      | $$$$$$$$|  $$$$$$$| $$| $$| $$__/ $$      | $$| $$| $$$$$$\ | $$$$$$$$      | $$| $$$$$$$$| $$ | $$ | $$| $$__/ $$| $$  | $$ _\$$$$$$\
# | $$      | $$       \$$     \ \$$    $$| $$| $$ \$$    $$      | $$| $$| $$  \$$\ \$$     \      | $$ \$$     \| $$ | $$ | $$ \$$    $$| $$  | $$|       $$
#  \$$       \$$        \$$$$$$$  \$$$$$$$ \$$ \$$ _\$$$$$$$       \$$ \$$ \$$   \$$  \$$$$$$$       \$$  \$$$$$$$ \$$  \$$  \$$  \$$$$$$  \$$   \$$ \$$$$$$$ 
#                                                 |  \__| $$                                                                                                  
#                                                  \$$    $$                                                                                                  
#                                                   \$$$$$$                                                                                                   
#
#
#       - source code
#       - made by 8AAFFF
#       - meaning extraction submodule

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# import the get_words script
from i_rly_like_lemons import get_words
# import the extras script
from i_rly_like_lemons import extras

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# a function to find a word's index
def word_to_index(word):
    # get all english words and split them into a list
    lst = get_words.get_words("everything").split("\n")
    
    # loop over the whole list, and see if it matches the word we that want to find its index
    for x in range(len(lst)):
        # if it MATCHES, return the line number of the word that wee found (its index)
        if lst[x] == word:
            return x

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# a function to get a word from its index
def index_to_word(index):
    # split all english words into a list
    lst = get_words.get_words("everything").split("\n")
    
    # the list's index matches the word's index so we just take the <index> word of the list
    return lst[index]

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# convert a whole sentence into indexes
def sentence_to_index(sentence):
    # clean up and break the sentence into a list
    broken_sentence = extras.cleanup(sentence).split(" ")
    result = []
    
    # loop over the broken sentence
    for x in range(len(broken_sentence)):
        # convert each word of the list into its index, and append it to the result
        result.append(word_to_index(broken_sentence[x]))
        
    return result

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# convert a sentence's index to a normal sentence
def index_to_sentence(index):
    # create the result that we will later be adding words to
    result = ""
    
    # loop over the index list
    for x in range(len(index)):
        # convert the current word's index to its corresponding word and add in to the result
        # also adding " " (space) at the end of every word
        result += index_to_word(index[x]) + " "
    
    # return the result from the first letter, up to the last letter -1 (to delete the last space from the line before)
    return result[0 : len(result) - 1]