# https://setuptools.pypa.io/en/stable/userguide/datafiles.html

from tweetSentimentAnalysis_MP import analyze
import os

data_file = os.path.join(os.path.dirname(__file__), 'vaccination_tweets.csv')
analyze(data_file)