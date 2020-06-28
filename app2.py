import re

import file as file
from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse

import tweepy
import os
import requests
import urllib.request

import time

from click._compat import raw_input

app = Flask(__name__)
app.secret_key = 'ayush'
# num=0
lvl = 0
print("changing lvl%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
ver = 0
counter = 0
login = 0
init = 0
sublvl = 0
# token=''
confirm = 0
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
    # resp.message(
    #     "Yo, *{}* (```{}```)\n----------------------------------------------\n```{}``` Following | ```{}``` Followers\n----------------------------------------------\n\n What would you like to do? \n\n 1. Make Tweet\n 2. Trending\n 3. Update Profile Picture\n 4. Follow/Unfollow by twitter handle \n 5. View your recent tweets".format(
    #         user.name, user.screen_name, user.friends_count, user.followers_count))
    #
    # lvl = 1.1
    return "Hey"


@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""

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

    global media
    global user
    global medianum
    global filename

    filename = 'temp.jpg'



    if (os.path.isfile(filename)):
        os.remove(filename)

    resp = MessagingResponse()

    print(request.form)
    print("-------------------------------------------- >", lvl)


    msg = request.form.get('Body')

    # if init==0:
    #     user = api.me()
    #     resp.message(
    #         "Yo, *{}* (```{}```)\n----------------------------------------------\n```{}``` Following | ```{}``` Followers\n----------------------------------------------\n\n What would you like to do? \n\n 1. Make Tweet\n 2. Trending\n 3. Update Profile Picture\n 4. Follow/Unfollow by twitter handle \n 5. View your recent tweets".format(
    #             user.name, user.screen_name, user.friends_count, user.followers_count))
    #
    #     lvl = 1.1
    #     init=1

    #
    # if lvl == 6:
    #     print(api.show_friendship(source_screen_name=user.screen_name, target_screen_name=msg)[0].following)
    #
    #     if (api.show_friendship(source_screen_name=user.screen_name, target_screen_name=msg)[0].following):
    #         api.destroy_friendship(msg)
    #         resp.message('Unfollowed {}'.format(msg))
    #     else:
    #         api.create_friendship(msg)
    #         resp.message('Followed {}'.format(msg))
    #     lvl = 3
    #
    # elif lvl == 5:
    #     media = request.form.get('MediaUrl0')
    #     medianum = request.form.get('NumMedia')
    #     if medianum != '0':
    #         r = requests.get(media, stream=True)
    #         if r.status_code == 200:
    #             with open(filename, 'wb') as image:
    #                 for chunk in r:
    #                     image.write(chunk)
    #
    #         api.update_profile_image(filename)
    #         resp.message("DONE !")
    #     lvl = 3
    #
    #
    # elif lvl == 3:
    #     user = api.me()
    #     resp.message(
    #         "yo, *{}* (```{}```)\n----------------------------------------------\n```{}``` Following | ```{}``` Followers\n----------------------------------------------\n\n What would you like to do? \n\n 1. Make Tweet\n 2. Trending\n 3. Update Profile Picture\n 4. Follow/Unfollow by twitter handle \n 5. View your recent tweets".format(
    #             user.name, user.screen_name, user.friends_count, user.followers_count))
    #     lvl = 4
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    # elif lvl == 4:
    #
    #     if (sublvl == 1):
    #         media = request.form.get('MediaUrl0')
    #         medianum = request.form.get('NumMedia')
    #
    #         tweet = []
    #         if (len(msg) < 280):
    #             tweet.append(msg)
    #         else:
    #             count = 0
    #             letter = 0
    #             tweetno = len(msg) / 280
    #             tweetno = (len(msg) + 2 * tweetno) // 280
    #             tweetno = int(tweetno)
    #
    #             while (letter < len(msg)):
    #                 # print(msg[letter:letter+274])
    #                 tweet.append(msg[letter:letter + 274] + " ({}/{})".format(count + 1, tweetno + 1))
    #                 count += 1
    #                 letter = letter + 275
    #                 # tweet[count]+=" ({}/{})".format(count+1,tweetno+1)
    #
    #         resp.message("You're going to make this/these tweet(s)\n------------------")
    #         for i in tweet:
    #             resp.message(i)
    #             sublvl = 2
    #     if (sublvl == 2):
    #         if (confirm == 0):
    #             resp.message("are you sure ? (y/n)?")
    #             confirm = 1
    #         else:
    #
    #             #
    #
    #             if (msg == 'y'):
    #
    #                 if (medianum != '0'):
    #
    #
    #
    #                     r = requests.get(media, stream=True)
    #                     if r.status_code == 200:
    #                         with open(filename, 'wb') as image:
    #                             for chunk in r:
    #                                 image.write(chunk)
    #
    #                 for i in tweet:
    #
    #
    #
    #                     if (medianum != '0'):
    #
    #                         api.update_with_media(filename, status=i)
    #                     else:
    #                         api.update_status(i)
    #
    #                 resp.message("done")
    #                 sublvl = 0
    #                 confirm = 0
    #                 lvl = 3
    #
    #             if msg == 'n':
    #                 resp.message("No changes made")
    #                 sublvl = 0
    #                 confirm = 0
    #                 lvl = 3
    #
    #     if (msg == '1' and sublvl == 0):
    #         resp.message("Type your tweet in (LIMIT : 1000 words)")
    #         sublvl = 1
    #
    #     if (msg == '2' and sublvl == 0):
    #         trending = api.trends_place(23424848)
    #         trendss = ''
    #
    #         for i in range(20):
    #             if trending[0]['trends'][i]['tweet_volume'] != None:
    #                 trendss += "{}. {} ... ({})\n".format(i + 1, trending[0]['trends'][i]['name'],
    #                                                       trending[0]['trends'][i]['tweet_volume'])
    #             else:
    #                 trendss += "{}. {} \n".format(i + 1, trending[0]['trends'][i]['name'])
    #
    #
    #         resp.message("{}".format(trendss))
    #         sublvl = 0
    #         confirm = 0
    #         lvl = 3
    #
    #     if (msg == '3' and sublvl == 0):
    #         resp.message("Send a photo to update your Profile Picture")
    #         lvl = 5
    #
    #     if (msg == '4' and sublvl == 0):
    #         resp.message("Enter the Twitter Handle of the user you want to follow/unfollow")
    #         lvl = 6
    #
    #     if (msg == '5' and sublvl == 0):
    #         timeline = ''
    #         timelinecount = 1
    #         for tweet in api.user_timeline():
    #
    #             if tweet.in_reply_to_status_id == None:
    #                 stringtoadd = "{}. {}{}\n\t*🔃 : {}\t💟 : {}*\n------------------------------------\n\n".format(
    #                     timelinecount, tweet.text, tweet.created_at.strftime("   (%b %d, %H:%M)"), tweet.retweet_count,
    #                     tweet.retweeted_status.favorite_count if tweet.retweeted == True else tweet.favorite_count)
    #
    #                 x = re.findall(r'(https?://[^\s]+)', stringtoadd)
    #                 print(x)
    #                 if (len(x) != 0):
    #                     stringtoadd = stringtoadd.replace(x[0], "\n{}".format(x[0]))
    #
    #                 if (len(timeline) + len(stringtoadd) > 1600):
    #                     break
    #                 timeline += stringtoadd
    #                 timelinecount += 1
    #         resp.message("{}".format(timeline))
    #
    #         lvl = 3
    #
    #
    #     else:
    #         resp.message("Wrong choice")



    if lvl == 0:

        try:
            resp.message(
                " Hi there. Login to Twitter here. \n{} \n\n\nAnd send the code".format(auth.get_authorization_url()))
            # t.MediaUrl0=("https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.HcQw5Zd1jJhmc1IYzADc3gHaHa%26pid%3DApi&f=1")
        except:
            print("************************************************")


    elif lvl ==0.1:
        user = api.me()
        resp.message(
            "Yo, *{}* (```{}```)\n----------------------------------------------\n```{}``` Following | ```{}``` Followers\n----------------------------------------------\n\n What would you like to do? \n\n 1. Make Tweet\n 2. Trending\n 3. Update Profile Picture\n 4. Follow/Unfollow by twitter handle \n 5. View your recent tweets".format(
                user.name, user.screen_name, user.friends_count, user.followers_count))

        lvl=1.1

    elif lvl==1.1:
        # type(msg)
        print(msg)
        if msg=='1':
            resp.message("Type your tweet in (LIMIT : 1000 words)")
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

            resp.message("{}".format(trendss))
            lvl = 1

            # lvl=1.3
        if msg=='3':
            resp.message("Send a photo to update your Profile Picture")
            lvl = 1.41

            # lvl=1.4
        if msg=='4':
            resp.message("Enter the Twitter Handle of the user you want to follow/unfollow")
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
            resp.message("{}".format(timeline))

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

        resp.message("You're going to make this/these tweet(s)\n------------------")
        for i in tweet:
            resp.message(i)
        resp.message("are you sure ? (y/n)?")

        lvl=1.22

    # elif lvl==1.21:
    #
    #     resp.message("are you sure ? (y/n)?")
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

            resp.message("done")


        if msg == 'n':
            resp.message("No changes made")

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
    #     resp.message("{}".format(trendss))
    #     lvl=0.1




    # elif lvl==1.4:
    #     resp.message("Send a photo to update your Profile Picture")
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
            resp.message("DONE !")


        else:
            resp.message("ERROR")


        lvl = 1



    # elif lvl==1.5:
    #     resp.message("Enter the Twitter Handle of the user you want to follow/unfollow")
    #     lvl=1.51



    elif lvl==1.51:
        print(api.show_friendship(source_screen_name=user.screen_name, target_screen_name=msg)[0].following)

        if (api.show_friendship(source_screen_name=user.screen_name, target_screen_name=msg)[0].following):
            api.destroy_friendship(msg)
            resp.message('Unfollowed {}'.format(msg))
        else:
            api.create_friendship(msg)
            resp.message('Followed {}'.format(msg))
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
    #     resp.message("{}".format(timeline))
    #
    #     lvl = 0.1





    if lvl ==1:
        user = api.me()
        resp.message(
            "*{}* (```{}```)\n----------------------------------------------\n```{}``` Following | ```{}``` Followers\n----------------------------------------------\n\n What would you like to do? \n\n 1. Make Tweet\n 2. Trending\n 3. Update Profile Picture\n 4. Follow/Unfollow by twitter handle \n 5. View your recent tweets".format(
                user.name, user.screen_name, user.friends_count, user.followers_count))

        lvl=1.1










    return str(resp)


if __name__ == "__main__":
    # print(
        # "55555555555555555555555555555555555555555555555starting555555555555555555555555555555555555555555555555555555555")
    app.run(debug=True)
