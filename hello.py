# hello.py

from flask import Flask

app = Flask(__name__)

# print(__name__)
# print(type(app))

@app.route("/")
def index():
    x = 2 + 2
    return f"Hello World! {x}"

@app.route("/about")
def about():
    return "About me"