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
#       - sentiment analysis submodule

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# import the get_words script
import get_words
# import the extras script
import extras

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# get positive sentiment (only count positive words)
def get_positive_sentiment(sentence):
  # define sentiment default value
  sentiment = 0
  # define check_for_words with all of the words in the text file and prepare them
  check_for_words = get_words.get_words("positive").split("\n")
  # prapare sentence
  sentence = sentence.lower()
  broken_sentence = sentence.split(" ")

  # loop over each word of the sentence and check if it is in the words list
  for x in range(len(broken_sentence)):
    for y in range(len(check_for_words)):
      # if it is: add 1 to sentiment
      if broken_sentence[x] == check_for_words[y]:
        sentiment += 1

  return sentiment

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# get negative sentiment (only count negative words)
def get_negative_sentiment(sentence):
  # define sentiment default value
  sentiment = 0
  # define check_for_words with all of the words in the text file and prepare them
  check_for_words = get_words.get_words("negative").split("\n")
  # prapare sentence
  sentence = sentence.lower()
  broken_sentence = sentence.split(" ")

  # loop over each word of the sentence and check if it is in the words list
  for x in range(len(broken_sentence)):
    for y in range(len(check_for_words)):
      # if it is: add 1 to sentiment
      if broken_sentence[x] == check_for_words[y]:
        sentiment -= 1

  return sentiment

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# check words that amplif a senences value (really, extremly...)
def check_amplifiers(sentence):
  # define the output result (by whitch we later multiply the final sentiment)
  result = 1

  # prapare the words from the file
  check_for_words = get_words.get_words("amplifiers").split("\n")
  # prapare sentence
  sentence = sentence.lower()
  broken_sentence = sentence.split(" ")

  # check if a word is in ampifiers list
  for x in range(len(broken_sentence)):
    for y in range(len(check_for_words)):
      if broken_sentence[x] == check_for_words[y]:
        # if it is, we add 1 to result
        result = result + 1

  return result

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# check for inverter words
def check_inverters(sentence):
  # we define the output value as 1 (because if there are no inverters we multiply the result by 1 (it doesnt change it))
  result = 1
  # papare the inverter words list
  check_for_words = get_words.get_words("inverters").split("\n")
  # break sentence
  sentence = sentence.lower()
  broken_sentence = sentence.split(" ")

  # if we find an inverter word, we flip the falue (* -1)
  for x in range(len(broken_sentence)):
    for y in range(len(check_for_words)):
      if broken_sentence[x] == check_for_words[y]:
        result = result * -1

  return result

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# get the full sentiment of 1 sentence
# input > a string sentence
# output > a float
def get_sentence_sentiment(sentence):
  # clean up the text
  sentence = extras.cleanup(sentence)
  # we return a value which is:
  # (((positive + negtive) / length of sentence) * (either -1 or 1 if there are inverters)) * amplfying words
  return (((get_positive_sentiment(sentence) + get_negative_sentiment(sentence)) / len(sentence.split(" "))) * check_inverters(sentence)) * check_amplifiers(sentence)

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

# get the full sentiment of a whole text
# input > a string text (seperated by . and ,)
# output > a list of the sentiment of each sentence
def get_text_sentiment(text):
    # define the list that we will later append the sentence sentiments into
    sentiment_list = []
    # split the text into sentences using the multiple sep function (in this case we split it with "," and ".")
    sentences = extras.split_with_multiple_seperators(",", ".", text = text[0 : len(text) - 1])
    
    # loop over each sentence from the line before
    for x in range(len(sentences)):
        # add the sentiment of each sentence to the sentiment list
        sentiment_list.append(get_sentence_sentiment(sentences[x]))

    # return the sentiment list
    return sentiment_list