# movie-recommendations-py

# Set up virtual environment

Setup a virtual environment using the below command:
```sh
conda create -n movie-recs-env python=3.8

```

Then activate the virtual environment using the below command:

``` 
conda activate movie-recs-env
```



# Install packages

```
pip install -r requirements.txt
```

# Create a TMBD API Key
This tool uses movie information from the TMDB API, so you will need ot set up a TMDB API Key to use this tool. Create a TMDB account via https://www.themoviedb.org/signup and generate an API key. You will then need to store this API key later in a .env file.

## Configuring Environment Variables
In the root directory of your local repository, create a new file called ".env", and update the contents of the ".env" file with the below information:

```
TMBD_API_KEY  = "enter TMDB API key here"
```


# Third Party Datasets and APIs Used

## Movie Data Pulled from TMDb API

https://www.themoviedb.org/documentation/api

