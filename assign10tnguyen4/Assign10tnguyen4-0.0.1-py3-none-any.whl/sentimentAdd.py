def sentimentAdd(df):
    sentiments = []
    for i in range(0,len(df["text"])):
        sentiments.append(get_tweet_sentiment(df["text"][i]))
    
    df['sentiments'] = sentiments
    
    return df