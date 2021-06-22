# movie-recommendations-py

## Set up virtual environment

Setup a virtual environment using the below command:
```sh
conda create -n movie-reco-env python=3.8

```

Then activate the virtual environment using the below command:

``` 
<<<<<<< Updated upstream
conda activate movie_recs-env
=======
conda activate movie-reco-env
>>>>>>> Stashed changes
```



## Install packages

Install the required packages using the below command:

```
pip install -r requirements.txt
<<<<<<< Updated upstream

pip install git+https://github.com/alberanid/imdbpy

```
>>>>>>> main
=======

```
## Create a TMBD API Key
This tool uses movie information from the TMDB API, so you will need ot set up a TMDB API Key to use this tool. Create a TMDB account via https://www.themoviedb.org/signup and generate an API key. You will then need to store this API key later in a .env file.

## Configuring Environment Variables
In the root directory of your local repository, create a new file called ".env", and update the contents of the ".env" file with the below information:

```
TMBD_API_KEY  = "enter store name here"

```

Additionally, in the .env file identify Sender Address where you would like emails sent to:

```
SENDER_ADDRESS = "enter email address"
```
Additionally, you will need to store your SENDGRID_API_KEY and SENDGRID_TEMPLATE_ID information to ensure the email integration works correctly"

```
SENDGRID_API_KEY = "enter API key"
SENDGRID_TEMPLATE_ID = "enter key to dynamic template"
```



# Movie Data

Movie dataset from Kaggle, based on The Movie Database (TMDb) data: https://www.kaggle.com/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv
>>>>>>> Stashed changes
