import re

import file as file
from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse
from flask_sqlalchemy import SQLAlchemy

import tweepy
import os
import requests
import urllib.request

import time

from click._compat import raw_input

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user_data.sqlite3'
app.secret_key = 'ayush'
# num=0

# print("changing lvl%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
# ver = 0
# counter = 0
# login = 0
# init = 0
# sublvl = 0
# # token=''
# zero=0
db = SQLAlchemy(app)
class user_data(db.Model):
   id = db.Column('user_id', db.Integer, primary_key = True)
   phno = db.Column(db.String(100))
   lvl = db.Column(db.Integer)

   def __init__(self, phno, lvl):
       self.phno = phno
       self.lvl = lvl



   # auth = db.Column(db.String(200))



       # self.auth = auth


auth = tweepy.OAuthHandler('t5qZhGyVwTkNArktAPM64nSvl', 'lk2ViVadYV6JbyeY7KLRfcDSxV9aGdn9ez9pTTO8cylnO7Z16J')


@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/auth", methods=['GET'])
def auth_page():
    global lvl
    global token
    global api
    global auth
    global resp
    global verifier
    token = request.args.get('oauth_token')
    verifier = request.args.get('oauth_verifier')

    auth.request_token = {'oauth_token': token,
                          'oauth_token_secret': verifier}
    try:

        auth.get_access_token(verifier)
        lvl = 0.1
        key = auth.access_token
        secret = auth.access_token_secret

        auth.set_access_token(key, secret)
        api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


    except tweepy.TweepError:
        print('Error! Failed to get access token.')
        lvl = 0

    # user = api.me()
    # print(
    #     "Yo, *{}* (```{}```)\n----------------------------------------------\n```{}``` Following | ```{}``` Followers\n----------------------------------------------\n\n What would you like to do? \n\n 1. Make Tweet\n 2. Trending\n 3. Update Profile Picture\n 4. Follow/Unfollow by twitter handle \n 5. View your recent tweets".format(
    #         user.name, user.screen_name, user.friends_count, user.followers_count))
    #
    # lvl = 1.1
    return "Hey"


