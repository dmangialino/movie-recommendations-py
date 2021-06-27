# movie-recommendations-py



![Python Personalized Movies  psd](https://user-images.githubusercontent.com/84421118/123532787-41cd7600-d6de-11eb-9b50-28bc45fcc5ea.jpg)

#### Welcome to the Python Personalized Movie Recos app. If you're in need of a movie recommendation, this is the tool for you!

------------


## Set up virtual environment

Setup a virtual environment using the below command:
```
conda create -n movie-recs-env python=3.8
```

Then activate the virtual environment using the below command:

``` 
conda activate movie-recs-env
```



## Install packages

```
pip install -r requirements.txt
```

## Create a TMBD API Key
This tool uses movie information from the **TMDB API,** so you will need to set up a TMDB API Key to use this tool. Create a TMDB account via https://www.themoviedb.org/signup and generate an API key. You will then need to store this API key later in a .env file (*instructions below*).


## Configuring Email Integration
Create a **SendGrid **account via https://signup.sendgrid.com/ and generate an API key. *You will then need to store this API key later in a .env file.*

Once setting up your account, select **Email API **and create your own **Dynamic Template**. Make note of the **Template ID,** as you will need to store this in your .enc file later. 

Aftre creating the Dynamic Template, select **Add Version**, then select **Blank Template**, and then select **Code Editor**.

Navigate to the **Code** page of the Dynamic Template, and paste the below code:

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

Next, go to the **Test Data** page and paste the below code:

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
Lastly, select **Settings** on the left-hand side of the screen, navigate to **Subject**, and paste "*Your Python Personalized Movie Reco*"

Make sure that you hit save at the top of the screen.


## Configuring Environment Variables
In the root directory of your local repository, create a new file called ".env", and update the contents of the ".env" file to include the below information:

> **TMBD_API_KEY ** = "enter your TMDB API key here"

> **SENDGRID_API_KEY** = "enter your SendGrid API key here"
> **SENDGRID_TEMPLATE_ID **= "enter your Dynamic Template ID here"
> **SENDER_ADDRESS** = "enter email address you would like email reco sent to"

*Note your SENDER_ADDRESS email should match the email used to setup your SendGrid account*

## Running the App

After following the above directions, you're ready to run the application and get your personalized movie reco!

After you have completed the below list, you're ready to run the game:
>[ ]  Downloaded the repo to your local computer
>[ ] Navigated to the repo in the command line
>[ ] Setup your virtual environment
>[ ] Installed the requirements.txt file
>[ ] Generated a TMDB API key
>[ ] Set up your SendGrid account and created a dynamic email template
>[ ] Configured your environment variables*

To run the game, enter the following command:


```
python app/movie_reco.py
```
You will then be prompted to select a **genre** from the following list:
>Action
>Adventure
>Animation
>Comedy
>Crime
>Documentary
>Drama
>Family
>Fantasy
>History
>Horror
>Music
>Mystery
>Romance
>Science Fiction
>TV Movie
>Thriller
>War
>Western

After selecting a genre, you will be prompted to select if you would like a **recently released film** (*film released in the past two years*).

Next, you will be prompted to select if you would like a **blockbuster** (*a popular film with a 7+ rating according to TMDB*).

The app will then generate your first recommendation! If you are not happy with your selection, you can say you would like another recommendation until you are happy with your selection.

After your recommendation is finalized, you will be asked if you would like an **email receipt **of your recommendation. If the answer is yes, you will be prompted to enter your email address, then you will receive an email receipt of your personalized recommendation.


## Third Party Datasets and APIs Used

Please note that movie recommendations were sourced using data from the **TMDB APi**:

> https://www.themoviedb.org/documentation/api

and from **TMDB 5000 Movie Dataset** CSV data file:

> https://www.kaggle.com/tmdb/tmdb-movie-metadata

## License

This repo uses an MIT license


------------

### Enjoy your Python Personalized Movie Reco!