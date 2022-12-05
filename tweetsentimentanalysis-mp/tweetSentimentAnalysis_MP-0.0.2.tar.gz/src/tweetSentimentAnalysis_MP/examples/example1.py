# https://setuptools.pypa.io/en/stable/userguide/datafiles.html

import tweetSentimentAnalysis_MP as tsa
import os

data_file = os.path.join(os.path.dirname(__file__), 'vaccination_tweets.csv')
tsa.analyze(data_file)