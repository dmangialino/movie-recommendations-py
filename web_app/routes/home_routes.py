# web_app/routes/home_routes.py

from flask import Blueprint, request, render_template

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
@home_routes.route("/home")
def index():
    print("HOME...")
    # return "Welcome Home"
    return render_template("home.html")

@home_routes.route("/about")
def about():
    print("ABOUT...")
    # return "About Me"
    return render_template("about.html")

# @home_routes.route("/hello")
# def hello_world():
#     print("HELLO...", dict(request.args))
#     # NOTE: `request.args` is dict-like, so below we're using the dictionary's `get()` method,
#     # ... which will return None instead of throwing an error if key is not present
#     # ... see also: https://www.w3schools.com/python/ref_dictionary_get.asp
#     name = request.args.get("name") or "World"
#     message = f"Hello, {name}!"
#     # return message
#     return render_template("hello.html", message=message)

# from app.movie_reco import new_movie

# movie_routes = Blueprint("movie_routes", __name__)

# @home_routes.route("/movie/form")
# def weather_form():
#     print("MOVIE FORM...")
#     return render_template("movie_form.html")

# @home_routes.route("/movie/results", methods=["GET", "POST"])
# def weather_forecast():
#     print("YOUR MOVIE SELECTION")

#     if request.method == "GET":
#         print("URL PARAMS:", dict(request.args))
#         request_data = dict(request.args)
#     elif request.method == "POST": # the form will send a POST
#         print("FORM DATA:", dict(request.form))
#         request_data = dict(request.form)

#     input_genre = request_data.get("input_genre") or "HORROR"
#     input_age = request_data.get("input_age") or "Y"
#     input_block = request_data.get("input_block") or "Y"

#     results = new_movie(genre=input_genre, age=input_age, blockbuster=input_block)
#     if results:
#         #flash("Weather Forecast Generated Successfully!", "success")
#         return render_template("movie_results.html", genre=input_genre, age=input_age, blockbuster=input_block, results=results)
#     else:
#         #flash("Geography Error. Please try again!", "danger")
#         return redirect("/movie/results")