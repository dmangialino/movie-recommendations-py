import os
from dotenv import load_dotenv
import requests
from pandas import read_csv 
import json
import datetime
from operator import itemgetter
import random

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

#print(gen_id)


# API call based on genre
request_url = f"https://api.themoviedb.org/3/discover/movie?api_key={TMBD_API_KEY}&with_genre={gen_id}"

response = requests.get(request_url)
parsed_response = json.loads(response.text)

# print(type(parsed_response["results"]))

# Create list of 10 movies to make it easier to review
movies = []
movie_list = parsed_response["results"]
for p in range(0,9):
    movies.append(parsed_response["results"][p])

while True:
    input_age = input("Would you prefer a recently released film?(Y/N) ").upper()
    if (input_age == "Y") or (input_age == "N"):
        break
    

today = datetime.datetime.today()
# date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d')
new = []
old = []

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

# Resetting Movies list based on user preference for recent vs. older movie
if(input_age == "Y"):
    movies = new
elif(input_age == "N"):
    movies = old
else:
    print("Invalid input. Proceeding with all movies currently selected.")


# Blockbuster film
while True:
    input_block = input("Would you like to see a blockbuster?(Y/N) ").upper()
    if (input_block == "Y") or (input_block == "N"):
        break


#print(len(movies))
movies_block = []

if(input_block == "Y"):
    for n in movies:
        if(float(n["vote_average"]) > float(7.0)):
            movies_block.append(n)
elif(input_block == "N"):
    for n in movies:
        if(float(n["vote_average"]) <= float(7.0)):
            movies_block.append(n)
else:
    print("INVALID INPUT")

#print(len(movies_block))
#for n in movies_block:
#    print(n["original_title"], n["vote_average"])

#if(input_block == "Y"):
#    for n in movies:
#        if(float(n["vote_average"]) < 7.0):
#            movies.remove(n)
#elif(input_block == "N"):
#    print(len(movies))
#    for n in movies:
#        print(n["original_title"], float(n["vote_average"]))
#        if(float(n["vote_average"]) >= 7.0):
#            print("NEED TO REMOVE")
#            movies.remove(n)
#else:
#    print("Invalid input. Proceeding with all movies currently selected.")


# Check that results are not empty...if not, use movies_block, else, revert back to movies
# Radomly sort resulsts so can provide different recommendation with same criteria (e.g., different one? otpion)
# Shuffle function found on W3Schools (https://www.w3schools.com/python/ref_random_shuffle.asp)
if(len(movies_block) > 0):
    random.shuffle(movies_block)
    print("This is the movie you get and you don't get upset: ", movies_block[0]['original_title'], 'People gave this movie a rating of ', movies_block[0]['vote_average'])
    print("Data from The Movie Database API (https://www.themoviedb.org/documentation/api)")
else:
    print("We're sorry! There were no perfect matches, but we'll give you a recommendation we think you'll enjoy!")
    random.suffle(movies)
    print("This is the movie you get and you don't get upset: ", movies[0]['original_title'], 'People gave this movie a rating of ', movies[0]['vote_average'])
    print("Data from The Movie Database API (https://www.themoviedb.org/documentation/api)")


#movies.sort(reverse=True, key=itemgetter('vote_average'))
