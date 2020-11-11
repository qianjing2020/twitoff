# web_app/routes/home_routes.py

from flask import Blueprint

# create blueprint instance, giving it name "home_routes"
home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
def index():
    x = 2 + 2
    return f"Hello World! {x}"


@home_routes.route("/about")
def about():
    return "About me"
