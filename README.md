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


## Configuring Email Integration
Create a SendGrid account via https://signup.sendgrid.com/ and generate an API key. You will then need to store this API key later in a .env file.

Once setting up your account, select Email API and create your own Dynamic Template. On the Code page, paste the below code and ensure you swap in the name of your tool in the line that says "Thank you for using our Python Personalized Movie Recos tool!" Also ensure you swap out the image link with a link to your own logo:

```
<!DOCTYPE html>
<html>

<head>
    <title></title>
</head>

<body style="color: rgb(0, 0, 0); background-color: rgb(253, 245, 255);">
    <p><img src="http://cdn.mcauto-images-production.sendgrid.net/b272db5d20876ea6/d2801bf9-07ca-4198-a1ff-a35974fcd821/750x422.jpg"></p>
    <h2><span style="font-family: Verdana, Geneva, sans-serif;">Thank you for using our Python Personalized Movie Recos tool!</span></h2>
    <p><span style="font-family: Verdana, Geneva, sans-serif;">We based your personalized recommendations based on your below inputs:</span></p>
    <p style="margin-left: 20px; line-height: 1;"><span style="font-family: Verdana, Geneva, sans-serif;"><strong>Genre:&nbsp;</strong>{{input_genre}}</span></p>
    <p style="margin-left: 20px; line-height: 1;"><span style="font-family: Verdana, Geneva, sans-serif;"><strong>Recency:&nbsp;</strong>{{input_age}}</span></p>
    <p style="margin-left: 20px; line-height: 1;"><span style="font-family: Verdana, Geneva, sans-serif;"><strong>Blockbuster:</strong> {{input_block}}</span></p>
    <p><span style="font-family: Verdana, Geneva, sans-serif;">Please see below for your personalized recommendations!</span></p>
    <p style="margin-left: 20px; line-height: 1;"><span style="font-family: Verdana, Geneva, sans-serif;"><strong>Recommended Movie:</strong> {{this.rec_title}}</span></p>
    <p style="margin-left: 20px; line-height: 1;"><span style="font-family: Verdana, Geneva, sans-serif;"><strong>People gave this movie a rating of:&nbsp;</strong>{{this.rec_rating}}</span></p>
        <p><img src="{{this.poster_path}}"></p>
    <p><span style="font-family: Verdana, Geneva, sans-serif;">Please come back for more recommendations!</span></p>
    <hr>
    <p style='margin:0in;font-size:16px;font-family:"Calibri",sans-serif;line-height:13.5pt;'><span style="font-family: Verdana, Geneva, sans-serif; color: black; font-size: 12px;">Data from The Movie Database API (https://www.themoviedb.org/documentation/api) and Kaggle dataset (https://www.kaggle.com/tmdb/tmdb-movie-metadata)</span></p>
</body>

</html>

```

On the Test Data page, paste the below code. You will not need to make any changes, unless you want the receipt to pull in any information:

```
{
    "input_genre": "Action",
    "input_age": "Y",
    "input_block": "Y",
    "rec_title":"Avengers",
    "rec_rating": "10.0",
    "poster_path": "https://image.tmdb.org/t/p/w500//tnAuB8q5vv7Ax9UAEje5Xi4BXik.jpg"

}

```


## Configuring Environment Variables
In the root directory of your local repository, create a new file called ".env", and update the contents of the ".env" file with the below information:

```
TMBD_API_KEY  = "enter TMDB API key here"
```
```
SENDGRID_API_KEY = "enter API key"
SENDGRID_TEMPLATE_ID = "enter key to dynamic template"
SENDER_ADDRESS = "enter email address"
```


# Third Party Datasets and APIs Used

## Movie Data Pulled from TMDb API
Please note that movie recommendations were sourced using data from the TMDB APi:
```
https://www.themoviedb.org/documentation/api
```
and from TMDB 5000 Movie Dataset CSV data file:

```
https://www.kaggle.com/tmdb/tmdb-movie-metadata
```
