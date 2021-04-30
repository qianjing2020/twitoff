# web_app/models.py

# The data that will be stored in the database will be represented by a collection of classes, usually called database models.

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy() # the db object

migrate = Migrate() # the migration engine

"""Use db.Model as base model to create model classes for database schema"""
# class for book data, correspond to table "book" in database
class Book(db.Model):
    # no need to define a __init__ method: SQLAlchemy models has an implicit constructor
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    author_id = db.Column(db.String(128))

    def __repr__(self):
        return f"<Book {self.id} {self.title}>"

# class for twitter user data
class User(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    screen_name = db.Column(db.String(128), nullable=False)
    name = db.Column(db.String)
    location = db.Column(db.String)
    followers = db.Column(db.Integer)
    latest_tweet_id = db.Column(db.BigInteger)

    def __repr__(self):
        return f"<User {self.id} {self.screen_name}>"

# class for twitter tweets data
class Tweet(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    # user_id column is a foreigh key, point to user table column id
    user_id = db.Column(db.BigInteger, db.ForeignKey("user.id"))
    full_text = db.Column(db.String(500))
    #embedding = db.Column(db.PickleType)
    # when invoking user on any Tweet, it will automaticaly form a relationship to corresponding user record, and invoke .user on any Tweet and bidirectionaly also associate tweet with a user, so user.tweets will automatically get all tweets from the user. and tweet.user will get the user from the user table. 
    user = db.relationship("User", backref=db.backref("tweets", lazy=True))

def parse_records(database_records):
    """
    A helper method for converting a list of database record objects into a list of dictionaries, so they can be returned as JSON

    Param: database_records (a list of db.Model instances)

    Example: parse_records(User.query.all())

    Returns: a list of dictionaries, each corresponding to a record, like...
        [
            {"id": 1, "title": "Book 1"},
            {"id": 2, "title": "Book 2"},
            {"id": 3, "title": "Book 3"},
        ]
    """
    parsed_records = []
    for record in database_records:
        print(record)
        parsed_record = record.__dict__
        del parsed_record["_sa_instance_state"]
        parsed_records.append(parsed_record)
    return parsed_records
