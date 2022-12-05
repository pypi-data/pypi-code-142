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