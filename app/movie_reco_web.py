import os
from dotenv import load_dotenv
import requests
from pandas import read_csv 
import json
import datetime
import random

load_dotenv()

# Get TMDb API key from .env file
TMBD_API_KEY = os.getenv("TMBD_API_KEY")

# Function to call TMDb API to specified genre_id
def fetch_movie_genre(genre_id):
    request_url = f"https://api.themoviedb.org/3/discover/movie?api_key={TMBD_API_KEY}&with_genres={genre_id}&with_original_language=en"

    response = requests.get(request_url)
    parsed_response = json.loads(response.text)
    movies = parsed_response["results"]
    return movies

def generate_gen_list():
    # Create Dictionary of Genres
    genre_url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={TMBD_API_KEY}"
    genre_response = requests.get(genre_url)
    parsed_genre = json.loads(genre_response.text)
    genres_list = parsed_genre["genres"]
    genres = {}
    for g in genres_list:
        genres.update({g["name"].upper():g["id"]})

    # Print list of available genres from which user can choose
    # print("AVAILABLE GENRES: ")
    # for genre in genres_list:
    #     print(genre["name"])
    return genres



def get_variables():
    # Prompt user to input genre
    genres = generate_gen_list()
    print("________")
    while True:
        input_genre = input("Please enter a genre for a film you would like to see (select from list above): ").upper()
        if input_genre in genres:
            break
        else:
            print("Invalid genre. Please select a genre from the list above.")
    # Prompt user to input age of movie
    while True:
        input_age = input("Would you prefer a recently released film? (Y/N) ").upper()
        if (input_age == "Y") or (input_age == "N"):
            break
        else:
            print("Invalid input. Please input 'Y' or 'N")   
    # Prompt user to input blockbuster
    while True:
        input_block = input("Would you like to see a blockbuster? (Y/N) ").upper()
        if (input_block == "Y") or (input_block == "N"):
            break
        else:
            print("Invalid input. Please input 'Y' or 'N")
    return input_genre, input_age, input_block




def new_movie(input_genre, input_age, input_block):
    genres = generate_gen_list()

    print("------------------------------")

    gen_id = genres[input_genre]

    movies = fetch_movie_genre(gen_id)

    today = datetime.datetime.today()

    # Create two new lists ("new" and "old") to be used in release date logic
    new = []
    old = []

    # Iterate through movies list, appending movies with release date less than 720 days from today to the "new" list 
    #  ... and those with release date more than 720 days from today to the "old" list
    # Includes "if 'release_date' in n" statement to handle any movie entries that do not have a release date
    for n in movies:
        if "release_date" in n:
            date_time_obj = datetime.datetime.strptime(n['release_date'], '%Y-%m-%d')
            if(today - date_time_obj).days < 720:
                new.append(n)
            else:
                old.append(n)

    # Resetting Movies list based on user preference for recent vs. older movie
    if(input_age == "Y"):
        movies = new
    elif(input_age == "N"):
        movies = old
    else:
        print("Invalid input. Proceeding with all movies currently selected.")


    # Blockbuster film

    # Create new list to store all movies that met previous preferences (genre, recency) and "blockbuster" preference 
    #  ... (i.e., if user preference is yes, "vote_average" > 7.0, while for no, "vote_average <= 7.0")
    movies_block = []

    # Iterates through "movies" list, which contains movies that have met all previously specified preferences
    #  ... if user preference for blockbuster was "Y", appends movies with "vote_average" > 7.0 to "movies_block" list
    #  ... if user preference for blockbuster was "N", appends movies with "vote_average" <= 7.0 to "movies_block" list
    # Casts n["vote_average"] value and "7.0" to which it is compared to floats to ensure comparison is possible
    # Both paths include a "if 'release_date' in n" check to handle any movie entries that may not have a "release_date" key 
    if(input_block == "Y"):
        for n in movies:
            if("release_date" in n) and (float(n["vote_average"]) > float(7.0)):
                movies_block.append(n)
    elif(input_block == "N"):
        for n in movies:
            if("release_date" in n) and (float(n["vote_average"]) <= float(7.0)):
                movies_block.append(n)

    print("------------------------------")

    # Select recommendation randomly from list of movies that match criteria
    # Shuffle function found on W3Schools (https://www.w3schools.com/python/ref_random_shuffle.asp)
    rec_title = ""
    rec_rating = ""
    from_list = ""
    if(len(movies_block) > 0):
        from_list = "movies_block"
        random.shuffle(movies_block)
        rec_title = movies_block[0]["original_title"]
        rec_rating = movies_block[0]["vote_average"]
        poster = movies_block[0]["poster_path"]
    elif(len(movies) > 0):
        from_list = "movies"
        random.shuffle(movies)
        rec_title = movies[0]["original_title"]
        rec_rating = movies[0]["vote_average"] 

    if(len(movies_block) == 0):
        print("We're sorry! There were no perfect matches, but we'll give you a recommendation we think you'll enjoy!")
        print("------------------------------------------------------------")

    # Print movie recommendation
    print("This is the movie you get and you don't get upset: ", rec_title)
    print("People gave this movie a rating of ", rec_rating)
    print("------------------------------")
    print("Data from The Movie Database API (https://www.themoviedb.org/documentation/api)")
    print("------------------------------")
    poster_path = f"https://image.tmdb.org/t/p/w500/{poster}"
    return [rec_title, rec_rating, poster_path]

