# Twitoff
Predict the twitter user of a tweet: model return the most likely twitter users who would have twitted the tweet. 

### Specs on database handling:

Run both when changing the schema:
~~~sh
FLASK_APP=web_app flask db migrate #>creates the db

FLASK_APP=web_app flask db upgrade #> creates the specified table
~~~

### Usage
Run the web app:
```sh
FLASK_APP=web_app flask run
```
Heroku postgresql 

source: https://devcenter.heroku.com/articles/heroku-postgresql#provisioning-heroku-postgres
