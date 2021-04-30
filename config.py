# /config.py

import os
from dotenv import load_dotenv

load_dotenv('.env')

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object): 

    SECRET_KEY = os.getenv("SECRET_KEY", default="you-will-never-guess-it")

    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL") or 'sqlite:///'+os.path.join(basedir, 'test.db')  # search for the URL in .env or else create a local file

    # if true it will signal the app everytime the database is about to change
    SQLALCHEMY_TRACK_MODIFICATIONS = False
