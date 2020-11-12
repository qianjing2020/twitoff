# web_app/routes/twitter_routes.py

from flask import Blueprint, render_template, jsonify
from web_app.models import db, User, Tweet, parse_records
from web_app.services.twitter_service import api as twitter_api_client
from web_app.services.basilica_service import basilica_api_client

# from web_app.services.basilica_service import basilica_api_client

twitter_routes = Blueprint("twitter_routes", __name__)

@twitter_routes.route("/users/<screen_name>/fetch")
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
    
    db.session.add(db_user)
    db.session.commit()
    # return "OK"

    # fetch tweets
    tweets = twitter_api_client.user_timeline(        screen_name, tweet_mode="extended", count=150)
    print("STATUSES COUNT:", len(tweets))

   
    # TODO: explore using the zip() function maybe...
        
    for tweet in tweets:
        print(tweet.full_text)
        print("----")
        
        breakpoint()
        embedding = basilica_api_client.embed_sentence(tweet.full_text, model="twitter") 

        ## get existing tweet from the db or initialize a new one:
        db_tweet = Tweet.query.get(tweet.id) or Tweet(id=tweet.id)
        db_tweet.user_id = tweet.author.id  # or db_user.id
        db_tweet.full_text = tweet.full_text  
        db_tweet.embedding = embedding
        db.session.add(db_tweet)
        
    db.session.commit()
    #breakpoint()
    
    #return render_template("user.html", user=db_user, tweets=statuses) # tweets=db_tweets
