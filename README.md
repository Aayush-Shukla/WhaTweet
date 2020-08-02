# WhaTweet

A twitter bot for whatsapp built using python, tweepy and twilio



<p float="left">
<img src="https://i.imgur.com/qXDnavE.png" width=30%>

<img src="https://i.imgur.com/ZaLd0yP.png" width=30%>

<img src="https://i.imgur.com/Wv8mh8f.png" width=30%>
</p>

---

## Table of Contents 

- [Installation](#installation)
- [Features](#features)

---

## Installation

### Clone

- Clone this repo to your local machine using `https://github.com/Aayush-Shukla/WhaTweet`

### Edit utils.py

- Edit the utils.py with your TWITTER CONSUMER KEY, SECRET and POSTGRES DATABASE URI.

```
CONSUMER_KEY = 't5qZhGyVwTkNArktAPM64nSvl'
CONSUMER_SECRET = 'lk2ViVadYV6JbyeY7KLRfcDSxV9aGdn9ez9pTTO8cylnO7Z16J'
DATABASE= 'postgres://xdqieazjvunfne:95c006314ec65cb73f0c7895ef905c64b6606932a7d13cbcab22cb7bdf7a0c0d@ec2-3-216-129-140.compute-1.amazonaws.com:5432/d3hdstc8500olp'
```

### Heroku Setup

#### 1. SIGNUP/LOGIN TO HEROKU
Run the following commands in your terminal (in your SERVER/BACKEND repo):
```
heroku --version
```
If it gives you a version, it means that the Heroku CLI interface is correctly installed.   
If not, create an account in Heroku (https://signup.heroku.com/) and repeat.

Once you have Heroku installed, run this command in your terminal to login:
```
heroku login
```
Type 'enter' or any key and you will be redirected to a browser window where you'll be able to login to your Heroku account.

&nbsp;
&nbsp;

#### 2. CREATE THE APP IN HEROKU
##### 2.1. Go to your dashboard, and click on the top right button that says "New: > 'Create New app'

* Give a name to your app (will be used as a url to your deployed app, so choose something meaningful)
* Choose region: 'Europe'
* Click on "Create"
You'll get to the application panel of your app: https://dashboard.heroku.com/apps/{NAME-OF-YOUR-APP-HERE}/deploy/heroku-git

&nbsp;

#### 2.2. Connect Heroku to your local repo
In the root folder of your SERVER/BACKEND repo, run the following command to add heroku remote (connect your local server repo to your app on heroku):   
```
$ heroku git:remote -a name-of-the-app
 ```
 _You will find that command under the "Create a new Git repository" section in your dashboard)_
 
Check that the remote has been correctly added to your project.    
You should see a new remote 'heroku' in addition to 'origin' (Github):
 ```
$ git remote -v
```
&nbsp;

#### 2.3. Deploy your server to Heroku

First, commit your last changes on 'master' branch and push them to Github.
On the master branch of your SERVER/BACKEND repo:
```
$ git add .
$ git commit -m 'Add last changes'
$ git push origin master
```

then deploy them as well to Heroku pushing them to your 'heroku' remote:
```
$ git push heroku master
```

&nbsp;
&nbsp;


### Twilio Setup

- To get started with WhatsApp, we need to first activate our Twilio Sandbox for WhatsApp. 
Once you have created a new Programmable SMS project, from the dashboard, select Programmable SMS then select WhatsApp. 
You will be prompted to activate your sandbox.

<img src="https://twilio-cms-prod.s3.amazonaws.com/images/g_SKIwL27hF3KB1jDDndfORnUxbZ3LR1OVnyP4k5wzsi2.width-1000.png">

- After following the instructions, you should get a message similar to this one on WhatsApp:

<img src="https://twilio-cms-prod.s3.amazonaws.com/images/8moM1Q8Omqkq12Xilf80qoMOM0DE-V3VNOSpsoEVI10cp.width-1000.png">

- Copy that URL of your Heroku App and  paste the URL into the WHEN A MESSAGE COMES IN input box of the sandbox configuration page:

<img src="https://twilio-cms-prod.s3.amazonaws.com/images/94aERB_6NAAEVqij3cQwRUwOe8cvSU_kaTvwDPCHvcAoq.width-1000.png">

---

## Features

- Makes Tweet along with images and videos.

- Tweets greater than 280 characters are automatically broken into smaller tweets.

- Can update user's profile picture

- Get trending twitter hastags.

- Shows users recent tweets and replies.

- Can follow and unfollow users

---

## License

Copyright © 2020, [Ayush Shukla](https://github.com/Aayush-Shukla).
Released under the [MIT license](LICENSE).