@app.route("/sms", methods=['POST'])
def sms_reply():



    global lvl
    global ver
    global counter
    global login
    global init
    global sublvl
    global confirm
    global verifier

    global api
    global request
    global auth
    global tweet
    global token
    zero=0
    global media
    global user
    global medianum
    global filename
    froms =request.form.get('From')
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    # print("jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj",request.form.get('From'))

    if(user_data.query.filter_by(phno = request.form.get('From')).scalar()!=None):
        print("yes")
    else:
        data = user_data(froms, zero)

        db.session.add(data)
        db.session.commit()
        print("no")
    # print(user_data.query(user_data.lvl).filter_by(phno = request.form.get('From')))
    # print(db.session.query(user_data.lvl).filter(user_data.phno ==request.form.get('From')).all())

    # row=db.session.query(user_data).filter(user_data.phno ==request.form.get('From')).all()

    row=user_data.query.filter_by(phno = request.form.get('From')).first()
    lvl=row.lvl

    print(lvl)


    # lvl=row[0][0]
    # print(lvl)



    """Respond to incoming calls with a simple text message."""


    filename = 'temp.jpg'



    if (os.path.isfile(filename)):
        os.remove(filename)

    resp = MessagingResponse()

    print(request.form)


    msg = request.form.get('Body')




    if lvl == 0:

        try:
            print(
                " Hi there. Login to Twitter here. \n{} \n\n\nAnd send the code".format(auth.get_authorization_url()))
            # t.MediaUrl0=("https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.HcQw5Zd1jJhmc1IYzADc3gHaHa%26pid%3DApi&f=1")
        except:
            print("************************************************")

        lvl=69






    elif lvl ==0.1:
        user = api.me()
        print(
            "Yo, *{}* (```{}```)\n----------------------------------------------\n```{}``` Following | ```{}``` Followers\n----------------------------------------------\n\n What would you like to do? \n\n 1. Make Tweet\n 2. Trending\n 3. Update Profile Picture\n 4. Follow/Unfollow by twitter handle \n 5. View your recent tweets".format(
                user.name, user.screen_name, user.friends_count, user.followers_count))

        lvl=1.1

    elif lvl==69:
        token = auth.request_token['oauth_token']
        verifier = msg

        auth.request_token = {'oauth_token': token,
                              'oauth_token_secret': verifier}
        try:

            auth.get_access_token(verifier)
            lvl = 0.1
            key = auth.access_token
            secret = auth.access_token_secret

            auth.set_access_token(key, secret)
            print(auth.set_access_token(key, secret))

        except tweepy.TweepError:
            print('Error! Failed to get access token.')
            lvl = 0

    elif lvl==1.1:
        # type(msg)
        print(msg)
        if msg=='1':
            print("Type your tweet in (LIMIT : 1000 words)")
            lvl=1.2
        if msg=='2':
            # print("into1,1")
            trending = api.trends_place(23424848)
            trendss = ''

            for i in range(20):
                if trending[0]['trends'][i]['tweet_volume'] != None:
                    trendss += "{}. {} ... ({})\n".format(i + 1, trending[0]['trends'][i]['name'],
                                                          trending[0]['trends'][i]['tweet_volume'])
                else:
                    trendss += "{}. {} \n".format(i + 1, trending[0]['trends'][i]['name'])

            print("{}".format(trendss))
            lvl = 1

            # lvl=1.3
        if msg=='3':
            print("Send a photo to update your Profile Picture")
            lvl = 1.41

            # lvl=1.4
        if msg=='4':
            print("Enter the Twitter Handle of the user you want to follow/unfollow")
            lvl = 1.51
            # lvl=1.5
        if msg=='5':
            timeline = ''
            timelinecount = 1
            for tweet in api.user_timeline():

                if tweet.in_reply_to_status_id == None:
                    stringtoadd = "{}. {}{}\n\t*🔃 : {}\t💟 : {}*\n------------------------------------\n\n".format(
                        timelinecount, tweet.text, tweet.created_at.strftime("   (%b %d, %H:%M)"), tweet.retweet_count,
                        tweet.retweeted_status.favorite_count if tweet.retweeted == True else tweet.favorite_count)

                    x = re.findall(r'(https?://[^\s]+)', stringtoadd)
                    print(x)
                    if (len(x) != 0):
                        stringtoadd = stringtoadd.replace(x[0], "\n{}".format(x[0]))

                    if (len(timeline) + len(stringtoadd) > 1600):
                        break
                    timeline += stringtoadd
                    timelinecount += 1
            print("{}".format(timeline))

            lvl = 1
            # lvl=1.6



    elif lvl==1.2:
        media = request.form.get('MediaUrl0')
        medianum = request.form.get('NumMedia')

        tweet = []
        if (len(msg) < 280):
            tweet.append(msg)
        else:
            count = 0
            letter = 0
            tweetno = len(msg) / 280
            tweetno = (len(msg) + 2 * tweetno) // 280
            tweetno = int(tweetno)

            while (letter < len(msg)):
                # print(msg[letter:letter+274])
                tweet.append(msg[letter:letter + 274] + " ({}/{})".format(count + 1, tweetno + 1))
                count += 1
                letter = letter + 275
                # tweet[count]+=" ({}/{})".format(count+1,tweetno+1)

        print("You're going to make this/these tweet(s)\n------------------")
        for i in tweet:
            print(i)
        print("are you sure ? (y/n)?")

        lvl=1.22

    # elif lvl==1.21:
    #
    #     print("are you sure ? (y/n)?")
    #     lvl=1.22

    elif lvl==1.22:

        #

        if (msg == 'y'):

            if (medianum != '0'):

                r = requests.get(media, stream=True)
                if r.status_code == 200:
                    with open(filename, 'wb') as image:
                        for chunk in r:
                            image.write(chunk)

            for i in tweet:

                if (medianum != '0'):

                    api.update_with_media(filename, status=i)
                else:
                    api.update_status(i)

            print("done")


        if msg == 'n':
            print("No changes made")

        lvl=1




    # elif lvl==1.3:
    #     trending = api.trends_place(23424848)
    #     trendss = ''
    #
    #     for i in range(20):
    #         if trending[0]['trends'][i]['tweet_volume'] != None:
    #             trendss += "{}. {} ... ({})\n".format(i + 1, trending[0]['trends'][i]['name'],
    #                                                   trending[0]['trends'][i]['tweet_volume'])
    #         else:
    #             trendss += "{}. {} \n".format(i + 1, trending[0]['trends'][i]['name'])
    #
    #     print("{}".format(trendss))
    #     lvl=0.1




    # elif lvl==1.4:
    #     print("Send a photo to update your Profile Picture")
    #     lvl = 1.41



    elif lvl==1.41:
        media = request.form.get('MediaUrl0')
        medianum = request.form.get('NumMedia')
        if medianum != '0':
            r = requests.get(media, stream=True)
            if r.status_code == 200:
                with open(filename, 'wb') as image:
                    for chunk in r:
                        image.write(chunk)

            api.update_profile_image(filename)
            print("DONE !")


        else:
            print("ERROR")


        lvl = 1



    # elif lvl==1.5:
    #     print("Enter the Twitter Handle of the user you want to follow/unfollow")
    #     lvl=1.51



    elif lvl==1.51:
        print(api.show_friendship(source_screen_name=user.screen_name, target_screen_name=msg)[0].following)

        if (api.show_friendship(source_screen_name=user.screen_name, target_screen_name=msg)[0].following):
            api.destroy_friendship(msg)
            print('Unfollowed {}'.format(msg))
        else:
            api.create_friendship(msg)
            print('Followed {}'.format(msg))
        lvl = 1


    # elif lvl==1.6:
    #     timeline = ''
    #     timelinecount = 1
    #     for tweet in api.user_timeline():
    #
    #         if tweet.in_reply_to_status_id == None:
    #             stringtoadd = "{}. {}{}\n\t*🔃 : {}\t💟 : {}*\n------------------------------------\n\n".format(
    #                 timelinecount, tweet.text, tweet.created_at.strftime("   (%b %d, %H:%M)"), tweet.retweet_count,
    #                 tweet.retweeted_status.favorite_count if tweet.retweeted == True else tweet.favorite_count)
    #
    #             x = re.findall(r'(https?://[^\s]+)', stringtoadd)
    #             print(x)
    #             if (len(x) != 0):
    #                 stringtoadd = stringtoadd.replace(x[0], "\n{}".format(x[0]))
    #
    #             if (len(timeline) + len(stringtoadd) > 1600):
    #                 break
    #             timeline += stringtoadd
    #             timelinecount += 1
    #     print("{}".format(timeline))
    #
    #     lvl = 0.1





    if lvl ==1:
        user = api.me()
        print(
            "*{}* (```{}```)\n----------------------------------------------\n```{}``` Following | ```{}``` Followers\n----------------------------------------------\n\n What would you like to do? \n\n 1. Make Tweet\n 2. Trending\n 3. Update Profile Picture\n 4. Follow/Unfollow by twitter handle \n 5. View your recent tweets".format(
                user.name, user.screen_name, user.friends_count, user.followers_count))

        lvl=1.1








    print("-------------------------------------------- >", lvl)
    row.lvl =lvl
    db.session.commit()
    print("++++++++++++++++++++++++++++++++++++++++++++++ >", lvl)



    return str(resp)


if __name__ == "__main__":
    # print(
        # "55555555555555555555555555555555555555555555555starting555555555555555555555555555555555555555555555555555555555")
    db.create_all()
    app.run(debug=True)
