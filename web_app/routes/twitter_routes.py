# web_app/routes/twitter_routes.py

from flask import Blueprint, render_template, jsonify
from web_app.models import db, User, Tweet, parse_records
from web_app.services.twitter_service import twitter_api_client
from web_app.services.basilica_service import basilica_api_client

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
    # return "OK"

    # fetch tweets
    tweets= twitter_api_client.user_timeline(screen_name, tweet_mode="extended", count=100)
    print("STATUSES COUNT:", len(tweets))
   
    # TODO: explore using the zip() function maybe...

    # Get tweets and write to db    
    all_tweet_texts = [tweet.full_text for tweet in tweets]
 
    embeddings = list(basilica_api_client.embed_sentences(
        all_tweet_texts, model='twitter'))
    print("Number of embeddings", len(embeddings))
    
    for index, tweet in enumerate(tweets):
        print(index)
        print(tweet.full_text)
        print("----")
        
        embedding = embeddings[index] 

        ## get existing tweet from the db or initialize a new one:
        db_tweet = Tweet.query.get(tweet.id) or Tweet(id=tweet.id)
        db_tweet.user_id = tweet.author.id  # or db_user.id
        db_tweet.full_text = tweet.full_text  
        db_tweet.embedding = embedding
        db.session.add(db_tweet)
    
    db.session.commit()
    
    
    #return render_template("user.html", user=db_user, tweets=statuses) # tweets=db_tweets
