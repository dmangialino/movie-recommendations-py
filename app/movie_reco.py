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

print("AVAILABLE GENRES: ")
for genre in genres_list:
    print(genre["name"])

#print(genres)
print("------------------------------")

while True:
    input_genre = input("Please enter a genre for a film you would like to see (select from list above): ").upper()
    if input_genre in genres:
        break
    else:
        print("Invalid genre. Please select a genre from the list above.")

gen_id = genres[input_genre]
    

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


# New release
print("------------------------------")
while True:
    input_age = input("Would you prefer a recently released film? (Y/N) ").upper()
    if (input_age == "Y") or (input_age == "N"):
        break
    else:
        print("Invalid input. Please input 'Y' or 'N")
    

today = datetime.datetime.today()
new = []
old = []

for n in movies:
    if "release_date" in n:
        date_time_obj = datetime.datetime.strptime(n['release_date'], '%Y-%m-%d')
        if(today - date_time_obj).days < 720:
            new.append(n)
        else:
            old.append(n)

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
print("------------------------------")
while True:
    input_block = input("Would you like to see a blockbuster? (Y/N) ").upper()
    if (input_block == "Y") or (input_block == "N"):
        break
    else:
        print("Invalid input. Please input 'Y' or 'N")


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


print("------------------------------")

#movies.sort(reverse=True, key=itemgetter('vote_average'))


# Select recommendation randomly from list of movies that match criteria
# Shuffle function found on W3Schools (https://www.w3schools.com/python/ref_random_shuffle.asp)
rec_title = ""
rec_rating = ""
if(len(movies_block) > 0):
    random.shuffle(movies_block)
    rec_title = movies_block[0]["original_title"]
    rec_rating = movies_block[0]["vote_average"]
elif(len(movies) > 0):
    random.suffle(movies)
    rec_title = movies[0]["original_title"]
    rec_rating = movies[0]["vote_average"]
else:
    # No movies match criteria
    # Randomly select movie from the CSV dataset
    print("NO MATCHES")

if(len(movies_block) == 0):
    print("We're sorry! There were no perfect matches, but we'll give you a recommendation we think you'll enjoy!")
    print("------------------------------")

print("This is the movie you get and you don't get upset: ", rec_title)
print("People gave this movie a rating of ", rec_rating)
print("------------------------------")
print("Data from The Movie Database API (https://www.themoviedb.org/documentation/api)")
print("------------------------------")
