# Twitoff
Predict the twitter user of a tweet: model return the most likely twitter users who would have twitted the tweet. 


### Flask

Create .flaskenv to specification to export 


### Specs on database handling:
~~~
$ flask db init
~~~ 
Run both when changing the schema:
~~~sh
$ flask db migrate 

$ flask db upgrade 

$ flask shell    # go to flash python shell to create all tables for the db
>>> from web_app.models import db
>>> db.create_all()

~~~

### Usage
Run the web app after store flask configurations in .flaskenv :
```sh
flask run
```

### Heroku postgresql 

source: https://devcenter.heroku.com/articles/heroku-postgresql#provisioning-heroku-postgres
