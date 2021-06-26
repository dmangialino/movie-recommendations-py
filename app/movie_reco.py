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


if __name__ == "__main__":


    ### OBTAIN AND PROCESS USER PREFERENCE: MOVIE GENRE ###

    # API call to obtain all available movie genres
    genre_url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={TMBD_API_KEY}"
    genre_response = requests.get(genre_url)
    parsed_genre = json.loads(genre_response.text)
    genres_list = parsed_genre["genres"]
    genres = {}
    for g in genres_list:
        genres.update({g["name"].upper():g["id"]})

    # Print list of available genres from which user can choose
    print("AVAILABLE GENRES: ")
    for genre in genres_list:
        print(genre["name"])
    print("------------------------------------------------------------")

    # Obtain genre selection from the user
    # Utilizes if statement to validate that the genre inputted by the user is available based on genre_list created above
    while True:
        input_genre = input("Please enter a genre for a film you would like to see (select from list above): ").upper()
        if input_genre in genres:
            break
        else:
            print("Invalid genre. Please select a genre from the list above.")

    # Translate string of genre name to genre ID required to make API call
    gen_id = genres[input_genre]

    # Calls fetch_movie_genre function with the genre ID selected by the user to obtain list of matching movies and store 
    #  ... them in "moives" variable
    movies = fetch_movie_genre(gen_id)


    ### OBTAIN AND PROCESS USER PREFERENCE: NEW RELEASE VS. OLDER FILM ###

    # Obtain and validate user input for y/n preference on recently released
    print("------------------------------------------------------------")
    while True:
        input_age = input("Would you prefer a recently released film? (Y/N) ").upper()
        if (input_age == "Y") or (input_age == "N"):
            break
        else:
            print("Invalid input. Please input 'Y' or 'N")
        
    # Obtain today's date, against which the release date of matching movies will be compared
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

    # Overwrite "movies" list with "new" list if user preference was a recently released film or with "old" list if 
    #  ... user preference was not a recently released film
    if(input_age == "Y"):
        movies = new
    elif(input_age == "N"):
        movies = old
    else:
        print("Invalid input. Proceeding with all movies currently selected.")


    ### OBTAIN AND PROCESS USER PREFERENCE: BLOCKBUSTER / POPULAR MOVIE ###

    # Obtain and validate user input for y/n preference on blockbuster / popular movie
    print("------------------------------------------------------------")
    while True:
        input_block = input("Would you like to see a blockbuster (i.e., popular film)? (Y/N) ").upper()
        if (input_block == "Y") or (input_block == "N"):
            break
        else:
            print("Invalid input. Please input 'Y' or 'N")


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
    else:
        print("Invalid input. Proceeding with all movies that met other specified criteria.")
    print("------------------------------------------------------------")

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
        random.suffle(movies)
        rec_title = movies[0]["original_title"]
        rec_rating = movies[0]["vote_average"]
        poster = movies[0]["poster_path"]
    else:
        # No movies match criteria
        # Randomly select movie from the CSV dataset
        from_list = "matching_genres"

        csv_filepath = "data/tmdb_5000_movies.csv"
        movies_df = read_csv(csv_filepath)
        
        # Convert dataframe to dictionary for easier processing
        movies_csv = movies_df.to_dict("records")

        # Create empty list to store movies from CSV (now in "movies_csv dictionary") that match specified genre
        matching_genres = []
        search_genre = ""

        # Format "input_genre" string from all capital to title case (except "TV Movie") to match genre format in CSV
        if(input_genre != "TV MOVIE"):
            search_genre = input_genre.title()
        else:
            # String concateation to translate "TV MOVIE" to "TV Movie" to find matches in CSV
            #  ...i.e., "TV MOVIE" is formatted as "TV Movie" in CSV and "search_genre" formatting must match      
            splt = input_genre.split("")
            search_genre = splt[0]+""+splt[1].capitalize()
            #print(search_genre)
        
        # Iterate through movies from CSV, appending the movie to "matching_genres" list if the genre matches that 
        #  ... specified by the user
        for n in movies_csv:
            if(search_genre in n["genres"]):
                matching_genres.append(n)

        # Shuffle list of movies with matching genre from the CSV to provide random recommendation to the user
        random.shuffle(matching_genres)
        rec_title = matching_genres[0]["original_title"]
        rec_rating = matching_genres[0]["vote_average"]


    # Print message to the user if there were no perfect matches (i.e., all three creitera were not met)
    if(len(movies_block) == 0):
        print("We're sorry! There were no perfect matches, but we'll give you a recommendation we think you'll enjoy!")
        print("------------------------------------------------------------")

    # Print movie recommendation
    print("This is the movie you get and you don't get upset: ", rec_title)
    print("People gave this movie a rating of ", rec_rating)
    print("------------------------------------------------------------")


    # Provide the user an option to obtain a different recommendation
    # "index" variable is used to iterate through list of movie recommendations to continue providing recommendations until the 
    #  ... user no longer requests a new recommendation or there are no movies left in the list
    index = 0
    while True:
        input_new = input("Already seen it? Not what you're looking for? Would you like a new recommendation? (Y/N) ").upper()
        if(input_new == "N"):
            break
        elif(input_new == "Y"):
            # Increase index by one to move to the next movie in the list
            index = index + 1
            
            # Original recommendation came from "movies_block" list and there is at least one more movie in the list 
            if(from_list == "movies_block") and (len(movies_block) > (index + 1)):
                print("------------------------------------------------------------")
                print("Ok, we'll find you something else you might like!")
                print("------------------------------------------------------------")

                rec_title = movies_block[index]["original_title"]
                rec_rating = movies_block[index]["vote_average"]
                poster = movies_block[index]["poster_path"]

                print("This is the movie you get and you don't get upset: ", rec_title)
                print("People gave this movie a rating of ", rec_rating)
                print("------------------------------------------------------------")                    
            # Original recommendation came from "movies" list and there is at least one more movie in the list
            elif(from_list == "movies") and (len(movies) > (index + 1)):
                print("------------------------------------------------------------")
                print("Ok, we'll find you something else you might like!")
                print("------------------------------------------------------------")

                rec_title = movies[index]["original_title"]
                rec_rating = movies[index]["vote_average"]
                poster = movies[index]["poster_path"]

                print("This is the movie you get and you don't get upset: ", rec_title)
                print("People gave this movie a rating of ", rec_rating)
                print("------------------------------------------------------------")                    
            # Original recommendation came from "matching_genres" list and there is at least one more movie in the list
            elif(from_list == "matching_genres") and (len(matching_genres) > (index + 1)):
                print("------------------------------")
                print("Ok, we'll find you something else you might like!")
                print("------------------------------------------------------------")

                rec_title = matching_genres[index]["original_title"]
                rec_rating = matching_genres[index]["vote_average"]

                print("This is the movie you get and you don't get upset: ", rec_title)
                print("People gave this movie a rating of ", rec_rating)
                print("------------------------------------------------------------")                    
            # There are no other movies in the list from which the original recommendation was provided
            else:
                print("------------------------------------------------------------")
                print("We're sorry! No other movies that matched the specified criteria. Try running again with different criteria.")
                break
        else:
            print("Invalid input. Please enter 'Y' or 'N'")


    # Accreditation to The Movie Database API and dataset through Kaggle
    print("------------------------------------------------------------")
    print("ACCREDITATION:")
    print("Data from The Movie Database API (https://www.themoviedb.org/documentation/api) and Kaggle dataset (https://www.kaggle.com/tmdb/tmdb-movie-metadata)")
    print("------------------------------------------------------------")



   
    ### Send email with recommended movie and details ###

    # Add poster path here
    if(from_list == "movies_block") or (from_list == "movies"):
        poster_path = f"https://image.tmdb.org/t/p/w500/{poster}"
        # print(poster_path)

    # breakpoint

    wants_email = input("Would you like an email with your recommendation? (Y/N)? ").strip()
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
        "rec_rating": rec_rating,
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

