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
#       - keyword detection submodule

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# import the get_words script
from i_rly_like_lemons import get_words
# import the extras script
from i_rly_like_lemons import extras

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# detect all keywords from a text
def detect_keywords(text):
    # define all the NOT keyword words as non_keywords
    non_keywords = get_words.get_words("non_kwrds").split("\n")
    # clean the text from unwanted characters and break it into a list
    broken_text = extras.cleanup(text).split()
    
    # loop over each word from the original text
    for x in range(len(broken_text)):
        # compare each word from the original text to all the NON keywords
        for y in range(len(non_keywords)):
            if broken_text[x] == non_keywords[y]:
                # if the current broken_text[x] word is NOT a keyword, then we remove it
                # so that by the end only words that ARE keywords are left
                broken_text[x] = ""

    # return the all the keywords in a list
    # did it like this bcs pop() didnt work for some reason (sorry future devs)
    return " ".join(broken_text).split()