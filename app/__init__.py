# twitoff_app/__init__.py

"""the Flask application object creation has to be in the __init__.py file"""

from flask import Flask

from config import Config

from twitoff_app.models import db, migrate
from twitoff_app.routes.home_routes import home_routes
from twitoff_app.routes.book_routes import book_routes
from twitoff_app.routes.twitter_routes import twitter_routes
from twitoff_app.routes.pred_routes import pred_routes

def create_app():
    # create the application factory functionf
    app = Flask(__name__) 

    # load configurations
    app.config.from_object(Config)  
    
    # prepare app for SQLAlchemy. it DOES NOT bind db to the app though 
    db.init_app(app)
    # db.reflect(app=app)

    # associate migration engine with app and db
    migrate.init_app(app, db)

    # register all blueprints for view functions
    app.register_blueprint(home_routes)
    app.register_blueprint(book_routes)
    app.register_blueprint(twitter_routes)
    app.register_blueprint(pred_routes)

    return app

