
from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse

import tweepy
import os

import time

from click._compat import raw_input



app = Flask(__name__)
app.secret_key='ayush'
num=0
lvl=0
ver=0
counter=0
login=0
auth=tweepy.OAuthHandler('t5qZhGyVwTkNArktAPM64nSvl','lk2ViVadYV6JbyeY7KLRfcDSxV9aGdn9ez9pTTO8cylnO7Z16J')

@app.before_request
def make_session_permanent():
    session.permanent = True

@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    global lvl
    global counter
    global ver
    global login
    resp = MessagingResponse()

    session['phone_no']=request.form.get('From')
    msg = request.form.get('Body')
    if lvl==0:
        if counter==0:
            resp.message("Hi there. Login to Twitter here. {} And send the code".format(auth.get_authorization_url()))
            counter=1
        else:
            token = auth.request_token['oauth_token']
            verifier = msg
            resp.message("Verifier code :".format(verifier))

            ver=1
            lvl=1

    if ver==1:
        auth.request_token = {'oauth_token': token,
                              'oauth_token_secret': verifier}
        try:
            auth.get_access_token(verifier)
            login=1
        except tweepy.TweepError:
            resp.message('Error! Failed to get access token.')
            lvl=0
            ver=0
            counter=0
            login=0

            resp.message("login:".format(login))

            key = auth.access_token
            secret = auth.access_token_secret

            auth.set_access_token(key, secret)



    if login==1:
        api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
        user = api.me()

        resp.message.body("Hi, {} ({})\n What would you like to do?\n1. Make Tweet\n".format(user.name,user.screen_name))
        resp.message.media("https://twitter.com/{}/photo".format(user.screen_name))

    # Create reply

    # session.permanent = True
    # if(msg=='69'):
    #     resp.message("Session is {}".format(num))
    # else:
    #
    #     resp.message("You said: {} ".format(msg))

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
