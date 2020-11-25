# web_app/services/twitter_service.py

import tweepy
import os
from dotenv import load_dotenv

load_dotenv()

TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")


class TwitterAPI():
    def __init__(self):
        self.auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
        self.auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
        # print("AUTH", auth)
        self.connect = tweepy.API(self.auth)

twitter_api_client = TwitterAPI().connect

if __name__ == "__main__":
    api = TwitterAPI().connect

    # get user
    screen_name = "billgates" # kamalaharris
    user = api.get_user(screen_name)
    
    print("User screen name:", user.screen_name)
    print("User name: ", user.name)
    print("Followed by: ", user.followers_count)

    # get tweets
    tweets = api.user_timeline(screen_name, tweet_mode="extended" )
    print(type(tweets))
    # from pprint import pprint
    # pprint(tweets[0]._json)

    last5 = tweets[:5]
    for tweet in last5:
        print(tweet.id, tweet.full_text)