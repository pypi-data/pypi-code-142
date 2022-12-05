#Mitch Regan
#CS501 Assignment 10
#Fall 2022
import pandas as pd
import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob


def clean_tweet(tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())


#Links to an external site. to generate the string 'positive' or 'negative'. Thus for each tweet, you will get a string level
def get_tweet_sentiment(tweet):
    analysis = TextBlob(clean_tweet(tweet))
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity == 0:
        return 'neutral'
    else:
        return 'negative'


#Write a function that takes a Pandas dataframe as an argument with one column named 'text' representing tweets.
def readTweets(df):
    print("Analyzing tweets...")
    sentiment = []

    #Use the Textblob library to find the sentiment of each tweet in the dataframe. Use clean_tweet() and get_tweet_sentiment() functions from here
    for t in df.text:
        sentiment.append(get_tweet_sentiment(t))

    #You need to create a column named sentiment in the data frame that stores the sentiment of each tweet. Returns the modified data frame
    df['Sentiment'] = sentiment
    return df


#Write code to load the CSV file into a pandas dataframe and call your method to get the modified dataframe.
print("Reading tweets...")
df = pd.read_csv('./vaccination_tweets.csv')
df = readTweets(df)

#Display the first 30 records from the dataframe.
print("First 30 records:")
print(df.head(30))

#Calculate and display the percentages of positive, negative, and neutral tweets in the dataset/dataframe.
total = len(df)
pos = len(df.loc[df['Sentiment'] == 'positive'])
neg = len(df.loc[df['Sentiment'] == 'negative'])
neu = len(df.loc[df['Sentiment'] == 'neutral'])
print("\nTotal tweets:", total)
print(" - Positive tweets:", pos, "Percent positive:", (pos/total))
print(" - Negative tweets:", neg, "Percent negative:", (neg/total))
print(" - Neutral tweets: ", neu, "Percent neutral: ", (neu/total))