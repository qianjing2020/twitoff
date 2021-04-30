# twitoff_app/routes/twitter_routes.py

from flask import Blueprint, render_template, jsonify

from twitoff_app.models import db, User, Tweet, parse_records
from twitoff_app.services.twitter_service import twitter_api_client
from twitoff_app.services.nlp_service import DocCompare
from pprint import pprint


twitter_routes = Blueprint("twitter_routes", __name__)

@twitter_routes.route("/users/<screen_name>/fetch") # dynamic route with user-input screen_name
def fetch_user(screen_name=None):

    print(screen_name)
    # fetch data from twitter api
    twitter_user = twitter_api_client.get_user(screen_name)
    
    # get existing user from the db OR initialize a new one:
    db_user = User.query.get(twitter_user.id) or User(id=twitter_user.id)
    
    db_user.screen_name = twitter_user.screen_name
    db_user.name = twitter_user.name
    db_user.location = twitter_user.location
    db_user.followers_count = twitter_user.followers_count

    # store the data in the database
    db.session.add(db_user)
    db.session.commit()

    # fetch tweets
    tweets= twitter_api_client.user_timeline(screen_name, tweet_mode="extended", count=100)
    print("STATUSES COUNT:", len(tweets))

    # Get tweets and write to db    
    all_tweet_texts = [t.full_text for t in tweets]
    
    
    for index, tweet in enumerate(tweets):
        print(index)
        print(tweet.full_text)
        print("----")   
        ## get existing tweet from the db or initialize a new one:
        db_tweet = Tweet.query.get(tweet.id) or Tweet(id=tweet.id)
        db_tweet.user_id = tweet.author.id  # or db_user.id
        db_tweet.full_text = tweet.full_text          
        db.session.add(db_tweet)
    
    db.session.commit()

    return render_template("user.html", user=db_user, tweets=tweets[:10]) # just show 10 tweets on webpage
