import re
import pandas as pd
import tweepy
from textblob import TextBlob

def clean_tweet(tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])(\w+:\/\/\S+)", " ", tweet).split())

def get_tweet_sentiment(tweet):
        # create TextBlob object of passed tweet text
        analysis = TextBlob(clean_tweet(tweet))
        # set sentiment
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'

def sentimentAdd(df):
    sentiments = []
    for i in range(0,len(df["text"])):
        sentiments.append(get_tweet_sentiment(df["text"][i]))
    
    df['sentiments'] = sentiments
    
    return df

def tweetRatio(df):
    # picking positive tweets from tweets
    ptweets = []
    for i in range(0,len(df["text"])):
        if df["sentiments"][i] == 'positive':
            ptweets.append(df['text'][i])
        
    ntweets = []
    for i in range(0,len(df["text"])):
        if df["sentiments"][i] == 'negative':
            ntweets.append(df['text'][i])
    # percentage of positive tweets
    print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(df['text'])))
    # percentage of negative tweets
    print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(df['text'])))
    # percentage of neutral tweets
    print("Neutral tweets percentage: {} %".format(100*(len(df['text']) -(len( ntweets )+len( ptweets)))/len(df['text'])))

df_csv = pd.read_csv('vaccination_tweets.csv')

df_re = sentimentAdd(df_csv)

df_re.head(30) #prints - but cannot print w/ tweetRatio function at same time

tweetRatio(df_re)