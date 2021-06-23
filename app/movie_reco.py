# Import os  and load_dotenv to read variables from .env
# Import read_csv from pandas to process CSV
import os
from dotenv import load_dotenv
import requests
from pandas import read_csv 
import json
import datetime
from operator import itemgetter

load_dotenv()

# Get TMDb API key
TMBD_API_KEY = os.getenv("TMBD_API_KEY")


csv_filepath = "data/tmdb_5000_movies.csv"
movies_df = read_csv(csv_filepath)

# Create Dictionary of Genres
genre_url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={TMBD_API_KEY}"
genre_response = requests.get(genre_url)
parsed_genre = json.loads(genre_response.text)
genres_list = parsed_genre["genres"]
genres = {}
for g in genres_list:
    genres.update({g["name"].upper():g["id"]})
print(genres)

input_genre = input("Please enter a genre for a film you would like to see ").upper()
gen_id = genres[input_genre]

print(gen_id)
# Testing API call
request_url = f"https://api.themoviedb.org/3/discover/movie?api_key={TMBD_API_KEY}&with_genre={gen_id}"

response = requests.get(request_url)



parsed_response = json.loads(response.text)

# print(type(parsed_response["results"]))

# Create list of 10 movies to make it easier to review
movies = []
movie_list = parsed_response["results"]
for p in range(0,9):
    movies.append(parsed_response["results"][p])

input_age = input("Would you prefer a recently released film?(Y/N) ").upper()
today = datetime.datetime.today()
# date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d')
new = []
old = []

for n in movies:
    date_time_obj = datetime.datetime.strptime(n['release_date'], '%Y-%m-%d')
    if (today - date_time_obj).days < 720:
        new.append(n)
    else:
        old.append(n)


# One of the movies (infinite) release date is in future...
# print("new", new)
# for n in new:
#     print(n["release_date"])
# print("old", old)

# Resetting Movies list based on user preference
if input_age == "Y":
    movies = new
else:
    movies = old

input_block = input("Would you like to see a blockbuster?(Y/N) ").upper()

if input_block == "Y":
    for n in movies:
        if float(n['vote_average']) < 7:
            movies.remove(n)
else:
    for n in movies:
        if float(n['vote_average']) >= 7:
            movies.remove(n)

movies.sort(reverse=True, key=itemgetter('vote_average'))

print("This is the movie you get and you don't get upset: ", movies[0]['original_title'], 'People gave this movie a rating of ', movies[0]['vote_average'])



# print("------------------------------")
# print("------------------------------")
# print("------------------------------")
# print(movies)
# print("------------------------------")
# print("------------------------------")
# print("------------------------------")

# print(type(movies[0]["release_date"]))
# print(movies[0]["release_date"])
# print(type(today))
# # Create a list of dictionaries from DataFrame
# movies = movies_df.to_dict("records")

# # Checking if each movie is printable
# #for movie in movies:
# #    print(movie)

# # Print keys for each dictionary in the list
# # print(movies[0].keys())
# # dict_keys(['budget', 'genres', 'homepage', 'id', 'keywords', 'original_language', 'original_title', 'overview', 'popularity', 'production_companies', 'production_countries', 'release_date', 'revenue', 'runtime', 'spoken_languages', 'status', 'tagline', 'title', 'vote_average', 'vote_count'])


# ########## GENRE ##########

# # Create list of available genres against which to compare user inputs
# available_genres = []

# genre = input("Please select a genre. Options include, but are not limited to: 'Comedy', 'Drama', 'Biography'. See README for full list of genres ")

# # Add user input validation

# # Create matching genre list and append movies that match the genre selected by the user
# matching_genre = []
# for movie in movies:
#     if(genre in movie["genres"]):
#         matching_genre.append(movie)


# ########## FOREIGN / US FILMS ##########

# # Foreign films
# foreign_film = input("Would you prefer a foreign or US film? Enter '1' for foreign film, '2' for US film, or '3' for no preference ")

# # Add user input validation
# # Logic can be movie["original_language"]=="en" for US film or not "en" for a foreign film

# matching_country = []

# if(foreign_film=="1"):
#     print("Foreign film")
#     for movie in matching_genre:
#         if(movie["original_language"] != "en"):
#             matching_country.append(movie)
# elif(foreign_film=="2"):
#     print("US film")
#     for movie in matching_genre:
#        if(movie["original_language"] == "en"):
#             matching_country.append(movie)
# elif(foreign_film=="3"):
#     print("Either foreign or US film")
#     for movie in matching_genre:
#         matching_country.append(movie)
# else:
#     print("Issue processing user input. Will proceed with both foreign and US films.")
#     for movie in matching_genre:
#         matching_country.append(movie)

# for movie in matching_country:
#     print(movie["title"])


# ########## MOVIE LENGTH ##########

# # Further narrow by time
# length = input("Approximately how long should the movie be? Please enter '1' for 60 mins, '2' for 90 mins, '3' for 120 mins, or '4' for any ")

# # Input validation
# # Logic based on movie["runtime"]

# if(length=="1"):
#     print("60 mins")
# elif(length=="2"):
#     print("90 mins")
# elif(length=="3"):
#     print("120 mins")
# elif(length=="4"):
#     print("any")
# else:
#     print("Issue processing user input. Will proceed with any length.")


# ########## OLD VS. NEW MOVIES ##########
# # Will need to define trhesholds / work out logic based on movie["year"]

# # Get input

# # Input Validation
# # Logic


# ########## SELECT  TITLE FROM LIST OF ALL MOVIES THAT MEET CRITERIA ##########
# # I think this should be random at this stage to avoid generating the same recommendation each time the app is run with the same inputs
# # Maybe we can ask user if they want the most popular that meets the specified criteria or a random title


# ########## PRINT MOVIE TITLE & INFORMATION (E.G., YEAR, GENRE, DESCRIPTION, ETC.) ##########
# # Add attribution to Kaggle / TMDb

