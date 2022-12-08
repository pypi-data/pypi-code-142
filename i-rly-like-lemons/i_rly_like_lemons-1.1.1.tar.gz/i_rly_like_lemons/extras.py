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
#       - extras submodule

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# import get_words
import get_words

# clean a text up from all unwanted characters
def cleanup(text):
    # define the variable we will be copying the clean text into
    clean = ""
    
    # loop over every single character of the text we are cleaning up
    for x in range(len(text)):
        # if the character is not dirty (not inside the filter from get_words)
        if text[x] not in get_words.get_words("filter"):
            # we add it to the clean characters
            clean += text[x]
        else:
            # if its dirty, then we just skip it and go to the next character
            pass
    
    return clean

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# split a string into a list with multiple seperatos
# when running function dont forget to declate variables like so:
# split_with_multiple_seperators(",", ".", " ", "|", text = "sep1, sep2. sep3 sep4| some more text")
def split_with_multiple_seperators(*seperators, text):
    # put all the seperators into a string like so:
    # [",", ".", "/"]   -->   ",./"
    seperators = "".join(list(seperators))
    # define the copied var which we will be pasting into all the not seperatror text
    copied = ""
    # define final list in which we will be appending all the seperated text
    final = []

    # loop over each character in the text
    for x in range(len(text)):
        # if the character that we are looking at is NOT a seperator, we add it to copied
        if text[x] not in seperators:
            copied = copied + text[x]
        # if the character IS a seperator, then we append copied to final, and reset copied to = ""
        else:
            final.append(copied)
            copied = ""

    # append whatever is left in copied to final and return final
    final.append(copied)

    return final

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# a function to lightly rephrase a sentence
def rephrase(indexes, strength):
    import random
    
    # loop over the indexes list
    for x in range(len(indexes)):
        # change every index to a itself + a random number
        indexes[x] = indexes[x] + random.randint(-strength, strength)
        
    return indexes

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# get the match precentage of 2 strings
# test and twst > 75.0% match
def compare(word1, word2):
    # define shorter and longer
    shorter = ""
    longer = ""
    # define "match" witch we will later be adding the amount of similar letters
    match = 0
    
    # set shorter as the shorter word, and longer as the longer word
    # if they are the same: shorter = word1, longer = word2
    # we do this since we want to compare the shorter word to the longer word and not the other way around because:
    # we cant compare the: for example: the 5th letter of a 6 letter word, to the 5th letter of a 4 letter word
    if len(word1) > len(word2):
        shorter = word2
        longer = word1
    elif len(word1) < len(word2):
        shorter = word1
        longer = word2
    else:
        shorter = word1
        longer = word2
    
    # cut the longer word to the length of the shorter word so that we can compare all the letters
    cut_longer = longer[0 : len(shorter)]
    
    # go over every single letter in the pair and see if they match
    for x in range(len(shorter)):
        # if they DO match add 1 to match
        if shorter[x] == cut_longer[x]:
            match += 1
    
    # return how many matches there were / amount of letters in the word <-- returns a value between 0 and 1
    # 1: 100% match
    # 0: no letters matched
    # *100 to get the value in precents and not in 0-1
    return match / len(longer) * 100