### Send email with recommended movie and details ###
# def send_email():
#     # Add poster path here
#     if(from_list == "movies_block") or (from_list == "movies"):
#         poster_path = f"https://image.tmdb.org/t/p/w500/{poster}"
#         # print(poster_path)

#     # breakpoint

#     wants_email = input("Would you like an email with your recommendation? (Y/N)? ").strip()
#     if wants_email.lower() in ['y','yes']:
#         send_email = True
#         user_email = input("Please type your email: ").strip()
#         email_confirm = input("Please retype your email: ").strip()
#         if user_email.lower() != email_confirm.lower():
#             user_email = input("Emails do not match. Please retype your email: ").strip()
#     else:
#         send_email = False


#     if send_email:
#         from sendgrid import SendGridAPIClient
#         from sendgrid.helpers.mail import Mail

#         load_dotenv()

#         SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY", default="OOPS, please set env var called 'SENDGRID_API_KEY'")
#         SENDGRID_TEMPLATE_ID = os.getenv("SENDGRID_TEMPLATE_ID", default="OOPS, please set env var called 'SENDGRID_TEMPLATE_ID'")
#         #SENDER_ADDRESS = os.getenv("SENDER_ADDRESS", default="OOPS, please set env var called 'SENDER_ADDRESS'")
#         SENDER_ADDRESS = user_email

#         # this must match the test data structure
#         template_data = {
#         "input_genre": input_genre,
#         "input_age": input_age,
#         "input_block": input_block,
#         "rec_title": rec_title,
#         "rec_rating": rec_rating,
#         } 


#         client = SendGridAPIClient(SENDGRID_API_KEY)
#         print("CLIENT:", type(client))

#         message = Mail(from_email=SENDER_ADDRESS, to_emails=SENDER_ADDRESS)
#         message.template_id = SENDGRID_TEMPLATE_ID
#         message.dynamic_template_data = template_data
#         print("MESSAGE:", type(message))

#         try:
#             response = client.send(message)
#             print("RESPONSE:", type(response))
#             print(response.status_code)
#             print(response.body)
#             print(response.headers)

#         except Exception as err:
#             print(type(err))
#             print(err)
#         finally:
#             print("Thank you!")
#     else:
#         print("Thank you!")



if __name__ == "__main__":
    # Creating list of genres
    # genres = generate_gen_list()
    # print(genres)
    # Gathering User Inputs
    input_genre, input_age, input_block = get_variables()
    # input_genre = input("please enter input genere")
    # input_age = input("please enter Y or N")
    # input_block = input("please enter block Y/nN ")
    
    # Running movie suggestion app
    new_movie(input_genre, input_age, input_block)
    
    # send email
    # send_email()
