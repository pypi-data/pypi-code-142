import pandas as pd
import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob

class TwitterClient(object):
    '''
    Generic Twitter Class for sentiment analysis.
    '''
    def __init__(self):
        '''
        Class constructor or initialization method.
        '''
        # keys and tokens from the Twitter Dev Console
        consumer_key = 'XXXXXXXXXXXXXXXXXXXXXXXX'
        consumer_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX'
        access_token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX'
        access_token_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXX'
  
        # attempt authentication
        try:
            # create OAuthHandler object
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            # set access token and secret
            self.auth.set_access_token(access_token, access_token_secret)
            # create tweepy API object to fetch tweets
            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed")
  
    def clean_tweet(self, tweet):
        '''
        Utility function to clean tweet text by removing links, special characters
        using simple regex statements.
        '''
        self.tweet = tweet
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", self.tweet).split())

    def get_tweet_sentiment(self, tweet):
        '''
        Utility function to classify sentiment of passed tweet
        using textblob's sentiment method
        '''
        # create TextBlob object of passed tweet text
        analysis = TextBlob(self.clean_tweet(tweet))
        # set sentiment
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'

def sentiment(df):
    api = TwitterClient()
    #list made to store sentiments
    sentiment = []
    
    #going through each tweet and using get_tweet_sentiment() to clean tweet and get sentiment
    #then adding it to the end of sentiment list
    for tweet in df['text']:
        sentiment.append(TwitterClient.get_tweet_sentiment(api, tweet))
    
    #adding new sentiment column to dataframe
    df['sentiment'] = sentiment
    return df        


#reading only the 'text' column from csv file and making that into a dataframe
data = pd.read_csv('vaccination_tweets.csv', usecols = ['text'])

#calling function made earlier to add sentiment column
sentiment(data)

#printing the first 30 records in the dataframe
print(data.head(n = 30))

#setting variables to count amount of each kind of tweet
positive = 0
neutral = 0
negative = 0
#total amount of tweets
length = len(data.index)

#looping through dataframe to count amount of each kind of tweet
for sentiment in data['sentiment']:
    if (sentiment == 'positive'):
        positive += 1
    elif (sentiment == 'neutral'):
        neutral += 1
    elif (sentiment == 'negative'):
        negative += 1

#getting percentage of each kind of tweet
pos_percent = (positive / length) * 100
neut_percent = (neutral / length) * 100
neg_percent = (negative / length) * 100

#printing percentages
print('\npercentage of positive tweets: %', pos_percent)
print('percentage of neutral tweets: %',neut_percent)
print('percentage of negative tweets: %',neg_percent)