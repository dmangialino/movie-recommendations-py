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

#csv_filepath = "data/tmdb_5000_movies.csv"
#movies_df = read_csv(csv_filepath)

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


# Added validation that n has a "release_date" 
for n in movies:
    if "release_date" in n:
        date_time_obj = datetime.datetime.strptime(n['release_date'], '%Y-%m-%d')
        if(today - date_time_obj).days < 720:
            new.append(n)
        else:
            old.append(n)

#print("LEN NEW", len(new))
#print("LEN OLD", len(old))
#print("MOVIES BEFORE RELEASE DATA LOGIC: ", len(movies))

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

print("MOVIES AFTER RELEASE DATA LOGIC: ", len(movies))

input_block = input("Would you like to see a blockbuster?(Y/N) ").upper()


# Add input validation


if input_block == "Y":
    for n in movies:
        if float(n['vote_average']) < 7:
            movies.remove(n)
else:
    for n in movies:
        if float(n['vote_average']) >= 7:
            movies.remove(n)

# Need to add validation that movies is not empty
# If yes, revert to version before last user input


# Maybe we should make this a random sort so we can provide different recommendation for same criteria
# We could then implement a "give me a different one" option for the same criteria
movies.sort(reverse=True, key=itemgetter('vote_average'))


print("This is the movie you get and you don't get upset: ", movies[0]['original_title'], 'People gave this movie a rating of ', movies[0]['vote_average'])
print("Data from The Movie Database API (https://www.themoviedb.org/documentation/api)")