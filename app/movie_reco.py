# Import os  and load_dotenv to read variables from .env
# Import read_csv from pandas to process CSV
import os
from dotenv import load_dotenv
import requests
from pandas import read_csv 

load_dotenv()

# Get TMDb API key
TMBD_API_KEY = os.getenv("TMBD_API_KEY")


csv_filepath = "data/tmdb_5000_movies.csv"
movies_df = read_csv(csv_filepath)

# Testing API call
request_url = f"https://api.themoviedb.org/3/movie/550?api_key={TMBD_API_KEY}"
response = requests.get(request_url)

print(response)
print("-----------------")
print("-----------------")
print("-----------------")
print("-----------------")

# Create a list of dictionaries from DataFrame
movies = movies_df.to_dict("records")

# Checking if each movie is printable
#for movie in movies:
#    print(movie)

# Print keys for each dictionary in the list
# print(movies[0].keys())
# dict_keys(['budget', 'genres', 'homepage', 'id', 'keywords', 'original_language', 'original_title', 'overview', 'popularity', 'production_companies', 'production_countries', 'release_date', 'revenue', 'runtime', 'spoken_languages', 'status', 'tagline', 'title', 'vote_average', 'vote_count'])


########## GENRE ##########

# Create list of available genres against which to compare user inputs
available_genres = []

genre = input("Please select a genre. Options include, but are not limited to: 'Comedy', 'Drama', 'Biography'. See README for full list of genres ")

# Add user input validation

# Create matching genre list and append movies that match the genre selected by the user
matching_genre = []
for movie in movies:
    if(genre in movie["genres"]):
        matching_genre.append(movie)


########## FOREIGN / US FILMS ##########

# Foreign films
foreign_film = input("Would you prefer a foreign or US film? Enter '1' for foreign film, '2' for US film, or '3' for no preference ")

# Add user input validation
# Logic can be movie["original_language"]=="en" for US film or not "en" for a foreign film

matching_country = []

if(foreign_film=="1"):
    print("Foreign film")
    for movie in matching_genre:
        if(movie["original_language"] != "en"):
            matching_country.append(movie)
elif(foreign_film=="2"):
    print("US film")
    for movie in matching_genre:
       if(movie["original_language"] == "en"):
            matching_country.append(movie)
elif(foreign_film=="3"):
    print("Either foreign or US film")
    for movie in matching_genre:
        matching_country.append(movie)
else:
    print("Issue processing user input. Will proceed with both foreign and US films.")
    for movie in matching_genre:
        matching_country.append(movie)

for movie in matching_country:
    print(movie["title"])


########## MOVIE LENGTH ##########

# Further narrow by time
length = input("Approximately how long should the movie be? Please enter '1' for 60 mins, '2' for 90 mins, '3' for 120 mins, or '4' for any ")

# Input validation
# Logic based on movie["runtime"]

if(length=="1"):
    print("60 mins")
elif(length=="2"):
    print("90 mins")
elif(length=="3"):
    print("120 mins")
elif(length=="4"):
    print("any")
else:
    print("Issue processing user input. Will proceed with any length.")


########## OLD VS. NEW MOVIES ##########
# Will need to define trhesholds / work out logic based on movie["year"]

# Get input

# Input Validation
# Logic


########## SELECT  TITLE FROM LIST OF ALL MOVIES THAT MEET CRITERIA ##########
# I think this should be random at this stage to avoid generating the same recommendation each time the app is run with the same inputs
# Maybe we can ask user if they want the most popular that meets the specified criteria or a random title


########## PRINT MOVIE TITLE & INFORMATION (E.G., YEAR, GENRE, DESCRIPTION, ETC.) ##########
# Add attribution to Kaggle / TMDb

