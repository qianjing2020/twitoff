#import pandas as pd
from gensim.models import Word2Vec

from twitter_service import twitter_api_client

screen_name='elonmusk'
tweets = twitter_api_client.user_timeline(screen_name, tweet_mode="extended", count=100)
print("STATUSES COUNT:", len(tweets))

# tweets_words 
# model = Word2Vec(tweets, min_count=1, size=100, workers=4, window=3, sg=1) 


for tweet in tweets:
    print(tweet.full_text)
    print('-----------------')
    breakpoint()
    

exit()
# Select skip-gram (sg) algorithm not CBOW, because the former can capture two semantics for a single word.
model = Word2Vec(tweet_words, min_count=1, size=100, workers=4, window=3, sg=1)  # size:output vector size
