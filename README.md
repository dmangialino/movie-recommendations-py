# movie-recommendations-py



![Python Personalized Movies Recs  psd](https://user-images.githubusercontent.com/84421118/123555432-ac6cc900-d753-11eb-9d41-69ccd88dd4b8.jpg)

#### Welcome to the Python Personalized Movie Recs app. If you're in need of a movie recommendation, this is the tool for you!

------------

![Python Line Break - virtual env](https://user-images.githubusercontent.com/84421118/123558251-48520100-d763-11eb-89b7-cba9c9d340eb.png)

## Set up virtual environment

Setup a virtual environment using the below command:
```
conda create -n movie-recs-env python=3.8
```

Then activate the virtual environment using the below command:

``` 
conda activate movie-recs-env
```

![Python Line Break - packages](https://user-images.githubusercontent.com/84421118/123558437-3cb30a00-d764-11eb-812c-9029917f497d.png)

## Install packages

```
pip install -r requirements.txt
```

![Python Line Break - tmdb](https://user-images.githubusercontent.com/84421118/123558453-4b99bc80-d764-11eb-9ebf-a06a56480530.png)

## Create a TMBD API Key
This tool uses movie information from the **TMDB API,** so you will need to set up a TMDB API Key to use this tool. Create a TMDB account via https://www.themoviedb.org/signup and generate an API key. You will then need to store this API key later in a .env file (*instructions below*).


![Python Line Break - sendgrid](https://user-images.githubusercontent.com/84421118/123558461-58b6ab80-d764-11eb-8ed4-e2f6c1af6007.png)

## Configuring Email Integration
Create a **SendGrid **account via https://signup.sendgrid.com/ and generate an API key. *You will then need to store this API key later in a .env file.*

Once setting up your account, select **Email API** and create your own **Dynamic Template**. Make note of the **Template ID,** as you will need to store this in your .enc file later. 

Aftre creating the Dynamic Template, select **Add Version**, then select **Blank Template**, and then select **Code Editor**.

Navigate to the **Code** page of the Dynamic Template, and paste the below code:

```
<!DOCTYPE html>
<html>

<head>
    <title></title>
</head>

<body style="color: rgb(0, 0, 0); background-color: rgb(253, 245, 255);">
    <p><img src="http://cdn.mcauto-images-production.sendgrid.net/b272db5d20876ea6/fa8f373e-8e4e-4f3b-aa55-6c4d54a820ab/750x422.jpg"></p>
    <h2><span style="font-family: Verdana, Geneva, sans-serif;">Thank you for using our Python Personalized Movie Recs tool!</span></h2>
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
Lastly, select **Settings** on the left-hand side of the screen, navigate to **Subject**, and paste "*Your Python Personalized Movie Rec*"

Make sure that you hit save at the top of the screen.


![Python Line Break - environment](https://user-images.githubusercontent.com/84421118/123558468-63714080-d764-11eb-8029-986c604e23b6.png)


## Configuring Environment Variables
In the root directory of your local repository, create a new file called ".env", and update the contents of the ".env" file to include the below information:

> **TMBD_API_KEY** = "enter your TMDB API key here"

> **SENDGRID_API_KEY** = "enter your SendGrid API key here" <br >
> **SENDGRID_TEMPLATE_ID** = "enter your Dynamic Template ID here" <br >
> **SENDER_ADDRESS** = "enter email address you would like email rec sent to" <br >

*Note your SENDER_ADDRESS email should match the email used to setup your SendGrid account*


![Python Line Break - tesing](https://user-images.githubusercontent.com/84421118/123558485-7edc4b80-d764-11eb-968f-1de0484a012d.png)

## Testing the Program

You can also test the program to ensure the logic is running correctly, by navigating to the root directory in the command line and entering the below command:

```
pytest
```
Running the above command will test the code's logic, and ensure that everything is functioning properly and running smoothly. 

Please also note that the repo incorporates a Continuous Integration service called **Travis CI**, which will run tests every time a pull request is opened. Travis CI can be setup using the following link, but it has already been integrated into the repo so you don't need to take any further steps here: 

> https://www.travis-ci.com/

Lastly, please note that this repo has been integrated with **Code Climate** to run checks on pull requests. While nothing is needed ont he user's end, you can integrate Code Climate on your end by creating a account and linking it to your GitHub repo:

> https://codeclimate.com/oss/dashboard



![Python Line Break - usage](https://user-images.githubusercontent.com/84421118/123558472-7257f300-d764-11eb-8270-a50705d5074d.png)


## Running the App

After following the above directions, you're ready to run the application and get your personalized movie reccomendation!

After you have completed the below list, you're ready to run the game:
>[ ]  Downloaded the repo to your local computer <br />
>[ ] Navigated to the repo in the command line <br />
>[ ] Setup your virtual environment <br />
>[ ] Installed the requirements.txt file <br />
>[ ] Generated a TMDB API key <br />
>[ ] Set up your SendGrid account and created a dynamic email template <br />
>[ ] Configured your environment variables<br />

To run the game, enter the following command:


```
python app/movie_reco.py
```
You will then be prompted to select a **genre** from the following list:
>Action <br >
>Adventure <br >
>Animation <br >
>Comedy <br >
>Crime <br >
>Documentary <br >
>Drama <br >
>Family <br >
>Fantasy <br >
>History <br >
>Horror <br >
>Music <br >
>Mystery <br >
>Romance <br >
>Science Fiction <br >
>TV Movie <br >
>Thriller <br >
>War <br >
>Western <br >

After selecting a genre, you will be prompted to select if you would like a **recently released film** (*film released in the past two years*).

Next, you will be prompted to select if you would like a **blockbuster** (*a popular film with a 7+ rating according to TMDB*).

The app will then generate your first recommendation! If you are not happy with your selection, you can say you would like another recommendation until you are happy with your selection.

After your recommendation is finalized, you will be asked if you would like an **email receipt** of your recommendation. If the answer is yes, you will be prompted to enter your email address, then you will receive an email receipt of your personalized recommendation.


![Python Line Break - Accreditation](https://user-images.githubusercontent.com/84421118/123558491-87cd1d00-d764-11eb-8049-6ef25facd1eb.png)

## Third Party Datasets and APIs Used

Please note that movie recommendations were sourced using data from the **TMDB APi**:

> https://www.themoviedb.org/documentation/api

and from **TMDB 5000 Movie Dataset** CSV data file:

> https://www.kaggle.com/tmdb/tmdb-movie-metadata

![Python Line Break - License](https://user-images.githubusercontent.com/84421118/123558498-91568500-d764-11eb-952e-0e0baf28e2e7.png)

## License

This repo uses an MIT license

![Python Line Break - enjoy](https://user-images.githubusercontent.com/84421118/123558539-c82c9b00-d764-11eb-92c8-ba2ab87bf703.png)

### Enjoy your Python Personalized Movie Reccomendation!


## Running the Web App

# Activate Flask
# For Mac OS:
FLASK_APP=web_app.py flask run
# For Windows OS:
export FLASK_APP=web_app.py
flask run
# **if `export` doesn't work for you, try `set` instead