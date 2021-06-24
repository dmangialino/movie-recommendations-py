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
movies = parsed_response["results"]

# print(type(parsed_response["results"]))

# Create list of 10 movies to make it easier to review
#movies = []
#movie_list = parsed_response["results"]
#for p in range(0,9):
#    movies.append(parsed_response["results"][p])


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

print("------------------------------")

# Select recommendation randomly from list of movies that match criteria
# Shuffle function found on W3Schools (https://www.w3schools.com/python/ref_random_shuffle.asp)
rec_title = ""
rec_rating = ""
if(len(movies_block) > 0):
    random.shuffle(movies_block)
    #rec_title = movies_block[0]["original_title"]
    #rec_rating = movies_block[0]["vote_average"]
    rec = movies_block[0]
elif(len(movies) > 0):
    random.suffle(movies)
    #rec_title = movies[0]["original_title"]
    #rec_rating = movies[0]["vote_average"]
    rec = movies[0]
else:
    # No movies match criteria
    # Randomly select movie from the CSV dataset
    csv_filepath = "data/tmdb_5000_movies.csv"
    movies_df = read_csv(csv_filepath)
    movies_csv = movies_df.to_dict("records")

    matching_genres = []
    search_genre = ""
    if(input_genre != "TV MOVIE"):
        search_genre = input_genre.title()
    
    else:
        # String concateation to translate "TV MOVIE" to "TV Movie" to find matches in CSV        
        print("TO DO")

    for n in movies_csv:
        if(search_genre in n["genres"]):
            #print(n["original_title"])
            matching_genres.append(n)
    print("LEN MATCHING GENRES: ", len(matching_genres))
    random.shuffle(matching_genres)
    rec_title = matching_genres[0]["original_title"]
    rec_rating = matching_genres[0]["vote_average"]

if(len(movies_block) == 0):
    print("We're sorry! There were no perfect matches, but we'll give you a recommendation we think you'll enjoy!")
    print("------------------------------")

#print("This is the movie you get and you don't get upset: ", rec_title)
#print("People gave this movie a rating of ", rec_rating)
print(rec)
print("------------------------------")
print("Data from The Movie Database API (https://www.themoviedb.org/documentation/api)")
print("------------------------------")


# SEND EMAIL RECEIPT



wants_email = input("Would you like an email receipt of your recommendation? (Y/N)? ").strip()
if wants_email.lower() in ['y','yes']:
    send_email = True
    user_email = input("Please type your email: ").strip()
    email_confirm = input("Please retype your email: ").strip()
    if user_email.lower() != email_confirm.lower():
        user_email = input("Emails do not match. Please retype your email: ").strip()

else:
    send_email = False

if send_email:
    from sendgrid import SendGridAPIClient
    from sendgrid.helpers.mail import Mail

    load_dotenv()

    SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY", default="OOPS, please set env var called 'SENDGRID_API_KEY'")
    SENDGRID_TEMPLATE_ID = os.getenv("SENDGRID_TEMPLATE_ID", default="OOPS, please set env var called 'SENDGRID_TEMPLATE_ID'")
    #SENDER_ADDRESS = os.getenv("SENDER_ADDRESS", default="OOPS, please set env var called 'SENDER_ADDRESS'")
    SENDER_ADDRESS = user_email

    # this must match the test data structure
    template_data = {
    "input_genre": input_genre,
    "input_age": input_age,
    "input_block": input_block,
    "rec_title": rec_title,
    } 

    client = SendGridAPIClient(SENDGRID_API_KEY)
    print("CLIENT:", type(client))

    message = Mail(from_email=SENDER_ADDRESS, to_emails=SENDER_ADDRESS)
    message.template_id = SENDGRID_TEMPLATE_ID
    message.dynamic_template_data = template_data
    print("MESSAGE:", type(message))

    try:
        response = client.send(message)
        print("RESPONSE:", type(response))
        print(response.status_code)
        print(response.body)
        print(response.headers)

    except Exception as err:
        print(type(err))
        print(err)
    finally:
        print("Thank you!")
else:
    print("Thank you!")

