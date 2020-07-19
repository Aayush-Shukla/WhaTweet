import re


from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool
from utils import *

engine = create_engine(
    "postgres://",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool
)


import tweepy
import os
import requests


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE
app.secret_key = 'ayush'


db = SQLAlchemy(app)
class user_data(db.Model):
    id = db.Column('user_id', db.Integer, primary_key = True)
    phno = db.Column(db.String(100))
    lvl = db.Column(db.Float)
    authz=db.Column(db.String(100))
    key=db.Column(db.String(100))
    secret=db.Column(db.String(100))

    def __init__(self, phno, lvl,authz,key,secret):
        self.phno = phno
        self.lvl = lvl
        self.authz=authz
        self.key=key
        self.secret=secret
db.create_all()
db.session.commit()








@app.route("/")
def hello():
    return "HI"





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


    global request
    global auth
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)


    global tweet
    global token
    zero=0
    global media
    global user
    global medianum
    global filename
    froms =request.form.get('From')


    if (user_data.query.filter_by(phno=request.form.get('From')).scalar() != None):
        print("yes")
    else:
        data = user_data(froms, zero,zero,zero,zero)

        db.session.add(data)
        db.session.commit()
        print("no")

    row = user_data.query.filter_by(phno=request.form.get('From')).first()
    print("00000000000000000000000000000000000000000000000000000000000000000",row.key,row.secret)
    lvl = row.lvl

    if row.key!=0 and row.secret!=0:
        auth.set_access_token(row.key, row.secret)
        api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    print(">>>>>>>>>>.",lvl,row.lvl)

    filename = 'temp.jpg'



    if (os.path.isfile(filename)):
        os.remove(filename)

    resp = MessagingResponse()

    print(request.form)


    msg = request.form.get('Body')

    medianum = request.form.get('NumMedia')

    if medianum!='0':
        media = request.form.get('MediaUrl0')

    if (user_data.query.filter_by(phno=request.form.get('From')).scalar() != None):
        print("yes")
    else:
        data = user_data(froms, lvl, zero, zero, zero)

        db.session.add(data)
        db.session.commit()
        print("no")

    if msg=='##':
        lvl=1
    if msg == '**':
        print("deleting db")


        db.session.delete(row)
        if (user_data.query.filter_by(phno=request.form.get('From')).scalar() != None):
            print("yes")
        else:
            print("no")

        lvl=0




    print(auth)



    if lvl == 0:
        print("int 0")
        resp.message(
            " Hi there. Login to Twitter here. \n{} \n\n\nAnd send the code".format(auth.get_authorization_url()))
        row.authz = auth.request_token['oauth_token']
        db.session.commit()

        lvl=69





    elif lvl==69:
        print("into 69")

        print(row.authz, "000000000000000000000000000000000")

        token = row.authz
        print(token)

        verifier = msg
        print(verifier,"000000000000000000000000")

        auth.request_token = {'oauth_token': token,
                              'oauth_token_secret': verifier}
        try:

            auth.get_access_token(verifier)
            lvl = 0.1
            key = auth.access_token
            secret = auth.access_token_secret
            print("//////////////////////////////////////////////////////////////",key,secret)

            auth.set_access_token(key, secret)
            print(key, secret)
            row.key = key
            row.secret = secret

            db.session.commit()
            api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


        except tweepy.TweepError:
            print('Error! Failed to get access token.')
            resp.message("ErrOR! Send \'**\'")
            lvl = 0




    if lvl ==0.1:
        try:
            user = api.me()
            media=0

            resp.message(
                "Yo, *{}* (```{}```)\n----------------------------------------------\n```{}``` Following | ```{}``` Followers\n----------------------------------------------\n\n What would you like to do? \n\n 1. Make Tweet\n 2. Trending\n 3. Update Profile Picture\n 4. Follow/Unfollow by twitter handle \n 5. View your recent tweets \n 6. View your recent replies\n\n\n\n(Send ## to show this message \nand send ** to logout.)".format(
                    user.name, user.screen_name, user.friends_count, user.followers_count))


        except:
            db.session.delete(row)
        lvl=1.1




    elif lvl==1.1:

        print(msg)

        if msg=='1':
            resp.message("Type your tweet in (LIMIT : 1000 words)")
            media=0
            lvl=1.2
        elif msg=='2':
            print("into1,1")

            trending = api.trends_place(23424848)
            trendss = ''

            for i in range(20):
                if trending[0]['trends'][i]['tweet_volume'] != None:
                    trendss += "{}. {} ... ({})\n".format(i + 1, trending[0]['trends'][i]['name'],
                                                          trending[0]['trends'][i]['tweet_volume'])
                else:
                    trendss += "{}. {} \n".format(i + 1, trending[0]['trends'][i]['name'])

            resp.message("{}".format(trendss))
            lvl = 1


        elif msg=='3':
            resp.message("Send a photo to update your Profile Picture")
            lvl = 1.41


        elif msg=='4':
            resp.message("Enter the Twitter Handle of the user you want to follow/unfollow")
            lvl = 1.51

        elif msg=='5':
            timeline = ''
            timelinecount = 1
            for tweet in api.user_timeline():

                if tweet.in_reply_to_status_id == None:
                    stringtoadd = "{}. {} \n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t{}\n\n\t*🔃 : {}\t💟 : {}*\n------------------------------------\n\n".format(
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
            resp.message("{}".format(timeline))

            lvl = 1


        elif msg=='6':

            print(api.user_timeline()[0])
            timeline = ''
            timelinecount = 1
            for tweet in api.user_timeline():

                if tweet.in_reply_to_status_id != None:
                    stringtoadd = "{}. Reply To  *@{}*({}) :\n {}\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t{}\n\n\t*🔃 : {}\t💟 : {}*\n------------------------------------\n\n".format(timelinecount,tweet.entities['user_mentions'][0]['screen_name'],tweet.entities['user_mentions'][0]['name'],
                         tweet.text, tweet.created_at.strftime("   (%b %d, %H:%M)"), tweet.retweet_count,
                        tweet.retweeted_status.favorite_count if tweet.retweeted == True else tweet.favorite_count)

                    x = re.findall(r'(https?://[^\s]+)', stringtoadd)
                    print(x)
                    if (len(x) != 0):
                        stringtoadd = stringtoadd.replace(x[0], "\n{}".format(x[0]))

                    if (len(timeline) + len(stringtoadd) > 1600):
                        break
                    timeline += stringtoadd
                    timelinecount += 1
            resp.message("{}".format(timeline))

            lvl = 1


        else:
            resp.message("*Wrong Choice Entered. Try again!*")
            lvl=1




    elif lvl==1.2:


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

                tweet.append(msg[letter:letter + 274] + " ({}/{})".format(count + 1, tweetno + 1))
                count += 1
                letter = letter + 275


        resp.message("You're going to make this/these tweet(s)\n------------------")
        for i in tweet:
            resp.message(i)
        resp.message("are you sure ? (y/n)?")

        lvl=1.22


    elif lvl==1.22:

        if (msg.lower == 'y' or 'yes' or 'yeah'or 'yea'):
            print(tweet)


            if (media!=0):

                r = requests.get(media, stream=True)
                if r.status_code == 200:
                    with open(filename, 'wb') as image:
                        for chunk in r:
                            image.write(chunk)

            for i in tweet:

                if (media!=0):

                    api.update_with_media(filename, status=i)
                else:
                    api.update_status(i)

            resp.message("done")


        if msg == 'n':
            resp.message("No changes made")

        lvl=1





    elif lvl==1.41:

        if media!=0:
            r = requests.get(media, stream=True)
            if r.status_code == 200:
                with open(filename, 'wb') as image:
                    for chunk in r:
                        image.write(chunk)

            api.update_profile_image(filename)
            resp.message("DONE !")


        else:
            resp.message("ERROR")


        lvl = 1





    elif lvl==1.51:
        print(api.show_friendship(source_screen_name=user.screen_name, target_screen_name=msg)[0].following)

        if (api.show_friendship(source_screen_name=user.screen_name, target_screen_name=msg)[0].following):
            api.destroy_friendship(msg)
            resp.message('Unfollowed {}'.format(msg))
        else:
            api.create_friendship(msg)
            resp.message('Followed {}'.format(msg))
        lvl = 1






    if lvl ==1:
        user = api.me()
        resp.message(
            "*{}* (```{}```)\n----------------------------------------------\n```{}``` Following | ```{}``` Followers\n----------------------------------------------\n\n What would you like to do? \n\n 1. Make Tweet\n 2. Trending\n 3. Update Profile Picture\n 4. Follow/Unfollow by twitter handle \n 5. View your recent tweets \n 6. View your recent replies\n\n\n\n(Send ## to show this message \nand send ** to logout.)".format(
                user.name, user.screen_name, user.friends_count, user.followers_count))
        media=0

        lvl=1.1








    print("-------------------------------------------- >", lvl)



    if (user_data.query.filter_by(phno=request.form.get('From')).scalar() != None):
        print("yes")
    else:
        data = user_data(froms, lvl,zero,zero,zero)

        db.session.add(data)
        db.session.commit()
        print("no")

    print("-------------------------------------------- >", lvl)
    row.lvl =lvl
    print("**********************************",row.lvl)
    db.session.commit()
    print("++++++++++++++++++++++++++++++++++++++++++++++ >", lvl)




    return str(resp)


if __name__ == "__main__":



    app.run(debug=True)
