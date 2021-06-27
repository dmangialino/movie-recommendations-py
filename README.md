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
    <h2>Thank you for using our Python Personalized Movie Recos tool!</h2>
    <p>We based your personalized recommendations based on your below inputs:</p>
    <p style="margin-left: 20px; line-height: 1;"><strong>Genre:&nbsp;</strong>{{input_genre}}</p>
    <p style="margin-left: 20px; line-height: 1;"><strong>Recency:&nbsp;</strong>{{input_age}}</p>
    <p style="margin-left: 20px; line-height: 1;"><strong>Blockbuster:</strong> {{input_block}}</p>
    <p>Please see below for your personalized recommendations!</p>
    <p style="margin-left: 20px; line-height: 1;"><strong>Recommended Movie:</strong> {{this.rec_title}}</p>
    <p style="margin-left: 20px; line-height: 1;"><strong>People gave this movie a rating of: </strong>{{this.rec_rating}} </p>
    <p>Please come back for more recommendations!</p>
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
    "rec_rating": "10.0"
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

https://www.themoviedb.org/documentation/api

## CSV

Add CSV link