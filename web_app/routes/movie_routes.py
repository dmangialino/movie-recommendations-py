# web_app/routes/movie_routes.py

from flask import Blueprint, request, jsonify, render_template, redirect, flash

from app.movie_reco import new_movie

movie_routes = Blueprint("movie_routes", __name__)

@movie_routes.route("/movie/form")
def movie_form():
    print("MOVIE FORM...")
    return render_template("movie_form.html")

@movie_routes.route("/movie/results", methods=["GET", "POST"])
def movie_results():
    print("YOUR MOVIE SELECTION")

    if request.method == "GET":
        print("URL PARAMS:", dict(request.args))
        request_data = dict(request.args)
    elif request.method == "POST": # the form will send a POST
        print("FORM DATA:", dict(request.form))
        request_data = dict(request.form)

    input_genre = request_data.get("input_genre") or "HORROR"
    input_age = request_data.get("input_age") or "Y"
    input_block = request_data.get("input_block") or "Y"

    results = new_movie(genre=input_genre, age=input_age, blockbuster=input_block)
    if results:
        #flash("Weather Forecast Generated Successfully!", "success")
        return render_template("movie_results.html", genre=input_genre, age=input_age, blockbuster=input_block, results=results)
    else:
        #flash("Geography Error. Please try again!", "danger")
        return redirect("/movie/results")