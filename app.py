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
app.secret_key='ayush'
# num=0
lvl=0
ver=0
counter=0
login=0
init=0
sublvl=0
confirm=0
auth=tweepy.OAuthHandler('t5qZhGyVwTkNArktAPM64nSvl','lk2ViVadYV6JbyeY7KLRfcDSxV9aGdn9ez9pTTO8cylnO7Z16J')

@app.before_request
def make_session_permanent():
    session.permanent = True

@app.route("/")
def hello():
    return "Hello, World!"






def download_photo(img_url, filename):
    try:
        image_on_web = urllib.urlopen(img_url)
        if image_on_web.headers.maintype == 'image':
            buf = image_on_web.read()
            path = os.getcwd()
            file_path = "%s/%s" % (path, filename)
            downloaded_image = file(file_path, "wb")
            downloaded_image.write(buf)
            downloaded_image.close()
            image_on_web.close()
        else:
            return False
    except:
        return False
    return True




@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    # num=0
    global lvl
    global ver
    global counter
    global login
    global init
    global sublvl
    global confirm
    global verifier
    global init
    global api
    global request
    global tweet
    global media
    global user
    global medianum
    global filename
    filename = 'temp.jpg'

    if init==0:
        session['phone_no']=request.form.get('From')
        init=1

    token=''
    if(os.path.isfile(filename)):
        os.remove(filename)
    # global lvl
    # global counter
    # global ver
    # global login
    resp = MessagingResponse()
    print(request)
    print(request.form)
    print(lvl)
    # resp.message("{}{}{}{}{}{}".format(num,ver,counter,login,init,session['phone_no']))
    msg = request.form.get('Body')
    # print(request)
    # print(request.form)
    # # print("everything >....{}".format(request.form))
    # print(media)
    #
    # if lvl==0:
    #     if counter==0:
    #         resp.message("Hi there. Login to Twitter here. {} And send the code".format(auth.get_authorization_url()))
    #         counter=1
    #         resp.message("{}".format(counter))
    #     else:
    #         token = auth.request_token['oauth_token']
    #         verifier = msg
    #         resp.message("Verifier code :".format(verifier))
    #
    #         ver=1
    #         lvl=1
    #
    # if ver==1:
    #     auth.request_token = {'oauth_token': token,
    #                           'oauth_token_secret': verifier}
    #     try:
    #         auth.get_access_token(verifier)
    #         login=1
    #     except tweepy.TweepError:
    #         resp.message('Error! Failed to get access token.')
    #         # lvl=0
    #         # ver=0
    #         # counter=0
    #         # login=0
    #
    #         resp.message("login:".format(login))
    #
    #         key = auth.access_token
    #         secret = auth.access_token_secret
    #
    #         auth.set_access_token(key, secret)


    #
    # if login==1:
    #     api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    #     user = api.me()
    #     resp.message("yo")
    #     start= resp.message("Hi, {} ({})\n What would you like to do?\n1. Make Tweet\n".format(user.name,user.screen_name))
    #     start.media("https://twitter.com/{}/photo".format(user.screen_name))

    # Create reply

    # session.permanent = True
    # if(msg=='69'):
    #     resp.message("Session is {}".format(num))
    # else:
    #
    #     resp.message("You said: {} ".format(msg))



    if(msg=='**'):
        session.clear()
        lvl=0
        counter=0
        sublvl=0
        login=0

    if lvl == 6:
        print(api.show_friendship(source_screen_name=user.screen_name, target_screen_name=msg)[0].following)

        if (api.show_friendship(source_screen_name=user.screen_name, target_screen_name=msg)[0].following):
            api.destroy_friendship(msg)
            resp.message('Unfollowed {}'.format(msg))
        else:
            api.create_friendship(msg)
            resp.message('Followed {}'.format(msg))
        lvl = 3

    if lvl == 5:
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
            lvl = 3

    if lvl == 1:
        token = auth.request_token['oauth_token']

        verifier = msg

        print(verifier,"1")

        # ver=1
        lvl = 2


    if lvl == 2:
        print(verifier,"2")

        auth.request_token = {'oauth_token': token,
                              'oauth_token_secret': verifier}
        try:

            auth.get_access_token(verifier)
            lvl = 3

        except tweepy.TweepError:
            print('Error! Failed to get access token.')
            # lvl=0

            # lvl=0
            # lvl=0
            # ver=0
            # counter=0
            # login=0

            # print("login:".format(login))

        key = auth.access_token
        secret = auth.access_token_secret

        auth.set_access_token(key, secret)

    if lvl == 3:
        api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
        user = api.me()
        resp.message(
            "yo, *{}* (```{}```)\n----------------------------------------------\n```{}``` Following | ```{}``` Followers\n----------------------------------------------\n\n What would you like to do? \n\n 1. Make Tweet\n 2. Trending\n 3. Update Profile Picture\n 4. Follow/Unfollow by twitter handle \n 5. View your recent tweets".format(user.name, user.screen_name,user.friends_count,user.followers_count))
        lvl = 4











    if lvl == 4:

        if (sublvl == 1):
            media = request.form.get('MediaUrl0')
            medianum=request.form.get('NumMedia')

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
                sublvl = 2
        if (sublvl == 2):
            if (confirm == 0):
                resp.message("are you sure ? (y/n)?")
                confirm = 1
            else:

            #


                if (msg == 'y'):

                    if (medianum != '0'):

                        # filename = 'temp.jpg'
                        # urllib.request.urlretrieve(media, filename)


                        # urllib.request.u


                        r = requests.get(media, stream=True)
                        if r.status_code == 200:
                            with open(filename, 'wb') as image:
                                for chunk in r:
                                    image.write(chunk)




                    for i in tweet:

                        # api.update_with_media('temp2.jpg', status=i)




                        if (medianum !='0'):

                            api.update_with_media(filename,status=i)
                        else:
                            api.update_status(i)


                    resp.message("done")
                    sublvl = 0
                    confirm = 0
                    lvl = 3






        if (msg == '1' and sublvl == 0):
            resp.message("Type your tweet in (LIMIT : 1000 words)")
            sublvl = 1

        if (msg == '2' and sublvl == 0):
            trending = api.trends_place(23424848)
            trendss=''

            for i in range(20):
                if trending[0]['trends'][i]['tweet_volume']!=None:
                    trendss+="{}. {} ... ({})\n".format(i + 1, trending[0]['trends'][i]['name'], trending[0]['trends'][i]['tweet_volume'])
                else:
                    trendss+="{}. {} \n".format(i + 1, trending[0]['trends'][i]['name'])

                # print(trending[0]['trends'][i])
            resp.message("{}".format(trendss))
            sublvl = 0
            confirm = 0
            lvl = 3

        if (msg == '3' and sublvl == 0):
            resp.message("Send a photo to update your Profile Picture")
            lvl=5




        if (msg=='4' and sublvl ==0):
            resp.message("Enter the Twitter Handle of the user you want to follow/unfollow")
            lvl=6

        if (msg =='5' and sublvl==0):
            timeline = ''
            timelinecount=1
            for tweet in api.user_timeline():

                if tweet.in_reply_to_status_id == None:
                    stringtoadd="{}. {}{}\n\t*🔃 : {}\t💟 : {}*\n------------------------------------\n\n".format(timelinecount,tweet.text, tweet.created_at.strftime("   (%b %d, %H:%M)"),tweet.retweet_count,tweet.retweeted_status.favorite_count if tweet.retweeted==True else tweet.favorite_count)

                    x = re.findall(r'(https?://[^\s]+)', stringtoadd)
                    print(x)
                    if(len(x)!=0):
                        stringtoadd=stringtoadd.replace(x[0], "\n{}".format(x[0]))




                    if(len(timeline)+len(stringtoadd)>1600):
                        break
                    timeline+=stringtoadd
                    timelinecount+=1
            resp.message("{}".format(timeline))
            # print(resp.message("{}".format(timeline)))
            lvl=3



    if lvl == 0:

        # if counter==0:
        # print("Hi there. Login to Twitter here. {} And send the code".format(auth.get_authorization_url()))
        # counter=1
        t=resp.message(" Hi there. Login to Twitter here. \n{} \n\n\nAnd send the code".format(auth.get_authorization_url()))
        t.MediaUrl0=("https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.HcQw5Zd1jJhmc1IYzADc3gHaHa%26pid%3DApi&f=1")


        


        lvl = 1

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
