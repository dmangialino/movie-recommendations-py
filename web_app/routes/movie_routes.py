# web_app/routes/movie_routes.py

from flask import Blueprint, request,  render_template, redirect, jsonify, flash

from app.movie_reco_web import new_movie
from app.movie_reco_web import new_movie

movie_routes = Blueprint("movie_routes", __name__)

# @movie_routes.route("/movie/results")
# def movie_results_api():
    
    
    
#     # print("URL PARAMS:", dict(request.args))
#     genre = "HORROR" # requests.args.get("input_genre") or "HORROR"
#     age = "Y" # requests.args.get("input_age") or "Y"
#     block =  "Y" # requests.args.get("input_block") or "Y"

#     return new_movie(input_genre=genre, input_age=age, input_block=block)
#     if results:
#         return new_movie(input_genre=genre, input_age=age, input_block=block)
#     # else:
#     #     return jsonify({"message":"Invalid Selection.  Please Try again"}), 404

@movie_routes.route("/movie/form")
def movie_form():
    print("MOVIE FORM...")
    return render_template("movie_form.html")

@movie_routes.route("/movie/results", methods=["POST"])
def movie_results():
    print("YOUR MOVIE SELECTION")

    if request.method == "GET":
        return "Hello this is GET"
        # print("URL PARAMS:", dict(request.args))
        # request_data = dict(request.args)
    if request.method == "POST": # the form will send a POST
        print("FORM DATA:", dict(request.form))
        request_data = dict(request.form)

    genre = request_data.get("input_genre").upper() ## or "HORROR"
    # genre = "HORROR"
    age = request_data.get("input_age").upper() ## or "Y"
    # age = "Y"
    block = request_data.get("input_block").upper() ## or "Y"
    # block = "Y"

    results = new_movie(input_genre=genre, input_age=age, input_block=block)
    # return render_template("movie_results.html", input_genre=genre, input_age=age, input_block=block, results=results)
    if results:
        # flash("Movie Rec Generated Successfully!", "success")
        return render_template("movie_results.html", input_genre=genre, input_age=age, input_block=block, results=results)
    else:
        # flash("Invalid Entry!", "danger")
        return redirect("/movie/form")